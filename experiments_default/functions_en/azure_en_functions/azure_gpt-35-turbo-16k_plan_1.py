# Sure! Here is the 'function.py' file based on your functional description and the given source code:

from home.home_plan import get_room_actuators, get_room_sensors

def morning_plan():
    # Get the actuators and sensors for the living room
    room_name = "LivingRoom"
    actuators = get_room_actuators(home, room_name)
    sensors = get_room_sensors(home, room_name)

    # Open the curtains
    for actuator in actuators:
        if actuator.actuator_type == "Curtain":
            actuator.turn_on()
    
    # Turn on the lights
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_on()
    
    # Play soothing music
    for actuator in actuators:
        if actuator.actuator_type == "MusicPlayer":
            actuator.play_music("soothing")
    
    # Make coffee
    for actuator in actuators:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.make_coffee("coffee")

def leave_home_plan():
    # Get the actuators for the living room
    room_name = "LivingRoom"
    actuators = get_room_actuators(home, room_name)

    # Close the door
    for actuator in actuators:
        if actuator.actuator_type == "Door":
            actuator.turn_off()
    
    # Turn off the lights
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            actuator.turn_off()

def movie_plan():
    # Get the actuators and sensors for the living room
    room_name = "LivingRoom"
    actuators = get_room_actuators(home, room_name)
    sensors = get_room_sensors(home, room_name)

    # Turn on the TV
    for actuator in actuators:
        if actuator.actuator_type == "SmartTV":
            actuator.turn_on()
    
    # Close the curtains
    for actuator in actuators:
        if actuator.actuator_type == "Curtain":
            actuator.turn_on()
    
    # Dim the lights
    for actuator in actuators:
        if actuator.actuator_type == "Light":
            actuator.set_brightness_level("low")