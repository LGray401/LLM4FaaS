# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function to implement the energy-saving mode for your smart home project. The main function will handle the logic for cooling based on outdoor and indoor temperatures, as well as managing the窗帘 (curtains) based on the sunlight intensity.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_HIGH

def energy_saving_mode(home):
    # Get all indoor and outdoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    
    # Get all windows and curtains actuators
    windows = get_all_actuators(home, "Window")
    curtains = get_all_actuators(home, "Curtain")
    
    # Ensure sensors and actuators are turned on
    for sensor in indoor_temp_sensors + outdoor_temp_sensors + light_intensive_sensors:
        if sensor.get_status() == "off":
            sensor.turn_on()
    
    for actuator in windows + curtains:
        if actuator.get_status() == "off":
            actuator.turn_on()
    
    # Collect readings
    indoor_temps = [sensor.get_reading() for sensor in indoor_temp_sensors if sensor.get_reading() is not None]
    outdoor_temps = [sensor.get_reading() for sensor in outdoor_temp_sensors if sensor.get_reading() is not None]
    light_intensities = [sensor.get_reading() for sensor in light_intensive_sensors if sensor.get_reading() is not None]
    
    # Average the readings
    if indoor_temps:
        average_indoor_temp = sum(indoor_temps) / len(indoor_temps)
    else:
        average_indoor_temp = None
        
    if outdoor_temps:
        average_outdoor_temp = sum(outdoor_temps) / len(outdoor_temps)
    else:
        average_outdoor_temp = None
    
    if light_intensities:
        average_light_intensity = sum(light_intensities) / len(light_intensities)
    else:
        average_light_intensity = None
    
    # Implement energy-saving logic
    if average_indoor_temp is not None and average_outdoor_temp is not None:
        # Cooling 1: If outdoor temp is lower than indoor temp, open windows
        if average_outdoor_temp < average_indoor_temp:
            for window in windows:
                window.turn_on()  # Open windows (assuming turn_on means open for windows)
        else:
            for window in windows:
                window.turn_off()  # Close windows (assuming turn_off means close for windows)
        
        # Cooling 2: If indoor temp is lower than outdoor temp and sunlight is strong, close curtains
        if average_indoor_temp < average_outdoor_temp and average_light_intensity is not None and average_light_intensity > LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                curtain.turn_on()  # Close curtains (assuming turn_on means close for curtains)
        else:
            for curtain in curtains:
                curtain.turn_off()  # Open curtains (assuming turn_off means open for curtains)

if __name__ == "__main__":
    # Initialize home plan
    home = home_plan()
    
    # Activate energy-saving mode
    energy_saving_mode(home)