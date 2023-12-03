## calibration value
##  combine first and last digit to get single 2-digit number
## sum up these values

import sys
# sys.path.append('/workspaces/advent_of_code/y2023')
## Look at parent directory for imports
sys.path.append('../')

from advent2023 import PerLineImport
    
class CalibrationValue(PerLineImport):
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

    def main_v1(self):
        self.import_file()
        print(self.calib_sum)

    def main_v2(self):
        self.import_file()
        # print(self.calib_sum)


if __name__ == "__main__":
    file = 'test.txt'
    file = 'data.txt'

    calib = CalibrationValue(file)
    # calib.import_file()
    calib.main_v1()
    ## answer 54632

    calib.main_v2()
    