# To create the `function.py` file based on your functional description "开窗关空调" (which translates to "open window, turn off AC"), we need to write a function that will achieve this behavior. The function should:
# 
# 1. Iterate through the rooms in the home.
# 2. Find the windows and AC units in each room.
# 3. Open the windows and turn off the AC.
# 
# We will use the classes and methods provided in your `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files to achieve this.
# 
# Here is the proposed content for the `function.py` file:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Window, AC

def main():
    # Get the home plan with all rooms and components
    home = home_plan()
    
    for room in home:
        print(f"Processing room: {room.name}")
        
        # Get actuators in the room
        actuators = get_room_actuators(home, room.name)
        
        if actuators:
            # Find windows and AC in the actuators
            windows = [actuator for actuator in actuators if isinstance(actuator, Window)]
            ac_units = [actuator for actuator in actuators if isinstance(actuator, AC)]
            
            # Open all windows
            for window in windows:
                if window.get_status() == 'off':
                    window.turn_on()  # Assuming 'on' means open for windows
            
            # Turn off all AC units
            for ac in ac_units:
                if ac.get_status() == 'on':
                    ac.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Imports**: We import necessary functions and classes from `home_plan` and `actuator`.
# - **home_plan()**: This function generates the home setup including rooms and their components.
# - **get_room_actuators()**: This function retrieves the actuators for each room.
# - **Loop through rooms**: We iterate over each room in the home setup.
# - **Filter actuators**: We filter out the actuators to find `Window` and `AC` types.
# - **Open windows**: We iterate over the windows and call `turn_on()` if the window is not already open.
# - **Turn off AC**: Similarly, we turn off any AC units that are currently on.
# 
# This script assumes that turning on a `Window` actuator means opening it, and turning off an `AC` means stopping it. Adjust these assumptions if your implementation details differ. Place this script in the `functions` folder as `function.py`.