# Given your functional description to turn off the living room lights, here's the content for the `function.py` file that meets your requirements. The `function.py` file will utilize the classes defined in your `actuator.py` and `home_plan.py` files to turn off the light in the living room.
# 
# Here is the content for `function.py`:
# 
# ```python
from home.home_plan import home_plan
from home.actuator import Light

def main():
    # Create the home plan
    home = home_plan()

    # Find the Living Room
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if living_room:
        # Get all lights in the Living Room
        lights = [actuator for actuator in living_room.actuators if isinstance(actuator, Light)]
        
        if lights:
            # Turn off the lights in the Living Room
            for light in lights:
                light.turn_off()
        else:
            print("No lights found in the Living Room.")
    else:
        print("Living Room not found in home plan.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Import Statements**: The necessary classes are imported from your existing modules.
# 2. **Main Function**: 
#    - It generates the home plan.
#    - Searches for the "LivingRoom".
#    - Retrieves all actuators of type `Light`.
#    - Turns off each light it finds in the living room.
# 3. **Execution**: The script will only execute the `main()` function if it's run as the main program.
# 
# Make sure to place this `function.py` file inside the `functions` folder of your project. This script will accomplish the task of turning off the lights in the living room as per your functional requirement.