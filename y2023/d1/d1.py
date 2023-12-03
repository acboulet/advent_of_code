## calibration value
##  combine first and last digit to get single 2-digit number
## sum up these values

import sys
# sys.path.append('/workspaces/advent_of_code/y2023')
## Look at parent directory for imports
sys.path.append('../')

from advent2023 import PerLineImport
    
class CalibrationValue_v1(PerLineImport):
    def __init__(self, datafile) -> None:
        super().__init__(datafile)

        self.calib_sum = 0

    def process_lines(self, line):
        ## Combine first and last digit
        ## Track sum
        first = self.find_first_digit(line.strip())
        last = self.find_last_digit(line.strip())

        self.calib_sum += int(f'{first}{last}')
    
    def find_first_digit(self, calib_string):
        for char in calib_string:
            if char.isdigit():
                return char
        return None
    
    def find_last_digit(self, calib_string):
        for char in reversed(calib_string):
            if char.isdigit():
                return char
        return None

    def main(self):
        self.import_file()
        print(self.calib_sum)


class CalibrationValue_v2(PerLineImport):
    def __init__(self, datafile) -> None:
        super().__init__(datafile)

        self.calib_sum = 0
        self.string_numbers = {
            'one' : 1, 
            'two' : 2,
            'three': 3,
            'four' : 4, 
            'five' : 5, 
            'six' : 6, 
            'seven' : 7, 
            'eight' : 8, 
            'nine': 9}

    def process_lines(self, line):
        ## Combine first and last digit
        ## Track sum
        first = self.find_first_digit(line.strip())
        last = self.find_last_digit(line.strip())

        # print(first, last)

        self.calib_sum += int(f'{first}{last}')
    
    def find_first_digit(self, calib_string):
        ## Track idx to see which appears first
        idx_num = 10000
        idx_str = 10000
        number_string = ""
        ## Find index of first number
        for index, char in enumerate(calib_string):
            if char.isdigit():
                idx_num = index
                break
        
        ## What is the smallest index found?
        potential_idx_str = self.find_string_numbers(calib_string)
        if potential_idx_str:
            idx_str = min(potential_idx_str.keys())
            number_string = potential_idx_str[idx_str]

        ## Which one appeared first?
        if idx_str < idx_num:
            return self.string_numbers[number_string]
        else:
            return calib_string[idx_num]

    
    def find_last_digit(self, calib_string):
        ## Largest index containing a number?
        idx_num = -1000
        potential_idx_num = []
        for index, char in enumerate(calib_string):
            if char.isdigit():
                potential_idx_num.append(index)
        if potential_idx_num:
            idx_num = max(potential_idx_num)
        
        ## Largest index for the string?
        idx_str = -1000
        potential_idx_str = self.find_string_numbers(calib_string)
        if potential_idx_str:
            idx_str = max(potential_idx_str.keys())
            number_string = potential_idx_str[idx_str]
            ## calculated value is length of the string as well
            idx_str = idx_str + len(number_string)

        ## Which one appeared last?
        if idx_str > idx_num:
            return self.string_numbers[number_string]
        else:
            return calib_string[idx_num]

    def find_string_numbers(self, calib_string):
        ## Find indexes and strings of numbers in the calib_String
        ## Track all string numbers found where key is index, and value is string number
        potential_idx_str = {}
        ## Find the index of the string number
        for s in self.string_numbers.keys():
            i = calib_string.find(s)
            ## Anything other means it was found
            if i > -1:
                potential_idx_str[i] = s
        return potential_idx_str

    def main(self):
        self.import_file()
        print(self.calib_sum)


if __name__ == "__main__":
    # file = 'test.txt'
    # file = 'test2.txt'
    file = 'data.txt'

    # calib = CalibrationValue_v1(file)
    # # calib.import_file()
    # calib.main()
    # ## answer 54632

    calib = CalibrationValue_v2(file)
    calib.main()
    ## answer 
    