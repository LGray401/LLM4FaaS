# Based on the provided functional description and source code, here's the `function.py` file placed in the `functions` folder. This file will include the main function that handles the described smart home logic.
# 
# ### functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
from home.home_plan import home_plan, get_room, get_room_actuators

def main():
    # Create home setup
    home = home_plan()

    # Define the rooms of interest
    rooms_of_interest = ["LivingRoom", "Bedroom"]

    while True:
        for room_name in rooms_of_interest:
            room = get_room(home, room_name)
            if not room:
                continue

            # Get the AC and Window actuators for the room
            acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
            windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]

            # Check if the AC is on and close the windows if it is
            for ac in acs:
                if ac.get_status() == "on":
                    for window in windows:
                        window.turn_off()

            # Get the indoor and outdoor temperature sensors
            indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
            outdoor_temp_sensors = [sensor for sensor in home if isinstance(sensor, OutdoorTemperatureSensor)]

            # If no sensors are found, skip to the next room
            if not indoor_temp_sensors or not outdoor_temp_sensors:
                continue

            # Read the temperature from the sensors
            indoor_temp = indoor_temp_sensors[0].get_reading()
            outdoor_temp = outdoor_temp_sensors[0].get_reading()

            # Open the windows if indoor temp > 26 and outdoor temp < 26
            if indoor_temp and outdoor_temp and indoor_temp > 26 and outdoor_temp < 26:
                for window in windows:
                    window.turn_on()

        # Wait before the next reading
        time.sleep(10)

if __name__ == "__main__":
    main()