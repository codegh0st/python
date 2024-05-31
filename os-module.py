'''
OS MODULE - This module is used to interact python with operating system

'''

#----------------------
#OS MODULE - INTERACTING WITH OPERATION SYSTEM USING PYTHON
#----------------------





#----------------------
import os
import os.path
import shutil
import sys



#----------------------

# os.system(command) - this function is used to run any system command on system, it will run one command at a time. 
# How to shutdown and Restart the system
# For shutdown your system: os.system("shutdown /s /t 1")
# For restart your system : os.system("shutdown /ri/t 1")
# For Logout your system : os.system("shutdown -I")

os.system("ls")

#----------------------

# # WRITE A PROGRAM TO ADD NEW PATH IN EXISTING PATH. 
# # os.path.join(<path-sepearatpr>, <list of directory or list of paths>)

# list1 = os.path.join("c:", "Users","Rahul","Devops-project")
# print(list1)


# path = sys.path # returns cureent path as a list

# path.append(list1) # appending our custome path into systme path
# new_path = sys.path
# print(new_path)


#----------------------
# # WRITE A PROGRAM TO RENAME A FILE
# # os.rename(src, dst) - renames source file and move it to destination with provided name in dst. 

# source = input("Input Source file Name which supposed to be renamed: ")
# dest = input("input destination file Name by which file will be renamed: ")

# if os.path.exists(source):
#     if os.path.exists(dest):
#         print("With this name one file already exists, So renaming not possible")
#     else:
#         os.rename(source, dest)
#         print("file is renames succesfully!")
# else:
#     print("With this name no file exist at souce")

#----------------------

# os.remove(path) - removes only file
# os.rmdir(path) - removes only empty dir

#----------------------
# # WRITE A PROGRAM TO COUNT NO OF FILE AND FOLDER ON GIVEN PATH.

# f = input("Enter the path to count its file and folders: ")

# file_list1 = os.listdir(f)
# file_count = 0
# folder_count = 0
# for file in file_list1:
#     if os.path.isfile(file):
#         file_count = file_count + 1
#     else:
#         folder_count = folder_count +1

# print(f"Total {file_count} File And {folder_count} Folder Found in This Directory-Structure/Users/frutos/F0x/Devops Projects/Python Projects/pycls/for-githu !")




#----------------------
# # FILE EXAMINE METHODS

# # os.path.exists(path) - Retuns true if file/folder exists on given path
# f = input("input folder name to create: ")
# folder = ".//files//" + f  # concating user's foldername with a path: <./files/myfolder>
# if os.path.exists(folder):
#     print(f"Folder with name is already exists in this directory: ")
# else:
#     os.mkdir(folder)
#     print(f"folder {folder} is creadted in path:  {os.getcwdb()}")


#----------------------
# # WRITE PROGRAM TO LIST CONTENT OF A FOLDER AND DELETE THAT DIRECTORY STRUCTURE
# # os.listdir(path='. OR PATH OF FOLDER') - lists all the file/fodler of currect directory 
# # os.listdir(path='..') - lists all the file/fodler of parent/previous directory
# # suttil.rmtree(path) - deletes complete directory structure, doenst matter of empty or non-empty.

# try:
#     os.mkdir("folder1")
#     os.chdir("folder1")
#     print(os.getcwdb())
# except FileExistsError:
#     print("Folder with this name is already exists!")

# with open("mytext.txt", "w") as f:
#     f.write("This is example text written in mytext.txt")
# # creating folder2 inside folder1
# try:
#     os.mkdir("folder2")
# except:
#     print("Folder with this name is already exists!")

# #listing directory structure of folder1
# dir_list = os.scandir("folder1")# retruns DirEntry iterator, which holds all folders and file properties
# print("DIRECTORY STRCUTE OF 'folder1' ")
# for dir in dir_list: # each file/folder will store in 'dir' as 'DirEntry' object, and this object have many properties/methods like name, path, is_file() is_foler() etc.
#     print(dir.name)

# # deleting all directory structure of folder1
# shutil.rmtree("folder1")
# print("folder1's directory structure is deleted !")


#----------------------
# # CREATE ONE FOLDER AND DELETE THAT FOLDER
# #os.rmdir(path) - removes empty directory, dir is not empty, raises OSError.

# os.mkdir("empty-folder1")
# print("folder is created")

# os.rmdir("empty-folder1")
# print("folder is deleted !")


#----------------------

# # os.mkdir(path, mode=0o777, *, dir_fd=None) - Create Directory at given path. 
# try:
#     os.mkdir("/Users/frutos/F0x/Devops Projects/Python Projects/pycls/for-github/os-module-folder1")
#     print("folder created ! Creating employee.txt in this filder")
#     os.chdir("/Users/frutos/F0x/Devops Projects/Python Projects/pycls/for-github/os-module-folder1")
#     with open("os-module-test.txt", "w") as f:
#         f.write("I love python")

# except FileExistsError: #exception raised when folder with this name already exists.
#     print(f"This Folder Name Already Exists ")
# except FileNotFoundError: #exception raised when any parent dirctory doesnt exist
#     print("This Path Doent Exists")

#----------------------

# # os.chdir() - Change Directory To Given Path.
# cwd = os.getcwdb()
# print(f"My curent working directory is : {cwd}")
# newdir = os.chdir("/Users/frutos")
# print(f"Directory Changed: {newdir}")


#----------------------

# # os.getcwdb() - Returns Current Working Directory.
# print()
# print(os.getcwdb())


#----------------------

