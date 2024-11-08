# Great! Based on your functional description and the provided source code, here's the `function.py` file that includes the main function. The main function will utilize the sensors and actuators to help manage energy consumption in the smart home.
# 
# ### functions/function.py

import time
from home.home_plan import home_plan, print_home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def manage_energy(home):
    # Manage temperature
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    
    for sensor in indoor_temperature_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.adjust_temperature(current_temp)
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.adjust_temperature(current_temp)

    # Manage humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

    # Manage light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity:
            for light in lights:
                if light.room_name == sensor.room_name:
                    if current_light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                        light.turn_off()

def main():
    home = home_plan()
    print_home_plan(home)
    while True:
        manage_energy(home)
        time.sleep(2)  # Time interval between each energy management cycle

if __name__ == "__main__":
    main()