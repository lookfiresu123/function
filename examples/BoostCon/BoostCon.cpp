//===- PrintFunctionNames.cpp ---------------------------------------------===//
//
//                     The LLVM Compiler Infrastructure
//
// This file is distributed under the University of Illinois Open Source
// License. See LICENSE.TXT for details.
//
//===----------------------------------------------------------------------===//
//
// Example clang plugin which simply prints the names of all the top-level decls
// in the input file.
//
//===----------------------------------------------------------------------===//

#include "clang/Frontend/FrontendPluginRegistry.h"
#include "clang/AST/AST.h"
#include "clang/AST/ASTConsumer.h"
#include "clang/AST/RecursiveASTVisitor.h"
#include "clang/Frontend/CompilerInstance.h"
#include "clang/Sema/Sema.h"
#include "llvm/Support/raw_ostream.h"
#include <vector>
#include <unordered_map>
#include <set>
#include <string>
#include <iostream>
#include <memory>

using namespace clang;

namespace {

class BoostConConsumer : public ASTConsumer, public RecursiveASTVisitor<BoostConConsumer> {
  typedef struct {
    std::string name;
    std::string location;
    bool ispointer;
  } FunctionInfo;

  CompilerInstance &Instance;
  std::set<std::string> ParsedTemplates;

  ASTContext *ptr = nullptr;
  FunctionInfo func;
  typedef std::shared_ptr<FunctionInfo> FunctionInfo_ptr;
  FunctionInfo_ptr fp;
  std::unordered_map<FunctionInfo_ptr, std::vector<FunctionInfo_ptr>> funcs;

public:
  BoostConConsumer(CompilerInstance &Instance,
                         std::set<std::string> ParsedTemplates)
      : Instance(Instance), ParsedTemplates(ParsedTemplates) {}

  void HandleTranslationUnit(ASTContext& context) override {
    ptr = &context;
    TraverseDecl(context.getTranslationUnitDecl());
  }

  bool VisitFunctionDecl(FunctionDecl *f) {
    if (f->isThisDeclarationADefinition()) {
      func.name = f->getNameAsString();
      //SourceLocation sl = f->getPointOfInstantiation();
      SourceLocation sl = f->getSourceRange().getBegin();
      //const SourceManager sm = ptr->getSourceManager();
      func.location = sl.printToString(ptr->getSourceManager());
      func.ispointer = false;
      //std::cout << "[" << func.name << "] " << "[" << func.location << "]" << std::endl;
      fp = std::make_shared<FunctionInfo>(FunctionInfo());
      fp->name = func.name;
      fp->location = func.location;
      fp->ispointer = func.ispointer;
      funcs[fp] = std::vector<FunctionInfo_ptr>();
    }
    return true;
  }

  bool VisitDeclRefExpr(DeclRefExpr *r) {
    if (dyn_cast<FunctionDecl>(r->getDecl())) {
      FunctionInfo tmp;
      tmp.name = r->getNameInfo().getAsString();
      SourceLocation sl = r->getLocation();
      //const SourceManager sm = ptr->getSourceManager();
      tmp.location = sl.printToString(ptr->getSourceManager());
      tmp.ispointer = false;
      //std::cout << "-> [" << tmp.name << "] " << "[" << tmp.location << "]" << std::endl;
      FunctionInfo_ptr tp = std::make_shared<FunctionInfo>(FunctionInfo());
      tp->name = tmp.name;
      tp->location = tmp.location;
      tp->ispointer = tmp.ispointer;
      funcs[fp].push_back(tp);
    }
    return true;
  }

  bool VisitMemberExpr(MemberExpr *m) {
    QualType t = m->getMemberDecl()->getType();
    if (t->isFunctionPointerType()) {
      FunctionInfo tmp;
      tmp.name = m->getMemberNameInfo().getAsString();
      SourceLocation sl = m->getMemberLoc();
      //const SourceManager sm = ptr->getSourceManager();
      tmp.location = sl.printToString(ptr->getSourceManager());
      tmp.ispointer = true;
      //std::cout << "-> [" << tmp.name << "] " << "[" << tmp.location << "] " << "[Function Pointer]" << std::endl;
      FunctionInfo_ptr tp = std::make_shared<FunctionInfo>(FunctionInfo());
      tp->name = tmp.name;
      tp->location = tmp.location;
      tp->ispointer = tmp.ispointer;
      funcs[fp].push_back(tp);
    }
    return true;
  }

  ~BoostConConsumer() {
    FunctionInfo_ptr target = nullptr;
    std::unordered_map<std::string, std::string> my_map;

    //std::cout << "Here is the call functions:" << std::endl;
    //std::cout << "-------------------------------------------------------" << std::endl; 
    for (auto iter = funcs.begin() ; iter != funcs.end(); ++iter) {
      FunctionInfo_ptr call = iter->first;
      std::vector<FunctionInfo_ptr> called = iter->second;
      std::cout << "[" << call->name << "]," << "[" << call->location << "]" << ":" << std::endl;
      my_map[call->name] = call->location;
      if (call->name == "smp_call_function_single")
        target = call;
      
      for (int i = 0 ; i < called.size() ; ++i) {
        FunctionInfo_ptr t = called[i];
        if (t->ispointer == false)
          std::cout << "-> [" << t->name << "]" << "," << "[" << t->location << "]" << std::endl;
        else
          std::cout << "-> [" << t->name << "]" << "," << "[" << t->location << "]" << "," << "[Function Pointer]" << std::endl;
      }
      
      std::cout << std::endl;
    }

    /*
    if (target != nullptr) {
       std::cout << std::endl << std::endl;
       std::cout << "Here is the called functions of smp_call_function_single()" << std::endl;
       std::cout << "-------------------------------------------------------" << std::endl;
       std::vector<FunctionInfo_ptr> target_called = funcs[target];
       for (auto iter = target_called.begin() ; iter != target_called.end() ; ++iter) {
         std::cout << "[" << (*iter)->name << "]," << "[" << (*iter)->location << "]" << std::endl;
       }
    }
    */
  }

};

class BoostConAction : public PluginASTAction {
  std::set<std::string> ParsedTemplates;
protected:
  std::unique_ptr<ASTConsumer> CreateASTConsumer(CompilerInstance &CI,
                                                 llvm::StringRef) override {
    return llvm::make_unique<BoostConConsumer>(CI, ParsedTemplates);
  }

  bool ParseArgs(const CompilerInstance &CI,
                 const std::vector<std::string> &args) override {
    for (unsigned i = 0, e = args.size(); i != e; ++i) {
      llvm::errs() << "BoostCon arg = " << args[i] << "\n";

      // Example error handling.
      DiagnosticsEngine &D = CI.getDiagnostics();
      if (args[i] == "-an-error") {
        unsigned DiagID = D.getCustomDiagID(DiagnosticsEngine::Error,
                                            "invalid argument '%0'");
        D.Report(DiagID) << args[i];
        return false;
      } else if (args[i] == "-parse-template") {
        if (i + 1 >= e) {
          D.Report(D.getCustomDiagID(DiagnosticsEngine::Error,
                                     "missing -parse-template argument"));
          return false;
        }
        ++i;
        ParsedTemplates.insert(args[i]);
      }
    }
    if (!args.empty() && args[0] == "help")
      PrintHelp(llvm::errs());

    return true;
  }
  void PrintHelp(llvm::raw_ostream& ros) {
    ros << "Help for BoostCon plugin goes here\n";
  }

};

}

static FrontendPluginRegistry::Add<BoostConAction>
X("boost-fns", "print boostcon");
