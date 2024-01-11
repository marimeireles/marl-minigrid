import numpy as np
import marlgrid
from marlgrid.envs import env_from_config

class SimpleAgent:
    def __init__(self, action_space):
        self.action_space = action_space

    def select_action(self):
        return self.action_space.sample()

# Environment configuration for multiple agents
env_config = {
    "env_class": "ClutteredGoalCycleEnv",
    "grid_size": 15,
    "max_steps": 250,
    "clutter_density": 0.10,
    "respawn": True,
    "ghost_mode": True,
    "reward_decay": False,
    "n_bonus_tiles": 3,
    "initial_reward": True,
    "penalty": -1.5,
    "agents": [
        {"view_size": 7, "view_offset": 1, "view_tile_size": 11, "observation_style": "rich", "color": "red"},
        {"view_size": 7, "view_offset": 1, "view_tile_size": 11, "observation_style": "rich", "color": "blue"}
        # Add more agent configurations if needed
    ]
}

env = env_from_config(env_config)

# Create simple agents
agents = [SimpleAgent(env.action_space.spaces[i]) for i in range(len(env.agents))]

# Start an episode
obs_list = env.reset()

done = False
while not done:
    env.render()

    # Get actions for all agents
    agent_actions = [agent.select_action() for agent in agents]

    # Environment steps
    next_obs_list, rew_list, done, _ = env.step(agent_actions)
    obs_list = next_obs_list

# Episode finished
print("Episode finished")
