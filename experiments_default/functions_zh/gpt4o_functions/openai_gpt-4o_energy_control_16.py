# Based on the provided code and functional description for a smart home project, here is the `function.py` file that should be located in the `functions` folder. This file will include the `main` function which will initialize the home plan and perform some basic operations for demonstration.
# 
# ### `function.py`

import time
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()
    # print_home_plan(home)

    # Example of automated energy-saving adjustments
    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        for sensor in sensors:
            sensor.turn_on()
            reading = sensor.get_reading()

            if sensor.sensor_type == "IndoorTemperature":
                heaters = [a for a in actuators if a.actuator_type == "Heater"]
                ac_units = [a for a in actuators if a.actuator_type == "AC"]
                
                for heater in heaters:
                    heater.set_target_temperature(TEMP_LOW)
                    heater.adjust_temperature(reading)
                
                for ac in ac_units:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(reading)

            elif sensor.sensor_type == "Humidity":
                humidifiers = [a for a in actuators if a.actuator_type == "Humidifier"]
                
                for humidifier in humidifiers:
                    if reading < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif reading > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

            elif sensor.sensor_type == "LightIntensive":
                lights = [a for a in actuators if a.actuator_type == "Light"]
                
                for light in lights:
                    if reading < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif reading > LIGHT_INTENSITY_HIGH:
                        light.turn_off()

            sensor.turn_off()
            time.sleep(1)  # simulate some delay for the sensors to turn off

if __name__ == "__main__":
    main()