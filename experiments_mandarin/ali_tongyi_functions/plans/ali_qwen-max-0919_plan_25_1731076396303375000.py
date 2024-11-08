# Based on the provided functional description and source code, I will create a `function.py` file that includes the main function to handle the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. This file will be placed in the `functions` folder.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, Door, SmartSocket, SmartTV
from home.config import LIGHT_INTENSITY_HIGH

def execute_morning_plan(home):
    """
    When the light intensity sensor detects a certain level of light, 
    open the curtains, turn off the bedroom lights, play music, and start the coffee machine.
    """
    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Check if the light intensity is high enough
        for sensor in sensors:
            if isinstance(sensor, LightIntensiveSensor):
                sensor.turn_on()
                if sensor.get_reading() >= LIGHT_INTENSITY_HIGH:
                    print(f"Light intensity in {room.name} is high. Executing morning plan.")
                    for actuator in actuators:
                        if isinstance(actuator, Curtain):
                            actuator.turn_on()
                            print(f"Curtain in {room.name} opened.")
                        elif isinstance(actuator, Light):
                            actuator.turn_off()
                            print(f"Light in {room.name} turned off.")
                        elif isinstance(actuator, MusicPlayer):
                            actuator.turn_on()
                            actuator.play_music("Morning Playlist")
                            print(f"Music player in {room.name} playing 'Morning Playlist'.")
                        elif isinstance(actuator, CoffeeMachine):
                            actuator.turn_on()
                            actuator.make_coffee("Espresso")
                            print(f"Coffee machine in {room.name} making Espresso.")
                    break  # Exit the loop after executing the plan

def execute_leave_home_plan(home):
    """
    When the command to lock the entrance door is given, 
    close the curtains, turn off all indoor lights, and cut off power to all smart sockets.
    """
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            if isinstance(actuator, Door):
                actuator.lock()
                print(f"Door in {room.name} locked.")
                for other_actuator in actuators:
                    if isinstance(other_actuator, Curtain):
                        other_actuator.turn_off()
                        print(f"Curtain in {room.name} closed.")
                    elif isinstance(other_actuator, Light):
                        other_actuator.turn_off()
                        print(f"Light in {room.name} turned off.")
                    elif isinstance(other_actuator, SmartSocket):
                        other_actuator.turn_off()
                        print(f"Smart socket in {room.name} turned off.")
                break  # Exit the loop after executing the plan

def execute_movie_plan(home):
    """
    When the command to turn on the TV is given, 
    close the curtains and dim the indoor lights.
    """
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            if isinstance(actuator, SmartTV):
                actuator.turn_on()
                actuator.play_channel("Movie Channel")
                print(f"Smart TV in {room.name} playing 'Movie Channel'.")
                for other_actuator in actuators:
                    if isinstance(other_actuator, Curtain):
                        other_actuator.turn_off()
                        print(f"Curtain in {room.name} closed.")
                    elif isinstance(other_actuator, Light):
                        other_actuator.set_brightness_level("low")
                        print(f"Light in {room.name} set to low brightness.")
                break  # Exit the loop after executing the plan

def main():
    home = home_plan()
    print("Home plan created. Executing plans...")

    # Execute Morning Plan
    execute_morning_plan(home)

    # Execute Leave Home Plan
    execute_leave_home_plan(home)

    # Execute Movie Plan
    execute_movie_plan(home)

if __name__ == "__main__":
    main()