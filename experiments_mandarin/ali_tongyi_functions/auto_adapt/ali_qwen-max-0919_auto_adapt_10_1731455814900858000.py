# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control the smart home system. The main function will read the sensor values and adjust the actuators according to the desired conditions.
# 
# Here's the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Define the desired conditions
    desired_temperature = 25  # Celsius
    desired_humidity = "适中"  # Moderate
    desired_light_intensity = "亮"  # Bright

    # Map the desired humidity and light intensity to their respective ranges
    humidity_ranges = {
        "低": (0, HUMIDITY_LOW),
        "适中": (HUMIDITY_LOW, HUMIDITY_HIGH),
        "高": (HUMIDITY_HIGH, 100)
    }

    light_intensity_ranges = {
        "暗": (0, LIGHT_INTENSITY_HIGH),
        "适中": (LIGHT_INTENSITY_HIGH, 1000),
        "亮": (900, 1000)
    }

    # Get all sensors and actuators
    all_indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    all_humidity_sensors = get_all_sensors(home, "Humidity")
    all_light_intensive_sensors = get_all_sensors(home, "LightIntensive")

    all_heaters = get_all_actuators(home, "Heater")
    all_acs = get_all_actuators(home, "AC")
    all_humidifiers = get_all_actuators(home, "Humidifier")
    all_lights = get_all_actuators(home, "Light")

    # Turn on all sensors
    for sensor in all_indoor_temp_sensors + all_humidity_sensors + all_light_intensive_sensors:
        sensor.turn_on()

    # Read and process the sensor values
    for room in home:
        # Get the sensors and actuators for the current room
        temp_sensors = get_room_sensors(home, room.name, "IndoorTemperature")
        humidity_sensors = get_room_sensors(home, room.name, "Humidity")
        light_sensors = get_room_sensors(home, room.name, "LightIntensive")

        heaters = get_room_actuators(home, room.name, "Heater")
        acs = get_room_actuators(home, room.name, "AC")
        humidifiers = get_room_actuators(home, room.name, "Humidifier")
        lights = get_room_actuators(home, room.name, "Light")

        # Process temperature
        if temp_sensors:
            current_temperature = sum(sensor.get_reading() for sensor in temp_sensors) / len(temp_sensors)
            print(f"Current temperature in {room.name}: {current_temperature}°C")

            for heater in heaters:
                heater.set_target_temperature(desired_temperature)
                heater.adjust_temperature(current_temperature)

            for ac in acs:
                ac.set_target_temperature(desired_temperature)
                ac.adjust_temperature(current_temperature)

        # Process humidity
        if humidity_sensors:
            current_humidity = sum(sensor.get_reading() for sensor in humidity_sensors) / len(humidity_sensors)
            print(f"Current humidity in {room.name}: {current_humidity}%")

            for humidifier in humidifiers:
                if current_humidity < humidity_ranges[desired_humidity][0]:
                    humidifier.increase_humidity()
                elif current_humidity > humidity_ranges[desired_humidity][1]:
                    humidifier.decrease_humidity()

        # Process light intensity
        if light_sensors:
            current_light_intensity = sum(sensor.get_reading() for sensor in light_sensors) / len(light_sensors)
            print(f"Current light intensity in {room.name}: {current_light_intensity} lux")

            for light in lights:
                if current_light_intensity < light_intensity_ranges[desired_light_intensity][0]:
                    light.set_brightness_level("high")
                elif current_light_intensity > light_intensity_ranges[desired_light_intensity][1]:
                    light.set_brightness_level("medium")

    # Turn off all sensors
    for sensor in all_indoor_temp_sensors + all_humidity_sensors + all_light_intensive_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()