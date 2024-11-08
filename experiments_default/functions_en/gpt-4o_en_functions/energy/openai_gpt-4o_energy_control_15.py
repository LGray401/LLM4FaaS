# Sure! Based on the provided functional description and the source code files for your smart home project, here is the `function.py` file. This file will be located in the `functions` folder and will include the main function.
# 
# ### functions/function.py

import time
from home.home_plan import home_plan, print_home_plan, get_room, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home with its rooms, sensors, and actuators
    home = home_plan()
    print_home_plan(home)

    # Example of getting a specific room and its components
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room.print_info()

    # Example of getting specific sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    lights = get_all_actuators(home, "Light")

    # Example of using sensors and actuators
    if indoor_temp_sensors:
        for sensor in indoor_temp_sensors:
            sensor.turn_on()
            current_temp = sensor.get_reading()
            if current_temp is not None:
                print(f"{sensor.id} current temperature: {current_temp}°C")

    if lights:
        for light in lights:
            light.turn_on()
            light.set_brightness_level("high")

    # Simulate a daily routine for the CleaningRobot
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    if cleaning_robots:
        for robot in cleaning_robots:
            robot.turn_on()
            robot.daily_routine()

    # Example of adjusting temperature based on current readings
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")
    if indoor_temp_sensors and (heaters or ac_units):
        for sensor in indoor_temp_sensors:
            current_temp = sensor.get_reading()
            if current_temp is not None:
                for heater in heaters:
                    heater.set_target_temperature(TEMP_LOW)
                    heater.adjust_temperature(current_temp)
                for ac in ac_units:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)

    # Example of managing humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    if humidity_sensors:
        for sensor in humidity_sensors:
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                print(f"{sensor.id} current humidity: {current_humidity}%")
                for humidifier in humidifiers:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

if __name__ == "__main__":
    main()