# Based on the provided functional description and source code, I will create a `function.py` file that includes a main function to control the smart home system. The main function will read the current temperature, humidity, and light intensity from the sensors, and then adjust the actuators (like heaters, ACs, and lights) based on the given thresholds.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Define the rooms to monitor
    rooms_to_monitor = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]

    while True:
        for room_name in rooms_to_monitor:
            # Get sensors and actuators for the current room
            sensors = get_room_sensors(home, room_name)
            actuators = get_room_actuators(home, room_name)

            if not sensors or not actuators:
                print(f"Skipping {room_name} as it has no sensors or actuators.")
                continue

            # Get the current readings from the sensors
            indoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
            humidity_sensor = next((sensor for sensor in sensors if isinstance(sensor, HumiditySensor)), None)
            light_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)

            if not all([indoor_temp_sensor, humidity_sensor, light_sensor]):
                print(f"Skipping {room_name} as it has missing sensors.")
                continue

            indoor_temp_sensor.turn_on()
            humidity_sensor.turn_on()
            light_sensor.turn_on()

            current_temp = indoor_temp_sensor.get_reading()
            current_humidity = humidity_sensor.get_reading()
            current_light_intensity = light_sensor.get_reading()

            indoor_temp_sensor.turn_off()
            humidity_sensor.turn_off()
            light_sensor.turn_off()

            # Adjust the actuators based on the current readings
            heater = next((actuator for actuator in actuators if isinstance(actuator, Heater)), None)
            ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
            light = next((actuator for actuator in actuators if isinstance(actuator, Light)), None)

            if heater and ac:
                if current_temp < TEMP_LOW:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temp)
                elif current_temp > TEMP_HIGH:
                    ac.set_target_temperature(TEMP_LOW)
                    ac.adjust_temperature(current_temp)
                else:
                    heater.turn_off()
                    ac.turn_off()

            if light:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    light.turn_off()
                else:
                    light.set_brightness_level("medium")

            # Log the current status
            print(f"Room: {room_name}")
            print(f"Current Temperature: {current_temp}°C")
            print(f"Current Humidity: {current_humidity}%")
            print(f"Current Light Intensity: {current_light_intensity} lux")
            print("-" * 40)

        # Wait for a short period before the next check
        time.sleep(60)

if __name__ == "__main__":
    main()