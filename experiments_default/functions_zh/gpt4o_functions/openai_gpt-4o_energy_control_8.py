# Sure, I'll help you create a `function.py` file that aligns with your description, which is to "打开空调，温度17度，同时关上窗户", meaning "turn on the air conditioner to 17 degrees and close the window".
# 
# Here's the `function.py`:

import sys
sys.path.append('../home')

from home_plan import home_plan, get_room_actuators
from actuator import AC, Window

def main():
    # Create home plan
    home = home_plan()

    # Specify the room you are working with, for example: 'LivingRoom'
    room_name = 'LivingRoom'

    # Get all actuators in the specified room
    actuators = get_room_actuators(home, room_name)

    if actuators is None:
        print(f"No actuators found in the room '{room_name}'")
        return

    # Initialize flags to check if we have found the AC and Window
    ac_found = False
    window_found = False

    # Iterate over the actuators to find the AC and Window
    for actuator in actuators:
        if isinstance(actuator, AC) and not ac_found:
            actuator.set_target_temperature(17)
            actuator.turn_on()
            ac_found = True
        elif isinstance(actuator, Window) and not window_found:
            actuator.turn_off()  # Assuming turn_off means "close the window"
            window_found = True

        # If both the AC and Window are found and set, break out of the loop
        if ac_found and window_found:
            break

    # If any of the required actuators are not found, print a message
    if not ac_found:
        print(f"No AC found in the room '{room_name}'")
    if not window_found:
        print(f"No Window found in the room '{room_name}'")

if __name__ == "__main__":
    main()