##
# grid.py
# Create a 2D list and populate with X
# Setup a starting point denoted by O


def setup_grid(grid):
    """
    Setup the 3x3 grid, populate with X
    """
    SIZE = 3
    for row in range(SIZE):
        grid.append([])
        for col in range(SIZE):
            grid[row].append('X')


def display_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            print(grid[row][col],end='')
        print()


def main():
    grid = []
    setup_grid(grid)
    display_grid(grid)
