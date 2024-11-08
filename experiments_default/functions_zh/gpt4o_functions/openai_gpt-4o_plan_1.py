# Sure, based on your functional description and the provided source code, I will create the `function.py` file to implement the plans for MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. This file will be located in the `functions` folder and contain the main function to execute these plans.
# 
# Here's the content for `function.py`:

from home.home_plan import home_plan, get_room, get_room_actuators

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    
    if living_room:
        actuators = get_room_actuators(home, "LivingRoom")
        for actuator in actuators:
            if actuator.actuator_type == "Curtain" or actuator.actuator_type == "Light" or actuator.actuator_type == "MusicPlayer":
                actuator.turn_on()
                if actuator.actuator_type == "MusicPlayer":
                    actuator.play_music("soothing playlist")
    if kitchen:
        coffee_machine = next((a for a in kitchen.actuators if a.actuator_type == "CoffeeMachine"), None)
        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("coffee")


def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")
    
    if living_room:
        door = next((a for a in living_room.actuators if a.actuator_type == "Door"), None)
        if door:
            door.lock()
        lights = [a for a in living_room.actuators if a.actuator_type == "Light"]
        for light in lights:
            light.turn_off()
    
    if kitchen:
        lights = [a for a in kitchen.actuators if a.actuator_type == "Light"]
        for light in lights:
            light.turn_off()


def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    
    if living_room:
        tv = next((a for a in living_room.actuators if a.actuator_type == "SmartTV"), None)
        if tv:
            tv.turn_on()
            tv.play_channel("movie channel")
        
        curtains = [a for a in living_room.actuators if a.actuator_type == "Curtain"]
        for curtain in curtains:
            curtain.turn_off()
        
        lights = [a for a in living_room.actuators if a.actuator_type == "Light"]
        for light in lights:
            light.turn_on()
            light.set_brightness_level("low")


def main():
    home = home_plan()
    print("Executing Morning Plan...")
    morning_plan(home)
    print("\nExecuting Leave Home Plan...")
    leave_home_plan(home)
    print("\nExecuting Movie Plan...")
    movie_plan(home)


if __name__ == "__main__":
    main()