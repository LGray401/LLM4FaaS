# Sure! Based on the functional description and the provided source code, I'll create the `function.py` file that will be located in the `functions` folder. This file will contain a `main` function that will handle the specified automation logic.
# 
# Here's the `function.py` file:
# 
# ### function.py

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, AC
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.config import TEMP_CHANGE_DURATION_WINDOW

def main():
    home = home_plan()
    
    # Get the relevant sensors and actuators
    bedroom_sensors = get_room_sensors(home, "Bedroom")
    bedroom_actuators = get_room_actuators(home, "Bedroom")
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    outdoor_sensors = get_all_sensors(home, "OutdoorTemperature")

    bedroom_ac = next((actuator for actuator in bedroom_actuators if isinstance(actuator, AC)), None)
    bedroom_windows = [actuator for actuator in bedroom_actuators if isinstance(actuator, Window)]
    living_room_ac = next((actuator for actuator in living_room_actuators if isinstance(actuator, AC)), None)
    living_room_windows = [actuator for actuator in living_room_actuators if isinstance(actuator, Window)]
    
    bedroom_temp_sensor = next((sensor for sensor in bedroom_sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    living_room_temp_sensor = next((sensor for sensor in living_room_sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    outdoor_temp_sensor = next((sensor for sensor in outdoor_sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)

    if not bedroom_ac or not living_room_ac or not bedroom_temp_sensor or not living_room_temp_sensor or not outdoor_temp_sensor:
        print("Necessary sensors or actuators are missing.")
        return
    
    while True:
        # Check Bedroom
        if bedroom_ac.get_status() == 'on':
            for window in bedroom_windows:
                window.turn_off()
        bedroom_temp = bedroom_temp_sensor.get_reading()
        outdoor_temp = outdoor_temp_sensor.get_reading()
        
        if bedroom_temp > 26 and outdoor_temp < 26:
            for window in bedroom_windows:
                window.turn_on()
        
        # Check Living Room
        if living_room_ac.get_status() == 'on':
            for window in living_room_windows:
                window.turn_off()
        living_room_temp = living_room_temp_sensor.get_reading()
        
        if living_room_temp > 26 and outdoor_temp < 26:
            for window in living_room_windows:
                window.turn_on()

        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()