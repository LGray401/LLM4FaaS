# Based on your functional description and provided source code, here is a `function.py` file that contains a `main` function to execute the smart home plans based on the time of day.

import time
from datetime import datetime
from home_plan import home_plan
from sensor import Sensor
from actuator import Actuator
from config import DAILY_ROUTINE_DURATION

def main():
    home = home_plan()
    
    while True:
        current_time = datetime.now().strftime('%H:%M')
        logger.info(f"Current time is {current_time}")

        if current_time == "07:00":
            # Morning plan
            wake_up(home)
        elif current_time >= "07:30" and current_time < "18:00":
            # Leave home plan
            leave_home(home)
        elif current_time >= "18:00":
            # Evening plan (could be extended to more specific times)
            evening_plan(home)
        time.sleep(60)  # Check every minute

def wake_up(home):
    # Call me up at 7:00
    notification_sender = get_all_actuators(home, "NotificationSender")[0]
    notification_sender.notification_sender("Wake up! It's 7 AM.")

    # Start music at 7:05
    music_player = get_all_actuators(home, "MusicPlayer")[0]
    music_player.play_music("Jay Chou Playlist")

    # Make coffee at 7:20
    coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]
    coffee_machine.make_coffee("Espresso")

def leave_home(home):
    # Lock the door after 7:30
    door = get_all_actuators(home, "Door")[0]
    door.lock()

    # Close curtains
    curtain = get_all_actuators(home, "Curtain")[0]
    curtain.turn_on()

    # Dim the lights
    light = get_all_actuators(home, "Light")[0]
    light.set_brightness_level("low")

def evening_plan(home):
    # Turn off the lights and music
    music_player = get_all_actuators(home, "MusicPlayer")[0]
    music_player.turn_off()

    light = get_all_actuators(home, "Light")[0]
    light.turn_off()

    # Start the cleaning robot
    cleaning_robot = get_all_actuators(home, "CleaningRobot")[0]
    cleaning_robot.daily_routine()

def get_all_actuators(home, actuator_type):
    all_actuators = []
    for room in home:
        for actuator in room.actuators:
            if actuator.actuator_type == actuator_type:
                all_actuators.append(actuator)
    return all_actuators

if __name__ == "__main__":
    main()