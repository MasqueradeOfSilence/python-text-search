import os

print("Hello string finder!")

search_path = input("What path do you want to search? (Type d for default) ")
file_type = input("What type of file do you want to search? ")
search_string = input("Enter your search string: ")

# Files must end with a /
if not (search_path.endswith("/") or search_path.endswith("\\")):
    search_path += "/"

# Defaults
if not os.path.exists(search_path) or search_path == "d/":
    search_path = "C:/Users/alexc/OneDrive/Documents/testFolder/"

print("\nThanks! Searching...\n")

for file_name in os.listdir(path=search_path):
    if file_name.endswith(file_type):
        opened_file = open(search_path + file_name)
        line = opened_file.readline()
        line_num = 1
        while line != '':
            index = line.find(search_string)
            if index != -1:
                print("String found in " + file_name + ", line " + str(line_num) + ", "
                      + "index " + str(index) + ". Line: " + line)
            line = opened_file.readline()
            line_num += 1
        opened_file.close()

# ©Alex Neville, January 2021
# 🍄
