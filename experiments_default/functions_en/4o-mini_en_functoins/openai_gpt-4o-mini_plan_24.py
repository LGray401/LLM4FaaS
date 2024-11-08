# Here’s the `function.py` file based on your functional description for the smart home project. This file includes the main function that implements the morning plan, leave home plan, and movie plan as described.

# function.py
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    
    # Open curtains
    for actuator in get_room_actuators(home, "Curtain"):
        if isinstance(actuator, Curtain):
            actuator.turn_on()  # Open Curtain
    
    # Check if it's cloudy to turn on lights
    light_sensor = get_room_sensors(home, "LivingRoom")
    if light_sensor:  # Assuming there's a light intensity sensor
        light_intensity_sensor = light_sensor[0]  # Using the first light sensor
        reading = light_intensity_sensor.get_reading()
        if reading and reading < 900:  # If light intensity is low (cloudy)
            for actuator in get_room_actuators(home, "Light"):
                if isinstance(actuator, Light):
                    actuator.turn_on()  # Turn on lights
    
    # Make coffee
    coffee_machine = get_room_actuators(home, "CoffeeMachine")[0]
    if isinstance(coffee_machine, CoffeeMachine):
        coffee_machine.turn_on()  # Turn on coffee machine
        coffee_machine.make_coffee("Espresso")  # Example coffee type
        music_player = get_room_actuators(home, "MusicPlayer")[0]
        if isinstance(music_player, MusicPlayer):
            music_player.turn_on()  # Turn on music player
            music_player.play_music("Morning Playlist")  # Play music when coffee is ready

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room(home, "LivingRoom")
    
    # Check if it's sunny (using outdoor sensor)
    outdoor_sensor = get_room_sensors(home, "Balcony")
    if outdoor_sensor:
        outdoor_temp_sensor = outdoor_sensor[0]  # Assuming it's the first outdoor temperature sensor
        reading = outdoor_temp_sensor.get_reading()
        if reading and reading >= 20:  # Assuming sunny if temperature is 20 or above
            # Open the curtains
            for actuator in get_room_actuators(home, "Curtain"):
                if isinstance(actuator, Curtain):
                    actuator.turn_on()  # Open curtains
            # Turn off lights and sockets
            for actuator in get_room_actuators(home, "Light"):
                if isinstance(actuator, Light):
                    actuator.turn_off()  # Turn off lights
            # Lock the door
            door = get_room_actuators(home, "Door")[0]
            if isinstance(door, Door):
                door.lock()  # Lock the door

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")
    
    # Close curtains
    for actuator in get_room_actuators(home, "Curtain"):
        if isinstance(actuator, Curtain):
            actuator.turn_off()  # Close curtains
    
    # Turn off lights
    for actuator in get_room_actuators(home, "Light"):
        if isinstance(actuator, Light):
            actuator.turn_off()  # Turn off lights

def main():
    home = home_plan()  # Initialize the home plan
    morning_plan(home)  # Execute morning plan
    leave_home_plan(home)  # Execute leave home plan
    movie_plan(home)  # Execute movie plan

if __name__ == "__main__":
    main()