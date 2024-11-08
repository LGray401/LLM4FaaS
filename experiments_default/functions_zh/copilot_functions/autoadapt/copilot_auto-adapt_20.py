# Based on the functional description and the provided source code, you need to create a `function.py` file that contains a main function to control the smart home system. The main function should be able to read sensor data and control actuators accordingly. Here is a basic structure of the `function.py` file:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Light, Humidifier
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Get the home plan
    home = home_plan()

    # Get all sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")
    lights = get_all_actuators(home, "Light")
    humidifiers = get_all_actuators(home, "Humidifier")

    # Iterate over all rooms and control the actuators based on the sensor readings
    for temperature_sensor, humidity_sensor, light_sensor, ac, heater, light, humidifier in zip(temperature_sensors, humidity_sensors, light_sensors, acs, heaters, lights, humidifiers):
        # Get sensor readings
        temperature = temperature_sensor.get_reading()
        humidity = humidity_sensor.get_reading()
        light_intensity = light_sensor.get_reading()

        # Control AC and Heater based on temperature
        if temperature > TEMP_HIGH:
            ac.turn_on()
            heater.turn_off()
        elif temperature < TEMP_LOW:
            ac.turn_off()
            heater.turn_on()

        # Control Humidifier based on humidity
        if humidity > HUMIDITY_HIGH:
            humidifier.decrease_humidity()
        elif humidity < HUMIDITY_LOW:
            humidifier.increase_humidity()

        # Control Light based on light intensity
        if light_intensity > LIGHT_INTENSITY_HIGH:
            light.turn_off()
        elif light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()

if __name__ == "__main__":
    main()
# ```
#
# This `function.py` file should be placed in the 'functions' folder as per your project structure. The main function reads the sensor data for temperature, humidity, and light intensity. It then controls the AC, heater, light, and humidifier based on the sensor readings. The thresholds for controlling the actuators are defined in the `config.py` file.