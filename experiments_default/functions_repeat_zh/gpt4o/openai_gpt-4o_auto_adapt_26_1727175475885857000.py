# Based on the provided functional descriptions and source code, here is the `function.py` file that will maintain the temperature at 26°C, humidity at 60%, and control light intensity based on the user's activities. This file will act as the main controller for managing the smart home environment.
# 
# ### functions/function.py

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light

# Function to maintain temperature at 26°C
def maintain_temperature(home):
    target_temp = 26
    sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")

    for sensor in sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp < target_temp:
            for heater in heaters:
                heater.set_target_temperature(target_temp)
                heater.adjust_temperature(current_temp)
        elif current_temp > target_temp:
            for ac in ac_units:
                ac.set_target_temperature(target_temp)
                ac.adjust_temperature(current_temp)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
        sensor.turn_off()

# Function to maintain humidity at 60%
def maintain_humidity(home):
    target_humidity = 60
    sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity < target_humidity:
            for humidifier in humidifiers:
                humidifier.turn_on()
                humidifier.increase_humidity()
        elif current_humidity > target_humidity:
            for humidifier in humidifiers:
                humidifier.turn_on()
                humidifier.decrease_humidity()
        sensor.turn_off()

# Function to control light intensity based on activity
def control_lighting(home, activity):
    lights = get_all_actuators(home, "Light")

    for light in lights:
        light.turn_on()
        if activity == "work":
            light.set_brightness_level("high")
        elif activity == "relax":
            light.set_brightness_level("low")
        elif activity == "rest":
            light.turn_off()
        else:
            print(f"Unknown activity: {activity}")

def main():
    home = home_plan()
    
    # Maintain temperature and humidity
    maintain_temperature(home)
    maintain_humidity(home)
    
    # Example: Control lighting based on different activities
    activities = ["work", "relax", "rest"]
    for activity in activities:
        print(f"Setting lights for activity: {activity}")
        control_lighting(home, activity)
        time.sleep(2)  # Wait for 2 seconds before changing to the next activity

if __name__ == "__main__":
    main()