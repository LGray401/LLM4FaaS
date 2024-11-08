# Given the functional description and the source code you've provided, I will create a `function.py` file that defines a main function to execute the morning plan, leave home plan, and movie plan based on the configurations and functionalities provided in the existing code.

# functions/function.py

from home.sensor import get_room_sensors, get_room_actuators
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, Door, Window, SmartSocket
from home_plan import home

def execute_morning_plan():
    # LivingRoom actuators
    curtain = get_room_actuators(home, "LivingRoom")[0]
    light = get_room_actuators(home, "LivingRoom")[1]
    coffee_machine = get_room_actuators(home, "LivingRoom")[7]
    music_player = get_room_actuators(home, "LivingRoom")[8]
    
    # Set curtain to open
    curtain.turn_on()
    
    # Set lights to medium brightness
    light.set_brightness_level("medium")
    
    # Start coffee machine
    coffee_machine.turn_on()
    coffee_machine.make_coffee("espresso")
    
    # Start playing music
    music_player.play_music("morning_playlist")

def execute_leave_home_plan():
    # LivingRoom actuators
    light = get_room_actuators(home, "LivingRoom")[1]
    window = get_room_actuators(home, "LivingRoom")[3]
    sockets = get_room_actuators(home, "LivingRoom")[9:11]  # Assuming two sockets for simplicity
    
    # Turn off lights
    light.turn_off()
    
    # Open window
    window.turn_on()
    
    # Turn off all sockets
    for socket in sockets:
        socket.turn_off()
    
    # Lock the door
    door = get_room_actuators(home, "LivingRoom")[0]
    door.turn_on()  # Assuming the door's 'on' state means locked

def execute_movie_plan():
    # LivingRoom actuators
    window = get_room_actuators(home, "LivingRoom")[3]
    curtain = get_room_actuators(home, "LivingRoom")[0]
    light = get_room_actuators(home, "LivingRoom")[1]
    tv = get_room_actuators(home, "LivingRoom")[11]  # Assuming SmartTV is the last actuator
    
    # Close window
    window.turn_off()
    
    # Close curtain
    curtain.turn_off()
    
    # Dim the lights
    light.set_brightness_level("low")
    
    # Turn on the TV
    tv.play_channel("movie_channel")

def main():
    # Execute the morning plan
    execute_morning_plan()
    
    # Execute the leave home plan
    execute_leave_home_plan()
    
    # Execute the movie plan
    execute_movie_plan()

if __name__ == "__main__":
    main()