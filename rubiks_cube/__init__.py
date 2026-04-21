from gymnasium.envs.registration import register
from rubiks_cube.cube import CubeEnv  # noqa

register(
    id="RubiksCube-v0",
    entry_point="rubiks_cube.ai:RubiksCubeEnv",
    max_episode_steps=150,
)
