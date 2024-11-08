# Sure! Here's the code for the 'function.py' file:

from home.sensor import LightIntensiveSensor
from home.actuator import Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def close_living_room_light():
    # Get the home plan
    home = home_plan()
    
    # Get the sensors and actuators in the LivingRoom
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Find the LightIntensiveSensor in the LivingRoom
    light_sensor = None
    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_sensor = sensor
            break
    
    # Find the Light actuator in the LivingRoom
    light_actuator = None
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            light_actuator = actuator
            break
    
    # Turning off the light
    light_actuator.turn_off()
    
# Call the function to close the living room light
close_living_room_light()