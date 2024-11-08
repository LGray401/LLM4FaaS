# Sure! Here is the code for the 'function.py' file based on the functional description and the provided source code:

from home.home_plan import get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Get all temperature sensors
    temperature_sensors = get_all_sensors("IndoorTemperature")

    # Set temperature to 17 degrees
    for sensor in temperature_sensors:
        sensor.turn_on()
        current_temperature = sensor.get_reading()
        if current_temperature < TEMP_LOW:
            actuator = get_actuator(sensor.room_name, "Heater")
            actuator.set_target_temperature(17)
            actuator.adjust_temperature(current_temperature)
        elif current_temperature > TEMP_HIGH:
            actuator = get_actuator(sensor.room_name, "AC")
            actuator.set_target_temperature(17)
            actuator.adjust_temperature(current_temperature)

    # Get all humidity sensors
    humidity_sensors = get_all_sensors("Humidity")

    # Ensure humidity is within normal range
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity < HUMIDITY_LOW or current_humidity > HUMIDITY_HIGH:
            actuator = get_actuator(sensor.room_name, "Humidifier")
            if current_humidity < HUMIDITY_LOW:
                actuator.increase_humidity()
            else:
                actuator.decrease_humidity()

    # Get all light intensity sensors
    light_intensity_sensors = get_all_sensors("LightIntensive")

    # Turn off lights if light intensity is too high
    for sensor in light_intensity_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity > LIGHT_INTENSITY_HIGH:
            actuator = get_actuator(sensor.room_name, "Light")
            actuator.turn_off()

def get_actuator(room_name, actuator_type):
    actuators = get_all_actuators(actuator_type)
    for actuator in actuators:
        if actuator.room_name == room_name:
            return actuator
    return None

if __name__ == "__main__":
    main()