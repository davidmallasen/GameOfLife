from random import random
import time

DEAD = 0
LIVE = 1

'''
Example state of height 3 and width 4 (dimensions 3x4) where the only 
live cell has coordinates (row=2, column=3):

state = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 1]
]
'''


def dead_state(height, width):
    """
    Construct a dead state with all cells set to DEAD.

    :arg height: The height of the state, in cells.
    :arg width: The width of the state, in cells.

    :returns: A state of dimensions height x width, with all cells set
        to DEAD.
    """

    return [[0 for _ in range(width)] for _ in range(height)]


def random_state(height, width):
    """
    Construct a random state with all cells randomly set.

    :arg height: The height of the state, in cells.
    :arg width: The width of the state, in cells.

    :return: A state of dimensions height x width, with all cells
        randomly set to either DEAD or LIVE with equal probability.
    """

    return [[DEAD if random() >= 0.5 else LIVE
             for _ in range(width)]
            for _ in range(height)]


def state_height(state):
    """
    Get the height of a state.

    :arg state: A game state.

    :return: The height of the input state.
    """

    return len(state)


def state_width(state):
    """
    Get the width of a state.

    :arg state: A game state.

    :return: The width of the input state.
    """

    if len(state) == 0:
        return 0
    else:
        return len(state[0])


def render(state):
    """
    Prints the game state.

    :arg state: A game state.

    :return: Nothing.
    """

    display_as = {DEAD: ' ', LIVE: '#'}
    width = state_width(state)

    board = ["-" * (width + 2)]
    for row in state:
        board.append("|%s|" % "".join(display_as[x] for x in row))
    board.append("-" * (width + 2))

    print("\n".join(board))


'''
def out_of_bounds(i, j, state):
    """
    Checks if a position is out of bounds.

    :param i: Position row.
    :param j: Position column.
    :param state: A game state.

    :return: True if (i, j) is out of bounds. False otherwise.
    """

    return (i < 0 or i >= state_height(state)
            or j < 0 or j >= state_width(state))
'''


def number_of_neighbors(i, j, height, width, state):
    """
    Counts the number of LIVE neighbors of the cell in position (i, j).

    :param i: Row of the cell.
    :param j: Column of the cell.
    :param height: Height of the input state.
    :param width: Width of the input state.
    :param state: A game state.

    :return: Number of LIVE neighbours of the input cell in the input
        state.
    """

    count = 0
    for h in range(i - 1, i + 2):
        if h < 0 or h >= height:
            continue
        for w in range(j - 1, j + 2):
            if w < 0 or w >= width or (h == i and w == j):
                continue
            if state[h][w] == LIVE:
                count += 1

    return count


def next_cell_value(i, j, height, width, state):
    """
    Calculates the next value of the cell (i, j) in the given state.

    :param i: Row of the cell.
    :param j: Column of the cell.
    :param height: Height of the input state.
    :param width: Width of the input state.
    :param state: A game state

    :return: Next value of the input cell in the input state.
    """

    num_neighbors = number_of_neighbors(i, j, height, width, state)
    if state[i][j] == LIVE:
        if num_neighbors < 2 or num_neighbors > 3:
            return DEAD
        else:
            return LIVE
    else:
        if num_neighbors == 3:
            return LIVE
        else:
            return DEAD


def next_board_state(state):
    """
    Given an input state, calculates the next state of the game.

    :param state: The current game state.

    :return: The next state of the game based on the input state.
    """

    height = state_height(state)
    width = state_width(state)
    next_state = dead_state(height, width)

    for i in range(height):
        for j in range(width):
            next_state[i][j] = next_cell_value(i, j, height, width, state)

    return next_state


def run_forever(init_state):
    """
    Runs the game of life, starting from the given initial state.

    :param init_state: The initial game state.

    :return: Nothing
    """

    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(1)


if __name__ == "__main__":
    run_forever(random_state(10, 15))
