

class RockPaperScissors_v1():
    scores = []


    def process_data(self, filepath):
        with open(filepath) as f:
            for line in f:
                ## For each turn, obtain the Elf's move [0], and the player's move [1]
                elf, player = line.rstrip().split(' ')
                self.scores.append(self.count_score(elf, player))

    
    def count_score(self, elf, player):
        """
        Determines the player score for the round
        """
        turn_score = 0
        p_rock, p_paper, p_scissors = 'X', 'Y', 'Z'
        e_rock, e_paper, e_scissors = 'A', 'B', 'C'
        ## Rock
        if player == p_rock:
            turn_score += 1
            if elf == e_rock:
                turn_score += 3 ## Tie
            elif elf == e_scissors:
                turn_score += 6 ## Win
        ## Paper
        elif player == p_paper:
            turn_score += 2
            if elf == e_paper:
                turn_score += 3 ## Tie
            elif elf == e_rock:
                turn_score += 6 ## Win
        ## Scissors
        elif player == p_scissors:
            turn_score +=3
            if elf == e_scissors:
                turn_score += 3 ## Tie
            elif elf == e_paper:
                turn_score += 6 ## Win
        else:
            print(f"Player: {player} doesn't match")

        return turn_score


class RockPaperScissors_v2(RockPaperScissors_v1):
    p_rock, p_paper, p_scissors = 'X', 'Y', 'Z'
    e_rock, e_paper, e_scissors = 'A', 'B', 'C'

    def process_data(self, filepath):
        with open(filepath) as f:
            for line in f:
                elf, goal = line.rstrip().split(' ')  
                self.scores.append(self.count_score(elf, goal))

    def count_score(self, elf, goal):
        turn_score = 0
        if goal == 'X': ## Need to lose
            if elf == self.e_rock:
                turn_score += 3 ## Play scissors
            elif elf == self.e_paper:
                turn_score += 1 ## Player rock
            elif elf == self.e_scissors:
                turn_score += 2 ## Player plays paper
        elif goal == 'Y': ## Need to tie
            turn_score += 3
            if elf == self.e_rock:
                turn_score += 1 ## Play rock
            elif elf == self.e_paper:
                turn_score += 2 ## Player paper
            elif elf == self.e_scissors:
                turn_score += 3 ## Player plays scissors
        elif goal == 'Z': ## Need to win
            turn_score += 6
            if elf == self.e_rock:
                turn_score += 2 ## Play paper
            elif elf == self.e_paper:
                turn_score += 3 ## Player scissors
            elif elf == self.e_scissors:
                turn_score += 1 ## Player plays rock
        return turn_score

if __name__ == '__main__':
    test_file = 'test_data.txt'
    real_file = 'real_data.txt'

    # v1 = RockPaperScissors_v1()
    # v1.process_data(real_file)
    # print(RockPaperScissors_v1.scores)
    # print(sum(RockPaperScissors_v1.scores))

    v2 = RockPaperScissors_v2()
    v2.process_data(real_file)
    print(v2.scores)
    print(sum(v2.scores))