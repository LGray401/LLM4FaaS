# Based on your provided functional description and source code files, I'll create a `function.py` file that will be located in the `functions` folder. The `function.py` will contain a main function that will interact with the sensors and actuators defined in the `home_plan.py`.
# 
# Here is the `function.py`:

# functions/function.py
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def main():
    # Initialize home
    home = home_plan()

    # Define desired conditions
    desired_temp = 20
    desired_humidity = 50
    desired_light_intensity = 15

    # Act on each room based on the desired conditions
    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        for sensor in sensors:
            sensor.turn_on()
            reading = sensor.get_reading()

            # Adjust temperature
            if sensor.sensor_type == "IndoorTemperature":
                adjust_temperature(actuators, reading, desired_temp)

            # Adjust humidity
            if sensor.sensor_type == "Humidity":
                adjust_humidity(actuators, reading, desired_humidity)

            # Adjust light intensity
            if sensor.sensor_type == "LightIntensive":
                adjust_light_intensity(actuators, reading, desired_light_intensity)

    print("Home automation actions have been executed successfully.")


def adjust_temperature(actuators, current_temp, desired_temp):
    for actuator in actuators:
        if isinstance(actuator, Heater):
            actuator.set_target_temperature(desired_temp)
            actuator.adjust_temperature(current_temp)
        elif isinstance(actuator, AC):
            actuator.set_target_temperature(desired_temp)
            actuator.adjust_temperature(current_temp)


def adjust_humidity(actuators, current_humidity, desired_humidity):
    for actuator in actuators:
        if isinstance(actuator, Humidifier):
            if current_humidity < desired_humidity:
                actuator.turn_on()
                actuator.increase_humidity()
            else:
                actuator.turn_off()
                actuator.decrease_humidity()


def adjust_light_intensity(actuators, current_light_intensity, desired_light_intensity):
    for actuator in actuators:
        if isinstance(actuator, Light):
            if current_light_intensity < desired_light_intensity:
                actuator.turn_on()
                actuator.set_brightness_level("high")
            else:
                actuator.turn_off()


if __name__ == "__main__":
    main()