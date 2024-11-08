# Here is the `function.py` file that you requested:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def morning_plan():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")

    # Open curtains in the living room
    curtains = get_room_actuators(home, "LivingRoom")[4]
    curtains.turn_on()
    logger.info("Curtains in the living room are opened.")

    # Start playing music in the living room
    music_player = get_room_actuators(home, "LivingRoom")[6]
    music_player.play_music("morning playlist")
    logger.info("Music player in the living room starts playing the morning playlist.")

    # Start the coffee machine in the kitchen
    coffee_machine = get_room_actuators(home, "Kitchen")[3]
    coffee_machine.make_coffee("espresso")
    logger.info("Coffee machine in the kitchen starts making espresso.")

def leave_home_plan():
    home = home_plan()

    # Turn off lights and close door in all rooms
    for room in home:
        lights = get_room_actuators(home, room.name)
        for light in lights:
            light.turn_off()
        door = get_room_actuators(home, room.name)[3]
        door.close()
    
    # Disconnect all sockets except for the refrigerator
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        if socket.room_name != "Kitchen" or socket.room_name != "LivingRoom":
            socket.disconnect()

def movie_plan():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")

    # Close curtains in the living room
    curtains = get_room_actuators(home, "LivingRoom")[4]
    curtains.turn_off()
    logger.info("Curtains in the living room are closed.")

    # Dim lights in the living room
    lights = get_room_actuators(home, "LivingRoom")[1:3]
    for light in lights:
        light.set_brightness_level("low")
    logger.info("Lights in the living room are dimmed.")

    # Turn on the TV in the living room
    tv = get_room_actuators(home, "LivingRoom")[9]
    tv.play_channel("favorite show")
    logger.info("TV in the living room starts playing the favorite show.")

def main():
    print_home_plan(home_plan())

    print("\nMorning Plan:")
    morning_plan()

    print("\nLeave Home Plan:")
    leave_home_plan()

    print("\nMovie Plan:")
    movie_plan()

if __name__ == "__main__":
    main()