# Here is the `function.py` file based on the provided functional description and given source code:

from home.home_plan import home_plan, get_room, get_all_actuators, get_all_sensors

def morning_plan(home):
    print("Executing Morning Plan...")
    curtain = get_all_actuators(home, "Curtain")[0]
    curtain.turn_on()

    outdoor_light_sensor = get_all_sensors(home, "LightIntensive")[0]
    outdoor_light_sensor.turn_on()
    if outdoor_light_sensor.get_reading() < 900:
        light = get_all_actuators(home, "Light")[0]
        light.turn_on()

    coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")
    
    music_player = get_all_actuators(home, "MusicPlayer")[0]
    music_player.turn_on()
    music_player.play_music("Morning Playlist")

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    curtain = get_all_actuators(home, "Curtain")[0]
    curtain.turn_on()

    outdoor_light_sensor = get_all_sensors(home, "LightIntensive")[0]
    outdoor_light_sensor.turn_on()
    if outdoor_light_sensor.get_reading() >= 900:
        curtain.turn_on()

    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()

    door = get_all_actuators(home, "Door")[0]
    door.lock()

def movie_plan(home):
    print("Executing Movie Plan...")
    curtain = get_all_actuators(home, "Curtain")[0]
    curtain.turn_off()

    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()