# Based on the provided functional description and source code, I will create a `function.py` file that contains a main function to control the smart home system. The main function will read the sensor values, check if they meet the specified conditions, and then control the actuators accordingly.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()

    while True:
        # Iterate through each room in the home
        for room in home:
            # Get all sensors in the current room
            sensors = get_room_sensors(home, room.name)
            # Get all actuators in the current room
            actuators = get_room_actuators(home, room.name)

            # Check and control temperature
            for sensor in sensors:
                if isinstance(sensor, (IndoorTemperatureSensor, OutdoorTemperatureSensor)):
                    sensor.turn_on()
                    temp_reading = sensor.get_reading()
                    sensor.turn_off()

                    if temp_reading is not None:
                        for actuator in actuators:
                            if isinstance(actuator, Heater):
                                if temp_reading < TEMP_HIGH:
                                    actuator.set_target_temperature(TEMP_HIGH)
                                    actuator.adjust_temperature(temp_reading)
                                else:
                            elif isinstance(actuator, AC):
                                if temp_reading > TEMP_HIGH:
                                    actuator.set_target_temperature(TEMP_HIGH)
                                    actuator.adjust_temperature(temp_reading)
                                else:
                                    actuator.turn_off()

            # Check and control humidity
            for sensor in sensors:
                if isinstance(sensor, HumiditySensor):
                    sensor.turn_on()
                    humidity_reading = sensor.get_reading()
                    sensor.turn_off()

                    if humidity_reading is not None:
                        for actuator in actuators:
                            if isinstance(actuator, Humidifier):
                                if humidity_reading < HUMIDITY_LOW:
                                    actuator.increase_humidity()
                                else:
                                    actuator.decrease_humidity()

            # Check and control light intensity
            for sensor in sensors:
                if isinstance(sensor, LightIntensiveSensor):
                    sensor.turn_on()
                    light_reading = sensor.get_reading()
                    sensor.turn_off()

                    if light_reading is not None:
                        for actuator in actuators:
                            if isinstance(actuator, Light):
                                if light_reading < LIGHT_INTENSITY_HIGH:
                                    actuator.turn_on()
                                    actuator.set_brightness_level("high")
                                else:
                                    actuator.turn_off()

        # Sleep for a while before the next iteration
        time.sleep(60)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()