# Based on your functional description and the provided source code files, I will create a `function.py` file that implements the main function. This function will set the temperature to 17 degrees, ensure that the humidity is normal, and turn off the light.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import Heater, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor

def main():
    # Initialize home plan
    home = home_plan()

    # Get the living room (assuming we want to control these parameters in the living room)
    living_room = None
    for room in home:
        if room.name == "LivingRoom":
            living_room = room
            break

    if living_room is None:
        print("Living room not found in home plan.")
        return

    # Get the temperature sensor and actuator in the living room
    temperature_sensor = None
    heater = None
    for sensor in living_room.sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature_sensor = sensor
            break

    for actuator in living_room.actuators:
        if isinstance(actuator, Heater):
            heater = actuator
            break

    # Get the humidity sensor and actuator in the living room
    humidity_sensor = None
    humidifier = None
    for sensor in living_room.sensors:
        if isinstance(sensor, HumiditySensor):
            humidity_sensor = sensor
            break

    for actuator in living_room.actuators:
        if isinstance(actuator, Humidifier):
            humidifier = actuator
            break

    # Set temperature to 17 degrees
    if heater and temperature_sensor:
        heater.set_target_temperature(17)
        temperature_sensor.turn_on()
        current_temperature = temperature_sensor.get_reading()
        if current_temperature is not None:
            heater.adjust_temperature(current_temperature)

    # Ensure humidity is normal
    if humidifier and humidity_sensor:
        humidity_sensor.turn_on()
        current_humidity = humidity_sensor.get_reading()
        if current_humidity is not None:
            if current_humidity < 30:  # Assuming normal humidity is between 30% and 50%
                humidifier.increase_humidity()
            elif current_humidity > 50:
                humidifier.decrease_humidity()

    # Turn off the lights
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

if __name__ == "__main__":
    main()