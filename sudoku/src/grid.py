class SudokuGrid:
    def __init__(self, initial_grid=None):
        if initial_grid:
            self.grid = initial_grid
        else:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]

    def __str__(self):
        result = ""
        for i in range(9):
            if i % 3 == 0 and i != 0:
                result += "- - - - - - - - - - - -\n"
            for j in range(9):
                if j % 3 == 0 and j != 0:
                    result += "| "
                result += str(self.grid[i][j]) + " "
            result += "\n"
        return result

    def set_cell(self, row, col, value):
        self.grid[row][col] = value

    def get_cell(self, row, col):
        return self.grid[row][col]

    def is_valid_move(self, row, col, num):
        # Check row
        for x in range(9):
            if self.grid[row][x] == num:
                return False

        # Check column
        for x in range(9):
            if self.grid[x][col] == num:
                return False

        # Check 3x3 subgrid
        start_row = row - row % 3
        start_col = col - col % 3
        for i in range(3):
            for j in range(3):
                if self.grid[i + start_row][j + start_col] == num:
                    return False
        return True

    def solve(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    for num in range(1, 10):
                        if self.is_valid_move(i, j, num):
                            self.grid[i][j] = num
                            if self.solve():
                                return True
                            self.grid[i][j] = 0
                    return False
        return True
