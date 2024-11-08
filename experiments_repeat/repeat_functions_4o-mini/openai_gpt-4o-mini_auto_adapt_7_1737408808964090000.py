# Based on your functional description and the provided source code, here is the `function.py` file that will handle the logic of your smart home project. The main function will check the readings from the sensors and activate the appropriate actuators based on the conditions you've specified:
# 
# 1. If the temperature is too high, turn on the AC or Heater.
# 2. If the humidity is too low, activate the Humidifier.
# 3. If the light intensity is too low, turn on the Light.
# 
# Here is the proposed `function.py`:
# 
# ```python
# function.py

import time
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import AC, Heater, Humidifier, Light

def check_and_control(home):
    for room in home:
        print(f"\nChecking room: {room.name}")
        
        # Get the sensors in the room
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]

        # Get the actuators in the room
        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        heaters = [actuator for actuator in room.actuators if isinstance(actuator, Heater)]
        humidifiers = [actuator for actuator in room.actuators if isinstance(actuator, Humidifier)]
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]

        # Check temperature
        for temp_sensor in temperature_sensors:
            temp_sensor.turn_on()  # Make sure the sensor is on
            current_temperature = temp_sensor.get_reading()
            if current_temperature is not None:
                print(f"Current temperature in {room.name}: {current_temperature}°C")
                if current_temperature > TEMP_HIGH and acs:
                    print("Temperature is too high! Turning on AC...")
                    for ac in acs:
                        ac.set_target_temperature(TEMP_HIGH)  # Set target temperature
                        ac.adjust_temperature(current_temperature)
                elif current_temperature < TEMP_LOW and heaters:
                    print("Temperature is too low! Turning on Heater...")
                    for heater in heaters:
                        heater.set_target_temperature(TEMP_LOW)  # Set target temperature
                        heater.adjust_temperature(current_temperature)

        # Check humidity
        for humidity_sensor in humidity_sensors:
            humidity_sensor.turn_on()  # Make sure the sensor is on
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                print(f"Current humidity in {room.name}: {current_humidity}%")
                if current_humidity < HUMIDITY_LOW and humidifiers:
                    print("Humidity is too low! Activating Humidifier...")
                    for humidifier in humidifiers:
                        humidifier.increase_humidity()

        # Check light intensity
        for light_sensor in light_sensors:
            light_sensor.turn_on()  # Make sure the sensor is on
            current_light = light_sensor.get_reading()
            if current_light is not None:
                print(f"Current light intensity in {room.name}: {current_light} lux")
                if current_light < LIGHT_INTENSITY_LOW and lights:
                    print("Light intensity is too low! Turning on Lights...")
                    for light in lights:
                        light.turn_on()

def main():
    home = home_plan()  # Create the home plan
    while True:
        check_and_control(home)  # Check and control the home environment
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **check_and_control(home)**: This function checks the readings from the sensors in each room and activates the necessary actuators based on the conditions specified in your functional description.
# - **main()**: This function initializes the home plan and enters an infinite loop to repeatedly check the environmental conditions every 10 seconds.
# 
# Make sure to adjust the logic and parameters according to your specific requirements and test the functionality to ensure it works correctly in your smart home environment.