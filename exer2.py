import os
path = str(input("Input path: "))
print(get_num_files(path))
def get_num_files(path):
    num_files = 0
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            num_files += 1
        if os.path.isdir(full_path):
            num_files += get_num_files(full_path)
    return num_files
