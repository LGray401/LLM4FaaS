# The provided code appears to be a part of a home automation system, where you have various devices and sensors connected. The `Room` class represents a room in the house, and it can contain multiple sensors and actuators.
# 
# Here are some suggestions for improvement:
# 
# 1. **Use meaningful variable names**: Instead of using `name`, consider renaming it to something like `room_name` or `label`.
# 
# 2. **Use type hints**: Python 3.5+ has support for type hints which can help catch errors and improve code readability. Consider adding type hints for function parameters and return types.
# 
# 3. **Follow PEP 8 conventions**: The provided code mostly follows the PEP 8 style guide, but there are a few places where it doesn't. For example, consider using consistent spacing around operators.
# 
# 4. **Consider using an ORM (Object-Relational Mapping) library for database interaction**: If you're planning to store data in a database, consider using an ORM like SQLAlchemy or Django's ORM.
# 
# 5. **Avoid global variables and functions**: The provided code has some global variables and functions, which can make the code harder to understand and maintain. Consider encapsulating them within a class or module.
# 
# 6. **Consider using a configuration management system**: If you have multiple configurations for your home automation system, consider using a configuration management system like Flask-Config.
# 
# 7. **Use logging levels correctly**: Instead of using `logger.info()` or `logger.warning()`, consider using different log levels like `logger.debug()`, `logger.info()`, `logger.warning()`, and `logger.error()` to indicate the severity of the message.
# 
# 8. **Consider using a more robust way to handle exceptions**: The provided code uses bare `except` clauses, which can catch exceptions that you didn't intend to catch. Consider using specific exception types instead.
# 
# 9. **Follow Don't Repeat Yourself (DRY) principle**: If you have repeated code in multiple places, consider extracting it into a separate function or method.
# 
# 10. **Test your code thoroughly**: Finally, make sure to test your code thoroughly before deploying it.
# 
# Here's an updated version of the provided code with these suggestions applied:
# 
# ```python
import logging

class Room:
    def __init__(self, room_name: str):
        self.room_name = room_name
        self.sensors = []
        self.actuators = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_actuator(self, actor):
        self.actuators.append(actor)

    def print_info(self) -> None:
        logging.debug(f"Room: {self.room_name}")
        logging.debug("Sensors:")
        for sensor in self.sensors:
            logging.debug(f"- {sensor.id}")
        logging.debug("Actuators:")
        for actor in self.actuators:
            logging.debug(f"- {actor.id}")


def create_room_with_components(room_name: str, sensor_types, actuator_types) -> Room:
    room = Room(room_name)
    for sensor_type in sensor_types:
        room.add_sensor(sensor_type(room_name))
    for actuator_type in actuator_types:
        room.add_actuator(actuator_type(room_name))
    return room


def get_room(home: list, room_name: str) -> Room | None:
    for room in home:
        if room.room_name == room_name:
            logging.debug(f"Room {room_name} found!")
            return room
    logging.warning(f"No room named {room_name}")
    return None


def get_all_sensors(home: list, sensor_type: type) -> list | None:
    all_sensors = []
    for room in home:
        for sensor in room.sensors:
            if isinstance(sensor, sensor_type):
                all_sensors.append(sensor)
    return all_sensors


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    # Test the functions
    home = [
        create_room_with_components("LivingRoom", [LightIntensiveSensor], [Door]),
        create_room_with_components("Bedroom", [IndoorTemperatureSensor], [Light])
    ]

    get_room(home, "LivingRoom")
    get_all_sensors(home, LightIntensiveSensor)
# ```