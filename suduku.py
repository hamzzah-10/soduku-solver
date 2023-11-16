from pprint import pprint

def find_next_empty(puzzle):
    # This function finds the next empty space on a 9x9 sudoku board.
    # An empty space is represented with -1. If there is no empty space,
    # the function returns (None, None).

    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c

    return None, None  

def is_valid(puzzle, guess, row, col):  
    # This function returns True if the guess is valid,
    # and False if the guess is invalid.
     
    # Rule: The guess should not be repeated in the row, column, or 3x3 grid.

    # 1) Row check
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # 2) Column check
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
        
    # 3) 3x3 grid check
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
            
    return True

def solve_sudoku(puzzle):
    # Backtrack approach
    # Our puzzle is a list of lists in which each inner list represents a row.
    # Mutates puzzle to be the solution (if a solution exists).

    # Make a guess on the puzzle
    row, col = find_next_empty(puzzle)

    if row is None:
        return True  # It means that no valid place is left on the puzzle
    
    # If not, then we will make a guess between 1 and 9
    for guess in range(1, 10):  # From 1 to 9
        # Check if the guess is valid or not
        if is_valid(puzzle, guess, row, col):
            # If yes, then place the guess on the table
            puzzle[row][col] = guess
            # Add a recursive call to the solve_sudoku function
            if solve_sudoku(puzzle):
                return True
        
        # If not valid, then we need to backtrack and try again with a new number
        puzzle[row][col] = -1

    return False     


if __name__ == '__main__':
    example_board = [
        [-1, -1, -1, 1, 7, -1, -1, 8, 2],
        [-1, 5, -1, -1, -1, 8, -1, -1, -1],
        [-1, -1, 2, -1, -1, -1, -1, 7, -1],
        [-1, -1, 5, -1, 2, 7, 8, -1, -1],
        [7, -1, -1, 5, -1, 4, -1, 6, -1],
        [9, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, 4, -1],
        [2, 6, 9, -1, -1, 1, 7, 3, -1],
        [-1, 7, 3, 9, -1, -1, 6, -1, -1]
    ]
    print(solve_sudoku(example_board))
    pprint(example_board)
