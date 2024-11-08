# Sure, I'll create a `function.py` file that meets the requirements based on the provided functional description and source code. This file will contain the main function to maintain the indoor temperature, humidity, and light intensity within specified limits.
# 
# Here's the `function.py` file:

# function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    home = home_plan()
    
    # Control indoor temperature
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    ac_units = get_all_actuators(home, "AC")
    
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp is not None and current_temp > TEMP_HIGH:
            for ac in ac_units:
                if ac.room_name == sensor.room_name:
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)
        sensor.turn_off()

    # Control humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity is not None and current_humidity > HUMIDITY_LOW:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.turn_on()
                    humidifier.decrease_humidity()
        sensor.turn_off()

    # Control light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")
    
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None:
            if current_light_intensity < LIGHT_INTENSITY_HIGH:
                for light in lights:
                    if light.room_name == sensor.room_name:
                        light.turn_on()
                        light.set_brightness_level("medium")
            else:
                for curtain in curtains:
                    if curtain.room_name == sensor.room_name:
                        curtain.turn_on()
        sensor.turn_off()

    print("Smart home system has adjusted the environment successfully.")

if __name__ == "__main__":
    main()