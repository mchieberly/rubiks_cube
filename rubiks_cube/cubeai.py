# Malachi Eberly
# cubeai.py

from rubiks_cube.cube import CubeEnv
from stable_baselines3 import DQN
from stable_baselines3.her.her_replay_buffer import HerReplayBuffer


def main():
    env = CubeEnv()

    model = DQN(
        "MultiInputPolicy",
        env,
        replay_buffer_class=HerReplayBuffer,
        replay_buffer_kwargs=dict(
            n_sampled_goal=4,
            goal_selection_strategy="future",
        ),
        learning_starts=1500,
        buffer_size=100000,
        verbose=1,
    )

    model.learn(total_timesteps=100000)
    model.save("dqn_her_rubikscube")

    test_agent(env, model)


def test_agent(env, model, num_tests=10):
    for test in range(num_tests):
        obs, _ = env.reset()
        num_steps = 0
        rewards = 0
        while True:
            action, _ = model.predict(obs, deterministic=True)
            obs, reward, terminated, truncated, info = env.step(int(action))
            num_steps += 1
            rewards += reward
            if terminated:
                print(f"Test {test + 1}: Solved in {num_steps} steps.")
                env.render()
                break
            if truncated:
                print(f"Ran out of all 150 moves, failed to solve. Reward: {rewards}")
                env.render()
                break


if __name__ == "__main__":
    main()
