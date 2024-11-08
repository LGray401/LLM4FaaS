# Certainly! Based on your functional description and the provided source code, I will create a `function.py` file. This file will implement the described energy-saving modes. Here is the `function.py`:
# 
# ## function.py

import time
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW

def energy_saving_mode(home):
    for room in home:
        # Get relevant sensors and actuators
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]
        light_sensors = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]
        
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]

        # Ensure all sensors are turned on to get readings
        for sensor in indoor_temp_sensors + outdoor_temp_sensors + light_sensors:
            sensor.turn_on()

        # Get readings from sensors
        indoor_temp = None
        outdoor_temp = None
        light_intensity = None

        if indoor_temp_sensors:
            indoor_temp = indoor_temp_sensors[0].get_reading()
        if outdoor_temp_sensors:
            outdoor_temp = outdoor_temp_sensors[0].get_reading()
        if light_sensors:
            light_intensity = light_sensors[0].get_reading()

        # Apply energy-saving mode logic
        if indoor_temp is not None and outdoor_temp is not None:
            if outdoor_temp < indoor_temp:
                for window in windows:
                    window.turn_on()
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                for window in windows:
                    window.turn_off()
            elif indoor_temp < outdoor_temp and light_intensity is not None and light_intensity > 900:
                for curtain in curtains:
                    curtain.turn_on()
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                for curtain in curtains:
                    curtain.turn_off()

        # Ensure all sensors are turned off after getting readings
        for sensor in indoor_temp_sensors + outdoor_temp_sensors + light_sensors:
            sensor.turn_off()

def main():
    home = home_plan()
    energy_saving_mode(home)

if __name__ == "__main__":
    main()