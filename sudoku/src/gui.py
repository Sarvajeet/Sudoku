import tkinter as tk
from tkinter import messagebox
from grid import SudokuGrid

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.root.geometry("500x600")

        self.intro_frame = tk.Frame(root)
        self.game_frame = tk.Frame(root)

        self.show_intro()

    def show_intro(self):
        self.game_frame.pack_forget()
        self.intro_frame.pack(expand=True)

        banner = tk.Label(self.intro_frame, text="Sudoku", font=('Arial', 50))
        banner.pack(pady=50)

        start_button = tk.Button(self.intro_frame, text="Start", command=self.show_game)
        start_button.pack(pady=20)

        created_by = tk.Label(self.intro_frame, text="Created by Sarvajeet Gada", font=('Arial', 12))
        created_by.pack(side="bottom", pady=10)

    def show_game(self):
        self.intro_frame.pack_forget()
        self.game_frame.pack()

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
        self.initial_grid = [row[:] for row in initial_grid]

        self.grid = SudokuGrid(initial_grid)
        self.frames = [[tk.Frame(self.game_frame, borderwidth=2, relief="solid") for _ in range(3)] for _ in range(3)]
        self.cells = [[tk.Entry(self.frames[i//3][j//3], width=2, font=('Arial', 18), justify='center') for j in range(9)] for i in range(9)]

        for i in range(3):
            for j in range(3):
                self.frames[i][j].grid(row=i, column=j)

        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i%3, column=j%3, padx=1, pady=1)

        self.update_ui_from_grid()

        button_frame = tk.Frame(self.game_frame)
        button_frame.grid(row=3, column=0, columnspan=3)

        solve_button = tk.Button(button_frame, text="Solve", command=self.solve)
        solve_button.pack(side="left", padx=10, pady=10)

        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_puzzle)
        reset_button.pack(side="left", padx=10, pady=10)

    def solve(self):
        self.get_grid_from_ui()
        if self.grid.solve():
            self.update_ui_from_grid()
        else:
            messagebox.showerror("Error", "No solution exists for the given puzzle.")

    def reset_puzzle(self):
        grid_copy = [row[:] for row in self.initial_grid]
        self.grid = SudokuGrid(grid_copy)
        self.update_ui_from_grid()

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
                cell = self.cells[i][j]
                cell.config(state='normal')
                cell.delete(0, tk.END)

                cell_value = self.grid.get_cell(i, j)

                if cell_value != 0:
                    cell.insert(0, str(cell_value))

                if self.initial_grid[i][j] != 0:
                    cell.config(state='readonly', readonlybackground='light gray', font=('Arial', 18, 'bold'))
                else:
                    cell.config(font=('Arial', 18), state='normal')

if __name__ == '__main__':
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
