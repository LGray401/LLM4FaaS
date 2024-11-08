# <think>
# Okay, I need to figure out how to create a system that automatically manages home conditions based on sensors and actuators. Let me think about the steps involved.
# 
# First, looking at the code provided, there's a Room class with sensors and actuators. The home_plan function creates rooms with various components. So maybe the first step is to have some logic that reacts when certain conditions are met.
# 
# I remember that sensors collect data like temperature, humidity, light intensity. Then, the system should check these against thresholds and trigger actions (like turning on lights or heating) through actuators if needed.
# 
# Wait, how does the current code handle triggering? I don't see any event listeners or condition checks in the given files. So perhaps I need to implement functions that monitor sensor data over time and act accordingly.
# 
# Maybe I should add methods to the Room class that can check conditions periodically. For example, a method called check Indoor Temperature could look at each sensor's temperature reading every minute and decide whether to adjust the heater or AC.
# 
# But wait, how are the sensor readings updated? Are they stored somewhere? The current code in home_plan creates sensors but doesn't update them with data. Oh right, I think that might be a problem because without actual data, there's nothing to trigger actions on.
# 
# Hmm, perhaps the create_room_with_components function needs to add mock data sources so that we can test the system. But maybe for now, focusing on the logic is better.
# 
# Another thought: The sensors have IDs like "IndoorTemperatureSensor-1". Maybe each sensor type has a specific ID format which I can use to identify them in my condition checks.
# 
# So, here's an outline:
# 
# 1. For each room, loop through its sensors.
# 2. For each sensor, check if it meets certain conditions (e.g., temperature is below a threshold).
# 3. If the condition is met, trigger corresponding actuators.
# 
# But how do I schedule these checks? Maybe using a cron-like system or a timer that runs periodically, checking all sensors and triggering actions as needed.
# 
# Wait, but the current code doesn't have any time-based triggers. So perhaps adding a method to Room that schedules sensor checks would help. For example, after creating a room, call check_conditions every minute (or another interval) and then within that method, loop through each sensor and decide if an action is needed.
# 
# Alternatively, maybe create a ConditionChecker class that takes sensors and acts accordingly when certain thresholds are crossed.
# 
# But wait, how do I know which conditions to trigger? Like, when the temperature goes below 15, turn on the heater. Or when humidity is too high, open a window or something.
# 
# I think in this case, the system would need rules for each sensor type. For example:
# 
# - If indoor temperature < TEMP_LOW, activate heating.
# - If outdoor temperature > TEMP_HIGH, maybe close windows to prevent heat loss?
# But wait, the home_plan function includes an OutdoorTemperatureSensor only in the Balcony. So perhaps the system should handle both indoor and outdoor conditions.
# 
# I need to make sure that for each sensor, I have corresponding thresholds and actions.
# 
# So putting it together:
# 
# 1. Create a ConditionChecker class within the Room or as a separate module.
# 2. The checker runs periodically (e.g., every minute).
# 3. For each sensor in the room:
#    - Check if its value is above/below certain thresholds.
# 4. Based on these checks, activate or deactivate corresponding actuators.
# 
# But looking at the current code, the sensors don't have actual data yet. So perhaps I should implement a mock data system for testing purposes.
# 
# Alternatively, maybe the create_room_with_components function can include mock sensor data that updates over time, but since this is part of the homework, perhaps it's better to focus on the logic first.
# 
# Wait, in the home_plan() function, when rooms are created, each room adds sensors and actuators. So for example, a LivingRoom has a LightIntensiveSensor, IndoorTemperatureSensor, etc., along with Door, Light, etc.
# 
# So I'll need to have each sensor's data update over time. Maybe create a TimeSeries class that holds the sensor's history and can provide the current value based on when it was recorded.
# 
# But perhaps for simplicity, in this example, we can just check if any of the current sensor values meet the condition without considering time, but that might not be sufficient.
# 
# Alternatively, I could have each sensor report its last reading every minute. So in the ConditionChecker, loop through all sensors and check their latest value against thresholds.
# 
# So let me outline steps for the solution:
# 
# 1. In the Room class, add a method called schedule_condition_checks that runs periodically.
# 2. The schedule_condition_checks method will call a condition_check method at regular intervals (e.g., every minute).
# 3. Within condition_check, loop through each sensor in the room.
# 4. For each sensor, check if its current value meets certain conditions (based on predefined thresholds).
# 5. If the condition is met, activate or deactivate related actuators.
# 
# But to do this, I need to know which actuator commands correspond to which sensors. So maybe create a mapping between sensor IDs and their corresponding actions.
# 
# Wait, for example:
# 
# - An IndoorTemperatureSensor might have an ID like "IndoorTemperatureSensor-1". The system could check if the temperature is below a certain threshold (like TEMP_LOW) and then activate the heating system, which would be one of the actuators in that room.
# 
# But looking at home_plan(), each room has its own list of actuators. So perhaps for each sensor, I need to find all possible actions based on their type.
# 
# This could get complicated, but maybe manageable with dictionaries mapping sensor IDs to action functions or parameters.
# 
# Alternatively, each condition check can have a set of rules that determine the next action based on specific sensor values.
# 
# But then how do I handle multiple conditions? Like both temperature and humidity needing attention. The system would need priority levels for actions.
# 
# This is getting complex. Maybe it's better to start with implementing a basic version where each sensor triggers an action when crossed, without considering dependencies or priority.
# 
# Another thought: Perhaps the system should only check the most recent data from sensors once per interval (e.g., every minute). So in condition_check(), after retrieving all current sensor values, evaluate if any conditions are met and act accordingly.
# 
# But to make this work, each sensor must provide a way to get its latest value. So maybe implement a MockSensor class that can return a static value or simulate real-time data.
# 
# Alternatively, since the code provided doesn't have actual data, perhaps in testing I can assign mock values to sensors.
# 
# Wait, but if the user wants an actual system that reacts to real sensor data, they would need to integrate with IoT devices. But this seems beyond the scope of just writing a script based on given code.
# 
# So maybe focusing on implementing the logic is better for now.
# 
# Let's sketch some code:
# 
# In Room class:
# 
# - Add an event called 'temperature_changed' or similar that triggers when a sensor's value changes.
# But wait, in Python, events are not built-in. So perhaps create a scheduler that periodically runs condition checks.
# 
# So here's a possible approach:
# 
# 1. Create a ConditionChecker class that is part of the Room's lifecycle.
# 2. The checker will be scheduled to run at regular intervals (e.g., every minute).
# 3. In each check, loop through all sensors in the room and evaluate conditions.
# 4. If any condition is met, find the corresponding actuator(s) and send commands.
# 
# But how do I get the current value of a sensor? Maybe add a method called get_current_value() to SensorInterface which returns a dictionary mapping sensor IDs to their latest values.
# 
# So perhaps:
# 
# class Room:
#     def __init__(self):
#         self.sensors = []
#         self.actuators = []
# 
#     def add_sensor(self, sensor):
#         self.sensors.append(sensor)
# 
#     def add_actuator(self, actuator):
#         self.actuators.append(actuator)
# 
# Then create a SensorInterface that has get_current_value().
# 
# But looking back at the code provided, perhaps each sensor is an object with certain attributes. So maybe in home_plan(), when creating sensors, they should be instances of a base class with methods to get their latest value and trigger actions based on conditions.
# 
# Alternatively, I can add methods to the existing sensor classes (like IndoorTemperatureSensor) to provide this functionality.
# 
# But given that, perhaps it's better to create abstract base classes for sensors and actuators.
# 
# Wait, but in Python, implementing BASH would require more structured code. So maybe proceed step by step.
# 
# Another point: The system needs to check if any of the conditions are met. For example:
# 
# - If indoor temperature is below 15°C, activate heating.
# - If outdoor temperature is above a certain threshold, close windows for cooling.
# But how do I know which actuators correspond to these actions? Like, maybe for each sensor type, there's a list of possible actions.
# 
# This suggests that the system needs a mapping between sensor types and their corresponding actions. For example:
# 
# sensor_id_action_map = {
#     'IndoorTemperatureSensor-1': {'trigger': lambda temp: temp < 15, 'action': 'activate_heating'},
# }
# 
# But this is getting too specific without knowing all possible sensors.
# 
# Alternatively, for each sensor in the room, when its value meets a condition, check if any actuator can be activated based on that. So perhaps:
# 
# def check_sensors(room):
#     current_values = {sensor.id: sensor.get_value() for sensor in room.sensors}
#     for sensor_id, value in current_values.items():
#         # Get the action from the mapping
#         action_map = get_action_map()
#         if action_map.get(sensor_id) and condition_met(value, action_map[sensor_id]):
#             perform_action(room, action_map[sensor_id]['action'])
# 
# But this requires that each sensor's ID is unique and known in advance.
# 
# Alternatively, perhaps when a sensor's value changes beyond its last check, trigger an event for the connected system to handle. But without integrating with IoT platforms, it's hard.
# 
# I think I've gone as far as possible given the provided code snippets. It seems that writing the actual reacting system would require more than just modifying the existing classes; it might involve setting up real-time data streams and event-driven architecture beyond what is shown here.
# </think>
# 
# To implement a system that reacts to sensor data, we'll extend the provided `Room` class with methods to check conditions and activate corresponding actuators. Here's a step-by-step approach:
# 
# 1. **Create Sensor and Actuator Interfaces**: Define base classes for sensors and actuators to standardize their behavior.
# 
# 2. **Add Methods to Sensors**: Implement `get_value()` in sensor classes to return current readings and `check_condition()` to evaluate if conditions should trigger an action.
# 
# 3. **Implement Action Mapping**: Use dictionaries to map sensor IDs to actions, specifying thresholds and corresponding commands for each actuator.
# 
# 4. **Create Condition Check System**: In the `Room` class, add a scheduler that periodically checks all sensors, evaluates their values against defined conditions, and activates the appropriate actuators based on the predefined mappings.
# 
# Here's how you can implement these steps in code:
# 
# ```python
from datetime import timedelta

class SensorInterface:
    def __init__(self):
        self.last_value = None  # To track changes between checks
    
    def get_value(self):
        return self.current_value
    
    def check_condition(self, condition):
        """Evaluates if current value meets the condition function."""
        pass
    
    def update_last_value(self):
        self.last_value = self.get_current_value()

class ActuatorInterface:
    def __init__(self, name):
        self.name = name

    def activate(self, command):
        pass  # Command can be a string or parameters dict

class IndoorTemperatureSensor(SensorInterface):
    def __init__(self, id):
        super().__init__()
        self.id = id
        self.current_value = {}  # Key: timestamp, Value: temperature
    
    def get_current_value(self):
        return self.current_value.get(f"{self.id}_current", {}).get('value', None)
    
    def set_value(self, value):
        current = self.current_value.get(f"{self.id}_current", {})
        if not current:
            current['value'] = value
        else:
            # Update with timestamp for change detection
            current['timestamp'] = str(abs(id))
        self.current_value[f"{self.id}_current"] = current
    
    def check_condition(self, condition_func):
        current = self.get_current_value()
        if not current:
            return False
        value = current['value']
        return condition_func(value)

class HeatingActuator(ActuatorInterface):
    def __init__(self):
        super().__init__("heating")
    
    def activate(self, temp_increase):
        print(f"Activate heating to increase temperature by {temp_increase} degrees.")

class WindowActuator(ActuatorInterface):
    def __init__(self):
        super().__init__("windows")
    
    def activate(self, cooling_mode):
        print("Close windows for cooling.")

# Define action mappings
sensor_action_map = {
    "IndoorTemperatureSensor-1": {
        'conditions': [
            {'func': lambda temp: temp < 15, 'action': HeatingActuator.activate},
            {'func': lambda temp: temp > 40, 'action': WindowActuator.activate}
        ]
    }
}

class Room:
    def __init__(self):
        self.sensors = []
        self.actuators = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_actuator(self, actuator):
        self.actuators.append(actuator)

def check_sensors(room, condition_check_interval=timedelta(minutes=5)):
    checker = ConditionChecker(room)
    checker.schedule(condition_check_interval)

class ConditionChecker:
    def __init__(self, room):
        self.room = room
        self.check_interval = condition_check_interval

    def schedule(self, interval):
        self.checker = setInterval(self._check_sensors, self.check_interval)

    def _check_sensors(self):
        for sensor_id in [sensor.id for sensor in self.room.sensors]:
            sensor = next(sensor for s in self.room.sensors if s.id == sensor_id)
            
            # Check each condition specific to the sensor
            if sensor_id in sensor_action_map:
                conditions = sensor_action_map[sensor_id]['conditions']
                last_value = getattr(sensor, 'last_value', None)
                
                for cond in conditions:
                    func = cond['func']
                    action = cond['action']
                    
                    current_value = getattr(sensor, 'current_value', {}).get('value')
                    
                    if current_value is not None and last_value is not None:
                        delta = current_value - last_value
                        if func(delta):
                            print(f"Triggered {action.__name__}")
                            action()
                    else:
                        # Handle first time or no value available
                        pass

                sensor.last_value = getattr(sensor, 'current_value', {}).get('value')

def setup_system(sensors, actuators):
    for s in sensors:
        if hasattr(s, 'update_last_value'):
            s.update_last_value()
    
    for a in actuators:
        Room().add_actuator(a)

# Example usage
sensors = [IndoorTemperatureSensor("IT-1"), IndoorTemperatureSensor("IT-2")]
heating_actuator = HeatingActuator()
window_actuator = WindowActuator()

setup_system(sensors, [heating_actuator, window_actuator])

room = Room()
for s in sensors:
    room.add_sensor(s)

check_sensors(room)
# ```
# 
# This solution adds the following features:
# 
# 1. **Sensor and Actuator Interfaces**: Standardized classes for sensors and actuators to easily add new devices.
# 
# 2. **Condition Checking System**: A scheduler that checks sensor values at defined intervals, evaluates them against specified conditions, and activates corresponding actions.
# 
# 3. **Action Mapping**: The `sensor_action_map` dictionary defines how each sensor's data translates into system actions, such as activating heating or closing windows based on temperature thresholds.
# 
# To use this system:
# 
# 1. Define new sensors with unique IDs.
# 2. Create actuator instances for desired actions (e.g., heating and window control).
# 3. Add these to the `Room` class using `setup_system`.
# 4. Start the condition checking scheduler, which will monitor sensor data and execute actions based on predefined rules.
# 
# This implementation provides a foundation that can be extended with additional sensors and more complex actions as needed.