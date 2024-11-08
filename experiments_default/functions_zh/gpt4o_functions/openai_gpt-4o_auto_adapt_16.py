# Based on your provided functional description and source code, I will create a `function.py` file that reads sensor values, compares them against the provided thresholds, and controls the actuators accordingly.
# 
# Here's the `function.py` file content that you can place in the `functions` folder:

# function.py
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    home = home_plan()

    # Define the target values based on your functional description
    target_temperature = 27
    target_humidity = 80
    target_light_intensity = 80

    # Check each room's sensors and adjust actuators accordingly
    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        for sensor in sensors:
            sensor.turn_on()
            reading = sensor.get_reading()

            if sensor.sensor_type == "IndoorTemperature":
                if reading < target_temperature:
                    for actuator in actuators:
                        if actuator.actuator_type == "Heater":
                            actuator.turn_on()
                            actuator.set_target_temperature(target_temperature)
                            actuator.adjust_temperature(reading)
                elif reading > target_temperature:
                    for actuator in actuators:
                        if actuator.actuator_type == "AC":
                            actuator.turn_on()
                            actuator.set_target_temperature(target_temperature)
                            actuator.adjust_temperature(reading)

            elif sensor.sensor_type == "Humidity":
                if reading < target_humidity:
                    for actuator in actuators:
                        if actuator.actuator_type == "Humidifier":
                            actuator.turn_on()
                            actuator.increase_humidity()
                elif reading > target_humidity:
                    for actuator in actuators:
                        if actuator.actuator_type == "Humidifier":
                            actuator.turn_on()
                            actuator.decrease_humidity()

            elif sensor.sensor_type == "LightIntensive":
                for actuator in actuators:
                    if actuator.actuator_type == "Light":
                        actuator.turn_on()
                        if reading < target_light_intensity:
                            actuator.set_brightness_level("high")
                        else:
                            actuator.set_brightness_level("low")

            sensor.turn_off()

if __name__ == "__main__":
    main()