import tkinter as tk
from tkinter import messagebox
from grid import SudokuGrid
from puzzles import get_puzzle

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.root.geometry("500x600")
        self.is_initializing = False

        self.intro_frame = tk.Frame(root)
        self.game_frame = tk.Frame(root)

        self.show_intro()

    def show_intro(self):
        self.game_frame.pack_forget()
        self.intro_frame.pack(expand=True)

        banner = tk.Label(self.intro_frame, text="Sudoku", font=('Arial', 50))
        banner.pack(pady=50)

        difficulty_frame = tk.Frame(self.intro_frame)
        difficulty_frame.pack(pady=20)

        easy_button = tk.Button(difficulty_frame, text="Easy", command=lambda: self.start_game("easy"))
        easy_button.pack(side="left", padx=10)

        medium_button = tk.Button(difficulty_frame, text="Medium", command=lambda: self.start_game("medium"))
        medium_button.pack(side="left", padx=10)

        hard_button = tk.Button(difficulty_frame, text="Hard", command=lambda: self.start_game("hard"))
        hard_button.pack(side="left", padx=10)

        created_by = tk.Label(self.intro_frame, text="Created by Sarvajeet Gada", font=('Arial', 12))
        created_by.pack(side="bottom", pady=10)

    def start_game(self, difficulty):
        puzzle = get_puzzle(difficulty)
        self.show_game(puzzle)

    def show_game(self, initial_grid):
        self.intro_frame.pack_forget()
        self.game_frame.pack()

        self.initial_grid = [row[:] for row in initial_grid]

        self.grid = SudokuGrid(initial_grid)
        self.cell_vars = [[tk.StringVar() for _ in range(9)] for _ in range(9)]
        self.frames = [[tk.Frame(self.game_frame, borderwidth=2, relief="solid") for _ in range(3)] for _ in range(3)]
        self.cells = [[tk.Entry(self.frames[i//3][j//3], width=2, font=('Arial', 18), justify='center', textvariable=self.cell_vars[i][j]) for j in range(9)] for i in range(9)]

        for i in range(3):
            for j in range(3):
                self.frames[i][j].grid(row=i, column=j)

        for i in range(9):
            for j in range(9):
                self.cells[i][j].grid(row=i%3, column=j%3, padx=1, pady=1)
                self.cell_vars[i][j].trace_add("write", lambda name, index, mode, r=i, c=j: self._cell_updated(r, c))

        self.is_initializing = True
        self.update_ui_from_grid()
        self.is_initializing = False

        button_frame = tk.Frame(self.game_frame)
        button_frame.grid(row=3, column=0, columnspan=3)

        solve_button = tk.Button(button_frame, text="Solve", command=self.solve)
        solve_button.pack(side="left", padx=10, pady=10)

        reset_button = tk.Button(button_frame, text="Reset", command=self.reset_puzzle)
        reset_button.pack(side="left", padx=10, pady=10)

    def solve(self):
        self.get_grid_from_ui()
        if self.grid.solve():
            self.is_initializing = True
            self.update_ui_from_grid()
            self.is_initializing = False
        else:
            messagebox.showerror("Error", "No solution exists for the given puzzle.")

    def reset_puzzle(self):
        grid_copy = [row[:] for row in self.initial_grid]
        self.grid = SudokuGrid(grid_copy)
        self.is_initializing = True
        self.update_ui_from_grid()
        self.is_initializing = False

    def _cell_updated(self, row, col):
        if self.is_initializing:
            return
        self.get_grid_from_ui()

        for i in range(9):
            for j in range(9):
                if self.initial_grid[i][j] == 0:
                    cell = self.cells[i][j]
                    if self.grid.is_conflict(i, j):
                        cell.config(fg='red')
                    else:
                        cell.config(fg='black')

    def get_grid_from_ui(self):
        for i in range(9):
            for j in range(9):
                try:
                    value = int(self.cell_vars[i][j].get())
                    if 0 <= value <= 9:
                        self.grid.set_cell(i, j, value)
                    else:
                        self.grid.set_cell(i, j, 0)
                except (ValueError, tk.TclError):
                    self.grid.set_cell(i, j, 0)

    def update_ui_from_grid(self):
        for i in range(9):
            for j in range(9):
                cell = self.cells[i][j]
                cell_value = self.grid.get_cell(i, j)

                if cell_value != 0:
                    self.cell_vars[i][j].set(str(cell_value))
                else:
                    self.cell_vars[i][j].set("")

                if self.initial_grid[i][j] != 0:
                    cell.config(state='readonly', readonlybackground='light gray', font=('Arial', 18, 'bold'))
                else:
                    cell.config(font=('Arial', 18), state='normal')

if __name__ == '__main__':
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
