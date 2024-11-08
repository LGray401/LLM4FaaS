# Given the functional description and the provided source code files, I will create a `function.py` file that implements the required functionality.
# 
# ## functions/function.py

import time
from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
from home.config import TEMP_CHANGE_DURATION_WINDOW

def main():
    # Initialize home plan
    home = home_plan()

    # Check the status of AC and windows in each room
    while True:
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
        for room in home:
            # Get the AC and window actuators
            acs = [act for act in room.actuators if isinstance(act, AC)]
            windows = [act for act in room.actuators if isinstance(act, Window)]

            # Get the temperature sensors
            indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
            outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")

            if not acs or not windows or not indoor_temp_sensors or not outdoor_temp_sensors:
                continue

            # Check AC status and control windows
            for ac in acs:
                if ac.get_status() == "on":
                    for window in windows:
                        window.turn_off()

            # Check temperature and control windows
            for indoor_temp_sensor in indoor_temp_sensors:
                indoor_temp_sensor.turn_on()
                indoor_temp = indoor_temp_sensor.get_reading()
                if indoor_temp > 26:
                    for outdoor_temp_sensor in outdoor_temp_sensors:
                        outdoor_temp_sensor.turn_on()
                        outdoor_temp = outdoor_temp_sensor.get_reading()
                        if outdoor_temp < 26:
                            for window in windows:
                                window.turn_on()

if __name__ == "__main__":
    main()