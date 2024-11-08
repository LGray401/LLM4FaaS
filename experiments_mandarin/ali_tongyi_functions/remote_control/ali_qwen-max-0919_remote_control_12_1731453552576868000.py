# Based on your functional description, you want to create a `function.py` file that will contain the main function to open windows in a specific room. This file will be located in the `functions` folder and will use the provided `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 
# Here is the `function.py` file with the main function to open windows in a specified room:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators

def main(room_name):
    # Create the home plan
    home = home_plan()

    # Get the actuators for the specified room
    actuators = get_room_actuators(home, room_name)

    if not actuators:
        print(f"No actuators found in {room_name}.")
        return

    # Find and open all windows in the specified room
    windows_opened = False
    for actuator in actuators:
        if actuator.actuator_type == "Window":
            if actuator.status == "off":
                actuator.turn_on()
                windows_opened = True
            else:
                print(f"Window {actuator.id} is already open.")

    if not windows_opened:
        print(f"No windows were opened in {room_name} because they are already open or no windows are present.")
    else:
        print(f"Windows in {room_name} have been opened.")

if __name__ == "__main__":
    # Example usage: Open windows in the "LivingRoom"
    main("LivingRoom")