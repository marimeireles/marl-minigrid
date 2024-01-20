import numpy as np
import marlgrid
from marlgrid.envs import env_from_config


class SimpleAgent:
    def __init__(self, action_space):
        self.action_space = action_space

    # this is actually where you'd implement the policy
    # by default they're random
    def select_action(self):
        return self.action_space.sample()


# Environment configuration for multiple agents
env_config = {
    "env_class": "ClutteredGoalCycleEnv",
    "grid_size": 6,
    "max_steps": 1500,
    "clutter_density": 0.10,
    "respawn": True,
    "ghost_mode": True,
    "reward_decay": False,
    "n_bonus_tiles": 2,
    "initial_reward": True,
    "penalty": -1.5,
    "agents": [
        {
            "view_size": 7,
            "view_offset": 1,
            "view_tile_size": 5,
            "observe_rewards": True,
            "observation_style": "rich",
            "color": "red",
            "name": "morgan",
        },
        {
            "view_size": 7,
            "view_offset": 1,
            "view_tile_size": 15,
            "observe_rewards": True,
            "observation_style": "rich",
            "color": "blue",
            "name": "josephina_sus",
        }
        # Add more agent configurations if needed
    ],
}

env = env_from_config(env_config)

# Create empty simple agents
# What is within an agent class?
# An env object with action spaces, coming from marlgrid.envs. We supply the info above

# What is a malgrid.env?
# It receives configurations from env_config variable. it looks for the string contained in "env_class"
# makes sure this string is a MultiGridEnv type
# ** it means if I want to bring in the minigrid envs I'll clearly have to reimplement them to match
# this MultiGridEnv class

# What are some general characteristics of breaks consistency between the states of the grid objects?
# Inheriting from gym 0.26, meaning not up to date with Farama.
# class MultiGridEnv(gym.Env).
# the class completely defines what a grid is, they don't use minigrid much, just
# use some functions of it.
# the grid initializes the agents within itself.
#    the action_space belongs to agents, each also has their own observation_space
# has a warning about "breaks consistency between the states of the grid objects"
# but I haven't understood these implications fully

# Which optimization function these agents are using? Everything seems to be contained in the env.
# after checking the MultiGridEnv class it seems related to each individual environment
# so let's case study ClutteredGoalCycleEnv

# Observe ClutteredGoalCycleEnv:
# The goal here is to cycle through the yellow blocks, the agents kinda learn it fast
# around 1000 iterations and they already understand what they should be doing (depending on the random grid)


# EX: adding agents to an environment
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
