# Sure, I'll help you create the `function.py` file based on the provided functional description and the existing code base.
# 
# The functional description specifies two energy-saving modes:
# 1. If the outdoor temperature is lower than the indoor temperature, open the window.
# 2. If the indoor temperature is lower than the outdoor temperature and the sunlight is intense, close the curtain.
# 
# Here's the `function.py` file that will include a main function to implement these modes:

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW

def energy_saving_mode(home):
    for room in home:
        # Get sensors
        indoor_temp_sensor = None
        outdoor_temp_sensor = None
        light_intensive_sensor = None

        for sensor in room.sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp_sensor = sensor
            elif isinstance(sensor, OutdoorTemperatureSensor):
                outdoor_temp_sensor = sensor
            elif isinstance(sensor, LightIntensiveSensor):
                light_intensive_sensor = sensor

        # Get actuators
        window = None
        curtain = None

        for actuator in room.actuators:
            if isinstance(actuator, Window):
                window = actuator
            elif isinstance(actuator, Curtain):
                curtain = actuator

        # Check conditions and act
        if indoor_temp_sensor and outdoor_temp_sensor and window:
            indoor_temp_sensor.turn_on()
            outdoor_temp_sensor.turn_on()
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            if outdoor_temp < indoor_temp:
                window.turn_on()  # Open window
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Simulate the time for temperature change
                window.turn_off()  # Close window

        if indoor_temp_sensor and outdoor_temp_sensor and light_intensive_sensor and curtain:
            indoor_temp_sensor.turn_on()
            outdoor_temp_sensor.turn_on()
            light_intensive_sensor.turn_on()
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            light_intensity = light_intensive_sensor.get_reading()

            if indoor_temp < outdoor_temp and light_intensity > LIGHT_INTENSITY_HIGH:
                curtain.turn_on()  # Close curtain

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()