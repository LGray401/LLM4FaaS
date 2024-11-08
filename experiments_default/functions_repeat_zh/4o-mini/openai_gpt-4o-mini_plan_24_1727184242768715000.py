# Based on your functional description and the provided code files, here's the `function.py` file that implements the morning, leave home, and movie plans for your smart home project.
# 
# ### File: `functions/function.py`

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door

def morning_plan(home):
    print("Executing Morning Plan...")
    
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    
    # Open curtains in the bedroom and living room
    for room in [living_room, bedroom]:
        for actuator in room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_on()  # Open curtains

    # Check weather and adjust lights accordingly
    light_sensor = get_room_sensors(home, "LivingRoom")[0]  # Assuming LightIntensiveSensor is first
    light_reading = light_sensor.get_reading()
    
    if light_reading < 500:  # Assuming 500 lux is the threshold for cloudy
        light = get_room_actuators(home, "LivingRoom")[0]  # Assuming Light is first
        light.turn_on()  # Turn on lights

    # Make coffee
    coffee_machine = get_room_actuators(home, "Kitchen")[3]  # Assuming CoffeeMachine is the 4th actuator
    coffee_machine.turn_on()  # Turn on coffee machine
    coffee_machine.make_coffee("Espresso")
    
    # Play music after coffee is done (just a simulated action here)
    music_player = get_room_actuators(home, "LivingRoom")[5]  # Assuming MusicPlayer is the 6th actuator
    music_player.turn_on()  # Turn on music player
    music_player.play_music("Morning Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    
    living_room = get_room(home, "LivingRoom")
    
    # Open curtains in the living room
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()  # Open curtains

    # Check weather and adjust lights accordingly
    light_sensor = get_room_sensors(home, "LivingRoom")[0]  # Assuming LightIntensiveSensor is first
    light_reading = light_sensor.get_reading()
    
    if light_reading >= 500:  # Assuming 500 lux is the threshold for sunny
        light = get_room_actuators(home, "LivingRoom")[0]  # Assuming Light is first
        light.turn_off()  # Turn off lights

    # Turn off socket devices
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

    # Lock the door
    door = get_room_actuators(home, "LivingRoom")[0]  # Assuming Door is the first actuator
    door.lock()

def movie_plan(home):
    print("Executing Movie Plan...")
    
    living_room = get_room(home, "LivingRoom")
    
    # Close curtains
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()  # Close curtains

    # Turn off lights
    light = get_room_actuators(home, "LivingRoom")[0]  # Assuming Light is first
    light.turn_off()  # Turn off lights

def main():
    home = home_plan()
    
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()