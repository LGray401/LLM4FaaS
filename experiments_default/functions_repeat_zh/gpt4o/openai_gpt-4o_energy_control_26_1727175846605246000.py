# Let's create the `function.py` file based on your functional description and the provided source code. This file will contain the main function that orchestrates the interactions between sensors and actuators according to the specified rules.
# 
# ### function.py

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH

def main():
    home = home_plan()

    while True:
        for room in ["LivingRoom", "Bedroom"]:
            acs = [actuator for actuator in get_room_actuators(home, room) if isinstance(actuator, AC)]
            windows = [actuator for actuator in get_room_actuators(home, room) if isinstance(actuator, Window)]
            indoor_temp_sensors = [sensor for sensor in get_room_sensors(home, room) if isinstance(sensor, IndoorTemperatureSensor)]
            outdoor_temp_sensors = [sensor for sensor in get_room_sensors(home, "Balcony") if isinstance(sensor, OutdoorTemperatureSensor)]

            # Check if AC is on and close the windows
            for ac in acs:
                if ac.get_status() == "on":
                    for window in windows:
                        window.turn_off()

            # Check temperature conditions to open/close windows
            for indoor_sensor in indoor_temp_sensors:
                indoor_temp = indoor_sensor.get_reading()
                if indoor_temp is None:
                    continue

                for outdoor_sensor in outdoor_temp_sensors:
                    outdoor_temp = outdoor_sensor.get_reading()
                    if outdoor_temp is None:
                        continue

                    if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_HIGH:
                        for window in windows:
                            window.turn_on()

        time.sleep(1)  # Add a delay to simulate real-time system

if __name__ == "__main__":
    main()