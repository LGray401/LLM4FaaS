# Sure, here is the 'function.py' file based on the given functional description:

from home.home_plan import *
from home.sensor import *
from home.actuator import *

def main():
    home = home_plan()
    command = input("Enter your command: ")

    if command == "MORNING PLAN":
        morning_plan(home)
    elif command == "LEAVE HOME PLAN":
        leave_home_plan(home)
    elif command == "MOVIE PLAN":
        movie_plan(home)
    else:
        print("Invalid command. Please try again.")

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")

    # Set alarm clock to 7 AM
    alarm_clock = get_all_actuators(living_room, "NotificationSender")[0]
    alarm_clock.notification_sender("Wake up! It's 7 AM!")

    # Open curtains in the bedroom
    bedroom_curtains = get_all_actuators(bedroom, "Curtain")
    for curtain in bedroom_curtains:
        curtain.turn_on()

    # Start coffee machine in the kitchen
    kitchen_coffee_machine = get_all_actuators(get_room(home, "Kitchen"), "CoffeeMachine")[0]
    kitchen_coffee_machine.turn_on()
    kitchen_coffee_machine.make_coffee("cappuccino")

    # Turn on lights if the room is dark
    living_room_light = get_all_actuators(living_room, "Light")[0]
    light_sensor = get_all_sensors(living_room, "LightIntensiveSensor")[0]
    light_reading = light_sensor.get_reading()
    if light_reading < LIGHT_INTENSITY_LOW:
        living_room_light.turn_on()
        living_room_light.set_brightness_level("medium")

def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")
    bathroom = get_room(home, "Bathroom")
    balcony = get_room(home, "Balcony")

    # Lock the door in the living room
    living_room_door = get_all_actuators(living_room, "Door")[0]
    living_room_door.lock()

    # Turn off lights in all rooms
    for room in [living_room, bedroom, kitchen, bathroom, balcony]:
        lights = get_all_actuators(room, "Light")
        for light in lights:
            light.turn_off()

    # Power off all sockets
    for room in [living_room, bedroom, kitchen, bathroom, balcony]:
        sockets = get_all_actuators(room, "SmartSocket")
        for socket in sockets:
            socket.turn_off()

def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")

    # Close curtains in the living room and bedroom
    living_room_curtains = get_all_actuators(living_room, "Curtain")
    bedroom_curtains = get_all_actuators(bedroom, "Curtain")
    for curtain in living_room_curtains + bedroom_curtains:
        curtain.turn_off()

    # Dim the lights in the living room and set the brightness level to low
    living_room_lights = get_all_actuators(living_room, "Light")
    for light in living_room_lights:
        light.turn_on()
        light.set_brightness_level("low")

    # Turn on the TV and play a movie
    living_room_tv = get_all_actuators(living_room, "SmartTV")[0]
    living_room_tv.turn_on()
    living_room_tv.play_channel("Movie Channel")

main()