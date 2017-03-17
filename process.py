import subprocess

symbals_file = open("/home/lookfiresu/Desktop/linux-3.13/symbals_function.txt")

'''
store information of symbals per module
'''
symbals_fs = open("/home/lookfiresu/function/symbals_fs.txt", "r+")
symbals_mm = open("/home/lookfiresu/function/symbals_mm.txt", "r+")
symbals_kernel = open("/home/lookfiresu/function/symbals_kernel.txt", "r+")
symbals_block = open("/home/lookfiresu/function/symbals_block.txt", "r+")
symbals_include = open("/home/lookfiresu/function/symbals_include.txt", "r+")



collect_symbals_table = []                              # [function, filename, linenum, module]
collect_symbals_dict = {}                               # {function, [function, filename, linenum, module]}

collect_interface_table = []                            # [function, filename, linenum, module]
collect_interface_dict = {}                             # {function, [function, filename, linenum, module]}

collect_function_call_table = []
collect_function_call_called_dict = {}                  # {call_function, [called_functions]}
collect_interface_call_called_dict = {}                 # {call_function, [called_interfaces]}

my_set = set([])
my_dict = {}

'''
store information of interface of per module
'''
interface_fs = open("/home/lookfiresu/function/interface_fs.txt", "r+")
interface_mm = open("/home/lookfiresu/function/interface_mm.txt", "r+")
interface_kernel = open("/home/lookfiresu/function/interface_kernel.txt", "r+")
interface_block = open("/home/lookfiresu/function/interface_block.txt", "r+")
interface_include = open("/home/lookfiresu/function/interface_include.txt", "r+")

'''
store ast information of function call
'''
function_call_fs_namei_ast = open("/home/lookfiresu/function/function_call_ast/function_call_fs_namei_ast.txt", "r+")
function_call_fs_ast = open("/home/lookfiresu/function/function_call_ast/function_call_fs_ast.txt", "r+")

'''
import symbals per modules
'''
def import_symbals_fs():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_all.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", "/fs/"], stdin = child1.stdout, stdout = symbals_fs)
        child2.wait()
        return

def import_symbals_mm():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_all.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", "/mm/"], stdin = child1.stdout, stdout = symbals_mm)
        child2.wait()
        return

def import_symbals_kernel():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_all.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", "/kernel/"], stdin = child1.stdout, stdout = symbals_kernel)
        child2.wait()
        return

def import_symbals_block():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_all.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", "/block/"], stdin = child1.stdout, stdout = symbals_block)
        child2.wait()
        return

def import_symbals_include():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_all.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", "/include/linux/"], stdin = child1.stdout, stdout = symbals_include)
        child2.wait()
        return

def import_symbals():
        import_symbals_fs()
        import_symbals_mm()
        import_symbals_kernel()
        import_symbals_block()
        import_symbals_include()
        return


'''
import interface per modules
'''
def import_interface_fs():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_fs.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", " T "], stdin = child1.stdout, stdout = interface_fs)
        child2.wait()
        return

def import_interface_mm():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_mm.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", " T "], stdin = child1.stdout, stdout = interface_mm)
        child2.wait()
        return

def import_interface_kernel():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_kernel.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", " T "], stdin = child1.stdout, stdout = interface_kernel)
        child2.wait()
        return

def import_interface_block():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_block.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", " T "], stdin = child1.stdout, stdout = interface_block)
        child2.wait()
        return
'''
because function defined in include is always static, so there are no interface
'''
def import_interface_include():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/function/symbals_include.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", " T "], stdin = child1.stdout, stdout = interface_include)
        child2.wait()
        return

def import_interface():
        import_interface_fs()
        import_interface_mm()
        import_interface_kernel()
        import_interface_block()
        import_interface_include()
        return

'''
collect symbals per modules by data struct
'''
def collect_symbals_fs(table):
        while 1:
                lines = symbals_fs.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "fs")
                        table.insert(len(table), list);
        return

def collect_symbals_mm(table):
        while 1:
                lines = symbals_mm.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "mm")
                        table.insert(len(table), list);
        return

def collect_symbals_kernel(table):
        while 1:
                lines = symbals_kernel.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "kernel")
                        table.insert(len(table), list);
        return

def collect_symbals_block(table):
        while 1:
                lines = symbals_block.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "block")
                        table.insert(len(table), list);
        return

def collect_symbals_include(table):
        while 1:
                lines = symbals_include.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "include")
                        table.insert(len(table), list);
        return

def collect_symbals():
        collect_symbals_fs(collect_symbals_table);
        collect_symbals_mm(collect_symbals_table);
        collect_symbals_kernel(collect_symbals_table);
        collect_symbals_block(collect_symbals_table);
        collect_symbals_include(collect_symbals_table);
        for pattern in collect_symbals_table:
                collect_symbals_dict[pattern[1]] = pattern
        '''
        for pattern in collect_symbals_dict:
                print pattern
        '''
        return

'''
collect interface per module
'''
def collect_interface_fs(table):
        while 1:
                lines = interface_fs.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "fs")
                        table.insert(len(table), list);
        return

def collect_interface_mm(table):
        while 1:
                lines = interface_mm.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "mm")
                        table.insert(len(table), list);
        return

def collect_interface_kernel(table):
        while 1:
                lines = interface_kernel.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "kernel")
                        table.insert(len(table), list);
        return

def collect_interface_block(table):
        while 1:
                lines = interface_block.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "block")
                        table.insert(len(table), list);
        return

def collect_interface_include(table):
        while 1:
                lines = interface_include.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        address = patterns[0]
                        function = patterns[2]
                        patterns = patterns[3].split(':')
                        filename = patterns[0]
                        linenum = patterns[1]
                        list = []
                        list.insert(len(list), address)
                        list.insert(len(list), function)
                        list.insert(len(list), filename)
                        list.insert(len(list), linenum)
                        list.insert(len(list), "include")
                        table.insert(len(table), list);
        return

'''
store collect_interface to dict data struct for search
'''
def collect_interface():
        collect_interface_fs(collect_interface_table);
        collect_interface_mm(collect_interface_table);
        collect_interface_kernel(collect_interface_table);
        collect_interface_block(collect_interface_table);
        collect_interface_include(collect_interface_table)

        # store to dict
        for pattern in collect_interface_table:
                collect_interface_dict[pattern[1]] = pattern

        return


'''
deal with function call information of fs/namei.c
'''
def collect_function_call_per_file(file, dict):
        temp_table = []
        called_functions = []
        call_function = ""
        while 1:
                # lines = function_call_fs_namei_ast.readlines(100000)
                lines = file.readlines(1000000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        temp_table.insert(len(temp_table), patterns)

                for index in range(len(temp_table) - 1):
                        patterns = temp_table[index]
                        # if this is a call function record
                        if patterns[0] == "FunctionDecl":
                                # determine defination with function call or (declaration or defination without function call)
                                patterns_next = temp_table[index+1]
                                if patterns_next[0] == "FunctionDecl":
                                        # declaration or defination without function call
                                        continue
                                # defination with function call
                                if call_function != "" and called_functions != []:
                                        dict[call_function] = called_functions
                                called_functions = []
                                call_function = ""
                                for index in range(len(patterns) - 1):
                                        if patterns[index].endswith('>'):
                                                call_function = patterns[index+1]
                        # if this is a called function record
                        if patterns[0] == "DeclRefExpr":
                                for pattern in patterns:
                                        if pattern == "Function":
                                                break;
                                index = patterns.index(pattern)
                                called_function = patterns[index+2]
                                called_function = called_function.replace("\'", "")
                                called_functions.insert(len(called_functions), called_function)
 

        return
'''
                        for pattern in patterns:
                                if pattern == "Function":
                                        break;
                        index = patterns.index(pattern)
                        function = patterns[index+2]
                        function = function.replace("\'", "")
                        table.insert(len(table), function)
return
'''

'''
collect relationship between call_function and called_functions, and print their module
'''
def collect_function_call(module_from):
        collect_function_call_per_file(function_call_fs_ast, collect_function_call_called_dict)
        for call_function in collect_function_call_called_dict:
                called_functions = collect_function_call_called_dict[call_function]
                function_module_list = []
                for function in called_functions:
                        function_module = []
                        value = collect_interface_dict.get(function)
                        if value == None:
                                value = collect_symbals_dict.get(function)
                                if value == None:
                                        function_module.insert(len(function_module), function)
                                        function_module.insert(len(function_module), "other")
                                else:
                                        function_module.insert(len(function_module), function)
                                        function_module.insert(len(function_module), value[4])
                        else:
                                function_module.insert(len(function_module), function)
                                function_module.insert(len(function_module), value[4])
                        function_module_list.insert(len(function_module_list), function_module);

                value = collect_symbals_dict.get(call_function)
                '''
                if value == None:
                        print call_function + ": "
                else:
                        print call_function + ": " + value[2]
                for pattern in function_module_list:
                        print pattern
                print ""
                '''

        return

'''
detect interface, for example fs/namei.c
'''
def detect_interface(module_from):
        for call_function in collect_function_call_called_dict:
                called_functions = collect_function_call_called_dict[call_function]
                called_interfaces = []
                for function in called_functions:
                        value = collect_interface_dict.get(function)
                        if value == None:
                                continue
                        if module_from != value[4]:
                                called_interfaces.insert(len(called_interfaces), function)
                if called_interfaces != []:
                        collect_interface_call_called_dict[call_function] = called_interfaces
        for pattern in collect_interface_call_called_dict:
                print pattern + ": "
                print collect_interface_call_called_dict[pattern]
                print ""
        return

def search_interface_per_function(function):
        #print function, index
        #check if @function is a valid symbal
        value = collect_symbals_dict.get(function)
        if value == None:
                return
        else:
                module = value[4]
                # check if @function is has a call-called relationship
                value = collect_function_call_called_dict.get(function)
                if value == None:
                        return
                else:
                        called_functions = collect_function_call_called_dict[function]
                        # use my_set as stack to avoid ring, for example: A -> B, B -> A
                        my_set.add(function)
                        for item in called_functions:
                                #check if this called_function is an interface function
                                value = collect_interface_dict.get(item)
                                if value == None:
                                        #this called function is not an interface function, go on search inside
                                        if item not in my_set:
                                                #my_set.add(item)
                                                search_interface_per_function(item)
                                        else:
                                                continue
                                elif value[4] == module or value[4] == "include":
                                        #go on search inside
                                        if item not in my_set:
                                                #my_set.add(item)
                                                search_interface_per_function(item)
                                        else:
                                                continue
                                else:
                                        my_dict[item] = function
                                        #print function + " -> " + item

                        my_set.remove(function)
                        return



def main():
        #import_symbals()
        #import_interface()
        collect_symbals()
        collect_interface()
        collect_function_call("fs")
        
        search_interface_per_function("do_sys_open")
        search_interface_per_function("ext2_lookup")
        search_interface_per_function("ext2_create")
        #print my_set
        
        print "do_sys_open: "
        print "------------------------------------------------"
        for item in my_dict:
                print my_dict[item] + " -> " + item      
        
        #detect_interface("fs")
        return
        

if __name__ == "__main__":
        main()
