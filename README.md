# Rubik's Cube
AI to speedrun a Rubik's Cube solve

Cube and AI code by Malachi Eberly
3D Rendering code by Ezekiel Eberly

Inspired by Code Bullet:
https://www.youtube.com/watch?v=f9smvQ5fc7Q&t=587s

To install the project:
```bash
# Clone the project
git clone git@github.com:mchieberly/rubiks_cube.git
cd rubiks_cube

# Initialize the virtual environment
uv venv
python -m ensurepip
python -m pip install --upgrade pip

# Install dependencies
uv pip install -e .
```

To run the AI agent:
```bash
cubeai
```

To run the unit tests:
```bash
python -m unittest rubiks_cube.test.test_cube
```
