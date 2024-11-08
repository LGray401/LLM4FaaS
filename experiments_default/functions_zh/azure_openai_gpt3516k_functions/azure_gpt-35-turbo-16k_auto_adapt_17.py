# Sure, here is the code for the 'function.py' file:

from home.logger_config import logger
from home.home_plan import home_plan, get_room_sensors, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Get the home plan
    home = home_plan()

    # Get all the temperature sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temperature_sensors = get_all_sensors(home, "OutdoorTemperature")
    
    # Get all the humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get all the light intensity sensors
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    # Check and control temperature
    for temperature_sensor in temperature_sensors:
        reading = temperature_sensor.get_reading()
        if reading is not None:
            if reading < TEMP_LOW:
                for actuator in temperature_sensor.room.actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.turn_on()
                        break
            elif reading > TEMP_HIGH:
                for actuator in temperature_sensor.room.actuators:
                    if actuator.actuator_type == "AC":
                        actuator.turn_on()
                        break

    # Check and control humidity
    for humidity_sensor in humidity_sensors:
        reading = humidity_sensor.get_reading()
        if reading is not None:
            if reading < HUMIDITY_LOW:
                for actuator in humidity_sensor.room.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.increase_humidity()
                        break
            elif reading > HUMIDITY_HIGH:
                for actuator in humidity_sensor.room.actuators:
                    if actuator.actuator_type == "Humidifier":
                        actuator.decrease_humidity()
                        break

    # Check and control light intensity
    for light_intensity_sensor in light_intensity_sensors:
        reading = light_intensity_sensor.get_reading()
        if reading is not None:
            if reading < LIGHT_INTENSITY_LOW:
                for actuator in light_intensity_sensor.room.actuators:
                    if actuator.actuator_type == "Light":
                        actuator.turn_on()
                        break
            elif reading > LIGHT_INTENSITY_HIGH:
                for actuator in light_intensity_sensor.room.actuators:
                    if actuator.actuator_type == "Light":
                        actuator.turn_off()
                        break

if __name__ == "__main__":
    main()