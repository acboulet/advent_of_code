import sys
sys.path.append('../')
print(sys.path)

from advent2023 import PerLineImport



class GearRatios_v1(PerLineImport):
    """
    1. Add up all numbers adjacent to a symbol in the provided input  
    """
    def __init__(self, datafile) -> None:
        super().__init__(datafile)
        self.engine_schematic = []

        self.symbols = '$*#@!%^&'

        ## row cursor locations starting at idx 0
        self.r1 = 2
        self.r2 = 3
        self.r3 = 4

        self.engine_size = 0
        self.engine_width = 0
        

    def import_engine(self):
        with open(self.datafile, 'r') as file:
            for line in file:
                self.engine_schematic.append(line.strip())
              
        self.engine_size = len(self.engine_schematic)
        self.engine_width = len(self.engine_schematic[0])

    def process_lines(self, line):
        print(line.strip())
        
        valid_numbers = []
        ## First row
        if self.r1 == 0:
            numbers_in_row = self.find_numbers(self.r1)
        elif self.r3 == self.engine_size:
            ## last row
            pass
        else:
            numbers_in_row = self.find_numbers(self.r1)
            print(numbers_in_row)
            for key in numbers_in_row.keys():
                if self.is_number_valid(idxs=numbers_in_row[key]):
                    valid_numbers.append(key)

        print(valid_numbers)
        return

    def find_numbers(self, row_idx):
        """Find numbers and stores the number and indices"""
        found = {}
        row = self.engine_schematic[row_idx]
        current_number = ''
        indices = []
        for idx, char in enumerate(list(row)):
            if char.isdigit():
                current_number = f"{current_number}{char}"
                indices.append(idx)
            else:
                ## If number found, append then reset
                if current_number:
                    found[current_number] = indices.copy()
                ## Reset
                current_number = ''
                indices = []
        return found

    def is_number_valid(self, idxs):
        """Checks adjacent areas to see if numbers are valid"""
        for idx in idxs:
            idx = int(idx)
            ## Check left
            left = idx-1
            if left >= 0:
                up = self.engine_schematic[self.r1][left]
                mid = self.engine_schematic[self.r2][left]
                down = self.engine_schematic[self.r3][left]
                if up in self.symbols or mid in self.symbols or down in self.symbols:
                    return True
            
            ## check same
            up = self.engine_schematic[self.r1][idx]
            mid = self.engine_schematic[self.r2][idx]
            down = self.engine_schematic[self.r3][idx]
            if up in self.symbols or mid in self.symbols or down in self.symbols:
                return True   
            
            ## check right
            right = idx + 1
            if right < self.engine_width:
                up = self.engine_schematic[self.r1][right]
                mid = self.engine_schematic[self.r2][right]
                down = self.engine_schematic[self.r3][right]
                if up in self.symbols or mid in self.symbols or down in self.symbols:
                    return True 
            
        return False



    def main(self):
        self.import_engine()
        self.import_file()
        for line in self.engine_schematic:
            print(line)
        return

if __name__ == "__main__":
    file = 'test.txt'
    # file = 'test2.txt'
    # file = 'data.txt'

    advent = GearRatios_v1(file).main()
    ## answer 
