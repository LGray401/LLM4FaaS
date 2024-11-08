# Based on your functional description and provided source code, I'll create a `function.py` file to monitor and control the temperature, humidity, and light intensity in your smart home.
# 
# Here's how `function.py` might look:
# 
# ### `function.py`

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH

def main():
    # Create home plan
    home = home_plan()
    
    # Get all relevant sensors and actuators in the home
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    light_sensors = get_all_sensors(home, "LightIntensive")

    ac_units = get_all_actuators(home, "AC")
    curtains = get_all_actuators(home, "Curtain")
    
    # Monitor and control temperature
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        if temp_reading is not None and temp_reading > TEMP_HIGH:
            for ac in ac_units:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temp_reading)
    
    # Monitor and control light intensity
    for sensor in light_sensors:
        sensor.turn_on()
        light_reading = sensor.get_reading()
        if light_reading is not None and light_reading > LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    curtain.turn_on()

if __name__ == "__main__":
    main()