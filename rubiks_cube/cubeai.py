# Malachi Eberly
# cubeai.py

from collections import deque

from rubiks_cube.cube import CubeEnv
from stable_baselines3 import DQN
from stable_baselines3.common.callbacks import BaseCallback
from stable_baselines3.her.her_replay_buffer import HerReplayBuffer


class CurriculumCallback(BaseCallback):
    def __init__(
        self,
        success_threshold=0.8,
        window=100,
        max_scramble=25,
        verbose=1,
    ):
        super().__init__(verbose)
        self.success_threshold = success_threshold
        self.window = window
        self.max_scramble = max_scramble
        self.successes = deque(maxlen=window)
        self.current_scramble = 1

    def _on_training_start(self):
        self.training_env.env_method("set_scramble_moves", self.current_scramble)

    def _on_step(self):
        for info, done in zip(self.locals["infos"], self.locals["dones"]):
            if done:
                self.successes.append(float(info.get("is_success", False)))

        if (
            len(self.successes) >= self.window
            and self.current_scramble < self.max_scramble
        ):
            rate = sum(self.successes) / len(self.successes)
            if rate >= self.success_threshold:
                self.current_scramble += 1
                self.training_env.env_method(
                    "set_scramble_moves", self.current_scramble
                )
                self.successes.clear()
                if self.verbose:
                    print(
                        f"[curriculum] success {rate:.2f} -> "
                        f"scramble depth {self.current_scramble}"
                    )

        self.logger.record("curriculum/scramble_moves", self.current_scramble)
        if self.successes:
            self.logger.record(
                "curriculum/success_rate",
                sum(self.successes) / len(self.successes),
            )
        return True


def main():
    env = CubeEnv(scramble_moves=1)

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
        learning_rate=5e-4,
        batch_size=256,
        target_update_interval=1000,
        exploration_fraction=0.3,
        exploration_final_eps=0.1,
        verbose=1,
    )

    curriculum = CurriculumCallback(
        success_threshold=0.7,
        window=50,
        max_scramble=25,
    )

    model.learn(total_timesteps=1_000_000, callback=curriculum)
    model.save("dqn_her_rubikscube")

    test_agent(env, model)


def test_agent(env, model, num_tests=10):
    env.set_scramble_moves(25)
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
