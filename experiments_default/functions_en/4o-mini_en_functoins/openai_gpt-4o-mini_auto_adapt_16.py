# Based on your functional description and the provided source code for the smart home project, I will create a `function.py` file that will utilize the classes defined in `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`. This file will include a main function that simulates a scenario based on the specified temperature, humidity, and light intensity.
# 
# Here is how the `function.py` file would look:

# function.py

from home.home_plan import home_plan, print_home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def control_home_environment(home):
    # Get all sensors and actuators in the home
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all actuators (Heaters, ACs, and Lights)
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")

    # Assume we have only one sensor of each type for simplicity
    if indoor_temperature_sensors:
        current_temp = indoor_temperature_sensors[0].get_reading() or 27  # Default to 27 if reading fails
        print(f"Current Indoor Temperature: {current_temp}°C")
        
        # Control Heater and AC based on current temperature
        for heater in heaters:
            heater.set_target_temperature(22)  # Example target temperature for heater
            heater.adjust_temperature(current_temp)

        for ac in acs:
            ac.set_target_temperature(24)  # Example target temperature for AC
            ac.adjust_temperature(current_temp)

    if humidity_sensors:
        current_humidity = humidity_sensors[0].get_reading() or 80  # Default to 80 if reading fails
        print(f"Current Humidity: {current_humidity}%")
        
        # Control humidifiers if humidity is below the threshold
        for humidifier in get_all_actuators(home, "Humidifier"):
            if current_humidity < HUMIDITY_LOW:
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()

    if light_sensors:
        current_light = light_sensors[0].get_reading() or 80  # Default to 80 if reading fails
        print(f"Current Light Intensity: {current_light} lux")
        
        # Control lights based on current light intensity
        for light in lights:
            if current_light < LIGHT_INTENSITY_LOW:
                light.turn_on()
            else:
                light.turn_off()

def main():
    home = home_plan()
    print_home_plan(home)
    control_home_environment(home)

if __name__ == "__main__":
    main()