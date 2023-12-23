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
            return int(number_string)
        else:
            return calib_string[idx_num]

    
    def find_last_digit(self, calib_string):
        ## Largest index containing a number?
        idx_num = -1
        idx_str = -1
        potential_idx_num = []

        # Find the index of the last digit in the string
        potential_idx_num = [index for index, char in enumerate(calib_string) if char.isdigit()]
        if potential_idx_num:
            idx_num = max(potential_idx_num)
        
        ## Largest index for the string?
        potential_idx_str = self.find_string_numbers(calib_string)
        if potential_idx_str:
            idx_str = max(potential_idx_str.keys())


        ## Which one appeared last?
        if idx_str > idx_num:
            return potential_idx_str[idx_str]
        else:
            return int(calib_string[idx_num])

    def find_string_numbers(self, calib_string):
        ## Find indexes and strings of numbers in the calib_String
        ## Track all string numbers found where key is index, and value is string number
        potential_idx_str = {}

        for word, number in self.string_numbers.items():
            index = calib_string.find(word)
            if index != -1:
                potential_idx_str[index] = number
        return potential_idx_str

    def main(self):
        self.import_file()
        print(self.calib_sum)


class CalibrationValue_GPT(PerLineImport):
    def __init__(self, datafile) -> None:
        super().__init__(datafile)

        self.calib_sum = 0
        self.string_numbers = {
            'one': 1,
            'two': 2,
            'three': 3,
            'four': 4,
            'five': 5,
            'six': 6,
            'seven': 7,
            'eight': 8,
            'nine': 9
        }

    def process_lines(self, line):
        first = self.find_first_digit(line.strip())
        last = self.find_last_digit(line.strip())

        # Check if first anzd last are valid digits, then add to sum
        if first is not None and last is not None:
            two_digit_number = int(str(first) + str(last))
            self.calib_sum += two_digit_number

    def find_first_digit(self, calib_string):
        int_idx = 100
        str_idx = 100
        for idx, char in enumerate(calib_string):
            if char.isdigit():
                int_idx = int(idx)
                break

        potential_idx_str = self.find_string_numbers(calib_string)
        if potential_idx_str:
            str_idx = min(potential_idx_str.keys())

        if str_idx < int_idx:
            return potential_idx_str[str_idx]
        else:
            return calib_string[int_idx]

    def find_last_digit(self, calib_string):
        int_idx = -1
        str_idx = -1
        potential_idx_num = [index for index, char in enumerate(calib_string) if char.isdigit()]
        if potential_idx_num:
            int_idx = int(max(potential_idx_num))

        potential_idx_str = self.find_string_numbers(calib_string)
        if potential_idx_str:
            str_idx = max(potential_idx_str.keys())

        if str_idx > int_idx:
            return potential_idx_str[str_idx]
        else:
            return calib_string[int_idx]

    def find_string_numbers(self, calib_string):
        potential_idx_str = {}
        for word, number in self.string_numbers.items():
            index = calib_string.find(word)
            if index != -1:
                potential_idx_str[index] = number
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

    calib = CalibrationValue_GPT(file)
    calib.main()
    ## answer 
    