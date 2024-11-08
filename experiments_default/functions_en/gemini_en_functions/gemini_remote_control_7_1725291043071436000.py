from home.home_plan import get_room, get_room_actuators
from home.actuator import Light


def dim_bedroom_lights(home):
    """
    Dim the bedroom lights.

    Args:
        home: The home plan object.

    Returns:
        None
    """

    bedroom = get_room(home, "Bedroom")
    if bedroom:
        bedroom_lights = get_room_actuators(bedroom, "Light")
        if bedroom_lights:
            for light in bedroom_lights:
                if isinstance(light, Light):
                    light.set_brightness_level("low")
                    print(f"Dimmed lights in Bedroom: {light.id}")
        else:
            print(f"No lights found in Bedroom.")
    else:
        print(f"Bedroom not found in the home plan.")


# **Explanation:**

# 1. **Import necessary functions:**
#    - `get_room`:  Retrieves the `Bedroom` object from the `home` plan.
#    - `get_room_actuators`:  Retrieves all `Light` actuators in the `Bedroom`.
#    - `Light`: Represents the `Light` actuator class from `actuator.py`.

# 2. **`dim_bedroom_lights` function:**
#    - Takes the `home` plan object as input.
#    - Uses `get_room` to find the `Bedroom`.
#    - If the `Bedroom` is found, uses `get_room_actuators` to find all `Light` actuators in the room.
#    - Iterates through each `Light` actuator:
#       - Checks if the actuator is actually a `Light` instance.
#       - Calls `light.set_brightness_level("low")` to dim the light.
#       - Prints a confirmation message.
#    - Handles cases where the `Bedroom`, `Light` actuators, or either are not found.

# **How to use:**

# 1. **Import the function:**
#    ```python
#    from functions.function import dim_bedroom_lights
#    ```

# 2. **Get the `home` plan object:**
#    ```python
#    from home.home_plan import home_plan
#    home = home_plan()
#    ```

# 3. **Call the `dim_bedroom_lights` function:**
#    ```python
#    dim_bedroom_lights(home)
#    ```

# This will dim the lights in the `Bedroom` of your smart home simulation.
