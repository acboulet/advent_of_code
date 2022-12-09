class SupplyStacks():
    ## Marked crates to be mvoed by a cargo crane
    ## Need to track the movement of crates within stacks

    def __init__(self) -> None:
        self.shipdeck = [] ## Add the stacks of crates here.

    def process_data(self, filepath):
        is_built = False ## Tracks whether the shipdeck is built
        with open(filepath) as f:
            for line in f:
                line = line.strip('\n') ## keep empty spaces
                if line.startswith('move'):
                    self.move_boxes(line)
                elif '[' in line:
                    self.build_initial_stack(line, is_built)
                    is_built = True
                else:
                    print('empty line?')
                # print(self.shipdeck) 
                # print()

    def build_initial_stack(self, line:str, is_built):
        """
        Builds the initial stack
        """

        ## Length is 11
        line_size = len(line)
        no_stacks = line_size//3
        if not is_built:
            self.shipdeck = [['|'] for _ in range(no_stacks + 1)] ##Bottom of stacks
        
        current_stack = 1 ## Start at one to avoid idx confusion
        ## Boxes appear at idx1, idx5, etc. 
        for n in range(1, line_size, 4): ## Location of each box
            if line[n].isalpha():
                self.shipdeck[current_stack].insert(1, line[n-1:n+2])
            current_stack += 1

    def move_boxes(self, line: str):
        """
        Move boxes based on directions.
        """
        ## The first number is how many boxes
        ## Second number is starting location
        ## Third number is end location
        no_boxes = int(line.split(' ')[1])
        start = int(line.split(' ')[3])
        end = int(line.split(' ')[5])

        for moves in range(no_boxes):
            # print(f"Move {start} to {end}")
            crate = self.shipdeck[start].pop()
            self.shipdeck[end].append(crate)


class SupplyStacks_v2(SupplyStacks):
    ## Cargo is now moved in a single step
    ## 

    def __init__(self) -> None:
        super().__init__()
    
    def process_data(self, filepath):
        is_built = False ## Tracks whether the shipdeck is built
        with open(filepath) as f:
            for line in f:
                line = line.strip('\n') ## keep empty spaces
                if line.startswith('move'):
                    self.move_boxes_v2(line)
                elif '[' in line:
                    self.build_initial_stack(line, is_built)
                    is_built = True
                else:
                    pass
                    # print('empty line?')
                # print(self.shipdeck) 
                # print()

    def move_boxes_v2(self, line: str):
                ## The first number is how many boxes
        ## Second number is starting location
        ## Third number is end location
        no_boxes = int(line.split(' ')[1])
        start = int(line.split(' ')[3])
        end = int(line.split(' ')[5])

        stack_idx = no_boxes * -1
        
        ## Save the boxes to remove, and delete them from original list
        stack = self.shipdeck[start][stack_idx:]
        del self.shipdeck[start][stack_idx:]
            
        self.shipdeck[end].extend(stack)
        
        # for stack in self.shipdeck:
        #     print(stack)
        # print()

if __name__ == '__main__':

    
    test_file = 'test_data.txt'
    real_file = 'real_data.txt'

    # v1 = SupplyStacks()
    # v1.process_data(real_file)
    # for stack in v1.shipdeck:
    #     print(stack)

    v2 = SupplyStacks_v2()
    v2.process_data(real_file)
    for stack in v2.shipdeck:
        print(stack)