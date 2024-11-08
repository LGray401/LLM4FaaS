# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home system. This main function will demonstrate basic control operations such as turning sensors and actuators on/off, getting readings from sensors, and adjusting actuators based on sensor readings.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, Heater, AC, Light
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Example: Get and print information about a specific room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room.print_info()

    # Example: Turn on all lights in the LivingRoom
    lights = get_all_actuators(home, "Light")
    for light in lights:
        if light.room_name == "LivingRoom":
            light.turn_on()
            light.set_brightness_level("high")

    # Example: Get temperature readings from all IndoorTemperature sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in temp_sensors:
        sensor.turn_on()
        print(f"{sensor.id} reading: {sensor.get_reading()}°C")

    # Example: Adjust heaters and ACs based on temperature readings
    for sensor in temp_sensors:
        current_temp = sensor.get_reading()
        room_name = sensor.room_name
        
        # Get heaters and ACs in the same room
        heaters = get_all_actuators(home, "Heater")
        acs = get_all_actuators(home, "AC")
        
        for heater in heaters:
            if heater.room_name == room_name:
                if current_temp < TEMP_LOW:
                    heater.turn_on()
                    heater.set_target_temperature(TEMP_LOW + 1)  # Set to a slightly higher temp than TEMP_LOW
                else:
                    heater.turn_off()
                
        for ac in acs:
            if ac.room_name == room_name:
                if current_temp > TEMP_HIGH:
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_HIGH - 1)  # Set to a slightly lower temp than TEMP_HIGH
                else:
                    ac.turn_off()

    # Example: Turn off all sensors after operations
    for sensor in temp_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()