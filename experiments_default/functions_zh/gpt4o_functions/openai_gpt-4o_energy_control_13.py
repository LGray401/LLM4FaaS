# Based on the functional description and the provided source code, I will create a `function.py` file that contains the main function to implement the described functionalities. 
# 
# Here's the `function.py` file:

import time
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Light, SmartSocket, Heater, AC, Window, Door
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, TEMP_CHANGE_DURATION_WINDOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Function to control lights
    def control_lights():
        light_sensors = get_all_sensors(home, "LightIntensive")
        lights = get_all_actuators(home, "Light")
        
        for light_sensor in light_sensors:
            reading = light_sensor.get_reading()
            if reading is not None and reading < LIGHT_INTENSITY_HIGH and light_sensor.get_status() == "on":
                for light in lights:
                    light.turn_off()

    # Function to control sockets
    def control_sockets():
        sockets = get_all_actuators(home, "SmartSocket")
        
        for socket in sockets:
            if socket.get_status() == "on":
                socket.turn_off()

    # Function to control heaters
    def control_heaters():
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        heaters = get_all_actuators(home, "Heater")
        
        for temp_sensor in indoor_temp_sensors:
            reading = temp_sensor.get_reading()
            if reading is not None and reading > TEMP_LOW:
                for heater in heaters:
                    heater.turn_off()

    # Function to control AC and windows
    def control_ac_and_windows():
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        windows = get_all_actuators(home, "Window")
        ac_units = get_all_actuators(home, "AC")
        doors = get_all_actuators(home, "Door")
        
        for temp_sensor in indoor_temp_sensors:
            reading = temp_sensor.get_reading()
            if reading is not None:
                if reading > TEMP_HIGH:
                    for window in windows:
                        window.turn_off()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                    for ac in ac_units:
                        ac.turn_on()
                else:
                    for window in windows:
                        window.turn_on()
                    for ac in ac_units:
                        ac.turn_off()

    # Execute control functions
    control_lights()
    control_sockets()
    control_heaters()
    control_ac_and_windows()

if __name__ == "__main__":
    main()