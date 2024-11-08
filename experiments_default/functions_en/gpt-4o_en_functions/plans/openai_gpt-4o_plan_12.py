# Based on the functional descriptions and the provided source code, `function.py` should contain a `main` function that includes the logic for the three plans: Morning Plan, Leave Home Plan, and Movie Plan. This function will interact with the sensors and actuators to execute the required actions for each plan. 
# 
# Here's the `function.py` file:

# function.py
from home.home_plan import home_plan, get_room_actuators, get_all_actuators

def morning_plan(home):
    print("Executing Morning Plan...")

    # Open curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Play music
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        player.turn_on()
        player.play_music("Morning Playlist")

    # Start coffee machine
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")

    # Close doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.turn_off()

    # Turn off lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def movie_plan(home):
    print("Executing Movie Plan...")

    # Close curtains
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()

    # Turn on TV
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        tv.turn_on()
        tv.play_channel("Movie Channel")

def main():
    home = home_plan()

    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()