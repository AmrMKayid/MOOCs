from utils import *
from ConstrainPropagation import *


def search(values):
    "Using Depth-First Search and Propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    
    # Failed
    if values is False:
    	return False

    # Solved
    if all(len(values[s]) == 1 for s in boxes):
    	return values

    # Choose one of the unfilled squares with the fewest possibilities
    minBox, index = min((len(values[index]), index) for index in boxes if len(values[index]) > 1)

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!
    for value in values[index]:
    	new_sudoku = values.copy()
    	new_sudoku[index] = value
    	attempt = search(new_sudoku)
    	if attempt:
    		return attempt


#display(search(grid_values('4.....8.5.3..........7......2.....6.....8.4......1.......6.3.7.5..2.....1.4......')))

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(search(grid_values(diag_sudoku_grid)))

