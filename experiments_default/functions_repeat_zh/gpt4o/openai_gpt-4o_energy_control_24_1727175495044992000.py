# Sure, based on the provided functional description and the source code, I will create a `function.py` file in the `functions` folder. This file will contain the main function that implements the described energy-saving modes.
# 
# Here's the implementation for `function.py`:

from home_plan import home_plan, get_all_sensors, get_all_actuators
from sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from actuator import Window, Curtain

def energy_saving_mode():
    # Initialize the home plan
    home = home_plan()
    
    # Get all indoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    
    # Get all outdoor temperature sensors
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    
    # Get all light intensive sensors
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    
    # Get all windows
    windows = get_all_actuators(home, "Window")
    
    # Get all curtains
    curtains = get_all_actuators(home, "Curtain")
    
    # Collect readings from sensors
    indoor_temp_readings = {sensor.room_name: sensor.get_reading() for sensor in indoor_temp_sensors}
    outdoor_temp_readings = {sensor.room_name: sensor.get_reading() for sensor in outdoor_temp_sensors}
    light_intensity_readings = {sensor.room_name: sensor.get_reading() for sensor in light_intensive_sensors}
    
    # Apply energy saving mode
    for room_name, indoor_temp in indoor_temp_readings.items():
        outdoor_temp = outdoor_temp_readings.get(room_name)
        light_intensity = light_intensity_readings.get(room_name)
        
        if outdoor_temp is not None:
            if outdoor_temp < indoor_temp:
                # Condition for opening the window
                for window in windows:
                    if window.room_name == room_name:
                        window.turn_on()
                        print(f"Opened window in {room_name}")
                        break
        
        if light_intensity is not None:
            if indoor_temp < outdoor_temp and light_intensity > 900:
                # Condition for closing the curtain
                for curtain in curtains:
                    if curtain.room_name == room_name:
                        curtain.turn_on()
                        print(f"Closed curtain in {room_name}")
                        break

if __name__ == "__main__":
    energy_saving_mode()