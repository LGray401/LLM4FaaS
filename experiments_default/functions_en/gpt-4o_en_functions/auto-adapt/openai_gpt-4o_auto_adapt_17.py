# Based on your functional description and the provided source code, I will create the `function.py` file. This file will primarily contain the main function, which will initialize the home plan, turn on the sensors, get their readings, and control the actuators accordingly.
# 
# Here's the `function.py` file content:

# function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Initialize home plan
    home = home_plan()
    
    # Get all sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    # Turn on all sensors and get their readings
    temp_readings = []
    humidity_readings = []
    light_readings = []

    for sensor in temperature_sensors:
        sensor.turn_on()
        temp_readings.append(sensor.get_reading())

    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_readings.append(sensor.get_reading())

    for sensor in light_sensors:
        sensor.turn_on()
        light_readings.append(sensor.get_reading())

    # Control actuators based on sensor readings
    # Control Temperature
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    for temp in temp_readings:
        if temp < TEMP_LOW:
            for heater in heaters:
                heater.set_target_temperature(TEMP_HIGH)
                heater.adjust_temperature(temp)
        elif temp > TEMP_HIGH:
            for ac in acs:
                ac.set_target_temperature(TEMP_LOW)
                ac.adjust_temperature(temp)

    # Control Humidity
    humidifiers = get_all_actuators(home, "Humidifier")
    for humidity in humidity_readings:
        if humidity < HUMIDITY_LOW:
            for humidifier in humidifiers:
                humidifier.increase_humidity()
        elif humidity > HUMIDITY_HIGH:
            for humidifier in humidifiers:
                humidifier.decrease_humidity()

    # Control Light Intensity
    lights = get_all_actuators(home, "Light")
    for light_intensity in light_readings:
        if light_intensity < LIGHT_INTENSITY_LOW:
            for light in lights:
                light.turn_on()
                light.set_brightness_level("high")
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            for light in lights:
                light.turn_off()

if __name__ == "__main__":
    main()