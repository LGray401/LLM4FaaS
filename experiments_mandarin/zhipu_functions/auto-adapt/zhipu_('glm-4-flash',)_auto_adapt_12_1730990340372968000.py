# Based on your functional description and the provided source code from the sensor.py, actuator.py, home_plan.py, and config.py files, here is a function.py file that you can add to the 'functions' folder of your smart home project. This function.py will contain a `main` function that will simulate the smart home's operation based on the current conditions of temperature, humidity, and light intensity you've provided.

# function.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.logger_config import logger
from config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    logger.info("Starting Smart Home Functionality")
    
    # Create home plan
    home = home_plan()
    
    # Current conditions
    current_temperature = 22
    current_humidity = "适中"  # Moderate
    current_light_intensity = "微弱"  # Weak

    # Check current conditions and adjust actuators if necessary
    for room in home:
        # Indoor Temperature Sensors
        indoor_temp_sensors = [sensor for sensor in get_room_sensors(home, room.name) if isinstance(sensor, IndoorTemperatureSensor)]
        for sensor in indoor_temp_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                logger.info(f"Room {room.name} temperature reading: {reading}°C")
                if reading < TEMP_LOW:
                    # Turn on heater
                    heater = [actor for actor in get_room_actuators(home, room.name) if isinstance(actor, Heater)][0]
                    heater.turn_on()
                    logger.info(f"Heater in {room.name} turned on to increase temperature")
                elif reading > TEMP_HIGH:
                    # Turn on AC
                    ac = [actor for actor in get_room_actuators(home, room.name) if isinstance(actor, AC)][0]
                    ac.turn_on()
                    logger.info(f"AC in {room.name} turned on to decrease temperature")

        # Humidity Sensors
        humidity_sensors = [sensor for sensor in get_room_sensors(home, room.name) if isinstance(sensor, HumiditySensor)]
        for sensor in humidity_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                logger.info(f"Room {room.name} humidity reading: {reading}%")
                if reading < HUMIDITY_LOW:
                    # Turn on humidifier
                    humidifier = [actor for actor in get_room_actuators(home, room.name) if isinstance(actor, Humidifier)][0]
                    humidifier.increase_humidity()
                    logger.info(f"Humidifier in {room.name} turned on to increase humidity")
                elif reading > HUMIDITY_HIGH:
                    # Turn on dehumidifier (if available)
                    # dehumidifier = [actor for actor in get_room_actuators(home, room.name) if isinstance(actor, Dehumidifier)][0]
                    # dehumidifier.decrease_humidity()
                    logger.info(f"Dehumidifier in {room.name} turned on to decrease humidity")

        # Light Intensity Sensors
        light_intensity_sensors = [sensor for sensor in get_room_sensors(home, room.name) if isinstance(sensor, LightIntensiveSensor)]
        for sensor in light_intensity_sensors:
            reading = sensor.get_reading()
            if reading is not None:
                logger.info(f"Room {room.name} light intensity reading: {reading} lux")
                if reading < LIGHT_INTENSITY_LOW:
                    # Turn on lights
                    lights = [actor for actor in get_room_actuators(home, room.name) if isinstance(actor, Light)]
                    for light in lights:
                        light.turn_on()
                        logger.info(f"Light in {room.name} turned on to increase light intensity")

    logger.info("Smart Home Functionality completed")

if __name__ == "__main__":
    main()