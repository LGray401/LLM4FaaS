# Based on the provided functional description and the existing code in your smart home project, I will create the `function.py` file to implement the energy-saving mode:
# 
# 1. **Cooling 1**: When the outdoor temperature is lower than the indoor temperature, open the window.
# 2. **Cooling 2**: When the indoor temperature is lower than the outdoor temperature and sunlight is intense, close the curtain.
# 
# Here is the `function.py` file:

# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW

def energy_saving_mode():
    home = home_plan()
    
    # Retrieve all indoor and outdoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    
    # Retrieve all windows and curtains
    windows = get_all_actuators(home, "Window")
    curtains = get_all_actuators(home, "Curtain")
    
    # Cooling 1: Open windows if outdoor temperature is lower than indoor temperature
    for indoor_sensor in indoor_temp_sensors:
        indoor_temp = indoor_sensor.get_reading()
        if indoor_temp is None:
            continue
        
        corresponding_outdoor_sensor = next((sensor for sensor in outdoor_temp_sensors if sensor.room_name == indoor_sensor.room_name), None)
        if corresponding_outdoor_sensor:
            outdoor_temp = corresponding_outdoor_sensor.get_reading()
            if outdoor_temp is None:
                continue
            
            if outdoor_temp < indoor_temp:
                for window in windows:
                    if window.room_name == indoor_sensor.room_name:
                        window.turn_on()
                        print(f"Opened {window.id} to cool down {indoor_sensor.room_name}")
    
    # Cooling 2: Close curtains if indoor temperature is lower than outdoor temperature and sunlight is intense
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    
    for indoor_sensor in indoor_temp_sensors:
        indoor_temp = indoor_sensor.get_reading()
        if indoor_temp is None:
            continue
        
        corresponding_outdoor_sensor = next((sensor for sensor in outdoor_temp_sensors if sensor.room_name == indoor_sensor.room_name), None)
        if corresponding_outdoor_sensor:
            outdoor_temp = corresponding_outdoor_sensor.get_reading()
            if outdoor_temp is None:
                continue
            
            if indoor_temp < outdoor_temp:
                for light_sensor in light_intensive_sensors:
                    if light_sensor.room_name == indoor_sensor.room_name:
                        light_intensity = light_sensor.get_reading()
                        if light_intensity is None:
                            continue
                        
                        if light_intensity > 900:  # Assuming 900 as the threshold for intense sunlight
                            for curtain in curtains:
                                if curtain.room_name == indoor_sensor.room_name:
                                    curtain.turn_on()
                                    print(f"Closed {curtain.id} to block sunlight in {light_sensor.room_name}")

if __name__ == "__main__":
    energy_saving_mode()