# Based on your functional description and the provided source code, I will create a `function.py` file that implements the main function to adjust the state of a specific device (turning it on, off, brightening, or dimming). 
# 
# Here's how the `function.py` file will be structured:
# 
# 1. It will import necessary classes from the other modules.
# 2. It will provide a command-line interface (CLI) to interact with the user and perform actions on the actuators.
# 
# Here is the content of `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Light
from home.logger_config import logger

def main():
    # Create home plan
    home = home_plan()

    # User input for room and device action
    room_name = input("Enter the room name (LivingRoom/Bathroom/Balcony/etc.): ").strip()
    action = input("Enter action (turn on, turn off, brighten, dim): ").strip().lower()
    brightness_level = None

    # Get the room
    room = next((r for r in home if r.name == room_name), None)
    if not room:
        print(f"Room '{room_name}' not found.")
        logger.warning(f"Room '{room_name}' not found.")
        return

    # Get the light actuator in the room
    light = next((a for a in room.actuators if isinstance(a, Light)), None)
    if not light:
        print(f"No light actuator found in '{room_name}'.")
        logger.warning(f"No light actuator found in '{room_name}'.")
        return

    # Perform the action
    if action == "turn on":
        light.turn_on()
    elif action == "turn off":
        light.turn_off()
    elif action == "brighten":
        brightness_level = input("Enter brightness level (low, medium, high): ").strip().lower()
        light.set_brightness_level(brightness_level)
    elif action == "dim":
        # Assuming 'dim' means to lower the brightness by one step
        if light.brightness_level == 0:
            print("Light is already at minimum brightness.")
        elif light.brightness_level == 30:
            light.set_brightness_level("low")  # Assuming low is the minimum
        elif light.brightness_level == 60:
            light.set_brightness_level("low")
        elif light.brightness_level == 90:
            light.set_brightness_level("medium")
    else:
        print("Invalid action. Please enter 'turn on', 'turn off', 'brighten', or 'dim'.")

if __name__ == "__main__":
    main()