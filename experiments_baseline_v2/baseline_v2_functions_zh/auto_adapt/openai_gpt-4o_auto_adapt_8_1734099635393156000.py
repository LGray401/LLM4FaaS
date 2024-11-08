# To create a smart home application based on the provided functional description and the reference code files, we can create a script that adjusts the temperature to 17 degrees Celsius, maintains normal humidity, and ensures there is no light intensity. We will make use of the classes and functionalities provided in the reference code files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`).
# 
# ### Application Code
# 
# Let's create a script named `smart_home.py` that will implement the desired functionality.
# 
# ```python
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, TEMP_CHANGE_DURATION_WINDOW

def adjust_temperature(home, target_temperature):
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        
        for heater in heaters:
            if heater.room_name == sensor.room_name:
                heater.set_target_temperature(target_temperature)
                heater.adjust_temperature(current_temp)
        
        for ac in acs:
            if ac.room_name == sensor.room_name:
                ac.set_target_temperature(target_temperature)
                ac.adjust_temperature(current_temp)
        
        sensor.turn_off()

def maintain_humidity(home):
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        
        for humidifier in humidifiers:
            if humidifier.room_name == sensor.room_name:
                if current_humidity < 40:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
                elif current_humidity > 60:
                    humidifier.turn_on()
                    humidifier.decrease_humidity()
                else:
                    humidifier.turn_off()
        
        sensor.turn_off()

def turn_off_lights(home):
    lights = get_all_actuators(home, "Light")
    
    for light in lights:
        light.turn_off()

def main():
    home = home_plan()
    
    # Adjust temperature to 17 degrees
    adjust_temperature(home, 17)
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
    
    # Maintain normal humidity
    maintain_humidity()

    # Ensure lights are turned off
    turn_off_lights(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Command to Run the Application
# 
# To run this application from a Linux terminal, you can use the following command:
# 
# ```bash
# python smart_home.py
# ```
# 
# ### Explanation
# 
# 1. **Temperature Adjustment**: We iterate through all the indoor temperature sensors, read the current temperature, and adjust the heaters and ACs based on whether the current temperature is below or above the target of 17 degrees Celsius.
# 
# 2. **Maintain Humidity**: We assume "normal" humidity is between 40% and 60%. Humidifiers are turned on to increase or decrease humidity if the current value is outside this range.
# 
# 3. **Turn Off Lights**: All lights in the home are turned off to meet the requirement of "不要光照" (no illumination).
# 
# Please ensure the `home` directory is in your Python path, and the script is executed in a context that allows access to the `home_plan`, `sensor`, and `actuator` modules.