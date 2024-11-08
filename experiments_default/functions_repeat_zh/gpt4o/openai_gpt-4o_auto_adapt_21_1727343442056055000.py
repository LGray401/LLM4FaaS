# Based on the functional description and the provided source code, I'll create the `function.py` file. This file will contain the main function which will control the smart home system according to the temperature, humidity, and light intensity conditions.
# 
# Here's the `function.py` content:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain, Humidifier
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Get all indoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    # Get all light intensity sensors
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    # Get all AC actuators
    ac_units = get_all_actuators(home, "AC")
    # Get all Curtain actuators
    curtains = get_all_actuators(home, "Curtain")
    # Get all Humidifier actuators
    humidifiers = get_all_actuators(home, "Humidifier")

    # Temperature Control
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        if temp_reading is not None and temp_reading > TEMP_HIGH:
            for ac in ac_units:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temp_reading)
                    ac.turn_off()

    # Humidity Control
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_reading = sensor.get_reading()
        if humidity_reading is not None:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if humidity_reading < HUMIDITY_LOW:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                        humidifier.turn_off()
                    elif humidity_reading > HUMIDITY_HIGH:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()
                        humidifier.turn_off()

    # Light Intensity Control
    for sensor in light_intensity_sensors:
        sensor.turn_on()
        light_intensity_reading = sensor.get_reading()
        if light_intensity_reading is not None and light_intensity_reading > LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    curtain.turn_on()
                    curtain.turn_off()

    # Turn off all sensors after readings
    for sensor in indoor_temp_sensors + humidity_sensors + light_intensity_sensors:
        sensor.turn_off()

if __name__ == "__main__":
    main()