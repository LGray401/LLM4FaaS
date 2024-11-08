# To implement the functionality described, we need to create a `function.py` file in the `functions` directory. This file will contain the `main` function, which will handle the following tasks:
# 
# 1. Automatically close doors and windows when the AC is turned on.
# 2. Check indoor and outdoor temperatures, and if the indoor temperature is higher than the outdoor temperature, prompt the user to decide whether to open a window to cool down.
# 
# Here's how you can implement this:
# 
# ```python
# functions/function.py
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window, Door
from home.home_plan import home_plan, get_all_actuators, get_room_actuators
from home.config import TEMP_HIGH

def main():
    # Create the home plan
    home = home_plan()

    # Get all ACs in the home
    acs = get_all_actuators(home, "AC")
    
    # Iterate over all ACs
    for ac in acs:
        # Check if the AC is on
        if ac.get_status() == "on":
            # Get all windows and doors in the room of this AC
            actuators = get_room_actuators(home, ac.room_name)
            for actuator in actuators:
                if isinstance(actuator, Window) or isinstance(actuator, Door):
                    # Turn off windows and doors
                    actuator.turn_off()

    # Check the temperature conditions
    for room in home:
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]

        if indoor_temp_sensors and outdoor_temp_sensors:
            # Assume one sensor for simplicity
            indoor_temp = indoor_temp_sensors[0].get_reading()
            outdoor_temp = outdoor_temp_sensors[0].get_reading()

            if indoor_temp is not None and outdoor_temp is not None:
                if indoor_temp > TEMP_HIGH and indoor_temp > outdoor_temp:
                    # Prompt the user whether to open the window to cool down
                    response = input(f"The indoor temperature in {room.name} is higher than outdoors. Do you want to open a window to cool down? (yes/no): ").strip().lower()
                    if response == 'yes':
                        for actuator in actuators:
                            if isinstance(actuator, Window):
                                actuator.turn_on()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **AC Control**: We first retrieve all AC actuators and check if they are turned on. If they are, we turn off all windows and doors in the same room to ensure energy efficiency.
#   
# - **Temperature Check**: We check the indoor and outdoor temperatures using the respective sensors. If the indoor temperature is higher than the outdoor temperature and exceeds a high threshold, the user is prompted to decide whether to open a window to cool down.
# 
# ### Notes:
# - This implementation assumes that there is exactly one indoor and one outdoor temperature sensor per room. If there are multiple sensors, you may need to adjust the logic to handle averages or other criteria.
# - The `input` function is used to prompt the user. This assumes the script is run in an environment where user interaction is possible (like a terminal).
# - Make sure the `functions` directory exists and is correctly structured to include this `function.py` file.