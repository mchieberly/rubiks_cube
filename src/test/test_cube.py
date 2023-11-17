from src.cube.cube import Cube

cube = Cube()
for x in range(3):
    for y in range(3):
        for z in range(3):
            print(cube.cube[x][y][z])