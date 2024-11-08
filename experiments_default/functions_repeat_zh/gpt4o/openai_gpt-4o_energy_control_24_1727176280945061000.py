# Based on the given functional description and source code files, here is the `function.py` file that will implement the energy-saving mode (节能模式) functionalities described:
# 
# 1. If the outdoor temperature is lower than the indoor temperature, open the window.
# 2. If the indoor temperature is lower than the outdoor temperature and the sunlight intensity is high, close the curtain.
# 
# The code assumes that the necessary imports and logging configurations are already handled in the provided files.
# 
# ### `function.py`

from home.home_plan import home_plan, get_all_sensors, get_all_actuators, print_home_plan
from home.config import TEMP_CHANGE_DURATION_WINDOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
import time

def energy_saving_mode(home):
    # Get all relevant sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    light_sensors = get_all_sensors(home, "LightIntensive")
    windows = get_all_actuators(home, "Window")
    curtains = get_all_actuators(home, "Curtain")

    # Ensure all relevant sensors are turned on to get readings
    for sensor in indoor_temp_sensors + outdoor_temp_sensors + light_sensors:
        sensor.turn_on()

    # Mapping room names to sensors and actuators for easy access
    indoor_temp_map = {sensor.room_name: sensor for sensor in indoor_temp_sensors}
    outdoor_temp_map = {sensor.room_name: sensor for sensor in outdoor_temp_sensors}
    light_sensor_map = {sensor.room_name: sensor for sensor in light_sensors}
    window_map = {actuator.room_name: actuator for actuator in windows}
    curtain_map = {actuator.room_name: actuator for actuator in curtains}

    # Implementing the energy-saving logic
    for room_name in indoor_temp_map:
        indoor_temp = indoor_temp_map[room_name].get_reading()
        outdoor_temp = outdoor_temp_map[room_name].get_reading() if room_name in outdoor_temp_map else None
        light_intensity = light_sensor_map[room_name].get_reading() if room_name in light_sensor_map else None
        
        # 降温1: 室外温度低于室内温度，开窗
        if outdoor_temp is not None and indoor_temp is not None and outdoor_temp < indoor_temp:
            if room_name in window_map:
                window_map[room_name].turn_on()
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                
        # 降温2: 室内温度低于室外温度，日照强烈，拉帘
        if indoor_temp is not None and outdoor_temp is not None and indoor_temp < outdoor_temp:
            if light_intensity is not None and light_intensity > LIGHT_INTENSITY_HIGH:
                if room_name in curtain_map:
                    curtain_map[room_name].turn_on()

if __name__ == "__main__":
    home = home_plan()
    print_home_plan(home)
    energy_saving_mode(home)