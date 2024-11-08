# Based on your provided functional description and source code files, I'll create a smart home application in Python. The application will configure the sensors and actuators according to your description and simulate a smart home environment.
# 
# ### Implementation
# 
# I'll create a new Python script called `smart_home_application.py` to integrate your functional description with the provided source code.
# 
# Here's the code for `smart_home_application.py`:
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Assume we are managing the LivingRoom
    room_name = "LivingRoom"

    # Get sensors and actuators for the room
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    # Set desired conditions
    desired_temperature = 23  # Celsius
    desired_humidity_desc = "人感觉舒适"  # Comfortable
    desired_light_desc = "柔和"  # Soft

    # Map descriptions to values
    humidity_target = (HUMIDITY_LOW + HUMIDITY_HIGH) / 2
    light_target = (LIGHT_INTENSITY_LOW + LIGHT_INTENSITY_HIGH) / 2

    # Process sensors and adjust actuators
    for sensor in sensors:
        sensor.turn_on()
        reading = sensor.get_reading()

        if isinstance(sensor, IndoorTemperatureSensor):
            for actuator in actuators:
                if isinstance(actuator, Heater) or isinstance(actuator, AC):
                    actuator.set_target_temperature(desired_temperature)
                    actuator.adjust_temperature(reading)

        elif isinstance(sensor, HumiditySensor):
            for actuator in actuators:
                if isinstance(actuator, Humidifier):
                    if reading < humidity_target:
                        actuator.increase_humidity()
                    elif reading > humidity_target:
                        actuator.decrease_humidity()

        elif isinstance(sensor, LightIntensiveSensor):
            for actuator in actuators:
                if isinstance(actuator, Light):
                    if reading < light_target:
                        actuator.turn_on()
                        actuator.set_brightness_level("medium")
                    else:
                        actuator.turn_off()

        sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Command to Run the Application
# 
# To run the application from a Linux terminal, navigate to the directory where the `home` folder and the `smart_home_application.py` script are located. Then, use the following command:
# 
# ```bash
# python3 smart_home_application.py
# ```
# 
# ### Explanation
# 
# - **Temperature**: The application sets the target temperature to 23°C and adjusts the heater or AC accordingly.
# - **Humidity**: It uses a target value between the defined low and high thresholds to represent "人感觉舒适" (Comfortable).
# - **Light Intensity**: The application interprets "柔和" (Soft) as a medium light level and adjusts the lights in the room accordingly.
# 
# This script will simulate the smart home environment using the sensors and actuators defined in your provided code. Adjustments are made based on the desired settings specified in the functional description.