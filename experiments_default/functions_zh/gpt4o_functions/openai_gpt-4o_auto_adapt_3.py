# Based on the provided functional description and source code, I'll create a `function.py` file that matches your requirements. The `function.py` will be located in the 'functions' folder and will contain a main function. This function will initialize the smart home setup, get sensor readings, and print the values according to the functional description.
# 
# Here is the code for `function.py`:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Heater, Humidifier, AC
from home.home_plan import home_plan, get_all_sensors, get_all_actuators

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all the relevant sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Turn on all the sensors to get readings
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
    for sensor in humidity_sensors:
        sensor.turn_on()
    for sensor in light_sensors:
        sensor.turn_on()

    # Get readings from the sensors
    temperature_readings = [sensor.get_reading() for sensor in indoor_temp_sensors]
    humidity_readings = [sensor.get_reading() for sensor in humidity_sensors]
    light_readings = [sensor.get_reading() for sensor in light_sensors]

    # Print readings according to the functional description
    if temperature_readings:
        avg_temp = sum(temperature_readings) / len(temperature_readings)
        print(f"Temperature: 温度{avg_temp}度")
    else:
        print("Temperature: No readings available")

    if humidity_readings:
        avg_humidity = sum(humidity_readings) / len(humidity_readings)
        print(f"Humidity: 湿度{avg_humidity}")
    else:
        print("Humidity: No readings available")

    if light_readings:
        avg_light = sum(light_readings) / len(light_readings)
        print(f"Light Intensity: 光适中")
    else:
        print("Light Intensity: No readings available")

if __name__ == "__main__":
    main()