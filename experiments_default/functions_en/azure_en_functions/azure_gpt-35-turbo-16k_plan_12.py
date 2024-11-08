# Sure! Here is the 'function.py' file based on the functional description and the provided source code:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors

def morning_plan():
    home = home_plan()
    
    # Open curtains
    living_room_curtains = get_room_actuators(home, "LivingRoom")
    for curtain in living_room_curtains:
        curtain.turn_on()
    
    # Play music
    living_room_music_player = get_room_actuators(home, "LivingRoom")
    for music_player in living_room_music_player:
        music_player.play_music("morning playlist")
    
    # Turn on coffee machine
    kitchen_coffee_machine = get_room_actuators(home, "Kitchen")
    for coffee_machine in kitchen_coffee_machine:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("black coffee")

def leave_home_plan():
    home = home_plan()
    
    # Close door
    living_room_door = get_room_actuators(home, "LivingRoom")
    for door in living_room_door:
        door.turn_on()
        door.lock()
    
    # Turn off lights
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        light.turn_off()

def movie_plan():
    home = home_plan()
    
    # Close curtains
    living_room_curtains = get_room_actuators(home, "LivingRoom")
    for curtain in living_room_curtains:
        curtain.turn_on()
    
    # Turn on TV
    living_room_tv = get_room_actuators(home, "LivingRoom")
    for tv in living_room_tv:
        tv.turn_on()
        tv.play_channel("movie channel")

def main():
    # Run the morning plan
    print("Running the Morning Plan:")
    morning_plan()
    
    # Run the leave home plan
    print("\nRunning the Leave Home Plan:")
    leave_home_plan()
    
    # Run the movie plan
    print("\nRunning the Movie Plan:")
    movie_plan()

if __name__ == "__main__":
    main()