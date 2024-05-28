'''
OS MODULE - This module is used to interact python with operating system


'''

#----------------------
#OS MODULE - INTERACTING WITH OPERATION SYSTEM USING PYTHON
#----------------------


#----------------------

#----------------------
#----------------------
#----------------------
#----------------------
#----------------------
#----------------------




#----------------------

import os







#os.mkdir(path, mode=0o777, *, dir_fd=None) - Create Directory at given path. 
try:
    os.mkdir("/Users/frutos/F0x/Devops Projects/Python Projects/pycls/for-github/os-module-folder1")
    print("folder created ! Creating employee.txt in this filder")
    os.chdir("/Users/frutos/F0x/Devops Projects/Python Projects/pycls/for-github/os-module-folder1")
    with open("os-module-test.txt", "w") as f:
        f.write("I love python")

except FileExistsError: #exception raised when folder with this name already exists.
    print(f"This Folder Name Already Exists ")
except FileNotFoundError: #exception raised when any parent dirctory doesnt exist
    print("This Path Doent Exists")



# #os.chdir() - Change Directory To Given Path.
# cwd = os.getcwdb()
# print(f"My curent working directory is : {cwd}")
# newdir = os.chdir("/Users/frutos")
# print(f"Directory Changed: {newdir}")




# #os.getcwdb() - Returns Current Working Directory.
# print()
# print(os.getcwdb())


#----------------------

