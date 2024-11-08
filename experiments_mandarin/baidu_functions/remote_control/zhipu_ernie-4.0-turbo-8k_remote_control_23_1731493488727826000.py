# Based on your functional description and the provided source code, I will now provide a `function.py` file that contains the main function to initialize and control your smart home system. This file will be located in the `functions` folder and will make use of the classes and methods defined in the `sensor.py`, `actuator.py`, and `home_plan.py` files.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def initialize_smart_home():
    # Initialize the smart home with rooms and components
    home = home_plan()
    print_home_plan(home)
    return home


def monitor_sensors(home):
    # Get all sensors from all rooms
    all_sensors = []
    for room in home:
        all_sensors.extend(room.sensors)
    
    # Turn on all sensors
    for sensor in all_sensors:
        sensor.turn_on()
    
    # Monitor sensors and log readings
    for sensor in all_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            # Here you can add logic to handle sensor readings, e.g., adjust actuators based on readings
            handle_sensor_reading(sensor, reading)


def handle_sensor_reading(sensor, reading):
    # Example logic to handle sensor readings
    if sensor.sensor_type == "IndoorTemperature":
        if reading < TEMP_LOW:
            logger.warning(f"Low temperature detected in {sensor.room_name}: {reading}°C")
            adjust_heater(sensor.room_name, True, TEMP_HIGH)
        elif reading > TEMP_HIGH:
            logger.warning(f"High temperature detected in {sensor.room_name}: {reading}°C")
            adjust_ac(sensor.room_name, True, TEMP_LOW)
    
    elif sensor.sensor_type == "Humidity":
        if reading < HUMIDITY_LOW:
            logger.warning(f"Low humidity detected in {sensor.room_name}: {reading}%")
            # Turn on humidifier
        elif reading > HUMIDITY_HIGH:
            logger.warning(f"High humidity detected in {sensor.room_name}: {reading}%")
            # Turn off humidifier or adjust accordingly
    
    elif sensor.sensor_type == "LightIntensive":
        if reading < LIGHT_INTENSITY_LOW:
            logger.warning(f"Low light intensity detected in {sensor.room_name}: {reading} lux")
            adjust_lights(sensor.room_name, True, "high")
        elif reading > LIGHT_INTENSITY_HIGH:
            logger.warning(f"High light intensity detected in {sensor.room_name}: {reading} lux")
            adjust_lights(sensor.room_name, True, "low")


def adjust_heater(room_name, turn_on, target_temperature):
    heaters = get_all_actuators(home, "Heater")
    for heater in heaters:
        if heater.room_name == room_name:
            if turn_on:
                heater.turn_on()
                heater.set_target_temperature(target_temperature)
            else:
                heater.turn_off()


def adjust_ac(room_name, turn_on, target_temperature):
    acs = get_all_actuators(home, "AC")
    for ac in acs:
        if ac.room_name == room_name:
            if turn_on:
                ac.turn_on()
                ac.set_target_temperature(target_temperature)
            else:
                ac.turn_off()


def adjust_lights(room_name, turn_on, brightness_level):
    lights = get_all_actuators(home, "Light")
    for light in lights:
        if light.room_name == room_name:
            if turn_on:
                light.turn_on()
                light.set_brightness_level(brightness_level)
            else:
                light.turn_off()


# Main function to run the smart home system
def main():
    # Initialize the smart home
    global home
    home = initialize_smart_home()
    
    # Monitor sensors continuously (for demonstration purposes, we'll use a loop with a sleep interval)
    try:
        while True:
            monitor_sensors(home)
            # Sleep for a while before checking sensors again (you can adjust the interval as needed)
            # Here we use 5 seconds interval for demonstration
            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("Smart home system stopped.")


if __name__ == "__main__":
    main()