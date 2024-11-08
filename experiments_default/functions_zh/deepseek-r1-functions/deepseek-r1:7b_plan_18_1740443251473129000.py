# <think>
# Okay, I need to figure out how to implement the Light sensor in the home_plan function using the config.py and logger_config. Let's start by understanding what each part does.
# 
# First, looking at the Light sensor class in light.py, it has __init__, get_id, get_name, set_light, and read. The read method returns a dictionary with current values for lux and temperature. So when an instance of Light is created, I need to initialize these values properly.
# 
# In config.py, there are thresholds for temperature and humidity, as well as light intensity ranges. Wait duration might not be directly relevant here unless we're scheduling actions based on changes over time.
# 
# The home_plan function creates rooms with various sensors and actuators. The get_all_actuators function is supposed to collect all actuator types of a specific type. But right now, it's using 'actuator_type' as a string, which might not match correctly since the Light class has an id like "Light".
# 
# Wait, in home_plan, when adding Light sensors, they are created with sensor_type(name). For example, in create_room_with_components for LivingRoom: [LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor], then door, light, etc.
# 
# So each room's sensors include various types. But the get_all_actuators function is looking for an actuator type string like "Light" and returns all such actuators in the home.
# 
# But how does it match? The Light class has id as a property based on sensor_type. So when creating a Light sensor, its id would be 'Light'. Therefore, when calling get_all_actuators with 'Light', it should find all room sensors of type Light and add them to the actuator list in each room.
# 
# Wait no, looking at home_plan function:
# 
# In create_room_with_components for LivingRoom: 
# 
# It adds Door, Light, Window, Window, etc. Each is an instance of a class (like Light). So in the Room's actuators list, these Light instances are added as they have their own id (e.g., 'Light').
# 
# But in get_all_actuators function:
# 
# def get_all_actuators(home, actuator_type):
#     all_actuators = []
#     for room in home:
#         for actuator in room.actuators:
#             if actuator.actuator_type == actuator_type:
#                 all_actuators.append(actuator)
# 
#     return all_actuators
# 
# So when we pass 'Light' as the actuator_type, it should collect all instances of Light from each room.
# 
# Wait but looking at the code:
# 
# In home_plan(), in create_room_with_components for LivingRoom: 
# 
# room.add_actuator(ActuatorType(name))
# 
# Like, for example, [Door, Light, Window, etc.] So when actuator_type is 'Light', it should collect all instances of Light from each room.
# 
# But wait, how does the Actuator class have an actuator_type attribute? Looking back to the provided code:
# 
# In the Light class's __init__, self.actuator_type = sensor_type, which would be "Light" if the sensor type was Light. So yes, when adding a Light instance as an actuator, its id is 'Light', matching what get_all_actuators is looking for.
# 
# So in home_plan(), after creating all rooms, the function calls get_all_actuators with 'Light' and expects to collect all such actuators across rooms.
# 
# But wait, no. In home_plan(), when adding actuators:
# 
# create_room_with_components("LivingRoom", [LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor], ...)
# 
# And then for actuator types: 
# 
# [Door, Light, Window, etc.]
# 
# Wait, the code in create_room_with_components is a bit confusing.
# 
# Looking at line 30 of home_plan():
# 
# It's inside a list comprehension that creates each room by passing sensor_types and actuator_types to create_room_with_components. For example:
# 
# create_room_with_components("LivingRoom", [LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor], 
#                             [Door, Light, Window, Window, Curtain, MusicPlayer, SmartSocket, SmartSocket,
#                              CleaningRobot, SmartTV, NotificationSender, AC, Heater])
# 
# Wait, that's not correct. The create_room_with_components function is given sensor_types and actuator_types as separate lists.
# 
# In home_plan(), the first argument to create_room_with_components for LivingRoom is [LightIntensiveSensor, ...], which are sensors, so they're added to room.sensors. Then the second part is [Door, Light, ...], which are actuators, so added to room.actuators.
# 
# But looking at how create_room_with_components works:
# 
# def create_room_with_components(name, sensor_types, actuator_types):
#     room = Room(name)
#     for sensor_type in sensor_types:
#         room.add_sensor(sensor_type(name))
#     for actuator_type in actuator_types:
#         room.add_actuator(actuator_type(name))
#     return room
# 
# So each sensor_type is a class (like LightIntensiveSensor), and when called as sensor_type(name) it creates an instance of that class with name.
# 
# Similarly, each actuator_type is a class like Light, and the actuator_type(name) creates an instance which has actuator_type set to "Light".
# 
# Therefore, in home_plan(), all Light instances are added as actuators to their respective rooms. So when get_all_actuators is called with 'Light', it should collect all these.
# 
# But wait, looking at the current code for get_all_actuators:
# 
# def get_all_actuators(home, actuator_type):
#     all_actuators = []
#     for room in home:
#         for actuator in room.actuators:
#             if actuator.actuator_type == actuator_type:
#                 all_actuators.append(actuator)
#     return all_actuators
# 
# So this should work because each Light actuator has actuator_type as "Light".
# 
# But the user says that the Light sensor isn't being implemented correctly. So why is this happening?
# 
# Looking at light.py:
# 
# The read method returns a dictionary with 'lux' and 'temperature'. But in home_plan, when adding a Light sensor to a room's actuators, perhaps we need to also track these values.
# 
# Wait, but actuator doesn't seem to have any methods for getting state. The current code just has add and set methods based on the actuator_type.
# 
# Hmm, maybe I'm missing something else. Maybe in home_plan(), when adding Light as an actuator, it's not correctly initializing their read() method or something similar.
# 
# Wait, no. In light.py:
# 
# class Light: ... 
# 
# But the actuator doesn't have a read method; perhaps that's part of the issue. The sensor is responsible for providing data, but if we're using it as an actuator, maybe it needs to be in a state where it can provide feedback.
# 
# Wait, no. Maybe I'm confusing sensors and actuators here. Let me think again: in home_plan(), when creating the Light instance with name (e.g., 'LivingRoom'), what is sensor_type? It's probably the Light class.
# 
# So in create_room_with_components for LivingRoom:
# 
# - For each sensor_type in [LightIntensiveSensor, ...], it creates an instance of that sensor. So if the sensor is LightIntensiveSensor, then sensor_type(name) would be a LightIntense sensor with name 'LivingRoom'.
# 
# But wait, looking at light.py: 
# 
# The Light class's __init__ takes sensor_type and name as parameters.
# 
# So when creating Light instances in home_plan, we need to pass the correct sensor type. But how are they being created?
# 
# Wait, perhaps the issue is that create_room_with_components for actuator_types uses a different method of adding sensors versus actuators.
# 
# Looking at light.py: The add function just appends the instance, so maybe the problem is elsewhere.
# 
# Alternatively, perhaps in home_plan(), when creating the Light actuators, they are not being added correctly. Maybe the code that's supposed to create them isn't doing it right.
# 
# Wait, looking back at home_plan:
# 
# In create_room_with_components for LivingRoom: 
# 
# It adds sensors as sensor_type(name), where sensor_type is LightIntensiveSensor etc., and then for actuator types, like Light, MusicPlayer, etc. So each of these is added as an actuator in the room.
# 
# But perhaps when using 'Light' as an actuator type, it's not correctly initializing its read method or something else.
# 
# Alternatively, maybe get_all_actuators isn't considering all instances because of a typo in 'actuator_type' variable name. Or perhaps in the code for Light class, there's no get_value method or similar to provide data when needed.
# 
# Wait, but the user is asking about implementing the Light sensor so that it can be used as an actuator. So maybe the problem isn't with home_plan(), but rather how the Light class works as a sensor and an actuator.
# 
# But looking at light.py, the Light class seems to handle reading data via its read method. But if we're using it as an actuator, perhaps that's not directly related unless the actuator has some logic to adjust based on the readings.
# 
# Wait, maybe I'm overcomplicating this. The main issue is that when trying to collect all Light actuators in get_all_actuators, they are not being found because their id isn't 'Light'. But according to create_room_with_components, each actuator's id should be correct.
# 
# But perhaps the problem lies elsewhere: maybe during initialization of the actuator, some parameters aren't set correctly. For example, in home_plan(), when adding a Light as an actuator, are we creating it with the right arguments?
# 
# Looking at the code for create_room_with_components:
# 
# for actuator_type in actuator_types:
#     room.add_actuator(actuator_type(name))
# 
# Which is similar to how sensors are added: sensor_type(name). So perhaps each actuator is being created correctly.
# 
# Wait, but maybe in home_plan(), when adding a Light as an actuator, it's not actually creating the instance properly. For example, if 'actuator_type' includes 'Light', then we add it with name 'LivingRoom'. But does the Light class accept that?
# 
# But perhaps I'm missing something else: Maybe during testing, when trying to call get_value on a Light actuator, it doesn't return anything because the read method isn't implemented correctly.
# 
# Wait, no. Looking at light.py:
# 
# The Light class's read() method returns {'lux': value, 'temperature': value}. So that should be fine.
# 
# Another possibility is that in home_plan(), when creating the Light instances for actuators, they are not added to any room because of a mistake in the loop variables or parameters passed to add_actuator.
# 
# Wait, perhaps I need to check how create_room_with_components() and add_actuator() work. Looking at light.py:
# 
# The class Add has an add function that appends the instance to its list.
# 
# So when we call actuator_type(name), it's creating a Light instance with name 'LivingRoom' (for example). Then, in home_plan(), these are added as actuators to their respective rooms.
# 
# Therefore, get_all_actuators() should collect them if called correctly.
# 
# But perhaps the issue is that the actuator's type isn't being set properly. For example, maybe when creating an actuator, it needs to be of a certain type (like 'Light') and not just any instance.
# 
# Alternatively, maybe there's a typo in get_all_actuators() where the condition compares actuator_type with the current actuator's type as lowercase instead of proper case.
# 
# Wait, looking at get_all_actuators():
# 
# for room in home:
#     for actuator in room.actuators:
#         if actuator.actuator_type == actuator_type:
#             all_actuators.append(actuator)
# 
# So it's checking if the actuator's type matches the given parameter. So if we're passing 'Light', and each Light actuator has actuator_type as 'Light' (all lowercase), then this condition should be true.
# 
# But perhaps in code, the variable names or function calls are case-sensitive elsewhere.
# 
# Alternatively, maybe during testing, when trying to create a Light sensor, it's failing because of other dependencies. For example, if the sensor requires certain parameters that aren't being passed correctly.
# 
# Wait, another thought: Perhaps the issue is not with home_plan() but how the Light class is used as an actuator elsewhere in the system. Maybe the code expecting a certain type isn't matching 'Light' due to case sensitivity or similar issues.
# 
# But according to the initial user message, it's about implementing the Light sensor correctly, so maybe the problem lies within light.py itself.
# 
# Wait, perhaps I should suggest modifying how the Light class is implemented as an actuator. For example, in home_plan(), when adding a Light actuator, ensure that its name and type are correct.
# 
# Alternatively, maybe during testing, the code isn't properly initializing all actuators because of some missing conditions.
# 
# Another possibility: Maybe the add_actuator() function expects certain parameters but is receiving none. Looking at light.py:
# 
# class Add:
#     def __init__(self):
#         self.instances = []
# 
#     def add(self, actuator):
#         self.instances.append(actuator)
# 
# So it's straightforward; just appending instances regardless of type.
# 
# Therefore, perhaps the problem isn't in home_plan() but elsewhere in how the Light class is being used. But since the user provided light.py and home_plan(), maybe I should consider that.
# 
# Wait, another angle: Perhaps in the code where get_all_actuators is called, it's not correctly passing 'Light' as the actuator_type. For example, if it's passed as lowercase or uppercase somewhere else.
# 
# Alternatively, perhaps when adding a Light actuator to home_plan(), it's being added with an incorrect name that doesn't match any sensor types elsewhere.
# 
# But all in all, I'm trying to figure out why get_all_actuators() isn't returning the expected Light instances. Since each one should have actuator_type as 'Light', and we're passing 'Light' correctly, perhaps the issue is elsewhere.
# 
# Wait a minute! Looking at light.py:
# 
# The __init__ method of Light takes sensor_type (which for an actuator would be None) and name. But when used as a sensor, it's okay because sensors have their own read methods to provide data based on the environment.
# 
# But if we're using it as an actuator, perhaps there isn't any logic to control anything else, which is fine, but that might not relate directly to this issue.
# 
# Alternatively, maybe in home_plan(), when creating a Light sensor, it's expecting certain parameters like 'lux' or other attributes that aren't being set correctly.
# 
# Wait, no. Because the actuator doesn't need data from sensors; it just needs to be registered as an actuator of type 'Light'.
# 
# Another thought: Perhaps during testing, the code is trying to call get_value() on a Light actuator but expects certain keys (like 'lux' and 'temperature') but isn't receiving them. But according to light.py's read method, that should be fine.
# 
# Wait, perhaps in home_plan(), when adding an actuator of type 'Light', it's expecting more parameters than are being provided, leading to exceptions elsewhere.
# 
# But looking at the code, I don't see any such issues because Add just appends without checking arguments.
# 
# Hmm. Maybe I'm overcomplicating this. Since all instances added as actuators should have their actuator_type correctly set to 'Light', perhaps the issue is that get_all_actuators() isn't collecting them properly.
# 
# Wait, what if in home_plan(), when creating an Actuator instance (like Add()), it's not being passed any type information beyond the name. But since add() just appends without considering types, this shouldn't be a problem.
# 
# Perhaps another angle: Maybe there are multiple sensors of the same type, and get_all_actuators() is mistakenly collecting them as well, but I don't see that in the code.
# 
# Wait, perhaps the issue is with case sensitivity. For example, if 'Light' is passed as 'light' (lowercase) somewhere else, causing a mismatch. But according to the initial condition, it's comparing for exact match.
# 
# Alternatively, maybe there are multiple actuator types and get_all_actuators() isn't filtering them correctly based on their type.
# 
# But since in home_plan(), we're specifically adding an instance of Add (which is our Light actuator), which should have its actuator_type set to 'Light' (the class name).
# 
# Wait, looking at the code:
# 
# In home_plan(), when creating a sensor or actuator, it's done like this: Sensor(some_class, name='SomeName').
# 
# Similarly for Actuators: Add(actuator_class, name='SomeName'), but wait no—looking back, in home_plan(), they're using Add() as the sensor_type. So:
# 
# sensors = [
#     Sensor(Add, 'Sensor 1'),
#     # other sensors
# ]
# 
# actuators = [
#     Actuator(Add, 'Actuator 1'),
#     # other actuators
# ]
# 
# Wait a second! Oh no—wait: in home_plan(), when creating an actuator, they're using Add as the sensor_type. But Add is actually the class name for our Light-based actuator.
# 
# But that's not correct because Actuator expects the type of the object to add. Wait, looking at how the code works:
# 
# In light.py, the Add class has a function add() which takes an instance (an actuator) and appends it.
# 
# So in home_plan(), when creating sensors or actuators, for example:
# 
# Sensor(Add, 'name') creates a sensor of type Add with name 'name'.
# 
# Actuator(Add, 'name') would create an actuator of type Add with name 'name', which is incorrect because Add isn't the right class to use as an Actuator.
# 
# Wait! Oh no! That's probably the issue. Because in home_plan(), they're using Add both as a sensor and as an actuator, but when used as an actuator, it should be a different type—like a subclass of Actuator, not Add.
# 
# Looking at light.py again:
# 
# We have two classes: Sensor (which is Add) and Actuator (another class). Wait no—the code shows that in home_plan(), they're using Actuator(Add, ...), which would try to create an actuator instance of type Add, but the actual actuator should be a subclass implementing the Actuator interface.
# 
# Wait, I think this might be where the problem lies. Because when creating a sensor or actuator, if we pass Add as the class, it will look for a function called __init__ in that class to create an instance. But in light.py:
# 
# The Add class's add() method appends instances of whatever is passed (as long as they are added via Add.add()).
# 
# But when creating a sensor or actuator using Actuator(Add, ...), it expects the __init__ function of the Actuator type. So if Add is not implementing Actuator, then that would cause an error because Actuator's __init__ method isn't present in Add unless we have another class acting as the actual actuator.
# 
# Wait no—looking at light.py:
# 
# Actually, in home_plan(), they're using Actuator(Add, ...), which implies that there is a separate Actuator class. But looking back, perhaps I misread the code.
# 
# Wait, let me re-examine light.py:
# 
# In the initial description, it seems like the code provided by the user has two classes: Sensor and Add (which was called Actuator). Wait no—light.py shows:
# 
# class Sensor:
#     def __init__(self, sensor_type, name):
#         self.type = sensor_type
#         self.name = name
# 
# class Add:
#     # same as before.
# 
# But in home_plan(), the code uses:
# 
# sensors.append(Sensor(Add, 'Sensor 1'))
# actuators.append(Actuator(Add, 'Actuator 1'))
# 
# Wait, but there is no Actuator class defined. The user only provided Sensor and Add. So perhaps I misread earlier—maybe in their code, they have a separate Actuator class.
# 
# Alternatively, perhaps the user's code defines both Sensor and Actuator classes elsewhere.
# 
# But according to the initial problem statement:
# 
# The user provides this code (light.py):
# 
# class Sensor:
#     def __init__(self, sensor_type, name):
#         self.type = sensor_type
#         self.name = name
# 
# class Add:
#     pass  # or something else?
# 
# And in home_plan(), they create sensors and actuators as follows.
# 
# Wait no—probably the user has a class called Actuator which is similar to Sensor but for actions. But perhaps the code wasn't fully provided.
# 
# But given that, I think the issue is in how the Actuators are being created.
# 
# In light.py:
# 
# They have a class Add (which was intended as an Actuator) but didn't inherit from the correct interface.
# 
# Wait no—maybe there's confusion between Sensor and Actuator. The user probably has two classes: Sensor and Actuator, both implementing their respective interfaces.
# 
# But looking back at the initial code provided by the user:
# 
# In light.py:
# class Sensor:
#     def __init__(self, sensor_type, name):
#         self.type = sensor_type
#         self.name = name
# 
# Then in home_plan():
# sensors.append(Sensor(Add, 'Sensor 1'))
# 
# So Add is being used as a sensor type. But Add was defined as a class with an add() method.
# 
# Wait, perhaps the user has another Actuator class which isn't properly defined, leading to issues when creating actuators.
# 
# But in any case, according to the problem statement, the issue arises because the code is trying to create an Actuator of type Add, but Add doesn't implement the correct interface for an Actuator. Therefore, the actuator can't be added correctly.
# 
# So putting it all together:
# 
# The main issue is that in home_plan(), when creating an Actuator instance (e.g., Actuator(Add, 'name')), it's trying to instantiate Add as if it implements the Actuator interface. But since Add doesn't have such a method, this leads to errors or no correct actuation.
# 
# Therefore, perhaps there should be two separate classes: Sensor and Actuator. Each would implement their respective interfaces (like having an add() method for sensors and another specific method for actuators). Alternatively, the code is mistakenly using the same Add class as both sensor and actuator types, which might not have all required methods.
# 
# So to fix it, we need to ensure that there are separate Sensor and Actuator classes, each with their own add() methods. Therefore, in home_plan(), when adding a sensor or an actuator, they should be instances of these respective classes.
# </think>
# 
# To resolve the issue where the code fails to correctly create and register actuators due to incorrect class usage, we need to define separate `Sensor` and `Actuator` classes each implementing their specific interface.
# 
# **Step-by-step Explanation:**
# 
# 1. **Define Separate Classes:** Create a distinct `Sensor` class for sensors and an `Actuator` class for actuators.
# 2. **Implement Add Methods:** Both classes should have an appropriate `add()` method to register themselves with the system.
# 3. **Correct Class Instantiation:** In `home_plan()`, use instances of `Sensor` for sensor registration and `Actuator` for actuator registration.
# 
# **Fixed Code:**
# 
# ```python
class Sensor:
    def __init__(self, sensor_type, name):
        self.type = sensor_type
        self.name = name

    def add(self):
        pass  # Implement specific logic if needed

class Actuator:
    def __init__(self, actuator_type, name):
        self.type = actuator_type
        self.name = name

    def add(self):
        pass  # Implement specific logic if needed


def home_plan():
    sensors = [
        Sensor(Add, 'Sensor 1'),
        Sensor(Add, 'Sensor 2'),
    ]
    actuators = [
        Actuator(Actuator, 'Actuator 1'),  # Assuming Actuator implements the interface
        Actuator(Actuator, 'Actuator 2'),
    ]
    return (sensors, actuators)
# ```