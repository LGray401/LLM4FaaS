# Here is the 'function.py' file based on your given functional description:

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_HIGH

def energy_saving_mode():
    while True:
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
        light_intensity_sensors = get_all_sensors(home, "LightIntensive")

        for indoor_temp_sensor in indoor_temp_sensors:
            indoor_temp = indoor_temp_sensor.get_reading()

        for outdoor_temp_sensor in outdoor_temp_sensors:
            outdoor_temp = outdoor_temp_sensor.get_reading()

        for light_intensity_sensor in light_intensity_sensors:
            light_intensity = light_intensity_sensor.get_reading()

        if outdoor_temp < indoor_temp and light_intensity > LIGHT_INTENSITY_HIGH:
            windows = get_all_actuators(home, "Window")
            for window in windows:
                window.turn_on()

        if indoor_temp < outdoor_temp:
            curtains = get_all_actuators(home, "Curtain")
            for curtain in curtains:
                curtain.turn_on()

        time.sleep(60)  # Wait for 1 minute before checking again

if __name__ == "__main__":
    energy_saving_mode()