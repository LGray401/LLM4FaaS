# Based on your functional description and provided source code, here's a `function.py` file that will be located in the `functions` folder. This script will utilize the functionalities provided in the other modules to implement the specified behaviors.

# function.py
import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Adjust temperature based on sensor reading
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp is not None and current_temp > TEMP_HIGH:
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)

    # Adjust humidity - Assume it's always normal as per the functional description
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        sensor.turn_on()
        sensor.get_reading()
        # No action needed since it's normal

    # Adjust light intensity based on sensor reading
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    curtains = get_all_actuators(home, "Curtain")

    for sensor in light_intensity_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None and current_light_intensity > LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    curtain.turn_on()

if __name__ == "__main__":
    main()