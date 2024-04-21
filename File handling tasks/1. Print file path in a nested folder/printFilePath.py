from os import walk

# input folder path
dir_path = input("Enter a directory path:")

# a function to get the directory path and name of all files
def get_file_names(dir_path):
# list to store files name
    names = []
    for (dir_path, dir_names, file_names) in walk(dir_path):
        for dir in dir_names:
            names.extend(get_file_names(dir))
        for name in file_names:
            names.append(dir_path + "\\" + name)
    return names

print(get_file_names(dir_path)) 