# Based on the provided functional description and source code, I will create a `function.py` file that contains a main function to control the smart home system. The main function will read the current temperature, humidity, and light intensity from the sensors, and then adjust the actuators (like heaters, ACs, and lights) based on the readings and the thresholds defined in `config.py`.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()

    while True:
        # Iterate through each room in the home
        for room in home:
            # Get the sensors and actuators for the current room
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Initialize variables to store sensor readings
            indoor_temp = None
            humidity = None
            light_intensity = None

            # Read the sensor values
            for sensor in sensors:
                if isinstance(sensor, IndoorTemperatureSensor):
                    sensor.turn_on()
                    indoor_temp = sensor.get_reading()
                    sensor.turn_off()
                elif isinstance(sensor, HumiditySensor):
                    sensor.turn_on()
                    humidity = sensor.get_reading()
                    sensor.turn_off()
                elif isinstance(sensor, LightIntensiveSensor):
                    sensor.turn_on()
                    light_intensity = sensor.get_reading()
                    sensor.turn_off()

            # Adjust the actuators based on the sensor readings
            for actuator in actuators:
                if isinstance(actuator, Heater):
                    if indoor_temp is not None:
                        if indoor_temp < TEMP_LOW:
                            actuator.set_target_temperature(TEMP_HIGH)
                            actuator.adjust_temperature(indoor_temp)
                        else:
                            actuator.turn_off()
                elif isinstance(actuator, AC):
                    if indoor_temp is not None:
                        if indoor_temp > TEMP_HIGH:
                            actuator.set_target_temperature(TEMP_LOW)
                            actuator.adjust_temperature(indoor_temp)
                        else:
                            actuator.turn_off()
                elif isinstance(actuator, Light):
                    if light_intensity is not None:
                        if light_intensity < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()
                            actuator.set_brightness_level("high")
                        elif light_intensity > LIGHT_INTENSITY_HIGH:
                            actuator.turn_off()
                        else:
                            actuator.set_brightness_level("medium")

            # Log the current state of the room
            print(f"Room: {room.name}")
            print(f"  Temperature: {indoor_temp}°C")
            print(f"  Humidity: {humidity}%")
            print(f"  Light Intensity: {light_intensity} lux")
            print("  Actuators:")
            for actuator in actuators:
                print(f"    - {actuator.id}: {actuator.status}")

        # Wait for a short period before the next iteration
        time.sleep(10)

if __name__ == "__main__":
    main()