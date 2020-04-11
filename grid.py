##
# grid.py
# Create a 2D list and populate with X
# Setup a starting point denoted by O


def setup_grid(grid, SIZE):
    """
    Setup the 3x3 grid, populate with X
    """
    for row in range(SIZE):
        grid.append([])
        for col in range(SIZE):
            grid[row].append('X')


def display_grid(grid):
    """ Display the grid to the screen """
    print("================")
    for row in range(len(grid)):
        for col in range(len(grid)):
            print(grid[row][col],end='')
        print()
    print("================")


def start_point(SIZE):
    """ Create a random starting point on the grid """
    import random
    return random.randint(0, SIZE-1), random.randint(0, SIZE-1)


def validate_move(x, y, direction):
    """
    Check if position is on boundary and return false if
    tries to move out of bounds.
    """
    if direction == 'u' and x == 0:
        return False
    elif direction == 'l' and y == 0:
        return False
    elif direction == 'r' and y == 2:
        return False
    elif direction == 'd' and x == 2:
        return False
    else:
        return True

def move_pos(x, y, direction):
    """ Change the position of the current location. """
    if direction == 'u':
        return x-1, y
    elif direction == 'l':
        return x, y-1
    elif direction == 'r':
        return x, y+1
    elif direction == 'd':
        return x+1, y

def main():
    """ Main routine """
    SIZE = 3
    grid = []
    setup_grid(grid, SIZE)
    display_grid(grid)
    x, y = start_point(SIZE)
    grid[x][y] = 'O'
    display_grid(grid)
    if not validate_move(x, y, 'u'):
        print("You cannot move up from here")
    else:
        grid[x][y] = 'X'
        x, y = move_pos(x,y,'u')
        grid[x][y] = 'O'
    display_grid(grid)

main()
