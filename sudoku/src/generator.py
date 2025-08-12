import random
try:
    from .grid import SudokuGrid
except ImportError:
    from grid import SudokuGrid

class SudokuGenerator:
    def __init__(self):
        self.grid = SudokuGrid()

    def generate(self, difficulty):
        # First, create a fully solved grid
        self.grid = SudokuGrid([[0]*9 for _ in range(9)])
        self.grid.solve(randomize=True)

        # Determine the number of cells to remove based on difficulty
        if difficulty == "easy":
            num_to_remove = 40
        elif difficulty == "medium":
            num_to_remove = 50
        else: # hard
            num_to_remove = 60

        puzzle = self._remove_numbers(self.grid, num_to_remove)
        return puzzle.grid

    def _remove_numbers(self, grid, num_to_remove):
        cells = [(r, c) for r in range(9) for c in range(9)]
        random.shuffle(cells)

        removed_count = 0
        for r, c in cells:
            if removed_count >= num_to_remove:
                break

            original_value = grid.get_cell(r, c)
            grid.set_cell(r, c, 0)

            # Check if the puzzle still has a unique solution
            grid_copy = SudokuGrid([row[:] for row in grid.grid])
            if grid_copy.count_solutions() != 1:
                grid.set_cell(r, c, original_value) # Put it back
            else:
                removed_count += 1

        return grid
