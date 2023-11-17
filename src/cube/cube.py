# Malachi Eberly
# cube.py

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
        if x == 0: colors.append(self.colors['L'])
        elif x == 2: colors.append(self.colors['R'])
        if y == 0: colors.append(self.colors['U'])
        elif y == 2: colors.append(self.colors['D'])
        if z == 0: colors.append(self.colors['F'])
        elif z == 2: colors.append(self.colors['B'])

        piece_type = 'center' if len(colors) == 1 else 'edge' if len(colors) == 2 else 'corner'
        return Piece(piece_type, tuple(colors))