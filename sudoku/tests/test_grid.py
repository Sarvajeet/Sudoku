import unittest
from ..src.grid import SudokuGrid

class TestSudokuGrid(unittest.TestCase):

    def setUp(self):
        self.empty_grid = SudokuGrid()
        self.solved_grid = SudokuGrid([
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 9]
        ])
        self.unsolved_grid = SudokuGrid([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])
        self.conflict_grid = SudokuGrid([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [5, 0, 0, 0, 8, 0, 0, 7, 9]
        ])

    def test_is_valid_move(self):
        self.assertFalse(self.solved_grid.is_valid_move(0, 0, 5))
        self.assertTrue(self.unsolved_grid.is_valid_move(0, 2, 1))
        self.assertFalse(self.unsolved_grid.is_valid_move(0, 2, 5))

    def test_solve(self):
        self.assertTrue(self.unsolved_grid.solve())
        self.assertEqual(self.unsolved_grid.get_cell(0, 2), 4)

    def test_is_conflict(self):
        # Test row conflict
        self.conflict_grid.set_cell(0, 2, 5)
        self.assertTrue(self.conflict_grid.is_conflict(0, 2))
        self.assertTrue(self.conflict_grid.is_conflict(0, 0))
        self.conflict_grid.set_cell(0, 2, 1) # Reset for next test

        # Test column conflict
        self.assertTrue(self.conflict_grid.is_conflict(8, 0))

        # Test box conflict
        self.conflict_grid.set_cell(1, 1, 9)
        self.assertTrue(self.conflict_grid.is_conflict(1, 1))

        # Test no conflict
        self.assertFalse(self.conflict_grid.is_conflict(0, 1))

    def test_count_solutions(self):
        # A solved grid has exactly one solution
        self.assertEqual(self.solved_grid.count_solutions(), 1)

        # The standard unsolved grid should have a unique solution
        self.assertEqual(self.unsolved_grid.count_solutions(), 1)

    def test_is_solved(self):
        # A solved grid is solved
        self.assertTrue(self.solved_grid.is_solved())

        # An unsolved grid is not solved
        self.assertFalse(self.unsolved_grid.is_solved())

        # A grid with conflicts is not solved
        self.assertFalse(self.conflict_grid.is_solved())

        # A full grid with a conflict is also not solved
        full_conflict_grid = SudokuGrid([
            [5, 3, 4, 6, 7, 8, 9, 1, 2],
            [6, 7, 2, 1, 9, 5, 3, 4, 8],
            [1, 9, 8, 3, 4, 2, 5, 6, 7],
            [8, 5, 9, 7, 6, 1, 4, 2, 3],
            [4, 2, 6, 8, 5, 3, 7, 9, 1],
            [7, 1, 3, 9, 2, 4, 8, 5, 6],
            [9, 6, 1, 5, 3, 7, 2, 8, 4],
            [2, 8, 7, 4, 1, 9, 6, 3, 5],
            [3, 4, 5, 2, 8, 6, 1, 7, 5] # Conflict with (0,0)
        ])
        self.assertFalse(full_conflict_grid.is_solved())

if __name__ == '__main__':
    unittest.main()
