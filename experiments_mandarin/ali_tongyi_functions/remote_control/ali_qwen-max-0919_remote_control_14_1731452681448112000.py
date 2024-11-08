# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to handle the command "小g 请打开客厅的灯" (which translates to "Please turn on the light in the living room"). This function will locate the lights in the living room and turn them on.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators
from home.actuator import Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def main():
    # Initialize the home plan
    home = home_plan()

    # Define the room name and actuator type
    room_name = "LivingRoom"
    actuator_type = Light

    # Get the actuators in the specified room
    actuators = get_room_actuators(home, room_name)

    # Filter out the lights in the room
    lights = [actuator for actuator in actuators if isinstance(actuator, actuator_type)]

    # Turn on each light in the room
    if lights:
        print(f"Turning on the lights in {room_name}...")
        for light in lights:
            light.turn_on()
    else:
        print(f"No lights found in {room_name}.")

if __name__ == "__main__":
    main()