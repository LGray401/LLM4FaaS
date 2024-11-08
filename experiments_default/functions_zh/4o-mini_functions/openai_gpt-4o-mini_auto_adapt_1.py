# Based on your functional description and the provided source code for your smart home project, I will create a `function.py` file that implements the required features. This file will contain a main function that adjusts the temperature to 26°C, humidity to 40%, and sets the light intensity to medium.
# 
# Here's the `function.py` file:

# function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.actuator import AC, Heater, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Getting the home plan
    home = home_plan()
    
    # Define target values
    target_temperature = 26
    target_humidity = 40
    light_intensity_level = "medium"

    # Find sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_actuators = get_all_actuators(home, "Light")

    # Adjust Temperature
    for sensor in temperature_sensors:
        sensor.turn_on()
        current_temperature = sensor.get_reading()
        
        if current_temperature is not None:
            # Determine which actuator to use for heating or cooling
            if current_temperature < target_temperature and current_temperature < TEMP_LOW:
                # Use Heater
                heater = Heater(sensor.room_name)
                heater.set_target_temperature(target_temperature)
                heater.adjust_temperature(current_temperature)
            elif current_temperature > target_temperature and current_temperature > TEMP_HIGH:
                # Use AC
                ac = AC(sensor.room_name)
                ac.set_target_temperature(target_temperature)
                ac.adjust_temperature(current_temperature)

    # Adjust Humidity
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        
        if current_humidity is not None:
            humidifier = Humidifier(sensor.room_name)
            if current_humidity < target_humidity and current_humidity < HUMIDITY_LOW:
                humidifier.increase_humidity()
            elif current_humidity > target_humidity and current_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()

    # Adjust Light Intensity
    for light in light_actuators:
        light.turn_on()
        light.set_brightness_level(light_intensity_level)

if __name__ == "__main__":
    main()