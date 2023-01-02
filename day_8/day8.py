import pathlib

class TreetopTreeHouse():

    # Square where eachdigit is the height of tream (0-9)
    # How many trees inside of the outer edges are visible
    # Outer edge trees are always visible from the outside
    # Have to check all trees between it and every edge.
    # Test case means to look at the middle 3x3
    

    def __init__(self, puzzle_input) -> None:
        ## Create a nested list where first item is the top row of the input 
        rows = puzzle_input.strip().split('\n')
        self.grid = [list(n) for n in rows]

        ## Initially, assume no trees are visible
        self.visible = 0
        ## Assume all rows and cols are same length 
        ## Remove 1 for idx
        self.max_row = len(self.grid[0]) - 1
        self.max_col = len(self.grid) - 1

    def check_visibility(self):
        """
        Check if each tree is visible
        """
        ## Start at top left
        cur_row = 0
        

        while cur_row <= self.max_row:

            cur_col = 0 # Start at left
            while cur_col <= self.max_col:
                ## Accounts for exterior row/cols
                if cur_row == 0 or cur_col == 0 or cur_row == self.max_row or cur_col == self.max_col:
                    self.visible += 1
                else:
                    up = self.check_visible_up(cur_row=cur_row, cur_col=cur_col)
                    down = self.check_visible_down(cur_row=cur_row, cur_col=cur_col)
                    left = self.check_visible_left(cur_row=cur_row, cur_col=cur_col)
                    right = self.check_visible_right(cur_row=cur_row, cur_col=cur_col)
                    if up or down or right or left:
                        # print(f'R: {cur_row+1} C: {cur_col+1} is visible')
                        self.visible += 1
                    else:
                        # print(f'R: {cur_row+1} C: {cur_col+1} is not visible')
                        # print(f'Up: {up} Down: {down} Right: {right} Left: {left}')
                        pass
                cur_col += 1 # Move to next column
            cur_row += 1 #Move to next row

    def check_visible_left(self, cur_row, cur_col):
        """
        Takes current row and column locations.
        Checks if any values above are greater than current tree size.
        If there is a taller tree, returns False. Otherwrise return True.
        """
        cur_tree = int(self.grid[cur_row][cur_col])
        for i in range(0, cur_col):
            adj_tree = int(self.grid[cur_row][i])
            # print(f'Row {cur_row} Col: {i}')
            # print(f'Cur {cur_tree} Adj: {adj_tree}')
            # print()
            if adj_tree >= cur_tree:
                return False
        return True

    def check_visible_right(self, cur_row, cur_col):
        cur_tree = int(self.grid[cur_row][cur_col])
        for i in range(cur_col+1, self.max_col+1):
            adj_tree = int(self.grid[cur_row][i])
            # print(f'Row {cur_row} Col: {i}')
            # print(f'Cur {cur_tree} Adj: {adj_tree}')
            # print()
            if adj_tree >= cur_tree:
                return False
        return True
    
    def check_visible_up(self, cur_row, cur_col):
        cur_tree = int(self.grid[cur_row][cur_col])
        for i in range(0, cur_row):
            adj_tree = int(self.grid[i][cur_col])
            # print(f'Row {cur_row} Col: {i}')
            # print(f'Cur {cur_tree} Adj: {adj_tree}')
            # print()
            if adj_tree >= cur_tree:
                return False
        return True

    def check_visible_down(self, cur_row, cur_col):
        cur_tree = int(self.grid[cur_row][cur_col])
        for i in range(cur_row+1, self.max_row+1):
            adj_tree = int(self.grid[i][cur_col])
            if adj_tree >= cur_tree:
                return False
        return True

    def solve_problem1(self):
        self.check_visibility()
        print(self.visible)
        # self.check_visible_right(2,1)

if __name__ == '__main__':

    test_file = 'day_8/test_data.txt'
    real_file = 'day_8/real_data.txt'

    puzzle_input = pathlib.Path(real_file).read_text().strip()

    tester = TreetopTreeHouse(puzzle_input=puzzle_input)
    tester.solve_problem1()