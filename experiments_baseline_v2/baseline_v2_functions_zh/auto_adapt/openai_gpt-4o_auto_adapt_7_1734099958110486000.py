# Based on the provided functional description and source code, we need to implement a smart home application that addresses specific conditions related to temperature, humidity, and light intensity in the home. We'll create a main script that utilizes the existing classes to simulate the smart home system's behavior according to the provided descriptions. Let's go through the requirements:
# 
# 1. **Temperature**: "屋里太热了" (It's too hot inside)
#    - We should turn on the AC if the temperature exceeds a certain threshold.
# 
# 2. **Humidity**: "屋里有点干" (It's a bit dry inside)
#    - We should turn on the Humidifier if the humidity falls below a certain threshold.
# 
# 3. **Light Intensity**: "屋里太暗了" (It's too dark inside)
#    - We should increase the light brightness if the light intensity falls below a certain threshold.
# 
# Given these requirements, here is a Python script that you can run in a Linux terminal. This script will simulate the home environment, check sensor readings, and adjust actuators accordingly.
# 
# ```python
#!/usr/bin/env python3

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Light
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def main():
    # Create the home plan
    home = home_plan()

    # Iterate through each room and process sensors and actuators
    for room in home:
        print(f"\nProcessing {room.name}...")

        # Check each sensor in the room
        for sensor in room.sensors:
            sensor.turn_on()
            reading = sensor.get_reading()

            # Handle temperature sensors
            if isinstance(sensor, IndoorTemperatureSensor):
                print(f"Temperature reading in {room.name}: {reading}°C")
                if reading > TEMP_HIGH:
                    # Find the AC in the room and turn it on
                    for actuator in room.actuators:
                        if isinstance(actuator, AC):
                            actuator.set_target_temperature(TEMP_HIGH - 5)
                            actuator.adjust_temperature(reading)

            # Handle humidity sensors
            elif isinstance(sensor, HumiditySensor):
                print(f"Humidity reading in {room.name}: {reading}%")
                if reading < HUMIDITY_LOW:
                    # Find the Humidifier in the room and turn it on
                    for actuator in room.actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.turn_on()
                            actuator.increase_humidity()

            # Handle light intensity sensors
            elif isinstance(sensor, LightIntensiveSensor):
                print(f"Light Intensity reading in {room.name}: {reading} lux")
                if reading < LIGHT_INTENSITY_LOW:
                    # Find the Light in the room and increase brightness
                    for actuator in room.actuators:
                        if isinstance(actuator, Light):
                            actuator.turn_on()
                            actuator.set_brightness_level('high')

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# 1. Save the script as `smart_home.py`.
# 2. Make sure the script is executable by running `chmod +x smart_home.py`.
# 3. Run the script in the terminal with `./smart_home.py`.
# 
# This script will simulate the smart home system by iterating over each room, turning on sensors, and adjusting the actuators based on the conditions specified in your functional description. The script uses the classes and methods provided in your reference code files.