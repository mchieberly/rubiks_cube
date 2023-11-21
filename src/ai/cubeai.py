# Malachi Eberly
# cubeai.py

from src.cube.cube import CubeEnv
from stable_baselines3 import PPO

def main():
    # Create the environment
    env = CubeEnv()

    # Initialize the agent
    model = PPO('MlpPolicy', env, verbose=1)

    # Train the agent
    model.learn(total_timesteps=100)

    # Save the model
    model.save("ppo_rubikscube")

    # Testing the trained agent
    test_agent(env, model)

def test_agent(env, model, num_tests=10):
    for test in range(num_tests):
        obs = env.reset()
        done = False
        num_steps = 0
        while not done:
            action, _states = model.predict(obs, deterministic=True)
            obs, rewards, terminated, truncated, info = env.step(action)
            num_steps += 1
            if done:
                print(f"Test {test + 1}: Solved in {num_steps} steps.")
                env.render()
                break

if __name__ == "__main__":
    main()