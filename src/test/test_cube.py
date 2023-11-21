# Malachi Eberly
# test_cube.py
# python3 -m unittest src/test/test_cube.py

import unittest
from src.cube.cube import Cube

class TestCubeRotations(unittest.TestCase):
    def setUp(self):
        self.cube = Cube()

    def test_front_clockwise_rotation(self):
        self.cube.rotate_front_clockwise()
        file = open("src/test/text_files/fcr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()
        
    def test_front_counterclockwise_rotation(self):
        self.cube.rotate_front_counterclockwise()
        file = open("src/test/text_files/fccr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()
        
    def test_back_clockwise_rotation(self):
        self.cube.rotate_back_clockwise()
        file = open("src/test/text_files/bcr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

    def test_back_counterclockwise_rotation(self):
        self.cube.rotate_back_counterclockwise()
        file = open("src/test/text_files/bccr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

    def test_top_clockwise_rotation(self):
        self.cube.rotate_top_clockwise()
        file = open("src/test/text_files/tcr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

    def test_top_counterclockwise_rotation(self):
        self.cube.rotate_top_counterclockwise()
        file = open("src/test/text_files/tccr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

    def test_bottom_clockwise_rotation(self):
        self.cube.rotate_bottom_clockwise()
        file = open("src/test/text_files/dcr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

    def test_bottom_counterclockwise_rotation(self):
        self.cube.rotate_bottom_counterclockwise()
        file = open("src/test/text_files/dccr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

    def test_left_clockwise_rotation(self):
        self.cube.rotate_left_clockwise()
        file = open("src/test/text_files/lcr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

    def test_left_counterclockwise_rotation(self):
        self.cube.rotate_left_counterclockwise()
        file = open("src/test/text_files/lccr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

    def test_right_clockwise_rotation(self):
        self.cube.rotate_right_clockwise()
        file = open("src/test/text_files/rcr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

    def test_right_counterclockwise_rotation(self):
        self.cube.rotate_right_counterclockwise()
        file = open("src/test/text_files/rccr.txt", 'r')
        cube_string = file.read()
        self.assertEqual(str(self.cube), cube_string)
        file.close()

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
        file = open("src/test/text_files/solved_cube_string.txt", 'r')
        solved_cube_string = file.read()
        self.assertEqual(str(self.cube), solved_cube_string)
        self.assertTrue(self.cube.is_solved())
        file.close()

    def test_unsolved_cube_after_one_rotation(self):
        self.assertTrue(self.cube.is_solved())
        self.cube.rotate_front_clockwise()
        self.assertFalse(self.cube.is_solved())

    def test_unsolved_cube_after_scramble(self):
        self.assertTrue(self.cube.is_solved())
        self.cube.scramble()
        self.assertFalse(self.cube.is_solved())

if __name__ == '__main__':
    unittest.main()