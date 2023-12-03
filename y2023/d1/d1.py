## calibration value
##  combine first and last digit to get single 2-digit number
## sum up these values

# class AdventImport():
#     def __init__(self, datafile) -> None:
#         self.datafile = datafile

    
#     def import_file(self):
#         with open(self.datafile, 'r') as file:
#             for line in file:
#                 self.process_lines(line)

#     def process_lines(self, line):
#         print(line.rstrip())

import sys
import os
sys.path.append('workspaces/advent_of_code')

print(os.getcwd())
from y2023.advent2023 import PerLineImport
    
class CalibrationValue(PerLineImport):
    def process_lines(self, line):
        print(line.strip() * 2)
    

if __name__ == "__main__":
    file = 'python/y2023/d1/test.txt'

    # advent = AdventImport(file)
    # advent.import_file()

    calib = CalibrationValue(file)
    calib.import_file()