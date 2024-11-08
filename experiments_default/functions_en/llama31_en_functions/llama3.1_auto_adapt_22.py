# It looks like you've written a Python script to simulate a smart home system. Here are some suggestions for improvement:
# 
# 1. **Use meaningful variable names**: Variable names like `sensor_types` and `actuator_types` could be more descriptive, e.g., `sensors_to_install` and `devices_to_install`.
# 
# 2. **Consider using a data structure**: Instead of having lists of sensors and actuators within each room, you might consider using a dictionary where the keys are the sensor/actuator types and the values are lists of instances.
# 
# 3. **Extract methods**: Your script does quite a bit in one place. Consider breaking it down into smaller functions, each with its own responsibility (e.g., `create_room`, `add_sensor_to_room`, etc.).
# 
# 4. **Use type hints**: Adding type hints for function parameters and return types can make your code more readable and self-documenting.
# 
# 5. **Error handling**: You might want to add some error handling in case a room is not found or if there's an issue with adding sensors/actuators to a room.
# 
# 6. **Use consistent naming conventions**: Python's official style guide, PEP 8, suggests using lowercase letters and underscores for variable names. You're currently using camelCase.
# 
# 7. **Consider using a configuration file**: Instead of hardcoding the temperature thresholds in your script, you could store them in a separate configuration file (like the `config.py` file you've provided).
# 
# Here's an example of how you might refactor your code to incorporate these suggestions:
# 
# ```python
from home.logger_config import logger

class Room:
    def __init__(self, name):
        self.name = name
        self.sensors = []
        self.actuators = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_actuator(self, actuator):
        self.actuators.append(actuator)


def create_room(name: str) -> Room:
    return Room(name)


def add_sensors_to_room(room: Room, sensors: list):
    for sensor in sensors:
        room.add_sensor(sensor)


def add_actuators_to_room(room: Room, actuators: list):
    for actuator in actuators:
        room.add_actuator(actuator)


class Sensor:
    def __init__(self, name: str, sensor_type: str):
        self.name = name
        self.sensor_type = sensor_type

    def __str__(self) -> str:
        return f"{self.name} ({self.sensor_type})"


class Actuator:
    def __init__(self, name: str, actuator_type: str):
        self.name = name
        self.actuator_type = actuator_type

    def __str__(self) -> str:
        return f"{self.name} ({self.actuator_type})"


def main():
    living_room = create_room("Living Room")
    add_sensors_to_room(living_room, [Sensor("Temperature", "Indoor Temperature"), Sensor("Humidity", "Humidity")])
    add_actuators_to_room(living_room, [Actuator("Light", "Light"), Actuator("Heater", "Heater")])

    print(f"\n{living_room.name}:")
    print("Sensors:")
    for sensor in living_room.sensors:
        print("-", sensor)
    print("Actuators:")
    for actuator in living_room.actuators:
        print("-", actuator)


if __name__ == "__main__":
    main()
# ```