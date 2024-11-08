# Based on the functional description and the provided source code, we'll create a `function.py` file that controls the smart home environment. This file will perform actions based on the descriptions for temperature, humidity, and light intensity.
# 
# Here's how the `function.py` file might look:
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def main():
    # Get the home plan
    home = home_plan()

    # Get all indoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    
    # Get all light intensity sensors
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get actuators
    ac_units = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Check temperature
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp is not None:
            if current_temp > TEMP_HIGH:
                print("屋里太热了")
                for ac in ac_units:
                    if ac.room_name == sensor.room_name:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temp)
            elif current_temp < TEMP_LOW:
                print("屋里太冷了")
                for heater in heaters:
                    if heater.room_name == sensor.room_name:
                        heater.set_target_temperature(TEMP_LOW)
                        heater.adjust_temperature(current_temp)
        sensor.turn_off()

    # Check humidity
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity is not None and current_humidity < HUMIDITY_LOW:
            print("屋里有点干")
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
        sensor.turn_off()

    # Check light intensity
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None and current_light_intensity < LIGHT_INTENSITY_LOW:
            print("屋里太暗了")
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    light.set_brightness_level("high")
        sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Temperature Management**: For each indoor temperature sensor, the program checks if the temperature is too high or too low and adjusts the AC or heater in the corresponding room.
# 
# 2. **Humidity Management**: For each humidity sensor, the program checks if the humidity is below the threshold and turns on the humidifier if necessary.
# 
# 3. **Light Management**: For each light intensity sensor, the program checks if the light level is below the threshold and turns on the lights to a high brightness level if necessary.
# 
# This script provides a simple automation logic using the provided sensor and actuator classes. Adjust the logic as needed for specific project requirements or additional functionality.