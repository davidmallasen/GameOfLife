from random import random
import time

_DEAD = 0
_LIVE = 1

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

    return [[_DEAD if random() >= 0.5 else _LIVE
             for _ in range(width)]
            for _ in range(height)]


def _state_height(state):
    """
    Get the height of a state.

    :arg state: A game state.

    :return: The height of the input state.
    """

    return len(state)


def _state_width(state):
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

    display_as = {_DEAD: ' ', _LIVE: '#'}
    width = _state_width(state)

    print("-" * (width + 2))
    board = ["|{line}|".format(
        line="".join(display_as[x] for x in row))
        for row in state]
    print("\n".join(board))
    print("-" * (width + 2))


def _number_of_neighbors(i, j, height, width, state):
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
            if state[h][w] == _LIVE:
                count += 1

    return count


def _next_cell_value(i, j, height, width, state):
    """
    Calculates the next value of the cell (i, j) in the given state.

    :param i: Row of the cell.
    :param j: Column of the cell.
    :param height: Height of the input state.
    :param width: Width of the input state.
    :param state: A game state

    :return: Next value of the input cell in the input state.
    """

    num_neighbors = _number_of_neighbors(i, j, height, width, state)
    if state[i][j] == _LIVE:
        if num_neighbors < 2 or num_neighbors > 3:
            return _DEAD
        else:
            return _LIVE
    else:
        if num_neighbors == 3:
            return _LIVE
        else:
            return _DEAD


def next_board_state(state):
    """
    Given an input state, calculates the next state of the game.

    :param state: The current game state.

    :return: The next state of the game based on the input state.
    """

    height = _state_height(state)
    width = _state_width(state)
    next_state = dead_state(height, width)

    for i in range(height):
        for j in range(width):
            next_state[i][j] = _next_cell_value(i, j, height, width, state)

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
        time.sleep(0.03)


def load_game_state(path):
    """
    Loads a game state from the input file.

    :param path: Input file path. It should be a rectangle of 0s and 1s.

    :return: The game state parsed from the input file.
    """
    with open(path) as file:
        lines = file.readlines()

    init_state = dead_state(len(lines), len(lines[0]) - 1)  # Minus \n
    for i, line in enumerate(lines):
        for j, num in enumerate(line.rstrip()):
            init_state[i][j] = int(num)

    return init_state


if __name__ == "__main__":
    run_forever(load_game_state("./Patterns/gosper_glider_gun.txt"))
