# Given the functional description and the source code for your smart home project, I will create a `function.py` file that contains the main function. This main function will demonstrate basic interactions between sensors and actuators in your smart home system. 
# 
# Here's the `function.py`:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()
    # print_home_plan(home)

    # Example usage: Get sensors and actuators in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_sensors = living_room.sensors
        living_room_actuators = living_room.actuators

        # Turn on all sensors and actuators in the living room
        for sensor in living_room_sensors:
            sensor.turn_on()

        for actuator in living_room_actuators:
            actuator.turn_on()

        # Get readings from sensors and adjust actuators accordingly
        for sensor in living_room_sensors:
            reading = sensor.get_reading()
            if isinstance(reading, (int, float)):
                if sensor.sensor_type == "IndoorTemperature":
                    adjust_temperature_actuators(reading, living_room_actuators)
                elif sensor.sensor_type == "Humidity":
                    adjust_humidity_actuators(reading, living_room_actuators)
                elif sensor.sensor_type == "LightIntensive":
                    adjust_light_actuators(reading, living_room_actuators)

        # Turn off all sensors and actuators in the living room
        for sensor in living_room_sensors:
            sensor.turn_off()

        for actuator in living_room_actuators:
            actuator.turn_off()

def adjust_temperature_actuators(current_temp, actuators):
    for actuator in actuators:
        if actuator.actuator_type == "Heater":
            actuator.set_target_temperature(TEMP_LOW)
            actuator.adjust_temperature(current_temp)
        elif actuator.actuator_type == "AC":
            actuator.set_target_temperature(TEMP_HIGH)
            actuator.adjust_temperature(current_temp)

def adjust_humidity_actuators(current_humidity, actuators):
    for actuator in actuators:
        if actuator.actuator_type == "Humidifier":
            if current_humidity < HUMIDITY_LOW:
                actuator.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                actuator.decrease_humidity()

def adjust_light_actuators(current_light_intensity, actuators):
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                actuator.set_brightness_level("high")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                actuator.set_brightness_level("low")

if __name__ == "__main__":
    main()