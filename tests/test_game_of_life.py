import unittest

from game_of_life.game_of_life import next_board_state


class TestGameOfLife(unittest.TestCase):

    def test_dead_cells_not_3_neighbors(self):
        init_state1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        init_state2 = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        expected_next_state1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected_next_state2 = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        actual_next_state1 = next_board_state(init_state1)
        actual_next_state2 = next_board_state(init_state2)
        self.assertEqual(expected_next_state1, actual_next_state1)
        self.assertEqual(expected_next_state2, actual_next_state2)

    def test_dead_cells_3_neighbors(self):
        init_state = [
            [0, 0, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        expected_next_state = [
            [0, 1, 1],
            [0, 1, 1],
            [0, 0, 0]
        ]
        actual_next_state = next_board_state(init_state)
        self.assertEqual(expected_next_state, actual_next_state)

    def test_live_cells_few_neighbors(self):
        init_state1 = [
            [1, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        init_state2 = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        expected_next_state1 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        expected_next_state2 = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        actual_next_state1 = next_board_state(init_state1)
        actual_next_state2 = next_board_state(init_state2)
        self.assertEqual(expected_next_state1, actual_next_state1)
        self.assertEqual(expected_next_state2, actual_next_state2)

    def test_live_cells_enough_neighbors(self):
        init_state1 = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        init_state2 = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        expected_next_state1 = [
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]
        ]
        expected_next_state2 = [
            [1, 1, 0],
            [1, 1, 0],
            [0, 0, 0]
        ]
        actual_next_state1 = next_board_state(init_state1)
        actual_next_state2 = next_board_state(init_state2)
        self.assertEqual(expected_next_state1, actual_next_state1)
        self.assertEqual(expected_next_state2, actual_next_state2)

    def test_live_cells_many_neighbors(self):
        init_state = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 1, 0]
        ]
        expected_next_state = [
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ]
        actual_next_state = next_board_state(init_state)
        self.assertEqual(expected_next_state, actual_next_state)

    def test_different_height_width(self):
        init_state = [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [1, 1, 0, 1]
        ]
        expected_next_state = [
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 1, 1, 0]
        ]
        actual_next_state = next_board_state(init_state)
        self.assertEqual(expected_next_state, actual_next_state)


if __name__ == "__main__":
    unittest.main()
