import pathlib
import sys


class Directory():
    def __init__(self) -> None:
        self.parent = None
        self.subfolders = []
        self.name = None
        self.size = 0
    
    def print_contents(self, action):
        print(f"'action:{action}'   name: {self.name} parent:{None if self.parent is None else self.parent.name} "
              f"num_subfolders:"
              f"{len(self.subfolders) if self.subfolders else None} size:{self.size}")

class File(Directory):
    def __init__(self) -> None:
        super().__init__()
        ## Set subfolders to none for a file
        self.subfolders = None
        


class NoSpaceOnDevice():
    ## Data is a list of linux navigation instructions
    ## Create the list of directories with file sizes
    ## Find the directory with the largest file size


    def __init__(self, puzzle_input) -> None:
        ## create the root node
        self.commands = puzzle_input.strip().split('\n')
        self.root = None
        self.curr_node = None

    def parse_commands(self):
        for command in self.commands:
            match command.split(' '):
                case '$', 'cd', directory:
                    if directory == '..':
                        ## Move current node up one
                        self.curr_node = self.curr_node.parent
                    elif directory == '/':
                        ## Initial creation at root
                        self.root = Directory()
                        self.root.name = directory
                        self.curr_node = self.root
                    else:
                        ## If moving to new node,
                        ## Find that node in the subfolders
                        ## Set curr_node to that new node
                        next_node = [d for d in self.curr_node.subfolders if d.name == directory]
                        self.curr_node = next_node[0]
                case '$', 'ls':
                    continue
                case 'dir', directory:
                    ## Create a new directory
                    ## Set the parent as current
                    ## Add new directory to current dir
                    new_dir = Directory()
                    new_dir.name = directory
                    new_dir.parent = self.curr_node
                    self.curr_node.subfolders.append(new_dir)
                case size, file:
                    new_file = File()
                    new_file.name = file
                    new_file.size = int(size)
                    new_file.parent = self.curr_node
                    self.curr_node.subfolders.append(new_file)
        return
        

    def calculate_folder_sizes(self, dir=None, size=0):
        ## First time calling, dir should be set to root.

        ## Recursively tracks files/folder sizes as it moves through tree
        if dir.subfolders is None:
            return dir, dir.size
        else:
            ## Return the sizes for each subdir/file in dir
            size_sum = sum([self.calculate_folder_sizes(dir=subdir, size=size)[1] for subdir in dir.subfolders])
            dir.size += size_sum
            return dir, dir.size
                    

    def sum_directories_less_than_100000(self, dir, total):
        if dir.subfolders is None:
            return dir, total
        else:
            ## Add dir size if directory smaller than 100k, else 0
            total += dir.size if dir.size <= 100000 else 0
            for subdir in dir.subfolders:
                total = self.sum_directories_less_than_100000(subdir, total)[1]
            
            return dir, total
    

    def solve_v1(self):
        self.parse_commands()
        self.calculate_folder_sizes(dir=self.root, size=0)
        sol1 = self.sum_directories_less_than_100000(dir=self.root, total=0)[1]
        print(f"Solution 1: {sol1}")

        





if __name__ == '__main__':

    test_file = 'test_data.txt'
    real_file = 'real_data.txt'

    puzzle_input = pathlib.Path(real_file).read_text().strip()
    tester = NoSpaceOnDevice(puzzle_input=puzzle_input)
    tester.solve_v1()
    
