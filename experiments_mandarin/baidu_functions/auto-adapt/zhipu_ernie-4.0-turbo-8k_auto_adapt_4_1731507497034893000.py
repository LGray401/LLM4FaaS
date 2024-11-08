# Based on your provided functional description and source code, I will create a `function.py` file that contains the main function to control and monitor the smart home environment. This main function will initialize the rooms, turn on the sensors, get readings, and adjust the actuators based on predefined thresholds.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Turn on all sensors
    for room in home:
        for sensor in room.sensors:
            sensor.turn_on()
    
    # Get readings from all sensors and adjust actuators accordingly
    adjust_temperature_actuators(home)
    adjust_humidity_actuators(home)
    adjust_light_actuators(home)
    
    # Example: Print the home plan (optional)
    for room in home:
        room.print_info()

def adjust_temperature_actuators(home):
    # Get all temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    
    # Get all heaters and ACs
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    
    for sensor in indoor_temp_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            room_name = sensor.room_name
            # Adjust heaters
            for heater in heaters:
                if heater.room_name == room_name:
                    if reading < TEMP_LOW:
                        heater.turn_on()
                        heater.set_target_temperature(TEMP_LOW)
                    else:
                        heater.turn_off()
            # Adjust ACs
            for ac in acs:
                if ac.room_name == room_name:
                    if reading > TEMP_HIGH:
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_HIGH)
                    else:
                        ac.turn_off()

def adjust_humidity_actuators(home):
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    
    # Get all humidifiers (assuming they are the only humidity actuators)
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            room_name = sensor.room_name
            # Adjust humidifiers
            for humidifier in humidifiers:
                if humidifier.room_name == room_name:
                    if reading < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif reading > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

def adjust_light_actuators(home):
    # Get all light intensity sensors
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    # Get all lights
    lights = get_all_actuators(home, "Light")
    
    for sensor in light_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            room_name = sensor.room_name
            # Adjust lights
            for light in lights:
                if light.room_name == room_name:
                    if reading < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    else:
                        light.turn_off()

if __name__ == "__main__":
    main()