## calibration value
##  combine first and last digit to get single 2-digit number
## sum up these values

import sys
# sys.path.append('/workspaces/advent_of_code/y2023')
## Look at parent directory for imports
sys.path.append('../')


import os
print(os.getcwd())
from advent2023 import PerLineImport
    
class CalibrationValue(PerLineImport):
    def process_lines(self, line):
        print(line.strip() * 2)
    

if __name__ == "__main__":
    file = 'test.txt'

    # advent = AdventImport(file)
    # advent.import_file()

    calib = CalibrationValue(file)
    calib.import_file()