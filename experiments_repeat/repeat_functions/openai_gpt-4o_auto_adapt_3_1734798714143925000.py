# Based on the functional description and the provided source code, we will create a `function.py` file with a `main` function. The purpose of this `main` function will be to simulate a basic interaction with your smart home system, focusing on reading temperature, humidity, and light intensity. It will also demonstrate how the sensors and actuators could be used together in a simple routine.
# 
# ```python
# function.py
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light

def main():
    # Initialize the home setup
    home = home_plan()

    # Example room
    room_name = "LivingRoom"

    # Retrieve sensors and actuators for a specific room
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    # Turn on all sensors in the room
    for sensor in sensors:
        sensor.turn_on()

    # Get readings from sensors
    temperature = None
    humidity = None
    light_intensity = None

    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature = sensor.get_reading()
        elif isinstance(sensor, HumiditySensor):
            humidity = sensor.get_reading()
        elif isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()

    # Adjust actuators based on sensor readings
    for actuator in actuators:
        if isinstance(actuator, Heater) or isinstance(actuator, AC):
            if temperature is not None:
                if temperature < 26:
                    actuator.set_target_temperature(26)
                    actuator.turn_on()
                else:
                    actuator.turn_off()
        elif isinstance(actuator, Humidifier):
            if humidity is not None:
                if humidity < 50:
                    actuator.increase_humidity()
                else:
                    actuator.decrease_humidity()
        elif isinstance(actuator, Light):
            if light_intensity is not None:
                if light_intensity < 900:
                    actuator.set_brightness_level("medium")
                else:
                    actuator.turn_off()

    # Turn off all sensors
    for sensor in sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Initialization**: The `home_plan()` function is called to initialize the home setup, which includes rooms and their associated sensors and actuators.
# - **Room Selection**: We choose a specific room, in this case, "LivingRoom", to demonstrate the interaction.
# - **Sensor Management**: All sensors in the room are turned on to get readings. Based on the readings, decisions are made to adjust the room environment.
# - **Actuator Control**: Depending on the sensor readings:
#   - Temperature is managed by turning on the heater or AC to reach a comfortable 26°C.
#   - Humidity is adjusted using a humidifier to maintain a 50% humidity level.
#   - Light intensity is managed by adjusting light brightness to a medium level if the intensity is low.
# - **Cleanup**: All sensors are turned off after the routine.
# 
# This script provides a basic framework for integrating sensors and actuators in a smart home setting, allowing for further customizations and enhancements.