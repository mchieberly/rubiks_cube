# Malachi Eberly
# cube.py

import random

class Cube:
    def __init__(self):
        self.solved_cube = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                            [[1, 1, 1], [1, 1, 1], [1, 1, 1]], 
                            [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
                            [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
                            [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
                            [[5, 5, 5], [5, 5, 5], [5, 5, 5]]]
        self.faces = {0 : 'Front', 1 : 'Back', 2 : 'Top', 3 : 'Bottom', 4 : 'Left', 5 : 'Right'}
        self.colors = {0 : 'green', 1 : 'blue', 2 : 'white', 3 : 'yellow', 4 : 'orange', 5 : 'red'}
        self.cube = [[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
                    [[1, 1, 1], [1, 1, 1], [1, 1, 1]], 
                    [[2, 2, 2], [2, 2, 2], [2, 2, 2]],
                    [[3, 3, 3], [3, 3, 3], [3, 3, 3]],
                    [[4, 4, 4], [4, 4, 4], [4, 4, 4]],
                    [[5, 5, 5], [5, 5, 5], [5, 5, 5]]]
        
    # =================================================================

    # Rotation methods

    def rotate_front_clockwise(self):
        row1, row2, row3, row4 = self.cube[2][2], [row[0] for row in self.cube[5]], \
            self.cube[3][0], [row[2] for row in self.cube[4]]
        self.cube[2][2], self.cube[3][0] = row4, row2
        for i in range(3):
            self.cube[5][i][0] = row1[i]
            self.cube[4][i][2] = row3[i]
        self.cube[0][0][0], self.cube[0][0][2], self.cube[0][2][2], self.cube[0][2][0] = \
        self.cube[0][2][0], self.cube[0][0][0], self.cube[0][0][2], self.cube[0][2][2]
        self.cube[0][0][1], self.cube[0][1][2], self.cube[0][2][1], self.cube[0][1][0] = \
        self.cube[0][1][0], self.cube[0][0][1], self.cube[0][1][2], self.cube[0][2][1]

    def rotate_front_counterclockwise(self):
        row1, row2, row3, row4 = self.cube[2][2], [row[0] for row in self.cube[5]], \
            self.cube[3][0], [row[2] for row in self.cube[4]]
        self.cube[2][2], self.cube[3][0] = row2, row4
        for i in range(3):
            self.cube[5][i][0] = row3[i]
            self.cube[4][i][2] = row1[i]
        self.cube[0][0][0], self.cube[0][0][2], self.cube[0][2][2], self.cube[0][2][0] = \
        self.cube[0][0][2], self.cube[0][2][2], self.cube[0][2][0], self.cube[0][0][0]
        self.cube[0][0][1], self.cube[0][1][2], self.cube[0][2][1], self.cube[0][1][0] = \
        self.cube[0][1][2], self.cube[0][2][1], self.cube[0][1][0], self.cube[0][0][1]

    def rotate_back_clockwise(self):
        row1, row2, row3, row4 = self.cube[2][0], [row[2] for row in self.cube[5]], \
            self.cube[3][2], [row[0] for row in self.cube[4]]
        self.cube[2][0], self.cube[3][2] = row2, row4
        for i in range(3):
            self.cube[5][i][2] = row3[i]
            self.cube[4][i][0] = row1[i]
        self.cube[1][0][0], self.cube[1][0][2], self.cube[1][2][2], self.cube[1][2][0] = \
        self.cube[1][2][0], self.cube[1][0][0], self.cube[1][0][2], self.cube[1][2][2]
        self.cube[1][0][1], self.cube[1][1][2], self.cube[1][2][1], self.cube[1][1][0] = \
        self.cube[1][1][0], self.cube[1][0][1], self.cube[1][1][2], self.cube[1][2][1]

    def rotate_back_counterclockwise(self):
        row1, row2, row3, row4 = self.cube[2][0], [row[2] for row in self.cube[5]], \
            self.cube[3][2], [row[0] for row in self.cube[4]]
        self.cube[2][0], self.cube[3][2] = row4, row2
        for i in range(3):
            self.cube[5][i][2] = row1[i]
            self.cube[4][i][0] = row3[i]
        self.cube[1][0][0], self.cube[1][0][2], self.cube[1][2][2], self.cube[1][2][0] = \
        self.cube[1][0][2], self.cube[1][2][2], self.cube[1][2][0], self.cube[1][0][0]
        self.cube[1][0][1], self.cube[1][1][2], self.cube[1][2][1], self.cube[1][1][0] = \
        self.cube[1][1][2], self.cube[1][2][1], self.cube[1][1][0], self.cube[1][0][1]

    def rotate_top_clockwise(self):
        self.cube[1][0], self.cube[5][0], self.cube[0][0], self.cube[4][0] = \
        self.cube[4][0], self.cube[1][0], self.cube[5][0], self.cube[0][0]
        self.cube[2][0][0], self.cube[2][0][2], self.cube[2][2][2], self.cube[2][2][0] = \
        self.cube[2][2][0], self.cube[2][0][0], self.cube[2][0][2], self.cube[2][2][2]
        self.cube[2][0][1], self.cube[2][1][2], self.cube[2][2][1], self.cube[2][1][0] = \
        self.cube[2][1][0], self.cube[2][0][1], self.cube[2][1][2], self.cube[2][2][1]

    def rotate_top_counterclockwise(self):
        self.cube[1][0], self.cube[5][0], self.cube[0][0], self.cube[4][0] = \
        self.cube[5][0], self.cube[0][0], self.cube[4][0], self.cube[1][0]
        self.cube[2][0][0], self.cube[2][0][2], self.cube[2][2][2], self.cube[2][2][0] = \
        self.cube[2][0][2], self.cube[2][2][2], self.cube[2][2][0], self.cube[2][0][0]
        self.cube[2][0][1], self.cube[2][1][2], self.cube[2][2][1], self.cube[2][1][0] = \
        self.cube[2][1][2], self.cube[2][2][1], self.cube[2][1][0], self.cube[2][0][1] 

    def rotate_bottom_clockwise(self):
        self.cube[0][2], self.cube[5][2], self.cube[1][2], self.cube[4][2] = \
        self.cube[4][2], self.cube[0][2], self.cube[5][2], self.cube[1][2]
        self.cube[3][0][0], self.cube[3][0][2], self.cube[3][2][2], self.cube[3][2][0] = \
        self.cube[3][2][0], self.cube[3][0][0], self.cube[3][0][2], self.cube[3][2][2]
        self.cube[3][0][1], self.cube[3][1][2], self.cube[3][2][1], self.cube[3][1][0] = \
        self.cube[3][1][0], self.cube[3][0][1], self.cube[3][1][2], self.cube[3][2][1] 

    def rotate_bottom_counterclockwise(self):
        self.cube[0][2], self.cube[5][2], self.cube[1][2], self.cube[4][2] = \
        self.cube[5][2], self.cube[1][2], self.cube[4][2], self.cube[0][2]
        self.cube[3][0][0], self.cube[3][0][2], self.cube[3][2][2], self.cube[3][2][0] = \
        self.cube[3][0][2], self.cube[3][2][2], self.cube[3][2][0], self.cube[3][0][0]
        self.cube[3][0][1], self.cube[3][1][2], self.cube[3][2][1], self.cube[3][1][0] = \
        self.cube[3][1][2], self.cube[3][2][1], self.cube[3][1][0], self.cube[3][0][1] 

    def rotate_left_clockwise(self):
        pass

    def rotate_left_counterclockwise(self):
        pass

    def rotate_right_clockwise(self):
        pass
    
    def rotate_right_counterclockwise(self):
        pass

    # =================================================================

    def scramble(self, moves=25):
        rotations = {
            'front': [self.rotate_front_clockwise, self.rotate_front_counterclockwise],
            'right': [self.rotate_right_clockwise, self.rotate_right_counterclockwise],
            'left': [self.rotate_left_clockwise, self.rotate_left_counterclockwise],
            'back': [self.rotate_back_clockwise, self.rotate_back_counterclockwise],
            'top': [self.rotate_top_clockwise, self.rotate_top_counterclockwise],
            'bottom': [self.rotate_bottom_clockwise, self.rotate_bottom_counterclockwise]
        }

        for _ in range(moves):
            face = random.choice(list(rotations.keys()))
            rotation = random.choice(rotations[face])
            rotation()

    def is_solved(self):
        if self.cube == self.solved_cube:
            return True
        return False

    def __str__(self):
        layout = "{0:>8}{1:>8}{2:>8}\n"
        cube_str = ""
        for face_name, face in enumerate(self.cube):
            cube_str += f"{self.faces[face_name]} face:\n"
            for row in face:
                cube_str += layout.format(self.colors[row[0]], self.colors[row[1]], self.colors[row[2]])
            if face_name < 5:
                cube_str += "\n"

        return cube_str