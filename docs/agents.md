## `GridAgentInterface` Class

### Overview

`GridAgentInterface` is an extension of the `GridAgent` class, designed for creating agents in a grid-based environment. It is equipped with various actions, observation capabilities, and customizable parameters.

### Actions

The `GridAgentInterface` class defines an enumeration `actions` with the following members:

- `left`: Rotate the agent left.
- `right`: Rotate the agent right.
- `forward`: Move the agent forward.
- `pickup`: Pick up an object.
- `drop`: Drop an object.
- `toggle`: Toggle or activate an object.
- `done`: Indicate the task completion.

### Constructor

The constructor of the `GridAgentInterface` class has the following parameters:

- `name`: Name of the agent.
- `view_size`: The size of the agent's field of view.
- `view_tile_size`: The size of each tile in the agent's view.
- `view_offset`: Offset of the view.
- `observation_style`: Style of the observation (`"image"` or `"rich"`).
- `observe_rewards`: If `True`, includes rewards in observations.
- `observe_position`: If `True`, includes position in observations.
- `observe_orientation`: If `True`, includes orientation in observations.
- `restrict_actions`: If `True`, restricts the action space.
- `see_through_walls`: If `True`, allows the agent to see through walls.
- `hide_item_types`: List of item types to hide from the agent.
- `prestige_beta`: Scaling factor for prestige calculations.
- `prestige_scale`: Scale for prestige.
- `allow_negative_prestige`: If `True`, allows negative prestige values.
- `spawn_delay`: Delay before the agent spawns.
- `kwargs`: Additional keyword arguments.

### Methods

- `render_post(self, tile)`: Method for post-processing the rendered tile.
- `clone(self)`: Creates a clone of the agent.
- `on_step(self, obj)`: Defines behavior upon stepping on a grid cell.
- `reward(self, rew)`: Method to handle reward assignment.
- `activate(self)`: Activates the agent.
- `deactivate(self)`: Deactivates the agent.
- `reset(self, new_episode=False)`: Resets the agent state.
- `render(self, img)`: Renders the agent on an image.
- `dir_vec(self)`: Returns the direction vector of the agent.
- `right_vec(self)`: Returns the right vector relative to the agent's direction.
- `front_pos(self)`: Returns the position in front of the agent.
- `get_view_coords(self, i, j)`: Translates absolute grid coordinates to the agent's view coordinates.
- `get_view_pos(self)`: Returns the agent's view position.
- `get_view_exts(self)`: Returns the extents of the tiles visible to the agent.
- `relative_coords(self, x, y)`: Checks if a position is in the agent's field of view and returns corresponding coordinates.
- `in_view(self, x, y)`: Checks if a grid position is visible to the agent.
- `sees(self, x, y)`: Checks if the agent sees a particular cell. (Not implemented in the provided code)
- `process_vis(self, opacity_grid)`: Processes visibility based on an opacity grid.

### Numba-JIT Compiled Functions

- `occlude_mask(grid, agent_pos)`: A Numba JIT-compiled function to calculate occlusion masks.