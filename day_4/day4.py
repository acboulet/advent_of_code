
class CampCleanup():
    ## Camp sections have unique ID number
    ## Input is list of section assignments for each elf pair
    ## First item per line is range of assigned sections for first elf
    ## Sasme thing for second item per line (inclusive with final number)

    

    def __init__(self) -> None:
        ## Pairs that have one section completed overlapped by the other assignment
        self.cleaning_pairs = []
        self.full_contained = 0

    def process_data(self, filepath):
        with open(filepath) as f:
            for line in f:
                self.cleaning_pairs.append(line.rstrip().split(','))

    def overlapping_assignments(self):
        for pair in self.cleaning_pairs:
            ## Determine the range of cleaning assignments for each elf
            first_set = [int(n) for n in pair[0].split('-')]
            
            second_set = [int(n) for n in pair[1].split('-')]

            ## First is contained
            if first_set[0] >= second_set[0] and first_set[1] <= second_set[1]:
                self.full_contained += 1

            ## Second set contained
            elif second_set[0] >= first_set[0] and second_set[1] <= first_set[1]:
                self.full_contained += 1


class CampCleanUp_v2(CampCleanup):
    
    def __init__(self) -> None:
        super().__init__()
        self.partial_contain = 0

    def partial_overlap(self):
        for pair in self.cleaning_pairs:
            min_1, max_1 = [int(n) for n in pair[0].split('-')]
            min_2, max_2 = [int(n) for n in pair[1].split('-')]



            ## If either 1 values are within the range-2
            if min_1 >= min_2 and min_1 <= max_2:
                self.partial_contain += 1
            elif max_1 >= min_2 and max_1 <= max_2:
                self.partial_contain += 1

            ## Of i 2 values overlap within the range-1
            elif min_2 >= min_1 and min_2 <= max_1:
                self.partial_contain += 1
            elif max_2 >= min_1 and max_2 <= max_1:
                self.partial_contain += 1

            

            

if __name__ == "__main__":

    test_file = 'test_data.txt'
    real_file = 'real_data.txt'

    v1 = CampCleanup()
    v1.process_data(real_file)
    v1.overlapping_assignments()
    print(v1.full_contained)

    v2 = CampCleanUp_v2()
    v2.process_data(real_file)
    v2.partial_overlap()
    print(v2.partial_contain)