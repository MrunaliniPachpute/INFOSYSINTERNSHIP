import os

#checking current working directory
# curr_dir = os.getcwd()
# print(curr_dir)

#listing all files and folders - returns list of string of names of files and folders in cwd
# items = os.listdir()
# print(items)

#creating and removing a folder
# os.mkdir("new folder")
# print("folder created successfully")
# os.rmdir("new folder")
# print("folder removed successfully")

#changing directory
print(os.getcwd())
os.chdir("c:\\Users\\mruna\\Desktop")
print(os.getcwd())