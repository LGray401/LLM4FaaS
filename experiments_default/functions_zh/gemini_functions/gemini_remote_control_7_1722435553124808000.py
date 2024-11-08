from home.home_plan import get_room, get_room_actuators, get_all_actuators

def main():
    # Get the home plan
    home = home_plan()

    # Get the bedroom
    bedroom = get_room(home, "Bedroom")

    # Get all lights in the bedroom
    bedroom_lights = get_room_actuators(home, "Bedroom", "Light")
    
    # Get all lights in the home
    all_lights = get_all_actuators(home, "Light")

    # Dim the lights in the bedroom
    for light in bedroom_lights:
        light.set_brightness_level("low")

    # Dim all the lights in the home
    for light in all_lights:
        light.set_brightness_level("low")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary functions:**
#    - `get_room`: Retrieves a specific room from the `home` plan.
#    - `get_room_actuators`: Retrieves actuators of a specific type within a room.
#    - `get_all_actuators`: Retrieves all actuators of a specific type in the home.

# 2. **`main()` function:**
#    - Creates a `home` plan using `home_plan()`.
#    - Gets the "Bedroom" room using `get_room()`.
#    - Gets all "Light" actuators in the "Bedroom" using `get_room_actuators()`.
#    - Gets all "Light" actuators in the entire `home` using `get_all_actuators()`.
#    - Iterates through the `bedroom_lights` and sets their brightness level to "low" using `set_brightness_level()`.
#    - Iterates through all `lights` and sets their brightness level to "low".

# **How to use this function.py file:**

# 1. **Save:** Save the code above in a file named `function.py` within your `functions` folder.
# 2. **Run:** From your project's root directory, run `python functions/function.py`.

# This will dim the lights in the "Bedroom" and all the lights in your home. 

# **Note:** This code assumes you have the other files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`) in the correct location within your project structure. 
