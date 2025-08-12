import unittest
from ..src.generator import SudokuGenerator
from ..src.grid import SudokuGrid

class TestSudokuGenerator(unittest.TestCase):

    def test_generate(self):
        generator = SudokuGenerator()

        for difficulty in ["easy", "medium", "hard"]:
            puzzle = generator.generate(difficulty)

            # Check if the puzzle is a 9x9 grid
            self.assertEqual(len(puzzle), 9)
            for row in puzzle:
                self.assertEqual(len(row), 9)

            # Check if all elements are integers
            for row in puzzle:
                for cell in row:
                    self.assertIsInstance(cell, int)

if __name__ == '__main__':
    unittest.main()
