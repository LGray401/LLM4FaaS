# Based on your functional description of "开灯" (turn on the light) and the provided source code, I will create a `function.py` file within the `functions` folder. The `function.py` will contain a `main` function that will be responsible for turning on the lights in the smart home system.
# 
# Here is the `function.py`:

# functions/function.py

from home.sensor import LightIntensiveSensor
from home.actuator import Light
from home_plan import home_plan, get_room, get_room_actuators

def turn_on_light(room_name):
    # Get the room where the light is supposed to be turned on
    room = get_room(home_plan(), room_name)
    if room is None:
        print(f"No room named '{room_name}' found in the home plan.")
        return

    # Get the light actuator from the room
    lights = get_room_actuators(room, "Light")
    if not lights:
        print(f"No lights found in the room '{room_name}'.")
        return

    # Turn on the light
    lights[0].turn_on()  # Assuming there is at least one light in the room
    print(f"Light in '{room_name}' has been turned on.")

def main():
    # Example usage: turn on the light in the LivingRoom
    turn_on_light("LivingRoom")

if __name__ == "__main__":
    main()