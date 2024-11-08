# Based on the functional description provided ("关闭客厅的灯", which translates to "turn off the lights in the living room") and the source code you've shared, I will create the `function.py` file in the `functions` folder. This file will contain a main function that will handle the logic to turn off the lights in the living room.
# 
# Here's the `function.py` file:
# 
# ```python
# function.py

from home.home_plan import home_plan
from home.actuator import Light

def turn_off_living_room_light():
    # Get the home plan
    home = home_plan()
    
    # Find the Living Room
    living_room = None
    for room in home:
        if room.name == "LivingRoom":
            living_room = room
            break
    
    if living_room is None:
        print("Living Room not found.")
        return

    # Get all lights in the Living Room
    lights = [actuator for actuator in living_room.actuators if isinstance(actuator, Light)]
    
    if not lights:
        print("No lights found in the Living Room.")
        return

    # Turn off all lights
    for light in lights:
        light.turn_off()
    
    print("All lights in the Living Room have been turned off.")

def main():
    turn_off_living_room_light()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Function Definition**: The function `turn_off_living_room_light` is defined to handle the logic of turning off all lights in the living room.
# 2. **Home Plan Retrieval**: It retrieves the home plan using the `home_plan` function.
# 3. **Room Search**: It searches for the "LivingRoom" in the home plan.
# 4. **Light Retrieval**: It retrieves all actuators of type `Light` in the living room.
# 5. **Turn Off Lights**: It iterates through the lights and calls the `turn_off` method on each.
# 6. **Main Function**: The `main` function is defined to invoke the light-turning-off functionality.
# 
# You can place this file in your `functions` directory, and it should work with the rest of your smart home project as intended. Make sure to adjust the import paths according to your project structure if necessary.