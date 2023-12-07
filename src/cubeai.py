# Malachi Eberly
# cubeai.py

from src.cube import CubeEnv
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.utils import set_random_seed

def main():
    # Create the environment
    env = make_vec_env(CubeEnv, n_envs=4)
    policy = 'MlpPolicy'

    # Initialize the agent
    model = PPO(policy, env, verbose=1,
                learning_rate=0.00025,
                n_steps=2048,
                batch_size=64,
                n_epochs=10,
                gamma=0.99,
                gae_lambda=0.95,
                clip_range=0.2,
                clip_range_vf=None,
                ent_coef=0.01,
                vf_coef=0.5,
                max_grad_norm=0.5,
                use_sde=False,
                sde_sample_freq=-1,
                target_kl=None,
                tensorboard_log="./ppo_rubiks_cube_tensorboard/",
                policy_kwargs=None,
                seed=42,
                device="auto",
                _init_setup_model=True)

    # Train the agent
    model.learn(total_timesteps=10000000)

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
            obs, reward, terminated, truncated, info = env.step(int(action))
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