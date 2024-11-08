# Here's the `function.py` file for your smart home project based on the provided functional description and source code. This file will be placed in the `functions` folder and will contain the main function to manage your smart home automation:
# 
# ### function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, TEMP_CHANGE_DURATION_WINDOW
import time

def main():
    # Initialize home plan
    home = home_plan()
    
    # Get all necessary sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")
    windows = get_all_actuators(home, "Window")
    smart_sockets = get_all_actuators(home, "SmartSocket")
    doors = get_all_actuators(home, "Door")

    # Iterate over sensors and actuators periodically
    while True:
        control_heating(indoor_temp_sensors, heaters)
        control_ac(indoor_temp_sensors, outdoor_temp_sensors, ac_units, windows, doors)
        control_lights(light_sensors, lights)
        control_sockets(smart_sockets)
        
        time.sleep(5)  # Wait for a while before repeating

def control_heating(indoor_temp_sensors, heaters):
    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        if current_temp is None:
            continue

        if current_temp < TEMP_LOW:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.turn_on()
        else:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.turn_off()

def control_ac(indoor_temp_sensors, outdoor_temp_sensors, ac_units, windows, doors):
    for sensor in indoor_temp_sensors:
        current_indoor_temp = sensor.get_reading()
        if current_indoor_temp is None:
            continue

        for ac_unit in ac_units:
            if ac_unit.room_name == sensor.room_name:
                if current_indoor_temp > TEMP_HIGH:
                    close_doors_and_windows(windows, doors, sensor.room_name)
                    ac_unit.turn_on()
                else:
                    ac_unit.turn_off()

def close_doors_and_windows(windows, doors, room_name):
    for window in windows:
        if window.room_name == room_name:
            window.turn_off()

    for door in doors:
        if door.room_name == room_name:
            door.turn_off()

def control_lights(light_sensors, lights):
    for sensor in light_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is None:
            continue

        for light in lights:
            if light.room_name == sensor.room_name:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                else:
                    light.turn_off()

def control_sockets(smart_sockets):
    for socket in smart_sockets:
        if socket.get_status() == "off":
            socket.turn_off()

if __name__ == "__main__":
    main()