from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def turn_on_sensor(home, room_name, sensor_type):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == sensor_type:
            sensor.turn_on()
            return True

    print(f"No {sensor_type} sensor found in {room_name}")
    logger.warning(f"No {sensor_type} sensor found in {room_name}")
    return False


def turn_off_sensor(home, room_name, sensor_type):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == sensor_type:
            sensor.turn_off()
            return True

    print(f"No {sensor_type} sensor found in {room_name}")
    logger.warning(f"No {sensor_type} sensor found in {room_name}")
    return False


def get_sensor_reading(home, room_name, sensor_type):
    sensors = get_room_sensors(home, room_name)
    for sensor in sensors:
        if sensor.sensor_type == sensor_type:
            return sensor.get_reading()

    print(f"No {sensor_type} sensor found in {room_name}")
    logger.warning(f"No {sensor_type} sensor found in {room_name}")
    return None


def turn_on_actuator(home, room_name, actuator_type):
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == actuator_type:
            actuator.turn_on()
            return True

    print(f"No {actuator_type} actuator found in {room_name}")
    logger.warning(f"No {actuator_type} actuator found in {room_name}")
    return False


def turn_off_actuator(home, room_name, actuator_type):
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == actuator_type:
            actuator.turn_off()
            return True

    print(f"No {actuator_type} actuator found in {room_name}")
    logger.warning(f"No {actuator_type} actuator found in {room_name}")
    return False


def set_actuator_target_temperature(home, room_name, actuator_type, target_temperature):
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == actuator_type:
            actuator.set_target_temperature(target_temperature)
            return True

    print(f"No {actuator_type} actuator found in {room_name}")
    logger.warning(f"No {actuator_type} actuator found in {room_name}")
    return False


def adjust_actuator_temperature(home, room_name, actuator_type, current_temperature):
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if actuator.actuator_type == actuator_type:
            actuator.adjust_temperature(current_temperature)
            return True

    print(f"No {actuator_type} actuator found in {room_name}")
    logger.warning(f"No {actuator_type} actuator found in {room_name}")
    return False


def adjust_room_temperature(home, room_name):
    temperature = get_sensor_reading(home, room_name, "IndoorTemperature")
    if temperature is not None:
        if temperature < TEMP_LOW:
            turn_on_actuator(home, room_name, "Heater")
            set_actuator_target_temperature(home, room_name, "Heater", TEMP_HIGH)
        elif temperature > TEMP_HIGH:
            turn_on_actuator(home, room_name, "AC")
            set_actuator_target_temperature(home, room_name, "AC", TEMP_LOW)
        else:
            turn_off_actuator(home, room_name, "Heater")
            turn_off_actuator(home, room_name, "AC")


def adjust_room_humidity(home, room_name):
    humidity = get_sensor_reading(home, room_name, "Humidity")
    if humidity is not None:
        if humidity < HUMIDITY_LOW:
            # TODO: Increase humidity in the room
            print(f"Humidity in {room_name} is too low, need to increase humidity!")
            logger.warning(f"Humidity in {room_name} is too low, need to increase humidity!")
        elif humidity > HUMIDITY_HIGH:
            # TODO: Decrease humidity in the room
            print(f"Humidity in {room_name} is too high, need to decrease humidity!")
            logger.warning(f"Humidity in {room_name} is too high, need to decrease humidity!")


def adjust_room_light_intensity(home, room_name):
    light_intensity = get_sensor_reading(home, room_name, "LightIntensive")
    if light_intensity is not None:
        if light_intensity < LIGHT_INTENSITY_LOW:
            # TODO: Turn on light in the room
            print(f"Light intensity in {room_name} is too low, need to turn on light!")
            logger.warning(f"Light intensity in {room_name} is too low, need to turn on light!")
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            # TODO: Turn off light in the room
            print(f"Light intensity in {room_name} is too high, need to turn off light!")
            logger.warning(f"Light intensity in {room_name} is too high, need to turn off light!")


def auto_adjust_room_conditions(home, room_name):
    adjust_room_temperature(home, room_name)
    adjust_room_humidity(home, room_name)
    adjust_room_light_intensity(home, room_name)


def main():
    home = home_plan()
    print("Welcome to your smart home! What would you like to do?")
    while True:
        # user input command
        command = input("> ")
        if command.lower() == "exit":
            break
        elif command.lower().startswith("turn on"):
            parts = command.split()
            if len(parts) >= 4:
                room_name = parts[2]
                device_type = parts[3]
                if device_type.lower() == "light":
                    if turn_on_actuator(home, room_name, "Light"):
                        print(f"Light in {room_name} is now turned on.")
                        logger.info(f"Light in {room_name} is turned on.")
                    else:
                        print(f"Failed to turn on light in {room_name}.")
                        logger.warning(f"Failed to turn on light in {room_name}.")
                elif device_type.lower() == "heater":
                    if turn_on_actuator(home, room_name, "Heater"):
                        print(f"Heater in {room_name} is now turned on.")
                        logger.info(f"Heater in {room_name} is turned on.")
                    else:
                        print(f"Failed to turn on heater in {room_name}.")
                        logger.warning(f"Failed to turn on heater in {room_name}.")
                elif device_type.lower() == "ac":
                    if turn_on_actuator(home, room_name, "AC"):
                        print(f"AC in {room_name} is now turned on.")
                        logger.info(f"AC in {room_name} is turned on.")
                    else:
                        print(f"Failed to turn on AC in {room_name}.")
                        logger.warning(f"Failed to turn on AC in {room_name}.")
                else:
                    print(f"Invalid device type: {device_type}")
            else:
                print("Invalid command format.")
        elif command.lower().startswith("turn off"):
            parts = command.split()
            if len(parts) >= 4:
                room_name = parts[2]
                device_type = parts[3]
                if device_type.lower() == "light":
                    if turn_off_actuator(home, room_name, "Light"):
                        print(f"Light in {room_name} is now turned off.")
                        logger.info(f"Light in {room_name} is turned off.")
                    else:
                        print(f"Failed to turn off light in {room_name}.")
                        logger.warning(f"Failed to turn off light in {room_name}.")
                elif device_type.lower() == "heater":
                    if turn_off_actuator(home, room_name, "Heater"):
                        print(f"Heater in {room_name} is now turned off.")
                        logger.info(f"Heater in {room_name} is turned off.")
                    else:
                        print(f"Failed to turn off heater in {room_name}.")
                        logger.warning(f"Failed to turn off heater in {room_name}.")
                elif device_type.lower() == "ac":
                    if turn_off_actuator(home, room_name, "AC"):
                        print(f"AC in {room_name} is now turned off.")
                        logger.info(f"AC in {room_name} is turned off.")
                    else:
                        print(f"Failed to turn off AC in {room_name}.")
                        logger.warning(f"Failed to turn off AC in {room_name}.")
                else:
                    print(f"Invalid device type: {device_type}")
            else:
                print("Invalid command format.")
        elif command.lower().startswith("set temperature"):
            parts = command.split()
            if len(parts) >= 5:
                room_name = parts[2]
                device_type = parts[3]
                target_temperature = float(parts[4])
                if device_type.lower() == "heater":
                    if set_actuator_target_temperature(home, room_name, "Heater", target_temperature):
                        print(f"Heater in {room_name} target temperature set to {target_temperature}°C.")
                        logger.info(f"Heater in {room_name} target temperature set to {target_temperature}°C.")
                    else:
                        print(f"Failed to set heater in {room_name} target temperature.")
                        logger.warning(f"Failed to set heater in {room_name} target temperature.")
                elif device_type.lower() == "ac":
                    if set_actuator_target_temperature(home, room_name, "AC", target_temperature):
                        print(f"AC in {room_name} target temperature set to {target_temperature}°C.")
                        logger.info(f"AC in {room_name} target temperature set to {target_temperature}°C.")
                    else:
                        print(f"Failed to set AC in {room_name} target temperature.")
                        logger.warning(f"Failed to set AC in {room_name} target temperature.")
                else:
                    print(f"Invalid device type: {device_type}")
            else:
                print("Invalid command format.")
        elif command.lower().startswith("get reading"):
            parts = command.split()
            if len(parts) >= 4:
                room_name = parts[2]
                sensor_type = parts[3]
                reading = get_sensor_reading(home, room_name, sensor_type)
                if reading is not None:
                    print(f"The {sensor_type} sensor reading in {room_name} is: {reading}")
                    logger.info(f"The {sensor_type} sensor reading in {room_name} is: {reading}")
                else:
                    print(f"Failed to get {sensor_type} sensor reading in {room_name}.")
                    logger.warning(f"Failed to get {sensor_type} sensor reading in {room_name}.")
            else:
                print("Invalid command format.")
        elif command.lower().startswith("auto adjust"):
            parts = command.split()
            if len(parts) >= 3:
                room_name = parts[2]
                auto_adjust_room_conditions(home, room_name)
                print(f"Auto adjusting room conditions in {room_name}.")
                logger.info(f"Auto adjusting room conditions in {room_name}.")
            else:
                print("Invalid command format.")
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

# This 'function.py' file defines functions to interact with the smart home system. It uses the classes and functions defined in other files to achieve the desired functionality. 

# Here's a breakdown of the functions:

# * **turn_on_sensor/turn_off_sensor/get_sensor_reading:** These functions control the sensors in a room. They turn sensors on/off and retrieve readings from sensors.
# * **turn_on_actuator/turn_off_actuator:** These functions control the actuators in a room. They turn actuators on/off.
# * **set_actuator_target_temperature:**  This function sets the target temperature for actuators like heaters and AC units.
# * **adjust_actuator_temperature:** This function automatically adjusts the actuator based on the current temperature.
# * **adjust_room_temperature/adjust_room_humidity/adjust_room_light_intensity:**  These functions handle automatic adjustments based on temperature, humidity, and light intensity readings, respectively.
# * **auto_adjust_room_conditions:** This function calls the above three functions to automatically adjust the room conditions.
# * **main:** This function handles user interaction. It takes commands from the user, parses them, and executes the appropriate functions to control the smart home.

# This structure provides a clear separation of concerns, making the code more organized and easier to maintain. It also allows for easy expansion with new features by simply adding more functions and updating the main function to handle them.
