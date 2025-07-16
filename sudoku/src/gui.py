import tkinter as tk
from tkinter import messagebox
from grid import SudokuGrid

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")

        initial_grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        self.grid = SudokuGrid(initial_grid)
        self.cells = [[tk.Entry(root, width=2, font=('Arial', 18), justify='center') for _ in range(9)] for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i, column=j, padx=5, pady=5)

        self.update_ui_from_grid()

        solve_button = tk.Button(root, text="Solve", command=self.solve)
        solve_button.grid(row=9, column=0, columnspan=4, pady=10)

        clear_button = tk.Button(root, text="Clear", command=self.clear)
        clear_button.grid(row=9, column=5, columnspan=4, pady=10)

    def solve(self):
        self.get_grid_from_ui()
        if self.grid.solve():
            self.update_ui_from_grid()
        else:
            messagebox.showerror("Error", "No solution exists for the given puzzle.")

    def clear(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)

    def get_grid_from_ui(self):
        for i in range(9):
            for j in range(9):
                try:
                    value = int(self.cells[i][j].get())
                    if 0 <= value <= 9:
                        self.grid.set_cell(i, j, value)
                    else:
                        self.grid.set_cell(i, j, 0)
                except ValueError:
                    self.grid.set_cell(i, j, 0)

    def update_ui_from_grid(self):
        for i in range(9):
            for j in range(9):
                self.cells[i][j].delete(0, tk.END)
                cell_value = self.grid.get_cell(i, j)
                if cell_value != 0:
                    self.cells[i][j].insert(0, str(cell_value))

if __name__ == '__main__':
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
