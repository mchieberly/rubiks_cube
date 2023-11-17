# Malachi Eberly
# cube.py
# 3D render link:
# https://github.com/davidwhogg/MagicCube/tree/master

import random

class Piece:
    def __init__(self, piece_type, colors):
        self.piece_type = piece_type
        self.colors = colors

    def __repr__(self):
        return f"Piece(type={self.piece_type}, colors={self.colors})"

class Cube:
    def __init__(self):
        self.colors = {'U': 'white', 'D': 'yellow', 'F': 'green', 'B': 'blue', 'L': 'orange', 'R': 'red'}
        self.cube = [[[None for _ in range(3)] for _ in range(3)] for _ in range(3)]

        for x in range(3):
            for y in range(3):
                for z in range(3):
                    self.cube[x][y][z] = self.initialize_piece(x, y, z)

    def initialize_piece(self, x, y, z):
        colors = []
        if x == 0: colors.append(self.colors['L'])  # Left face
        if x == 2: colors.append(self.colors['R'])  # Right face
        if y == 0: colors.append(self.colors['U'])  # Top face
        if y == 2: colors.append(self.colors['D'])  # Bottom face
        if z == 0: colors.append(self.colors['F'])  # Front face
        if z == 2: colors.append(self.colors['B'])  # Back face

        piece_type = 'center' if len(colors) == 1 else 'edge' if len(colors) == 2 else 'corner'
        return Piece(piece_type, tuple(colors))

    def rotate_matrix_clockwise(self, matrix):
        return [list(reversed(col)) for col in zip(*matrix)]

    def rotate_matrix_counterclockwise(self, matrix):
        return [list(col) for col in reversed(list(zip(*matrix)))]

    # =================================================================

    # Rotation methods

    def rotate_front_clockwise(self):
        # Rotate the front face itself
        front_face = [row[0] for row in self.cube]
        rotated_front = self.rotate_matrix_clockwise(front_face)
        for i in range(3):
            for j in range(3):
                self.cube[i][j][0] = rotated_front[i][j]

        # Rotate the adjacent edges
        top_edge = [self.cube[2][i][0] for i in range(3)]
        right_edge = [self.cube[i][0][1] for i in range(3)]
        bottom_edge = [self.cube[0][i][0] for i in range(3)]
        left_edge = [self.cube[i][0][2] for i in range(3)]

        # Top edge to right edge
        for i in range(3):
            self.cube[i][0][1] = top_edge[i]

        # Right edge to bottom edge
        for i in range(3):
            self.cube[0][2 - i][0] = right_edge[i]

        # Bottom edge to left edge
        for i in range(3):
            self.cube[i][0][2] = bottom_edge[2 - i]

        # Left edge to top edge
        for i in range(3):
            self.cube[2][i][0] = left_edge[i]

    def rotate_front_counterclockwise(self):
        # Rotate the front face counterclockwise
        front_face = [row[0] for row in self.cube]
        rotated_front = self.rotate_matrix_counterclockwise(front_face)
        for i in range(3):
            for j in range(3):
                self.cube[i][j][0] = rotated_front[i][j]

        # Rotate the adjacent edges
        top_edge = [self.cube[2][i][0] for i in range(3)]
        left_edge = [self.cube[i][0][2] for i in range(3)]
        bottom_edge = [self.cube[0][i][0] for i in range(3)]
        right_edge = [self.cube[i][0][1] for i in range(3)]

        # Top edge to left edge
        for i in range(3):
            self.cube[i][0][2] = top_edge[2 - i]

        # Left edge to bottom edge
        for i in range(3):
            self.cube[0][i][0] = left_edge[i]

        # Bottom edge to right edge
        for i in range(3):
            self.cube[i][0][1] = bottom_edge[2 - i]

        # Right edge to top edge
        for i in range(3):
            self.cube[2][2 - i][0] = right_edge[i]

    def rotate_back_clockwise(self):
        # Rotate the back face itself
        back_face = [row[2] for row in self.cube]
        rotated_back = self.rotate_matrix_clockwise(back_face)
        for i in range(3):
            for j in range(3):
                self.cube[i][j][2] = rotated_back[i][j]

        # Rotate the adjacent edges
        top_edge = [self.cube[0][i][2] for i in range(3)]
        right_edge = [self.cube[i][2][2] for i in range(3)]
        bottom_edge = [self.cube[2][2 - i][2] for i in range(3)]
        left_edge = [self.cube[i][2][0] for i in range(3)]

        for i in range(3):
            self.cube[i][2][2] = top_edge[i]  # Top to right
            self.cube[2][2 - i][2] = right_edge[i]  # Right to bottom
            self.cube[i][2][0] = bottom_edge[2 - i]  # Bottom to left
            self.cube[0][i][2] = left_edge[i]  # Left to top

    def rotate_back_counterclockwise(self):
        # Rotate the back face itself
        back_face = [row[2] for row in self.cube]
        rotated_back = self.rotate_matrix_counterclockwise(back_face)
        for i in range(3):
            for j in range(3):
                self.cube[i][j][2] = rotated_back[i][j]

        # Rotate the adjacent edges
        top_edge = [self.cube[0][i][2] for i in range(3)]
        left_edge = [self.cube[i][2][0] for i in range(3)]
        bottom_edge = [self.cube[2][2 - i][2] for i in range(3)]
        right_edge = [self.cube[i][2][2] for i in range(3)]

        for i in range(3):
            self.cube[i][2][0] = top_edge[2 - i]  # Top to left
            self.cube[2][2 - i][2] = left_edge[i]  # Left to bottom
            self.cube[i][2][2] = bottom_edge[i]  # Bottom to right
            self.cube[0][i][2] = right_edge[i]  # Right to top

    def rotate_right_clockwise(self):
        # Rotate the right face itself
        right_face = [row[2] for row in self.cube]
        rotated_right = self.rotate_matrix_clockwise(right_face)
        for i in range(3):
            for j in range(3):
                self.cube[i][j][2] = rotated_right[i][j]

        # Rotate the adjacent edges
        top_edge = [self.cube[0][i][2] for i in range(3)]
        front_edge = [self.cube[i][2][0] for i in range(3)]
        bottom_edge = [self.cube[2][i][2] for i in range(3)]
        back_edge = [self.cube[i][2][2] for i in range(3)]

        for i in range(3):
            self.cube[i][2][0] = top_edge[i]  # Top to front
            self.cube[2][2 - i][2] = front_edge[i]  # Front to bottom
            self.cube[i][2][2] = bottom_edge[2 - i]  # Bottom to back
            self.cube[0][i][2] = back_edge[i]  # Back to top

    def rotate_right_counterclockwise(self):
        # Rotate the right face itself
        right_face = [row[2] for row in self.cube]
        rotated_right = self.rotate_matrix_counterclockwise(right_face)
        for i in range(3):
            for j in range(3):
                self.cube[i][j][2] = rotated_right[i][j]

        # Rotate the adjacent edges
        top_edge = [self.cube[0][i][2] for i in range(3)]
        back_edge = [self.cube[i][2][2] for i in range(3)]
        bottom_edge = [self.cube[2][i][2] for i in range(3)]
        front_edge = [self.cube[i][2][0] for i in range(3)]

        for i in range(3):
            self.cube[i][2][2] = top_edge[2 - i]  # Top to back
            self.cube[2][i][2] = back_edge[i]  # Back to bottom
            self.cube[i][2][0] = bottom_edge[2 - i]  # Bottom to front
            self.cube[0][2 - i][2] = front_edge[i]  # Front to top

    def rotate_left_clockwise(self):
        # Rotate the left face itself
        left_face = [row[0] for row in self.cube]
        rotated_left = self.rotate_matrix_clockwise(left_face)
        for i in range(3):
            for j in range(3):
                self.cube[i][j][0] = rotated_left[i][j]

        # Rotate the adjacent edges
        top_edge = [self.cube[0][i][0] for i in range(3)]
        back_edge = [self.cube[i][2][2] for i in range(3)]
        bottom_edge = [self.cube[2][2 - i][0] for i in range(3)]
        front_edge = [self.cube[i][0][0] for i in range(3)]

        for i in range(3):
            self.cube[i][2][2] = top_edge[i]  # Top to back
            self.cube[2][2 - i][0] = back_edge[i]  # Back to bottom
            self.cube[i][0][0] = bottom_edge[2 - i]  # Bottom to front
            self.cube[0][i][0] = front_edge[i]  # Front to top

    def rotate_left_counterclockwise(self):
        # Rotate the left face itself
        left_face = [row[0] for row in self.cube]
        rotated_left = self.rotate_matrix_counterclockwise(left_face)
        for i in range(3):
            for j in range(3):
                self.cube[i][j][0] = rotated_left[i][j]

        # Rotate the adjacent edges
        top_edge = [self.cube[0][i][0] for i in range(3)]
        front_edge = [self.cube[i][0][0] for i in range(3)]
        bottom_edge = [self.cube[2][2 - i][0] for i in range(3)]
        back_edge = [self.cube[i][2][2] for i in range(3)]

        for i in range(3):
            self.cube[i][0][0] = top_edge[2 - i]  # Top to front
            self.cube[2][2 - i][0] = front_edge[i]  # Front to bottom
            self.cube[i][2][2] = bottom_edge[i]  # Bottom to back
            self.cube[0][i][0] = back_edge[i]  # Back to top

    def rotate_top_clockwise(self):
        # Rotate the top face itself
        top_face = self.cube[0]
        rotated_top = self.rotate_matrix_clockwise(top_face)
        self.cube[0] = rotated_top

        # Rotate the adjacent edges
        front_edge = [self.cube[0][0][i] for i in range(3)]
        right_edge = [self.cube[i][0][2] for i in range(3)]
        back_edge = [self.cube[0][2][2 - i] for i in range(3)]
        left_edge = [self.cube[2 - i][0][0] for i in range(3)]

        for i in range(3):
            self.cube[i][0][2] = front_edge[i]  # Front to right
            self.cube[0][2][2 - i] = right_edge[i]  # Right to back
            self.cube[2 - i][0][0] = back_edge[i]  # Back to left
            self.cube[0][0][i] = left_edge[i]  # Left to front

    def rotate_top_counterclockwise(self):
        # Rotate the top face itself
        top_face = self.cube[0]
        rotated_top = self.rotate_matrix_counterclockwise(top_face)
        self.cube[0] = rotated_top

        # Rotate the adjacent edges
        front_edge = [self.cube[0][0][i] for i in range(3)]
        left_edge = [self.cube[2 - i][0][0] for i in range(3)]
        back_edge = [self.cube[0][2][2 - i] for i in range(3)]
        right_edge = [self.cube[i][0][2] for i in range(3)]

        for i in range(3):
            self.cube[2 - i][0][0] = front_edge[i]  # Front to left
            self.cube[0][2][2 - i] = left_edge[i]  # Left to back
            self.cube[i][0][2] = back_edge[i]  # Back to right
            self.cube[0][0][i] = right_edge[i]  # Right to front

    def rotate_bottom_clockwise(self):
        # Rotate the bottom face itself
        bottom_face = self.cube[2]
        rotated_bottom = self.rotate_matrix_clockwise(bottom_face)
        self.cube[2] = rotated_bottom

        # Rotate the adjacent edges
        front_edge = [self.cube[2][2][i] for i in range(3)]
        left_edge = [self.cube[i][2][0] for i in range(3)]
        back_edge = [self.cube[2][0][2 - i] for i in range(3)]
        right_edge = [self.cube[2 - i][2][2] for i in range(3)]

        for i in range(3):
            self.cube[i][2][0] = front_edge[i]  # Front to left
            self.cube[2][0][2 - i] = left_edge[i]  # Left to back
            self.cube[2 - i][2][2] = back_edge[i]  # Back to right
            self.cube[2][2][i] = right_edge[i]  # Right to front

    def rotate_bottom_counterclockwise(self):
        # Rotate the bottom face itself
        bottom_face = self.cube[2]
        rotated_bottom = self.rotate_matrix_counterclockwise(bottom_face)
        self.cube[2] = rotated_bottom

        # Rotate the adjacent edges
        front_edge = [self.cube[2][2][i] for i in range(3)]
        right_edge = [self.cube[2 - i][2][2] for i in range(3)]
        back_edge = [self.cube[2][0][2 - i] for i in range(3)]
        left_edge = [self.cube[i][2][0] for i in range(3)]

        for i in range(3):
            self.cube[2 - i][2][2] = front_edge[i]  # Front to right
            self.cube[2][0][2 - i] = right_edge[i]  # Right to back
            self.cube[i][2][0] = back_edge[i]  # Back to left
            self.cube[2][2][i] = left_edge[i]  # Left to front

    # =================================================================

    def is_solved(self):
        # Check if each face is of a uniform color
        for face in self.get_faces():
            if not self.is_face_uniform(face):
                return False
        return True

    def get_faces(self):
        # Extract the 6 faces of the cube
        faces = []
        faces.append([self.cube[i][j][0] for i in range(3) for j in range(3)])  # Front face
        faces.append([self.cube[i][j][2] for i in range(3) for j in range(3)])  # Back face
        faces.append([self.cube[0][i][j] for i in range(3) for j in range(3)])  # Top face
        faces.append([self.cube[2][i][j] for i in range(3) for j in range(3)])  # Bottom face
        faces.append([self.cube[i][0][j] for i in range(3) for j in range(3)])  # Left face
        faces.append([self.cube[i][2][j] for i in range(3) for j in range(3)])  # Right face
        return faces

    def is_face_uniform(self, face):
        # Check if all pieces on the face have the same color
        # Assuming the first color of each piece represents the color of the face
        face_color = face[0].colors[0]
        return all(piece.colors[0] == face_color for piece in face)

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

        print(f"Scrambled Cube with {moves} moves")

    def __str__(self):
        def format_face(face):
            face_str = ""
            for i in range(3):
                face_str += ' '.join(piece.colors[0] for piece in face[i*3:(i+1)*3]) + "\n"
            return face_str

        faces = self.get_faces()
        cube_str = ""
        for face_name, face in zip(['Front', 'Right', 'Back', 'Left', 'Top', 'Bottom'], faces):
            cube_str += f"{face_name} face:\n{format_face(face)}\n"
        return cube_str