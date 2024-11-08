# Sure! I can help you with that. I will create the 'function.py' file in the 'functions' folder based on the provided functional description and source code. Here's the 'function.py' file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Get all sensors and actuators
    home = home_plan()
    all_sensors = get_all_sensors(home)
    all_actuators = get_all_actuators(home)

    # Check temperature
    for sensor in all_sensors:
        if sensor.sensor_type == "IndoorTemperature":
            reading = sensor.get_reading()
            if reading is not None:
                if reading < TEMP_LOW:
                    # Adjust temperature with heaters or ACs
                    for actuator in all_actuators:
                        if actuator.actuator_type in ["Heater", "AC"]:
                            actuator.adjust_temperature(reading)
                elif reading > TEMP_HIGH:
                    # Adjust temperature with heaters or ACs
                    for actuator in all_actuators:
                        if actuator.actuator_type in ["Heater", "AC"]:
                            actuator.adjust_temperature(reading)

    # Check humidity
    for sensor in all_sensors:
        if sensor.sensor_type == "Humidity":
            reading = sensor.get_reading()
            if reading is not None:
                if reading < HUMIDITY_LOW:
                    # Increase humidity with humidifiers
                    for actuator in all_actuators:
                        if actuator.actuator_type == "Humidifier":
                            actuator.increase_humidity()
                elif reading > HUMIDITY_HIGH:
                    # Decrease humidity with dehumidifiers
                    for actuator in all_actuators:
                        if actuator.actuator_type == "Humidifier":
                            actuator.decrease_humidity()

    # Check light intensity
    for sensor in all_sensors:
        if sensor.sensor_type == "LightIntensive":
            reading = sensor.get_reading()
            if reading is not None:
                if reading < LIGHT_INTENSITY_LOW:
                    # Turn on lights
                    for actuator in all_actuators:
                        if actuator.actuator_type == "Light":
                            actuator.turn_on()
                elif reading > LIGHT_INTENSITY_HIGH:
                    # Turn off lights
                    for actuator in all_actuators:
                        if actuator.actuator_type == "Light":
                            actuator.turn_off()

if __name__ == "__main__":
    main()