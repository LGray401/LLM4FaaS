# <think>
# Okay, I'm trying to figure out how the user is using their code and what they might need help with. They provided several Python files: preparation.py, config.py, home_plan.py, and some logger stuff.
# 
# Looking at their code, it seems like they're setting up a smart home system. The Room class in home_plan.py has sensors and actuators added to it. Then there are functions to create rooms with various components. In the main block, they generate a list of rooms using these components.
# 
# In the get_all_actuators function, they have an if statement that checks actuator.actuator_type == actuator_type. Wait, that can't be right because actuators don't have a type attribute as per their classes. For example, the Light class probably doesn't have an 'actuator_type' attribute.
# 
# So I think there's a mistake in how they're filtering the actuators. They might have intended to check if each actuator is of a certain subclass or has specific attributes that define their type. Maybe they should be checking for the actual classes instead of comparing some generic 'type'.
# 
# I should suggest changing the condition to use isinstance and check against the desired actuator types like Door, Light, etc. That way, it correctly identifies which actuators belong to each category.
# 
# Also, looking at the example code in home_plan(), they have a list comprehension that creates various room components with specific names. They might not be using these parameters correctly when instantiating sensors and actuators. It's better to use callable objects by calling them with (name), like LightIntensiveSensor(name) instead of name().
# 
# So, I'll outline the steps: first fix the actuator type check in get_all_actuators, then correct how sensor and actuator instances are created when adding components.
# </think>
# 
# Based on the code provided, it seems you're working on a smart home system with room configuration. However, there's a bug in your `get_all_actuators` function that needs to be fixed.
# 
# Looking at this line:
# ```python
for actuator in room.actuators:
    if actuator.actuator_type == actuator_type:
# ```
# 
# This will throw an error because the `actuator` objects don't have an `actuator_type` attribute. Instead, you should check against the actual type or class of the actuator.
# 
# Here's how to fix it:
# 
# ```python
def get_room_actuators(home, room_name):
    for room in home:
        if room.name == room_name:
            # Use isinstance and compare against known actuator types
            target_actuators = [
                Door, 
                Light,
                ...
            ]
            return [actuator for actuator in room.actuators if isinstance(actuator, target_actuator)]

    print(f"there is no Actuator found in {room_name}")
    logger.warning(f"there is no Actuator found in {room_name}")
    return None
# ```
# 
# For your `home_plan()` example, you were using the components incorrectly. Here's how to fix that:
# 
# ```python
def home_plan():
    rooms = [
        create_room_with_components("LivingRoom", [LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor],
                                    [Door, Light, Window, Window, Curtain, MusicPlayer, SmartSocket, SmartSocket,
                                     CleaningRobot, SmartTV, NotificationSender, AC, Heater]),
        ...
    ]
    return rooms
# ```
# 
# Key changes made:
# 1. Corrected the sensor and actuator instantiation method by using callable objects (sensor_type(name) instead of name())
# 2. Fixed the `get_room_actuators` function to properly filter actuators based on their actual class types
# 
# Let me know if you need help with anything else!