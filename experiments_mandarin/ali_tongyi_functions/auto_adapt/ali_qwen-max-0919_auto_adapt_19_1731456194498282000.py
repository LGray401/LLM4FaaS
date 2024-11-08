# Based on your provided functional description and the source code, I will create a `function.py` file that includes a main function to handle the conditions where the temperature is too high, the humidity is too low, or the light intensity is too high. The main function will check the sensor readings and control the actuators accordingly.
# 
# Here's the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Define the rooms and their sensors/actuators
    rooms = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]

    for room in rooms:
        # Get the sensors and actuators for the current room
        sensors = get_room_sensors(home, room)
        actuators = get_room_actuators(home, room)

        if not sensors or not actuators:
            continue

        # Check and handle temperature
        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                sensor.turn_on()
                temp_reading = sensor.get_reading()
                if temp_reading and temp_reading > TEMP_HIGH:
                    print(f"Temperature in {room} is too high: {temp_reading}°C")
                    for actuator in actuators:
                        if isinstance(actuator, AC):
                            actuator.set_target_temperature(TEMP_HIGH - 1)
                            actuator.adjust_temperature(temp_reading)
                sensor.turn_off()

        # Check and handle humidity
        for sensor in sensors:
            if isinstance(sensor, HumiditySensor):
                sensor.turn_on()
                humidity_reading = sensor.get_reading()
                if humidity_reading and humidity_reading < HUMIDITY_LOW:
                    print(f"Humidity in {room} is too low: {humidity_reading}%")
                    for actuator in actuators:
                        if isinstance(actuator, Humidifier):
                            actuator.increase_humidity()
                sensor.turn_off()

        # Check and handle light intensity
        for sensor in sensors:
            if isinstance(sensor, LightIntensiveSensor):
                sensor.turn_on()
                light_reading = sensor.get_reading()
                if light_reading and light_reading > LIGHT_INTENSITY_HIGH:
                    print(f"Light intensity in {room} is too high: {light_reading} lux")
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.set_brightness_level("low")
                sensor.turn_off()

if __name__ == "__main__":
    main()