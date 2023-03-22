class MyDirectory:
    def __init__(self, dir_name, dir_contents):
        self.dir_name = dir_name
        self.dir_contents = dir_contents

class MyFile:
    def __init__(self, file_name):
        self.file_name = file_name
 
 
def populateDirectory(dir_name, dir_dictionary):
    if dir_name[0] == "f" or dir_name not in dir_dictionary:
        return MyFile(dir_name)
    else:
        return MyDirectory(dir_name, [populateDirectory(i, dir_dictionary) for i in dir_dictionary[dir_name]])


def print_directory(root, i_spaces):
    if isinstance(root,MyDirectory):
        print(f'{i_spaces}{root.dir_name}') 
        for r in root.dir_contents:
            print_directory(r, i_spaces+'   ')
    else:
        print(f'{i_spaces}{root.file_name}')


if __name__ == '__main__':
    directory_dict = {
        'dir0': ['f0.txt', 'f1.txt','dir1', 'dir2'],
        'dir1': ['dir3', 'f2.txt', 'dir4'],
        'dir4': ['f3.txt'],
        'dir2': ['dir5', 'dir6'],
        'dir6': ['f4.txt']
    }

    result = populateDirectory('dir0', directory_dict) 
   #  print(result.dir_contents)
    print_directory(result,'')