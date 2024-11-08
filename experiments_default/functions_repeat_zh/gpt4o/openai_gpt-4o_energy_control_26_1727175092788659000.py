# Based on your functional description and the provided source code, I will create a `function.py` file to meet your requirements.
# 
# Here is the `function.py` file:
# 
# ### function.py

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, AC
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH

def main():
    # Get the home plan
    home = home_plan()

    # Print initial status
    print("Initial Home Status:")
    for room in home:
        room.print_info()

    # Define the rooms to monitor
    rooms_to_monitor = ['LivingRoom', 'Bedroom']

    while True:
        for room_name in rooms_to_monitor:
            room = get_room(home, room_name)

            if room:
                # Get AC and Window actuators
                acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
                windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]

                for ac in acs:
                    if ac.get_status() == 'on':
                        for window in windows:
                            window.turn_off()

                # Get temperature sensors
                indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
                outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]

                for indoor_temp_sensor in indoor_temp_sensors:
                    indoor_temp = indoor_temp_sensor.get_reading()
                    if indoor_temp is not None and indoor_temp > TEMP_HIGH:
                        for outdoor_temp_sensor in outdoor_temp_sensors:
                            outdoor_temp = outdoor_temp_sensor.get_reading()
                            if outdoor_temp is not None and outdoor_temp < TEMP_HIGH:
                                for window in windows:
                                    window.turn_on()

        time.sleep(1)  # Delay for a while before checking again

if __name__ == "__main__":
    main()