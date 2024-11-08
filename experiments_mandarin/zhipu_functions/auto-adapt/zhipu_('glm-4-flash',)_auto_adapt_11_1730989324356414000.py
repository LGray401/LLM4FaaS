# Based on your functional description and the provided source code, I will create a `function.py` file that defines a `main` function that integrates the sensor and actuator classes to automate the smart home system based on the environmental conditions you've specified.

# function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH

def main():
    # Load the home plan
    home = home_plan()

    # Get all AC actuators in the home
    acs = [actuator for room in home for actuator in room.actuators if isinstance(actuator, AC)]

    # Get all sensors for temperature, humidity, and light intensity
    temperature_sensors = [sensor for room in home for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
    humidity_sensors = [sensor for room in home for sensor in room.sensors if isinstance(sensor, HumiditySensor)]
    light_intensity_sensors = [sensor for room in home for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]

    # Monitor and control the home
    while True:
        # Get readings from all sensors
        temperature_readings = [sensor.get_reading() for sensor in temperature_sensors]
        humidity_readings = [sensor.get_reading() for sensor in humidity_sensors]
        light_intensity_readings = [sensor.get_reading() for sensor in light_intensity_sensors]

        # Check conditions and control AC
        for ac in acs:
            # Check temperature
            if any(reading > TEMP_HIGH for reading in temperature_readings):
                ac.turn_on()
            else:
                ac.turn_off()

            # Check humidity
            if any(reading > HUMIDITY_HIGH for reading in humidity_readings):
                ac.turn_on()
            else:
                ac.turn_off()

            # Check light intensity
            if any(reading > LIGHT_INTENSITY_HIGH for reading in light_intensity_readings):
                ac.turn_on()
            else:
                ac.turn_off()

        # Sleep for a while before checking again
        time.sleep(60)

if __name__ == "__main__":
    main()