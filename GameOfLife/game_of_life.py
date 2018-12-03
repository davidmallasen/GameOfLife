from random import random

DEAD = 0
LIVE = 1


def random_state(width=3, height=3):
    """
    Construct a random state with all cells randomly set.

    :arg width: the width of the state, in cells
    :arg height: the height of the state, in cells

    :returns: A state of dimensions width x height, with all cells randomly
        set to either DEAD or LIVE with equal probability.
    """

    return [[DEAD if random() >= 0.5 else LIVE
            for _ in range(height)]
            for _ in range(width)]


def state_height(state):
    """
    Get the height of a state

    :arg state: a game state

    :returns: The height of the input state
    """

    return len(state)


def state_width(state):
    """
    Get the width of a state

    :arg state: a game state

    :returns: The width of the input state
    """

    return len(state[0])


def render(state):
    """
    Prints the game state

    :arg state: a game state
    """

    display_as = {DEAD: ' ', LIVE: '#'}

    print('-' * (state_width(state) * 2 + 3))
    for row in state:
        print("| %s |" % " ".join(display_as[x] for x in row))
    print('-' * (state_width(state) * 2 + 3))


width = 5
height = 5
render(random_state(width, height))
