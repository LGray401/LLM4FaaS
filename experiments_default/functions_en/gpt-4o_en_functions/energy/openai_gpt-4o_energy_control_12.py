# Here's the `function.py` file based on your provided functional description and existing source code. This script will start the energy-saving mode and automatically decide whether to enable the air conditioner based on the outdoor temperature and humidity.

# function.py

from home.sensor import OutdoorTemperatureSensor, HumiditySensor
from home.actuator import AC
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all outdoor temperature sensors and humidity sensors
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get the AC actuators
    ac_units = get_all_actuators(home, "AC")

    # Check the readings from the outdoor sensors
    for temp_sensor in outdoor_temp_sensors:
        temp_sensor.turn_on()
        outdoor_temp = temp_sensor.get_reading()
        temp_sensor.turn_off()

        for humidity_sensor in humidity_sensors:
            humidity_sensor.turn_on()
            outdoor_humidity = humidity_sensor.get_reading()
            humidity_sensor.turn_off()

            # Decide whether to turn on the AC based on the temperature and humidity
            for ac in ac_units:
                ac.turn_on()
                if outdoor_temp > TEMP_HIGH or outdoor_humidity > HUMIDITY_HIGH:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(outdoor_temp)
                else:
                    ac.turn_off()

if __name__ == "__main__":
    main()