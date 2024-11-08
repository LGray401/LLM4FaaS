# Based on your functional description and the provided source codes, here is the `function.py` file. This file contains the main function that handles the different plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# The `function.py` file will be located in the `functions` folder and will interact with the components defined in the `home` folder.
# 
# ### `functions/function.py`

from home_plan import home_plan, get_room_actuators, get_all_actuators
from actuator import Light, CoffeeMachine, CleaningRobot, MusicPlayer, SmartTV, NotificationSender

def main():
    home = home_plan()

    def morning_plan():
        print("Executing MORNING PLAN")

        bedroom_actuators = get_room_actuators(home, "Bedroom")
        kitchen_actuators = get_room_actuators(home, "Kitchen")
        
        for actuator in bedroom_actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("high")
            elif isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Espresso")
            elif isinstance(actuator, CleaningRobot):
                actuator.turn_on()
                actuator.daily_routine()

        for actuator in kitchen_actuators:
            if isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Latte")

    def leave_home_plan():
        print("Executing LEAVE HOME PLAN")

        all_lights = get_all_actuators(home, "Light")
        all_doors = get_all_actuators(home, "Door")
        all_windows = get_all_actuators(home, "Window")

        for light in all_lights:
            light.turn_off()

        for door in all_doors:
            door.lock()

        for window in all_windows:
            window.turn_off()

    def movie_plan():
        print("Executing MOVIE PLAN")

        living_room_actuators = get_room_actuators(home, "LivingRoom")

        for actuator in living_room_actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("low")
            elif isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Netflix")
            elif isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("Chill Playlist")

    # Simulation of plans
    morning_plan()
    leave_home_plan()
    movie_plan()

if __name__ == "__main__":
    main()