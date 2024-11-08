# Sure! Based on your functional description, here's a `function.py` file that manages the smart home system to automatically control the air conditioner and the curtain based on the given temperature and light intensity thresholds.

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Get all indoor temperature sensors and air conditioners
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    air_conditioners = get_all_actuators(home, "AC")

    # Get all light intensity sensors and curtains
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    curtains = get_all_actuators(home, "Curtain")

    # Check temperature and control AC
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temperature = sensor.get_reading()
        if temperature and temperature > TEMP_HIGH:
            for ac in air_conditioners:
                if ac.room_name == sensor.room_name:
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_HIGH)

    # Check light intensity and control curtains
    for sensor in light_intensity_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity and light_intensity > LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    curtain.turn_on()

if __name__ == "__main__":
    main()