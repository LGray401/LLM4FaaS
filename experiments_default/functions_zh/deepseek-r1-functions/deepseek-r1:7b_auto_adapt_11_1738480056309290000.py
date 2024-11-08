# <think>
# Okay, I need to figure out how to write a Python program that simulates a home automation system based on the provided code snippets. Let's break down what each part does and see how they fit together.
# 
# First, looking at config.py, it sets some thresholds for temperature, humidity, light intensity, and other settings. These values are probably used by sensors to determine when certain actions should be taken, like adjusting the temperature or lighting.
# 
# Then, in the logger_config.py snippet, there's a logger setup with different levels: info, warning, critical, error, and debug. This means that any messages during runtime will be logged appropriately based on their severity. I'll need to make sure logs are correctly formatted and handled as intended.
# 
# Next is the Room class in home_plan.py. Each room has sensors and actuators added via add_sensor and add_actuator methods. The print_info method displays the room's name, followed by a list of sensors and actuators with their IDs. So when creating rooms, I need to ensure that each sensor and actuator is correctly initialized.
# 
# The create_room_with_components function takes a room name, sensor types, and actuator types. It adds one instance of each sensor type (like LightIntensiveSensor) and each actuator type (like Door). This seems straightforward, but I should check if all sensors and actuators are properly imported from the logger_config module.
# 
# In home_plan(), multiple rooms are created using create_room_with_components, each with specific sensors and actuators. For example, LivingRoom has a LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor as its base sensors, and various doors, lights, etc., as actuators. This setup allows for adding different components to rooms dynamically.
# 
# The print_home_plan function loops through each room in the home list and calls print_info(), which displays all the sensors and actuators per room. The get_room function checks if a room exists by name and logs accordingly; same with get_room_sensors and get_room_actuators, which retrieve the respective lists from a specific room.
# 
# The get_all_sensors and get_all_actuators functions loop through each room in the home list and collect sensors or actuators of a specified type. This is useful for filtering components by their types.
# 
# Looking at the main block, it calls home_plan() to create all rooms, then gets all actuators of type "Light" from the entire home setup. The print statement will display these lights.
# 
# Now, thinking about how everything interacts: when sensors are added to a room, they get registered and can be accessed via their names or types. Actuators can also be accessed similarly. The logger is used for logging actions taken by the system, which could help in debugging or monitoring the automation process.
# 
# Potential issues I might encounter:
# 
# 1. **Initialization of Sensors and Actuators**: Each sensor and actuator must be properly initialized with correct parameters when added to a room. For example, a LightIntensiveSensor needs its name attribute set correctly during instantiation.
# 
# 2. **Room Identification**: When adding rooms via create_room_with_components, the function uses the provided sensor_types and actuator_types lists. I need to ensure that each type corresponds to an actual class from the logger_config module.
# 
# 3. **Component Types in home_plan()**: The home_plan function defines specific sensors and actuators for each room but may miss some. For example, a "Balcony" might only have OutdoorTemperatureSensor or similar; also, verify if all needed components are imported.
# 
# 4. **Sensors and Actuators Access**: When retrieving sensors or actuators via get_room_sensors or get_room_actuators, the function returns None if no matching room is found. I need to handle this case properly, perhaps by returning an empty list instead.
# 
# 5. **Logging Errors**: The logger_config sets up different log levels. Ensuring that all messages are logged correctly without exceeding log levels (like not logging critical or error when info suffices) is important for system efficiency and logs readability.
# 
# 6. **Dependencies**: All classes like Light, Door, SmartSocket must be defined in the logger_config module along with their sensor types to avoid NameErrors.
# 
# 7. **Room Print Info Handling**: The print_info method lists each sensor and actuator by their IDs but doesn't indicate which room they belong to. When a room has multiple sensors or actuators of the same type, this could cause confusion. Perhaps adding information about which room the sensor/actuator belongs to would be helpful.
# 
# Possible improvements:
# 
# - Implementing a way to associate sensors with specific regions (like "living", "bedroom") based on their placement in rooms.
#   
# - Adding functionality to trigger actions automatically when certain conditions are met, like adjusting lighting based on temperature changes or motion detected by cameras (though this isn't covered here).
# 
# But for now, focusing on the given code snippets and ensuring that all components are correctly initialized and logged.
# 
# Testing steps:
# 
# 1. Run home_plan() without any parameters to see if rooms are created as expected.
# 2. Check each room's print output using print_home_plan() to ensure sensors and actuators are listed correctly.
# 3. Test getting individual rooms or components via get_room(), get_room_sensors(), etc., ensuring they return the correct data.
# 4. Verify that logging messages are appropriate in terms of log level (e.g., info vs warning) when actions occur.
# 
# Potential mistakes:
# 
# - Forgetting to import classes from logger_config, leading to NameErrors.
#   
# - Misusing sensor and actuator names during instantiation; for example, not setting 'name' correctly as required by the sensor/actuator classes.
# 
# Additionally, ensuring that each room's add_sensor() or add_actuator() method is properly called with the correct arguments. For instance, sensors might require a name parameter which should match exactly between create_room_with_components and when adding via the room's interface.
# 
# Also, checking if all the imported types (like Light) are correctly defined in logger_config so that they can be instantiated without issues.
# </think>
# 
# To implement the home automation system based on the provided code snippets, follow these steps:
# 
# 1. **Import Necessary Modules**: Ensure that all required classes from `logger_config` are imported, such as `Config`, `Sensor`, `Actuator`, and logging functions.
# 
# 2. **Define Configurations**: Use the `Config` class to set sensor and actuator thresholds according to requirements.
# 
# 3. **Create Rooms**: Utilize `create_room_with_components` to define each room with its specific sensors and actuators, ensuring that each instance is properly initialized.
# 
# 4. **Implement Functions**:
#    - `print_info(room)`: Display the room's name, sensors, and actuators.
#    - `get_room(name)`, `get_room_sensors(room)`, and `get_room_actuators(room)` to retrieve specific components by name or type.
# 
# 5. **Run Main Block**: Execute the main function to create rooms and collect all relevant actuator information.
# 
# 6. **Handle Logging**: Ensure that logging messages are correctly formatted and at appropriate levels for each action taken by the system.
# 
# 7. **Test Functions**: Verify each step by running `print_home_plan()` after creating rooms, checking if sensors and actuators are listed correctly.
# 
# Potential issues to watch out for:
# - Incorrect initialization of sensors or actuators.
# - Missing imports of required classes from `logger_config`.
# - Properly setting attributes during sensor/actuator instantiation (like 'name').
# - Handling cases where a room doesn't exist via the get_room function without errors.
# 
# Here's a sample implementation:
# 
# ```python
from logger_config import Config, Sensor, Actuator, info, warning, critical, error, debug

# Initialize configuration with appropriate thresholds and component types
config = Config(
    temperature_min=20,
    temperature_max=30,
    humidity_low=50,
    light_high=100,
    # Add more configurations as needed
)

def create_room_with_components(room_name: str, sensor_types: list, actuator_types: list):
    room = Room()
    for sensor_type in sensor_types:
        room.add_sensor(eval(sensor_type)(name=sensor_type.replace('_', ' ').title()))
    for actuator_type in actuator_types:
        room.add_actuator(eval(actuator_type)(name=actuator_type.replace('_', ' ').title()))
    return room

class Room:
    def __init__(self, name):
        self.name = name
        self.sensors = []
        self.actors = []

    def add_sensor(self, sensor):
        if hasattr(sensor, '__class__'):
            self.sensors.append(sensor)
        else:
            raise TypeError("Invalid sensor type")

    def add_actuator(self, actuator):
        if hasattr(actuator, '__class__'):
            self.actors.append(actuator)
        else:
            raise TypeError("Invalid actuator type")

    def print_info(self):
        info(f"Room {self.name}")
        for sensor in self.sensors:
            info(sensor.__class__.__name__ + " - " + str(sensor))
        for actuator in self.actors:
            info(actuator.__class__.__name__ + " - " + str(actuator))

def get_room(name: str, rooms):
    if any(room.name == name for room in rooms.values()):
        return next(room.values())
    warning(f"Room {name} does not exist")

def get_room_sensors(room):
    sensors = []
    for sensor in room.sensors:
        sensors.append(sensor.__class__.__name__)
    return sensors

def get_room_actuators(room):
    actuators = []
    for actuator in room.actors:
        actuators.append(actuator.__class__.__name__)
    return actuators

rooms = {
    "Living Room": create_room_with_components("Living Room", ["LightIntensiveSensor", "IndoorTemperatureSensor", "HumiditySensor"], [
        "Door",
        "Light",
        "SmartSocket"
    ]),
    "Dining Room": create_room_with_components("Dining Room", ["TemperatureSensor", "HumiditySensor"], [
        "ServeActuator",
        "CleanActuator"
    ]),
    # Add more rooms as needed
}

def main():
    for room_name in rooms:
        print(f"\nRoom {room_name}")
        get_room(room_name, rooms).__print_info__()

if __name__ == "__main__":
    main()
# ```
# 
# **Step-by-Step Explanation:**
# 
# 1. **Import Necessary Classes**: Import the required classes from `logger_config` to handle configurations and logging.
# 
# 2. **Define Configuration**: Create a configuration class instance (`Config`) with appropriate thresholds for sensors and actuators.
# 
# 3. **Create Rooms Function**: Implement `create_room_with_components` to generate rooms with predefined sensors and actuators, ensuring each is properly initialized.
# 
# 4. **Room Class**: Define a `Room` class that holds the room's name, sensors, and actors, providing methods to add these components and print information about them.
# 
# 5. **Helper Functions**:
#    - `get_room`: Checks if a room exists by comparing names.
#    - `get_room_sensors` and `get_room_actuators`: Retrieve lists of sensor and actuator types from the room's components.
# 
# 6. **Main Function**: Creates rooms, assigns their sensors and actuators, and prints their information using helper functions.
# 
# 7. **Run Main Block**: Executes all defined functions to set up and display the created rooms with their respective components.
# 
# This implementation ensures that each room is correctly configured, logged appropriately, and provides a structured way to retrieve specific components as needed.