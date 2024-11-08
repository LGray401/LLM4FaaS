# To create the `function.py` file, which will contain the main logic to control the smart home environment based on the provided functional description, we can follow these steps:
# 
# 1. **Import Required Modules and Classes**: Import the necessary classes and functions from the `home` module.
# 2. **Initialize the Home Plan**: Create an instance of the home plan to access the rooms and their sensors/actuators.
# 3. **Control Logic for Temperature, Humidity, and Light Intensity**: Implement the logic to maintain temperature, humidity, and light intensity as specified.
# 
# Here is the `function.py` file:

# function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW
import time

def main():
    # Initialize home plan
    home = home_plan()
    
    # Constants
    TARGET_TEMPERATURE = 26  # Celsius
    TARGET_HUMIDITY = 60  # Percentage
    WORKING_LIGHT = "high"
    RELAXING_LIGHT = "medium"
    RESTING_LIGHT = "off"
    
    # Get all sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    
    # Turn on all sensors
    for sensor in indoor_temp_sensors + humidity_sensors + light_intensive_sensors:
        sensor.turn_on()
    
    # Turn on all actuators
    for actuator in heaters + acs + humidifiers + lights:
        actuator.turn_on()
    
    # Set target temperature for heaters and ACs
    for heater in heaters:
        heater.set_target_temperature(TARGET_TEMPERATURE)
    for ac in acs:
        ac.set_target_temperature(TARGET_TEMPERATURE)
    
    while True:
        # Control Temperature
        for sensor in indoor_temp_sensors:
            current_temp = sensor.get_reading()
            if current_temp is not None:
                for heater in heaters:
                    heater.adjust_temperature(current_temp)
                for ac in acs:
                    ac.adjust_temperature(current_temp)
        
        # Control Humidity
        for sensor in humidity_sensors:
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                for humidifier in humidifiers:
                    if current_humidity < TARGET_HUMIDITY:
                        humidifier.increase_humidity()
                    elif current_humidity > TARGET_HUMIDITY:
                        humidifier.decrease_humidity()
        
        # Control Light Intensity
        # Assuming a function to get current activity: get_current_activity()
        current_activity = get_current_activity()
        for light in lights:
            if current_activity == "working":
                light.set_brightness_level(WORKING_LIGHT)
            elif current_activity == "relaxing":
                light.set_brightness_level(RELAXING_LIGHT)
            elif current_activity == "resting":
                light.turn_off()
        
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

def get_current_activity():
    # Mock function to get the current activity of the user
    # This should be replaced with actual implementation, e.g., reading from a schedule or user input
    activities = ["working", "relaxing", "resting"]
    return activities[int(time.time()) % len(activities)]

if __name__ == "__main__":
    main()