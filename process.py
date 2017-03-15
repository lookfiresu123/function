import subprocess

symbals_file = open("/home/lookfiresu/Desktop/linux-3.13/symbals_function.txt")

'''
store information of symbals per module
'''
symbals_fs = open("/home/lookfiresu/function/symbals_fs.txt", "r+")
symbals_mm = open("/home/lookfiresu/function/symbals_mm.txt", "r+")
symbals_kernel = open("/home/lookfiresu/function/symbals_kernel.txt", "r+")
symbals_block = open("/home/lookfiresu/function/symbals_block.txt", "r+")



collect_symbals_table = []              # [function, filename, linenum, module]
collect_interface_table = []              # [function, filename, linenum, module]
collect_interface_dict = {}

collect_function_call_table = []

'''
store information of interface of per module
'''
interface_fs = open("/home/lookfiresu/function/interface_fs.txt", "r+")
interface_mm = open("/home/lookfiresu/function/interface_mm.txt", "r+")
interface_kernel = open("/home/lookfiresu/function/interface_kernel.txt", "r+")
interface_block = open("/home/lookfiresu/function/interface_block.txt", "r+")

'''
store ast information of function call
'''
function_call_fs_namei_ast = open("/home/lookfiresu/function/function_call_ast/function_call_fs_namei_ast.txt", "r+")

'''
import symbals per modules
'''
def import_symbals_fs():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/Desktop/linux-3.13/symbals_function.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", "/fs/"], stdin = child1.stdout, stdout = symbals_fs)
        child2.wait()
        return

def import_symbals_mm():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/Desktop/linux-3.13/symbals_function.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", "/mm/"], stdin = child1.stdout, stdout = symbals_mm)
        child2.wait()
        return

def import_symbals_kernel():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/Desktop/linux-3.13/symbals_function.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", "/kernel/"], stdin = child1.stdout, stdout = symbals_kernel)
        child2.wait()
        return

def import_symbals_block():
        child1 = subprocess.Popen(["cat", "/home/lookfiresu/Desktop/linux-3.13/symbals_function.txt"], stdout = subprocess.PIPE)
        child2 = subprocess.Popen(["grep", "/block/"], stdin = child1.stdout, stdout = symbals_block)
        child2.wait()
        return

def import_symbals():
        import_symbals_fs()
        import_symbals_mm()
        import_symbals_kernel()
        import_symbals_block()
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

def import_interface():
        import_interface_fs()
        import_interface_mm()
        import_interface_kernel()
        import_interface_block()
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

def collect_symbals():
        collect_symbals_fs(collect_symbals_table);
        collect_symbals_mm(collect_symbals_table);
        collect_symbals_kernel(collect_symbals_table);
        collect_symbals_block(collect_symbals_table);
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

'''
store collect_interface to dict data struct for search
'''
def collect_interface():
        collect_interface_fs(collect_interface_table);
        collect_interface_mm(collect_interface_table);
        collect_interface_kernel(collect_interface_table);
        collect_interface_block(collect_interface_table);

        # store to dict
        for pattern in collect_interface_table:
                collect_interface_dict[pattern[1]] = pattern

        return


'''
deal with function call information of fs/namei.c
'''
def collect_function_call_per_file(file, table):
        per_table = []
        while 1:
                lines = function_call_fs_namei_ast.readlines(100000)
                if not lines:
                        break
                for line in lines:
                        patterns = line.split()
                        for pattern in patterns:
                                if pattern == "Function":
                                        break;
                        index = patterns.index(pattern)
                        function = patterns[index+2]
                        function = function.replace("\'", "")
                        table.insert(len(table), function)
        return

def collect_function_call():
        collect_function_call_per_file(function_call_fs_namei_ast, collect_function_call_table)
        return

'''
detect interface, for example fs/namei.c
'''
def detect_interface(module_from):
        for function in collect_function_call_table:
                value = collect_interface_dict.get(function)
                if value == None:
                        continue
                if value[4] != module_from:
                        print function + ", " + value[4]
        return



def main():
        #import_symbals()
        #import_interface()
        collect_symbals()
        collect_interface()
        collect_function_call()
        detect_interface("fs")
        return

if __name__ == "__main__":
        main()
