# Sure! Please find below the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import home_plan, get_room_actuators, get_all_actuators
from home.actuator import NotificationSender

def morning_plan():
    home = home_plan()
    room_names = ["LivingRoom", "Bedroom", "Kitchen"]
    for room_name in room_names:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if actuator.actuator_type == "Curtain":
                actuator.turn_on()
            elif actuator.actuator_type == "MusicPlayer":
                actuator.play_music("playlist")
            elif actuator.actuator_type == "CoffeeMachine":
                actuator.make_coffee("coffee_type")

def leave_home_plan():
    home = home_plan()
    room_names = ["LivingRoom", "Bedroom", "Kitchen"]
    for room_name in room_names:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if actuator.actuator_type == "Door":
                actuator.close()

def movie_plan():
    home = home_plan()
    room_names = ["LivingRoom"]
    for room_name in room_names:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if actuator.actuator_type == "Curtain":
                actuator.turn_off()
            elif actuator.actuator_type == "SmartTV":
                actuator.play_channel("movie_channel")

def send_notification(message):
    home = home_plan()
    actuators = get_all_actuators(home, "NotificationSender")
    for actuator in actuators:
        if actuator.actuator_type == "NotificationSender":
            actuator.notification_sender(message)


def main():
    # morning_plan()
    # send_notification("Good morning!")
    leave_home_plan()
    # movie_plan()

if __name__ == "__main__":
    main()