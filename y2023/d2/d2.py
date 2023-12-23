import sys
sys.path.append('../')
print(sys.path)

from advent2023 import PerLineImport


## The line identifies the 'Game ##'
## Followed by number and color of cubes column seperarted
## Include subsets of how they were revealed seperated by ';'
## Is the game True if only 12 red, 13 green, and 14 blue

class CubeConundrum_v1(PerLineImport):
    def __init__(self, datafile) -> None:
        super().__init__(datafile)

        ## MAX values
        self.RED = 12
        self.GREEN = 13
        self.BLUE = 14

        self.TRUE_GAMES = 0

    def process_lines(self, line):
        # print(line.strip())
        game = self.count_cubes(line.strip())
        is_valid_game = self.check_game(game)
        # print(is_valid_game)
        if is_valid_game:
            self.TRUE_GAMES += int(game['game_ID'])
        return
    
    def count_cubes(self, line):
        # Split the line based on ';'
        ## Remove the gameID at the front
        subsets = line.split(':')[-1].split(';')

        max_red = 0
        max_green = 0
        max_blue = 0

        for subset in subsets:
            colors = subset.split(', ')
            for color in colors:
                count, col = color.split()
                count = int(count)
                if col == 'red':
                    max_red = max(max_red, count)
                elif col == 'green':
                    max_green = max(max_green, count)
                elif col == 'blue':
                    max_blue = max(max_blue, count)

        return {
            'game_ID': line.split(':')[0].split(' ')[-1],
            'max_red': max_red,
            'max_green': max_green,
            'max_blue': max_blue
        }

    def check_game(self, cubes_count):
        max_red = cubes_count['max_red']
        max_green = cubes_count['max_green']
        max_blue = cubes_count['max_blue']

        if max_red > self.RED or max_green > self.GREEN or max_blue > self.BLUE:
            return False
        else:
            return True

    def main(self):
        lines = self.import_file()
        print(self.TRUE_GAMES)


class CubeConundrum_v2(PerLineImport):
    def __init__(self, datafile) -> None:
        super().__init__(datafile)

        ## MAX values
        self.RED = 12
        self.GREEN = 13
        self.BLUE = 14

        self.TOTAL_POWER = 0

    def process_lines(self, line):
        # print(line.strip())
        game = self.count_cubes(line.strip())
        
        game_power = (game['max_red'] * game['max_green'] * game['max_blue'])
        self.TOTAL_POWER += game_power
        return
    
    def count_cubes(self, line):
        # Split the line based on ';'
        ## Remove the gameID at the front
        subsets = line.split(':')[-1].split(';')

        max_red = 0
        max_green = 0
        max_blue = 0

        for subset in subsets:
            colors = subset.split(', ')
            for color in colors:
                count, col = color.split()
                count = int(count)
                if col == 'red':
                    max_red = max(max_red, count)
                elif col == 'green':
                    max_green = max(max_green, count)
                elif col == 'blue':
                    max_blue = max(max_blue, count)

        return {
            'game_ID': line.split(':')[0].split(' ')[-1],
            'max_red': max_red,
            'max_green': max_green,
            'max_blue': max_blue
        }

    
    def main(self):
        lines = self.import_file()
        print(self.TOTAL_POWER)


if __name__ == "__main__":
    # file = 'test.txt'
    # file = 'test2.txt'
    file = 'data.txt'

    # advent = CubeConundrum_v1(file).main()
    ## answer 2416

    advent = CubeConundrum_v2(file).main()
    ## answer 63307