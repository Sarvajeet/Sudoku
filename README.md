# Sudoku

A simple Sudoku game implemented in Python.

## How to Play

Sudoku is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid contain all of the digits from 1 to 9.

## Project Structure

- `sudoku/src/main.py`: The main entry point for the game.
- `sudoku/tests/test_main.py`: Unit tests for the game.

## How to Run

To run the GUI application, navigate to the `sudoku/src` directory and execute the following command:

```bash
python main.py
```

To run the tests, execute the following command from the project root:

```bash
python -m unittest sudoku/tests/test_grid.py
```
