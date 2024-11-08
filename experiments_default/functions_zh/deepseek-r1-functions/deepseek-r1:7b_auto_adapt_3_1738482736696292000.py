# <think>
# Okay, I'm trying to help the user with their code. Let me see what they have here.
# 
# Looking at the files provided: there's a Room class in home_plan.py which adds sensors and actuators. The main script runs some functions that probably fetch rooms, sensors, and actuators based on room names or types.
# 
# In config.py, there are several variables set for thresholds like temperature ranges and light intensity. These might be used by the sensors to determine if conditions need to trigger actions.
# 
# The user is asking about integrating these configuration values into their Room class. So they want each sensor type (like TemperatureSensor) to check its relevant thresholds when triggered.
# 
# Hmm, so I think the approach should be:
# 
# 1. For each sensor in a room, define which config parameters it uses.
# 2. When a sensor's trigger condition is met, it calls an appropriate action method on the Room object.
# 
# So for example, if a TemperatureSensor checks if temperature is too low or high, and based on that decides to call either turn_on_heater or turn_off_heater.
# 
# I'll need to modify the Room class to include this logic. Each sensor will have its own set of thresholds and actions.
# 
# Wait, but how do I map each sensor type to these actions? Maybe by adding attributes like sensor_type to each sensor instance in the room's sensors list.
# 
# Also, for actuators like heater or cooling devices, they should know their power level based on the light intensity. So when the light is too high, maybe turn_on_heater at max power; if too low, turn_off_heater.
# 
# So I'll need to add a get_power method to the actuator class that returns 0-100% based on light intensity thresholds.
# 
# Putting it all together:
# 
# First, in the Room's __init__, each sensor is added with its type. Then, for each sensor, if it's a TemperatureSensor, set its thresholds and actions; same for Humidity or Light sensors.
# 
# Then, during initialization of actuators, each actuator knows how to adjust based on light intensity.
# 
# This way, when the room's sensors are triggered, they automatically call the correct method on the Room object with the appropriate parameters.
# 
# I think that makes sense. Now I can outline the code steps:
# 
# 1. Modify the Room class to include sensor type information.
# 2. For each sensor in add_sensor, set its sensor_type attribute and initialize thresholds and action methods based on that.
# 3. Add a get_power method to Actuators so they know how to adjust based on light intensity.
# 
# Yes, that should cover it. Now I can write the code accordingly.
# </think>
# 
# Based on your files, you want to integrate these configuration values into your Room class to handle sensor thresholds and trigger appropriate actions. Here's how we can modify the code:
# 
# 1. First, let's update the Room class with better structure for sensors:
# 2. Add sensor types and their corresponding thresholds
# 3. Implement logic to trigger actions based on sensor data
# 
# Here are the changes:
# 
# home_plan.py (modified):
# 
# ```python
class Room:
    def __init__(self, name):
        self.name = name
        self.sensors = []
        
        # Define default sensor thresholds
        self._sensor_thresholds = {
            "temperature": {"low": TEMP_LOW, "high": TEMP_HIGH},
            "humidity": {"low": HUMIDITY_LOW, "high": HUMIDITY_HIGH},
            "light_intensity": {"low": LIGHT_INTENSITY_LOW, "high": LIGHT_INTENSITY_HIGH}
        }
        
    def add_sensor(self, sensor):
        # Add sensor with its type information
        self.sensors.append({
            'sensor': sensor,
            'type': sensor.__class__.__name__,
            'thresholds': None,
            'actions': []
        })
    
    def set_sensor_thresholds(self, sensor_type, thresholds):
        if thresholds is not None:
            for sensor in self.sensors:
                if sensor['type'] == sensor_type:
                    sensor['thresholds'] = thresholds.copy()
                    break
        
    def add_sensor_action(self, sensor_type, action):
        if isinstance(action, list) and len(action) > 0:
            for sensor in self.sensors:
                if sensor['type'] == sensor_type:
                    sensor['actions'].append(action)
                    break
# ```
# 
# To use this modified Room class:
# 
# 1. You'll need to create sensor objects that match your defined types (e.g., TemperatureSensor, HumiditySensor, LightIntensitySensor)
# 
# Here's an example of how you might define sensors in your code:
# 
# ```python
class TemperatureSensor:
    def __init__(self):
        self.sensordata = {"temp": None}
        self.thresholds = {
            "low": config.TEMP_LOW,
            "high": config.TEMP_HIGH
        }
        self.actions = [
            {"method": "turn_on_heater"},
            {"method": "turn_off_heater"}
        ]

class HumiditySensor:
    def __init__(self):
        self.sensordata = {"humidity": None}
        self.thresholds = {
            "low": config.HUMIDITY_LOW,
            "high": config.HUMIDITY_HIGH
        }
        self.actions = [
            {"method": "turn_on_heating_system"},
            {"method": "do_not_turn_on_heating_system"}
        ]

class LightIntensitySensor:
    def __init__(self):
        self.sensordata = {"light": None}
        self.actions = [
            {"method": "adjust_heater_power", "params": {"max": True}},
            {"method": "adjust_heater_power", "params": {"min": False}}
        ]

class Actuator:
    def __init__(self, max_power=100):
        self.max_power = max_power
        
    def adjust_heater_power(self, params):
        if 'min' in params and 'max' in params:
            power = params['max'] or (params['min'] * 2)
            if isinstance(power, bool):
                power = int(power)
            return f"adjust_heater_power_to_{power}%"
        else:
            return "adjust_heater_power_to Default"
# ```
# 
# Now you can use the Room class like this:
# 
# ```python
# Example room setup
room = Room("Living Room")

# Adding sensors to the room
room.add_sensor(TemperatureSensor())
room.add_sensor(HumiditySensor())
room.add_sensor(LightIntensitySensor())

# Accessing sensor data and triggering actions
def handle_temperature_data(sensordata):
    if sensordata > room.sensors[0]['thresholds']['high']:
        action = room.sensors[0]['actions'][1]
        return action

def handle_light_data(sensordata):
    light_action = room.sensors[2]['actions'][0]
    if room.sensors[2]['sensordata']['light'] > config.LIGHT_INTENSITY_HIGH:
        return f"adjust_heater_power_to_{100}%"
# ```
# 
# The key changes are:
# 
# - The Room class now stores sensor type information
# - Each sensor can be configured with its own thresholds and actions
# - Actuators can now control operations based on light intensity
# 
# You'll need to create your actual sensor and actuator classes that implement these interfaces. This architecture allows for easy configuration and extension of sensors and their corresponding actions.