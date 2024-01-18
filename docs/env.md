## `ObjectRegistry` Class

### Overview

`ObjectRegistry` manages the mapping of objects to numeric keys and vice versa in a grid world. It facilitates representing objects using numerical arrays.

### Constructor

- `objs`: A list of initial objects.
- `max_num_objects`: Maximum number of objects to manage.

### Methods

- `get_next_key`: Returns the next available key for a new object.
- `add_object(obj)`: Adds an object and returns its key.
- `contains_object(obj)`: Checks if an object is in the registry.
- `contains_key(key)`: Checks if a key is in the registry.
- `get_key(obj)`: Retrieves the key of an object, adding it if not present.
- `obj_of_key(key)`: Retrieves the object associated with a key.

## `rotate_grid` Function

Rotates a grid by a specified number of 90-degree rotations.

- `grid`: The grid to rotate.
- `rot_k`: Number of 90-degree rotations.

## `MultiGrid` Class

### Overview

`MultiGrid` represents a grid in the environment, handling object placements and interactions.

### Constructor

- `shape`: Tuple or array specifying the grid's dimensions.
- `obj_reg`: An instance of `ObjectRegistry`.
- `orientation`: Initial orientation of the grid.

### Properties

- `opacity`: Returns a grid showing the opacity of each cell.

### Methods

- `rotate_left(k)`: Rotates the grid left by `k` steps.
- `slice(topX, topY, width, height, rot_k)`: Returns a sliced part of the grid.
- `set(i, j, obj)`: Places an object at a specified position.
- `get(i, j)`: Retrieves an object at a specified position.
- `horz_wall(x, y, length, obj_type)`: Places a horizontal wall.
- `vert_wall(x, y, length, obj_type)`: Places a vertical wall.
- `wall_rect(x, y, w, h, obj_type)`: Places a rectangular wall.
- `encode(vis_mask)`: Encodes the grid into a compact numpy array.
- `decode(array)`: Decodes a numpy array into a grid. (Not implemented)
- `cache_render_fun(key, f, *args, **kwargs)`: Caches a render function.
- `cache_render_obj(obj, tile_size, subdivs)`: Caches rendered objects.
- `empty_tile(tile_size, subdivs)`: Renders an empty tile.
- `render_object(obj, tile_size, subdivs)`: Renders an object.
- `blend_tiles(img1, img2)`: Blends two tile images.
- `render_tile(obj, tile_size, subdivs, top_agent)`: Renders a tile.
- `render(tile_size, highlight_mask, visible_mask, top_agent)`: Renders the entire grid.

## `MultiGridEnv` Class (Inherits from `gym.Env`)

### Overview

`MultiGridEnv` is a Gym environment for multi-agent gridworld simulations.

### Constructor

- `agents`: List of agents in the environment.
- `grid_size`: Size of the grid.
- `width`: Width of the grid.
- `height`: Height of the grid.
- `max_steps`: Maximum number of steps per episode.
- `reward_decay`: If `True`, decays rewards over time.
- `seed`: Random seed.
- `respawn`: If `True`, respawns agents after they're done.
- `ghost_mode`: If `True`, allows agent stacking.
- `agent_spawn_kwargs`: Additional arguments for spawning agents.

### Properties

- `action_space`: Defines the action space for the agents.
- `observation_space`: Defines the observation space for the agents.
- `num_agents`: Number of agents in the environment.

### Methods

- `add_agent(agent_interface)`: Adds an agent to the environment.
- `reset(**kwargs)`: Resets the environment.
- `gen_obs_grid(agent)`: Generates an observation grid for an agent.
- `gen_agent_obs(agent)`: Generates an observation for an agent.
- `gen_obs()`: Generates observations for all agents.
- `check_agent_position_integrity(title)`: Checks agent positions.
- `step(actions)`: Executes a step in the environment.
- `put_obj(obj, i, j)`: Places an object at a specific position.
- `try_place_obj(obj, pos)`: Tries to place an object at a position.
- `place_obj(obj, top, size, reject_fn, max_tries)`: Places an object with conditions.
- `place_agents(top, size, rand_dir, max_tries)`: Places agents. (Deprecated)
- `render(mode, close, highlight, tile_size, show_agent_views, max_agents_per_col, agent_col_width_frac, agent_col_padding_px, pad_grey)`: Renders the environment.