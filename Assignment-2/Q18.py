def test1():
    print("test1 in imported module")
def test2():
    print("test2 in imported module")
test1()
test2()

import importedModule
print('hello')

# Output : test1 in imported module
#          test2 in imported module
# ModuleNotFoundError: No module named 'importedModule'
