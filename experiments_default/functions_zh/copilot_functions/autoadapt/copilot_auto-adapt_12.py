# Based on the functional description and the provided source code, it seems like you need a `function.py` file that will handle the smart home's functionality. The file should be located in the 'functions' folder and should contain a main function.
#
# The functional description is in Chinese, but it seems to be related to temperature, humidity, and light intensity.
#
# Here's a basic structure for your `function.py` file:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    # Get the home plan
    home = home_plan()

    # Iterate over each room
    for room in home:
        # Get the sensors and actuators in the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Iterate over each sensor
        for sensor in sensors:
            # Get the sensor reading
            reading = sensor.get_reading()

            # Based on the sensor type, control the actuators
            if isinstance(sensor, IndoorTemperatureSensor):
                for actuator in actuators:
                    if isinstance(actuator, Heater):
                        if reading < 22:  # If temperature is less than 22
                            actuator.turn_on()
                        else:
                            actuator.turn_off()
                    elif isinstance(actuator, AC):
                        if reading > 22:  # If temperature is more than 22
                            actuator.turn_on()
                        else:
                            actuator.turn_off()

            elif isinstance(sensor, HumiditySensor):
            # Add your logic here based on the humidity reading

            elif isinstance(sensor, LightIntensiveSensor):
        # Add your logic here based on the light intensity reading

if __name__ == "__main__":
    main()
# ```
#
# This is a basic structure and you might need to modify it based on your exact requirements. For example, the logic for controlling the actuators based on the sensor readings is very basic and might not be suitable for your needs. You might also need to add error handling code.