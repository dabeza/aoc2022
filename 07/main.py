f = open("input.txt","r")
lines = f.readlines()
SIZE_LIMIT =        100000
FILE_SYSTEM_SIZE =  70000000
UPDATE_SIZE =       30000000
# class definitions
class Directory:
    def __init__(self,name,parent) -> None:
        self.files = []
        self.directories = []
        self.name = name
        self.parent = parent

    def get_size(self) -> int:
        size = 0
        for file in self.files:
            size += file.get_size()
        for directory in self.directories:
            size += directory.get_size()
        return size

    def add_directory(self,name):
        new_dir = Directory(name,self) 
        self.directories.append(new_dir)
        return new_dir

    def add_file(self,name,size) -> None:
        self.files.append(File(name,size))
        return


class File :
    def __init__(self,name,size) -> None:
        self.name = name
        self.size = size
    
    def get_size(self) -> int:
        return self.size
    
lines.pop(0) # remove first input, i.e. $ cd / 
current_dir = Directory("/",None)

def back_out(current_dir,total_size,size_list):
    dir_size = current_dir.get_size()
    # print(current_dir.name + ": " + str(dir_size))
    if dir_size < SIZE_LIMIT: # save size if smaller than limit
        total_size += dir_size
    size_list.append(dir_size)
    current_dir = current_dir.parent
    return current_dir,total_size,size_list

size_list = []
total_size = 0
for line in lines:
    args = (line.strip().split(" "))
    if args[1] == "cd":
        # print(args[2])
        if args[2] == "..": # backing out, before backing out, I want to check the total size of current directory
             current_dir,total_size,size_list = back_out(current_dir,total_size,size_list)
        else:
            current_dir = current_dir.add_directory(args[2])
    elif (args[0] != "dir") & (args[1] != "ls"): # This line is a file, add to current directory
        # print(int(args[0]))
        current_dir.add_file(args[1],int(args[0]))
        # do not need to do anything for e.g. "dir a" lines as the operator is going into all files anyway (...?)

while current_dir.parent != None:
    current_dir,total_size,size_list = back_out(current_dir,total_size,size_list)

main_directory_size = current_dir.get_size()
print(current_dir.name + ": " + str(main_directory_size))

available_space = FILE_SYSTEM_SIZE - main_directory_size

size_list.sort(reverse=False)
for size in size_list:
    print(available_space + size)
    if available_space + size > UPDATE_SIZE:
        break

print("answer 1 is: ",total_size)
print("answer 2 is: ",size)
