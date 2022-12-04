

class RuckSackReorganization_v1():
    ## Each sack contains two large compartments
    ## Input is list of items in each rucksack
    ## Each item is a single letter character (case-sensitive)
    ## Each rucksack has half items in first compartment, and half in second compartment
    ## Assign a priority value
    ## Only items that are in both compartments get a priority value

    ## The index value of the alphabet number is equivalent to the score
    items = '.abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def __init__(self) -> None:
        self.all_rucksack = []
        self.rucksack_scores = []

    def process_data(self, filepath):
        with open(filepath) as f:
            for line in f:
                line = line.rstrip()
                split = len(line) // 2
                first = line[0:split]
                second = line[split:]
                self.all_rucksack.append([first, second])

    def count_priority_score(self):
        for rucksack in self.all_rucksack:
            ## Find all common items
            common_items = []
            for idx, char in enumerate(rucksack[0]):
                ## item is in both rucksacks, but not already identified
                if char in rucksack[1] and char not in common_items:
                    common_items.append(char)
            ## Calculate the scores
            rucksack_score = 0
            for item in common_items:
                score = self.items.index(item)
                rucksack_score += score
        
            self.rucksack_scores.append(rucksack_score)


class RuckSackReorganization_v2(RuckSackReorganization_v1):
    ## Elves in the groups now.
    ## An item in common to three elvs is their badge
    ## Each three elves (lines) is a group.
    ## What item is common to these three elves?

    

    def __init__(self) -> None:
        self.badge_scores = []
        super().__init__()


    def count_badge_scores(self):
        num_groups = len(self.all_rucksack) // 3
        first_elf = 0
        groups = 1
        ## For each group, find the common item
        while groups <= num_groups:
            bag1 = ''.join(self.all_rucksack[first_elf])
            bag2 = ''.join(self.all_rucksack[first_elf + 1])
            bag3 = ''.join(self.all_rucksack[first_elf + 2])

            common_char = ''.join(set(bag1).intersection(bag2).intersection(bag3))

            self.badge_scores.append(self.items.index(common_char))
            ## Move to next elf group
            groups += 1
            first_elf += 3



if __name__ == "__main__":

    test_file = 'test_data.txt'
    real_file = 'real_data.txt'

    v1 = RuckSackReorganization_v1()
    v1.process_data(real_file)
    # print(v1.all_rucksack)
    v1.count_priority_score()
    # print(v1.rucksack_scores)
    print(sum(v1.rucksack_scores))

    v2 = RuckSackReorganization_v2()
    v2.process_data(real_file)
    v2.count_badge_scores()
    print(v2.badge_scores)
    print(sum(v2.badge_scores))