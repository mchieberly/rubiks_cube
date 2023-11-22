from gymnasium.envs.registration import register
from src.cube import CubeEnv

register(
     id="RubiksCube-v0",
     entry_point="src.ai:RubiksCubeEnv",
     max_episode_steps=150,
)