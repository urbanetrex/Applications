import random

def generate_sudoku(size):
    # Templates
    sudoku_4x4 = [
        [1, 2, 3, 4],
        [3, 4, 1, 2],
        [2, 1, 4, 3],
        [4, 3, 2, 1]
    ]
    sudoku_6x6 = [
        [1, 2, 3, 4, 5, 6],
        [4, 5, 6, 1, 2, 3],
        [2, 3, 1, 5, 6, 4],
        [5, 6, 4, 2, 3, 1],
        [3, 1, 2, 6, 4, 5],
        [6, 4, 5, 3, 1, 2]
    ]
    sudoku_9x9 = [
        [1, 2, 3, 4, 5, 6, 7, 8, 9],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [2, 3, 1, 5, 6, 4, 8, 9, 7],
        [5, 6, 4, 8, 9, 7, 2, 3, 1],
        [8, 9, 7, 2, 3, 1, 5, 6, 4],
        [3, 1, 2, 6, 4, 5, 9, 7, 8],
        [6, 4, 5, 7, 8, 9, 3, 1, 2],
        [9, 7, 8, 3, 1, 2, 6, 4, 5]
    ]

    # Constants
    BX_ROWS = None
    BX_COLS = None
    BOX_ROW_SIZE = None
    BOX_COL_SIZE = None
    copied_sudoku = None

    # Constant assigning depending on size
    if size == 4:
        BX_ROWS = 2
        BX_COLS = 2
        BOX_ROW_SIZE = 2
        BOX_COL_SIZE = 2
        copied_sudoku = sudoku_4x4.copy()
    elif size == 6:
        BX_ROWS = 3
        BX_COLS = 2
        BOX_ROW_SIZE = 2
        BOX_COL_SIZE = 3
        copied_sudoku = sudoku_6x6.copy()
    elif size == 9:
        BX_ROWS = 3
        BX_COLS = 3
        BOX_ROW_SIZE = 3
        BOX_COL_SIZE = 3
        copied_sudoku = sudoku_9x9.copy()
    
    # Generate the puzzle (Not repeating the code for each size)
    for i in range(random.randint(0, 1000)):
        instruction = random.randint(0, 4)
        if instruction == 0:
            # Swap rows within the same box row
            box_row = random.choice(range(BX_ROWS)) * BOX_ROW_SIZE
            row1, row2 = random.sample(range(box_row, box_row + BOX_ROW_SIZE), 2)
            copied_sudoku[row1], copied_sudoku[row2] = copied_sudoku[row2], copied_sudoku[row1]
        elif instruction == 1:
            # Swap columns within the same box column
            box_col = random.choice(range(BX_COLS)) * BOX_COL_SIZE
            col1, col2 = random.sample(range(box_col, box_col + BOX_COL_SIZE), 2)
            for row in copied_sudoku:
                row[col1], row[col2] = row[col2], row[col1]
        elif instruction == 2:
            # Swap box rows
            box_row1, box_row2 = random.sample(range(BX_ROWS), 2)
            box_row1 *= BOX_ROW_SIZE
            box_row2 *= BOX_ROW_SIZE
            copied_sudoku[box_row1:box_row1 + BOX_ROW_SIZE], copied_sudoku[box_row2:box_row2 + BOX_ROW_SIZE] = (
                copied_sudoku[box_row2:box_row2 + BOX_ROW_SIZE],
                copied_sudoku[box_row1:box_row1 + BOX_ROW_SIZE],
            )
        elif instruction == 3:
            # Swap box columns
            box_col1, box_col2 = random.sample(range(BX_COLS), 2)
            box_col1 *= BOX_COL_SIZE
            box_col2 *= BOX_COL_SIZE
            for row in copied_sudoku:
                row[box_col1:box_col1 + BOX_COL_SIZE], row[box_col2:box_col2 + BOX_COL_SIZE] = (
                    row[box_col2:box_col2 + BOX_COL_SIZE],
                    row[box_col1:box_col1 + BOX_COL_SIZE],
                )
    return copied_sudoku

def print_sudoku(sudoku):
    """
    Prints the Sudoku puzzle in a readable format.
    """
    for row in sudoku:
        print(" ".join(str(num) for num in row))
    print()  # Add an extra newline for better readability

def print_sudoku_with_box_outlines(sudoku, size):
    """
    Prints the Sudoku puzzle with box outlines for better visualization.
    """

    #Setting up constants based on size
    BX_ROWS = None
    BX_COLS = None
    BOX_ROW_SIZE = None
    BOX_COL_SIZE = None
    copied_sudoku = None
    if size == 4:
        BX_ROWS = 2
        BX_COLS = 2
        BOX_ROW_SIZE = 2
        BOX_COL_SIZE = 2
    elif size == 6:
        BX_ROWS = 3
        BX_COLS = 2
        BOX_ROW_SIZE = 2
        BOX_COL_SIZE = 3
    elif size == 9:
        BX_ROWS = 3
        BX_COLS = 3
        BOX_ROW_SIZE = 3
        BOX_COL_SIZE = 3

    for i, row in enumerate(sudoku):
        if i % BOX_ROW_SIZE == 0 and i != 0:
            for j in range(size * 2 + BX_COLS):
                if (j + 1) % (BOX_COL_SIZE * 2 + 1) == 0:
                    print("+", end="")
                else:
                    print("-", end="")
            print()
        for j, num in enumerate(row):
            if j % BOX_COL_SIZE == 0 and j != 0:
                print("|", end=" ")
            print(num if num != 0 else "_", end=" ")
        print()

def remove_numbers(sudoku, level):
    """
    Removes numbers from the Sudoku puzzle based on the difficulty level.
    """
    size = len(sudoku)
    num_to_remove = int(size * size * level / 100)  # Calculate number of cells to remove
    for _ in range(num_to_remove):
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        while sudoku[row][col] == 0:  # Ensure we don't remove an already empty cell
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
        sudoku[row][col] = 0  # Remove the number by setting it to 0
    return sudoku


print("Generated Sudoku Puzzle:")
print()
print_sudoku_with_box_outlines(remove_numbers(generate_sudoku(9), 50), 9)  # Example for a 9x9 Sudoku with 50% numbers removed
print()
    



























































































































































































































































'''
Application

'''

import tkinter as tk

root = tk.Tk()
root.title("King Sudoku -- Starting...")

root.geometry("400x300")

root.mainloop()