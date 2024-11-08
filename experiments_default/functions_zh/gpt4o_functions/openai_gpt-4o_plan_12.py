# Here's your `function.py` file based on the provided functional description and source code:

from home.home_plan import home_plan, get_all_actuators

def execute_morning_plan(home):
    print("Executing Morning Plan...")
    curtains = get_all_actuators(home, "Curtain")
    music_players = get_all_actuators(home, "MusicPlayer")
    coffee_machines = get_all_actuators(home, "CoffeeMachine")

    for curtain in curtains:
        curtain.turn_on()

    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Morning Playlist")

    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

def execute_leave_home_plan(home):
    print("Executing Leave Home Plan...")
    doors = get_all_actuators(home, "Door")
    lights = get_all_actuators(home, "Light")
    
    for door in doors:
        door.turn_off()
        door.lock()

    for light in lights:
        light.turn_off()

def execute_movie_plan(home):
    print("Executing Movie Plan...")
    curtains = get_all_actuators(home, "Curtain")
    tvs = get_all_actuators(home, "SmartTV")

    for curtain in curtains:
        curtain.turn_off()

    for tv in tvs:
        tv.turn_on()
        tv.play_channel("Movie Channel")

def main():
    home = home_plan()

    # Execute different plans
    execute_morning_plan(home)
    execute_leave_home_plan(home)
    execute_movie_plan(home)

if __name__ == "__main__":
    main()