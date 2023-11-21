from gymnasium.envs.registration import register

register(
     id="src/RubiksCube",
     entry_point="src.ai:RubiksCubeEnv",
     max_episode_steps=100,
)