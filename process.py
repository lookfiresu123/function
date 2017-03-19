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
result_set = set([])
have_analysised_set = set([])
interface_per_module_dict = {}                          # {call_function, [called_interfaces]}
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
deal with function call information of fs/*.c and fs/ext2/*.c
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
                                #print called_function
                                value = collect_symbals_dict.get(called_function)
                                if value == None:
                                        pair = [called_function, "other"]
                                        called_functions.insert(len(called_functions), pair)
                                else:
                                        pair = [called_function, value[4]]
                                        called_functions.insert(len(called_functions), pair)
 

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
        '''
        for call_function in collect_function_call_called_dict:
                called_functions = collect_function_call_called_dict[call_function]
                #function_module_list = []
                print call_function + ": "
                for item in called_functions:
                        print item
                print ""
        '''


        return

'''
search interface per module
'''
def search_interface_per_module(module_from):
        for call_function in collect_function_call_called_dict:
                called_functions = collect_function_call_called_dict[call_function]
                #print call_function, called_functions
                called_interfaces = []
                for pattern in called_functions:
                        item = pattern[0]
                        module = pattern[1]
                        if module == module_from or module == "include" or module == "other":
                                continue
                        else:
                                value = collect_interface_dict.get(item)
                                if value != None:
                                        called_interfaces.insert(len(called_interfaces), pattern)
                if called_interfaces != []:
                        #print called_interfaces
                        interface_per_module_dict[call_function] = called_interfaces
        
        return                                                                          

'''
search interface per function
'''
def search_interface_per_function(function):
        #print function, index
        # check if @function is has a call-called relationship
        value = collect_function_call_called_dict.get(function)
        if value == None:
                return
        else:

                called_functions = collect_function_call_called_dict[function]
                # if this function have been analysised, we could avoid to do again
                if function in have_analysised_set:
                        return
                # use my_set as stack to avoid ring, for example: A -> B, B -> A
                my_set.add(function)
                have_analysised_set.add(function)
                for pattern in called_functions:
                        item = pattern[0]
                        module = pattern[1]
                        #value = collect_interface_dict.get(item)
                        if module == "other" or module == "fs" or module == "include":
                                #go on search inside
                                if item not in my_set:
                                        #my_set.add(item)
                                        search_interface_per_function(item)
                                else:
                                        continue
                        else:
                                #my_dict[item] = function
                                str = function + " " + item + " " + module
                                #print str, index
                                result_set.add(str)
                                #print function + " -> " + item

                my_set.remove(function)
                return


def format_and_print_search_result(list):
        dict = {}       # {call_function, [interface_functions] }
        for str in list:
                patterns = str.split();
                call_function = patterns[0]
                interface_function = patterns[1]
                module = patterns[2]
                value = dict.get(call_function)
                if value == None:
                        dict[call_function] = [interface_function + " " + module]
                else:
                        dict[call_function].insert(len(dict[call_function]), interface_function + " " + module);

        dict_per_module = {}
        dict_per_module["mm"] = []
        dict_per_module["kernel"] = []
        dict_per_module["block"] = []
        for pattern in dict:
                interfaces_per_subfunction = dict[pattern]
                for item in interfaces_per_subfunction:
                        strs = item.split()
                        dict_per_module[strs[1]].insert(len(dict_per_module[strs[1]]), strs[0])

        for pattern in dict_per_module:
                print pattern + ": "
                print "*********************************"
                interfaces_per_module = dict_per_module[pattern]
                interfaces_set = set([])
                for item in interfaces_per_module:
                        interfaces_set.add(item)
                for item in interfaces_set:
                        print item
                print "*********************************"
                print ""

        
        '''
        for pattern in dict:
                #print pattern + " -> ", dict[pattern]
                print pattern + ": "
                interfaces_per_subfunction = dict[pattern]
                for item in interfaces_per_subfunction:
                        strs = item.split()
                        print [strs[0], strs[1]]
                print ""
        '''

        return

def test_search_for_interface_per_function(function):
        search_interface_per_function(function)
        
        search_interface_per_function("ext2_get_acl")
        search_interface_per_function("ext2_lookup")
        search_interface_per_function("ext2_follow_link")
        search_interface_per_function("page_put_link")
        search_interface_per_function("ext2_tmpfile")
        search_interface_per_function("dquot_alloc")
        search_interface_per_function("dquot_acquire")
        search_interface_per_function("dquot_commit")
        search_interface_per_function("dquot_release")
        search_interface_per_function("dquot_destroy")
        search_interface_per_function("ext2_create")
        search_interface_per_function("ext2_write_inode")
        search_interface_per_function("ext2_evict_inode")
        search_interface_per_function("fanotify_free_group_priv")
        search_interface_per_function("ext2_destroy_inode")
        
        #print my_set

        print function + ": "
        print "------------------------------------------------"
        sorted_result = sorted(result_set)      # result_set is a set, but sorted_result is a list
        format_and_print_search_result(sorted_result)
        return


def test_search_for_interface_per_module(module):
        search_interface_per_module(module)

        for pattern in interface_per_module_dict:
                print pattern + ": "
                called_interfaces = interface_per_module_dict[pattern]
                for item in called_interfaces:
                        print item
                print ""
        return

def main():
        #import_symbals()
        #import_interface()
        collect_symbals()
        collect_interface()
        collect_function_call("fs")
        test_search_for_interface_per_function("do_sys_open")
        #test_search_for_interface_per_module("fs")
        return
        

if __name__ == "__main__":
        main()
