# import os

# path = input("Enter the path: ")

# print("Directories: ")
# for entry in os.listdir(path):
#     if os.path.isdir(os.path.join(path, entry)):
#         print(entry)

# print("Files: ")
# for entry in os.listdir(path):
#     if os.path.isfile(os.path.join(path, entry)):
#         print(entry)

# print("All: ")
# print(os.listdir(path))
# import os

# path = input()
# if os.path.exists(path):
#     print('path exist')
#     if os.access(path,os.R_OK):
#         print('path is readable')
#     else:
#         print('path isnt readable')
#     if os.access(path,os.W_OK):
#         print('path is writable')
#     else:
#         print('path isnt writable')
#     if os.access(path,os.X_OK):
#         print('path is executable')
#     else:
#         print('path isnt executable')
# else:
#     print('path doesnt exist')
# import os
# path = input()
# if os.path.exists(path):
#     print('path exists')
#     print('filename '+ os.path.basename(path))
#     print('Directory ' + os.path.dirname(path))
# else:
#     print('path doesnt exists')
# filep = input()
# try:
#     with open(filep, 'r') as file:
#         lines = file.readlines()
#         print(len(lines))
# except FileNotFoundError:
#     print('file wasnt found')
# file_path = input()
# data_list = ['apple', 'banana', 'cherry']

# with open(file_path, 'w') as file:
#     for item in data_list:
#         file.write(item + '\n')
#     print("List written")
# import string

# for letter in string.ascii_uppercase:
#     with open(f"{letter}.txt", 'w') as file:
#         file.write(letter)
# print('generated')
# spath = input()
# dpath = input()
# try:
#     with open(spath, 'r') as sf:
#         content = source_file.read()
#     with open(dpath, 'w') as df:
#         df.write(content)
#     print("copied")
# except FileNotFoundError:
#     print('not found')
# import os
# fpath = input()
# if os.path.exists(fpath):
#     if os.access(fpath, os.W_OK):
#         os.remove(fpath)
#         print('deleted ')
#     else:
#         print('file cant be deleted')
# else:
#     print('file doesnt exist')