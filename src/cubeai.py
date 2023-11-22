# Malachi Eberly
# cubeai.py

from src.cube import CubeEnv
from stable_baselines3 import PPO

def main():
    # Create the environment
    env = CubeEnv()

    # Initialize the agent
    model = PPO('MlpPolicy', env, verbose=1)

    # Train the agent
    model.learn(total_timesteps=100000)

    # Save the model
    model.save("ppo_rubikscube")

    # Testing the trained agent
    test_agent(env, model)

def test_agent(env, model, num_tests=10):
    for test in range(num_tests):
        obs = env.reset()
        num_steps = 0
        rewards = 0
        while True:       
            obs = obs[0] if type(obs) == tuple else obs
            action, _states = model.predict(obs, deterministic=True)
            action = int(action)
            obs, reward, terminated, truncated, info = env.step(action)
            num_steps += 1
            rewards += reward
            if truncated:
                print(f"Test {test + 1}: Solved in {num_steps} steps.")
                env.render()
                break
            if terminated:
                print(f"Ran out of all 150 moves, failed to solve. Reward: {rewards}")
                env.render()
                break

if __name__ == "__main__":
    main()