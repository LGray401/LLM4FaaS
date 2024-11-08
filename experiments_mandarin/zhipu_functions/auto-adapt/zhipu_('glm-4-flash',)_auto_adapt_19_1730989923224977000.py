# Based on the provided functional description and source code, here is the `function.py` file located in the `functions` folder of your project. The file will contain a `main` function that will handle the core logic of your smart home system.

# functions/function.py
import time
from home.sensor import Sensor
from home.actuator import Actuator
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.logger_config import logger

def main():
    # Load home plan
    home = home_plan()

    # Example of getting a room's sensors and actuators
    room_name = "LivingRoom"
    room_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    # Process sensors readings
    for sensor in room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            current_temp = sensor.get_reading()
            if current_temp < TEMP_LOW:
                logger.info(f"Temperature too low in {room_name}: {current_temp}°C")
                # Turn on heater
                for actuator in room_actuators:
                    if isinstance(actuator, Heater):
                        actuator.turn_on()
                        break
        elif isinstance(sensor, HumiditySensor):
            current_humidity = sensor.get_reading()
            if current_humidity < HUMIDITY_LOW:
                logger.info(f"Humidity too low in {room_name}: {current_humidity}%")
                # Turn on humidifier
                for actuator in room_actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.increase_humidity()
                        break
        elif isinstance(sensor, LightIntensiveSensor):
            current_light_intensity = sensor.get_reading()
            if current_light_intensity > LIGHT_INTENSITY_HIGH:
                logger.info(f"Light too bright in {room_name}: {current_light_intensity} lux")
                # Turn off lights
                for actuator in room_actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_off()
                        break

    # Process actuators
    for actuator in room_actuators:
        if isinstance(actuator, CleaningRobot):
            actuator.daily_routine()

    # Sleep for a while before repeating
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()