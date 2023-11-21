# Malachi Eberly
# cube.py

import numpy as np
import gymnasium as gym
from gymnasium import spaces
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
        row2.reverse()
        self.cube[2][2], self.cube[3][0] = row4, row2
        row4.reverse()
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
        row1.reverse()
        row3.reverse()
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
        row1.reverse()
        row3.reverse()
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
        row2.reverse()
        row4.reverse()
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
        row1, row2, row3, row4 = [row[0] for row in self.cube[2]], [row[0] for row in self.cube[0]], \
            [row[0] for row in self.cube[3]], [row[2] for row in self.cube[1]]
        row3.reverse()
        row4.reverse()
        for i in range(3):
            self.cube[2][i][0] = row4[i]
            self.cube[0][i][0] = row1[i]
            self.cube[3][i][0] = row2[i]
            self.cube[1][i][2] = row3[i]
        self.cube[4][0][0], self.cube[4][0][2], self.cube[4][2][2], self.cube[4][2][0] = \
        self.cube[4][2][0], self.cube[4][0][0], self.cube[4][0][2], self.cube[4][2][2]
        self.cube[4][0][1], self.cube[4][1][2], self.cube[4][2][1], self.cube[4][1][0] = \
        self.cube[4][1][0], self.cube[4][0][1], self.cube[4][1][2], self.cube[4][2][1] 

    def rotate_left_counterclockwise(self):
        row1, row2, row3, row4 = [row[0] for row in self.cube[2]], [row[0] for row in self.cube[0]], \
            [row[0] for row in self.cube[3]], [row[2] for row in self.cube[1]]
        row1.reverse()
        row4.reverse()
        for i in range(3):
            self.cube[2][i][0] = row2[i]
            self.cube[0][i][0] = row3[i]
            self.cube[3][i][0] = row4[i]
            self.cube[1][i][2] = row1[i]
        self.cube[4][0][0], self.cube[4][0][2], self.cube[4][2][2], self.cube[4][2][0] = \
        self.cube[4][0][2], self.cube[4][2][2], self.cube[4][2][0], self.cube[4][0][0]
        self.cube[4][0][1], self.cube[4][1][2], self.cube[4][2][1], self.cube[4][1][0] = \
        self.cube[4][1][2], self.cube[4][2][1], self.cube[4][1][0], self.cube[4][0][1] 

    def rotate_right_clockwise(self):
        row1, row2, row3, row4 = [row[2] for row in self.cube[2]], [row[0] for row in self.cube[1]], \
            [row[2] for row in self.cube[3]], [row[2] for row in self.cube[0]]
        row1.reverse()
        row2.reverse()
        for i in range(3):
            self.cube[2][i][2] = row4[i]
            self.cube[1][i][0] = row1[i]
            self.cube[3][i][2] = row2[i]
            self.cube[0][i][2] = row3[i]
        self.cube[5][0][0], self.cube[5][0][2], self.cube[5][2][2], self.cube[5][2][0] = \
        self.cube[5][2][0], self.cube[5][0][0], self.cube[5][0][2], self.cube[5][2][2]
        self.cube[5][0][1], self.cube[5][1][2], self.cube[5][2][1], self.cube[5][1][0] = \
        self.cube[5][1][0], self.cube[5][0][1], self.cube[5][1][2], self.cube[5][2][1] 
    
    def rotate_right_counterclockwise(self):
        row1, row2, row3, row4 = [row[2] for row in self.cube[2]], [row[0] for row in self.cube[1]], \
            [row[2] for row in self.cube[3]], [row[2] for row in self.cube[0]]
        row2.reverse()
        row3.reverse()
        for i in range(3):
            self.cube[2][i][2] = row2[i]
            self.cube[1][i][0] = row3[i]
            self.cube[3][i][2] = row4[i]
            self.cube[0][i][2] = row1[i]
        self.cube[5][0][0], self.cube[5][0][2], self.cube[5][2][2], self.cube[5][2][0] = \
        self.cube[5][0][2], self.cube[5][2][2], self.cube[5][2][0], self.cube[5][0][0]
        self.cube[5][0][1], self.cube[5][1][2], self.cube[5][2][1], self.cube[5][1][0] = \
        self.cube[5][1][2], self.cube[5][2][1], self.cube[5][1][0], self.cube[5][0][1] 

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

    ###########################################################################

    # RL Methods

    def get_observation(self):
        # Return the flattened state of the cube
        return np.array(self.cube).flatten()

    def step(self, action):
        # Perform the action (rotation)
        self.perform_rotation(action)

        # Check to see if we terminate
        terminated = False

        # Check if the cube is solved
        truncated = self.is_solved()

        # Define the reward
        # TODO: Implement reward method for steps to solve
        reward = 100 if truncated else -1

        # Return observation, reward, and done status
        return self.get_observation(), reward, terminated, truncated

    def reset(self):
        # Scramble the cube
        self.scramble()
        return self.get_observation()
    
    def perform_rotation(self, action):
        # Define the mapping from action number to cube rotation
        actions = {
            0: self.rotate_front_clockwise,
            1: self.rotate_front_counterclockwise,
            2: self.rotate_back_clockwise,
            3: self.rotate_back_counterclockwise,
            4: self.rotate_top_clockwise,
            5: self.rotate_top_counterclockwise,
            6: self.rotate_bottom_clockwise,
            7: self.rotate_bottom_counterclockwise,
            8: self.rotate_left_clockwise,
            9: self.rotate_left_counterclockwise,
            10: self.rotate_right_clockwise,
            11: self.rotate_right_counterclockwise
        }

        # Execute the rotation method corresponding to the action
        rotation_method = actions.get(action)
        if rotation_method:
            rotation_method()
        else:
            raise ValueError("Invalid action!")
    
class CubeEnv(gym.Env):
    metadata = {"render_modes": ["human"], "render_fps": 4}

    def __init__(self):
        self.cube = Cube()
        self.action_space = spaces.Discrete(12)
        self.observation_space = spaces.Box(low=0, high=5, shape=(54,), dtype=np.int64)

    def _get_obs(self):
        return np.array(self.cube.get_observation())

    def _get_info(self):
        # This method can provide additional info, e.g., number of correct positions
        return {}

    def step(self, action):
        obs, reward, terminated, truncated, _ = self.cube.step(action)
        return obs, reward, terminated, truncated, self._get_info()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)  # If using any RNG, ensure it's seeded correctly
        return self.cube.reset()

    def render(self, mode='human'):
        if mode == 'human':
            print(self.cube)