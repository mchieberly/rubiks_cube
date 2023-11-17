# Malachi Eberly
# test_cube.py

import unittest
from src.cube.cube import Cube

class TestCubeRotations(unittest.TestCase):
    def setUp(self):
        self.cube = Cube()

    def test_front_clockwise_rotation(self):
        # Initial state check (optional)
        # Perform rotation
        # Check the state of a few key pieces to ensure they moved correctly
        pass

    def test_front_counterclockwise_rotation(self):
        # Similar structure to above
        pass

    # ... tests for other rotations ...

class TestCubeScramble(unittest.TestCase):
    def setUp(self):
        self.cube = Cube()
        
    def test_scramble(self):
        original_state = str(self.cube)
        self.cube.scramble()
        scrambled_state = str(self.cube)
        self.assertNotEqual(original_state, scrambled_state)

class TestCubeSolved(unittest.TestCase):
    def setUp(self):
        self.cube = Cube()

    def test_solved_cube(self):
        # Assuming the cube is initialized in a solved state
        print(self.cube)
        self.assertTrue(self.cube.is_solved())

    def test_unsolved_cube_after_one_rotation(self):
        self.cube.rotate_front_clockwise()
        self.assertFalse(self.cube.is_solved())

    def test_unsolved_cube_after_scramble(self):
        self.cube.scramble()
        self.assertFalse(self.cube.is_solved())

if __name__ == '__main__':
    unittest.main()