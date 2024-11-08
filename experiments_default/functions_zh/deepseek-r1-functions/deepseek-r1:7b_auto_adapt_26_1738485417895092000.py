# <think>
# Okay, I'm looking at the user's problem. They've provided three Python files and a question about how to implement an automatic home plan system based on temperature, humidity, and light levels.
# 
# First, in config.py, there are several constants for thresholds like temperature and humidity ranges. So those would be used by other parts of the code to determine when something needs adjusting.
# 
# In the Room class within home_plan.py, each room has sensors and actuators. The create_room_with_components function adds specific sensor types (like LightIntensiveSensor) and actuator types (like Door). These are then used in the main home_plan function which creates multiple rooms with their respective components.
# 
# Looking at get_room_sensors and get_room_actuators functions, they search through each room to find sensors or actuators of a certain type. But maybe this isn't efficient because it loops through every room for each call.
# 
# The user might want these functions to be more efficient. Perhaps using caching would help so that once we've checked all rooms, the data is readily available without re-scanning each time.
# 
# Also, in home_plan.py's main function, they're creating a list of rooms and then processing them. Maybe moving this into a separate module or class could make it cleaner.
# 
# Another thought: when getting room info using get_room(), it prints out room details but doesn't store the data anywhere except for printing. There might be a need to collect all room information in a structured way, like a dictionary with name and sensors/actuators arrays, so that this info is accessible elsewhere without re-scanning rooms.
# 
# So, steps I should consider:
# 
# 1. Refactor home_plan into a module that creates the Home object, which includes all rooms' data efficiently.
# 2. Ensure that when searching for room components (sensors or actuators), we don't scan each room every time but have some efficient method.
# 3. Possibly implement caching mechanisms in these search functions to avoid redundant processing.
# 
# I should also think about how to structure the Room and Home classes so that accessing sensors and actuators is straightforward, maybe by creating properties for them instead of having separate lists.
# 
# Wait, looking at the original code: get_room_sensors loops through each room, adds sensors if they match. That's inefficient because it does this every time someone calls it. Instead, perhaps during home creation, we can build a data structure that allows quick lookups based on sensor type or room name.
# 
# So maybe when creating rooms in home_plan(), for each room, store the list of sensors and actuators. Then, have helper functions that quickly search through these lists to find matching entries without iterating all rooms every time.
# 
# Another point is error handling: if a room doesn't exist, return None as per current code. That's good.
# 
# So putting it all together, I think the main steps are:
# 
# - Refactor get_room_sensors and get_room_actuators to use efficient lookups.
# - Build a structured data model (like dictionaries) that holds sensors and actuators by room name or type.
# - Possibly precompute these for each room during home creation.
# 
# I should also consider if any other parts of the code need adjusting, like in sensor.py where different sensor types are defined. But from what's given, I don't see issues there.
# 
# So to sum up, my thoughts are about making the search functions more efficient by caching or structuring data properly.
# </think>
# 
# Based on the provided files and understanding their functionalities, here's a structured approach to implement an automatic home plan system:
# 
# ### 1. **Setup Home Configuration**
# 
# - Use `config.py` constants (`TEMP_LOW`, `TEMP_HIGH`, etc.) for temperature and humidity thresholds.
# 
# ### 2. **Create Rooms with Sensors and Actuators**
# 
# - Utilize the `create_room_with_components` function to define rooms with their respective sensors (e.g., `LightIntensiveSensor`) and actuators (e.g., `Door`).
# 
# ### 3. **Efficiently Search for Components**
# 
# Instead of scanning all rooms every time, implement caching or helper functions that store component information by room name.
# 
# ### 4. **Organize Data Structure**
# 
# - Create a structured data model where each room contains its sensors and actuators.
# - Use dictionaries to map sensor/actuator types and names for quick lookup.
# 
# ### 5. **Implementation Steps**
# 
# 1. **Refactor Home Creation:**
#    - Move the `home_plan` function into a separate module (e.g., `home_plan.py`) to encapsulate room creation logic.
#    
# 2. **Optimize Search Functions:**
#    - Modify `get_room_sensors` and `get_room_actuators` to use cached data instead of iterating through rooms each time.
# 
# 3. **Refactor for Clarity:**
#    - Extract common functionality into helper methods, such as creating rooms with components or caching component lists by name.
# 
# ### 6. **Example Code Structure**
# 
# ```python
from home.logger_config import logger

class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.sensors = {}  # Maps sensor type to instance
        self.actuators = {}  # Maps actuator type to instance

    def add_sensor(self, sensor_type, **kwargs):
        """Add a sensor with specific parameters."""
        pass

    def add_actuator(self, actuator_type, **kwargs):
        """Add an actuator with specific parameters."""
        pass

class Home:
    def __init__(self):
        self.rooms = {}  # Maps room name to Room object
        self.sensors_cache = {}  # Maps sensor type to list of rooms and sensors
        self.actuators_cache = {}  # Maps actuator type to list of rooms and actuators

    def create_room(self, room_name, components):
        """Create a new room with specified components."""
        if room_name in self.rooms:
            raise ValueError("Room already exists")
        
        new_room = Room(room_name)
        for sensor_type, instance in components['sensors'].items():
            new_room.sensors[sensor_type] = instance
        for actuator_type, instance in components['actuators'].items():
            new_room.actuators[actuator_type] = instance
        
        self.rooms[room_name] = new_room
        # Cache sensor and actuator information by type
        self._cache_sensors(sensor_type, room_name)
        self._cache_actuators(actuator_type, room_name)

    def _cache_sensors(self, sensor_type, room_name):
        """Cache sensor types in the home."""
        if sensor_type not in self.sensors_cache:
            self.sensors_cache[sensor_type] = []
        self.sensors_cache[sensor_type].append(room_name)

    def _cache_actuators(self, actuator_type, room_name):
        """Cache actuator types in the home."""
        if actuator_type not in self.actuators_cache:
            self.actuators_cache[actuator_type] = []
        self.actuators_cache[actuator_type].append(room_name)

    def get_room_sensors(self, sensor_type):
        """Return rooms that have a specific sensor type."""
        return [room.name for room in self.sensors_cache.get(sensor_type, [])]

    def get_room_actuators(self, actuator_type):
        """Return rooms that have a specific actuator type."""
        return [room.name for room in self.actuators_cache.get(actuator_type, [])]
# ```
# 
# ### 7. **Advantages of the Approach**
# 
# - **Efficiency:** Caching allows quick retrieval of room names based on sensor or actuator types without scanning all rooms each time.
# - **Clarity:** The structured data model makes it easier to manage and extend with new sensor/actuator types.
# - **Reusability:** The `Home` class can be reused across different projects, making setup consistent.
# 
# ### 8. **Testing**
# 
# Ensure that the implementation works as expected by:
# 
# 1. Creating multiple rooms with various components.
# 2. Verifying that searching for sensors and actuators returns correct room names.
# 3. Testing error cases, such as a sensor type not found in any room.
# 
# This approach provides a scalable and maintainable foundation for an automatic home planning system based on temperature, humidity, and light levels.