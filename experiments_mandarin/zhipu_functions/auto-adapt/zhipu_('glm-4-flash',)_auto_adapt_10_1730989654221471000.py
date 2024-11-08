# Based on the provided functional description and source code, I will create a `function.py` file that will contain the main function to simulate the home automation system based on the given conditions.
# 
# The `function.py` will utilize the classes from the provided source code to control the actuators based on the sensor readings.

# function.py
import time
from home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators

def main():
    # Get the home plan and initialize the sensors and actuators
    home = home_plan()

    # Define the target conditions
    target_temperature = 25
    target_humidity = 50
    target_light_intensity = 900

    # Main loop
    while True:
        # Get all sensors and actuator readings
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        humidity_sensors = get_all_sensors(home, "Humidity")
        light_intensity_sensors = get_all_sensors(home, "LightIntensive")

        # Check the conditions and adjust the actuators
        for sensor in indoor_temp_sensors:
            current_temp = sensor.get_reading()
            if current_temp < target_temperature:
                room = get_room(home, sensor.room_name)
                heater = get_room_actuators(room, "Heater")
                heater.adjust_temperature(current_temp)

        for sensor in humidity_sensors:
            current_humidity = sensor.get_reading()
            if current_humidity < target_humidity:
                room = get_room(home, sensor.room_name)
                humidifier = get_room_actuators(room, "Humidifier")
                humidifier.increase_humidity()
            elif current_humidity > target_humidity:
                room = get_room(home, sensor.room_name)
                humidifier = get_room_actuators(room, "Humidifier")
                humidifier.decrease_humidity()

        for sensor in light_intensity_sensors:
            current_light_intensity = sensor.get_reading()
            if current_light_intensity < target_light_intensity:
                room = get_room(home, sensor.room_name)
                light = get_room_actuators(room, "Light")
                light.set_brightness_level("high")

        # Sleep for a while before checking again
        time.sleep(60)

if __name__ == "__main__":
    main()