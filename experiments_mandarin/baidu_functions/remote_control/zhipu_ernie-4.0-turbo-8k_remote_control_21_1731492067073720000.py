# Based on your functional description and the provided source code, here is a `function.py` file that contains the main function to control the smart home devices as per your requirements:

from home.home_plan import home_plan, get_room, get_all_actuators
from home.actuator import Light, MusicPlayer, CoffeeMachine, AC, Curtain, CleaningRobot

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Define the tasks
    tasks = [
        {"action": "turn_on_light", "room": "LivingRoom", "brightness": "medium"},
        {"action": "play_music", "room": "LivingRoom", "playlist": "relaxing songs"},
        {"action": "make_coffee", "room": "Kitchen", "coffee_type": "espresso"},
        {"action": "set_ac_temperature", "room": "LivingRoom", "temperature": 22},
        {"action": "close_curtains", "room": "LivingRoom"},
        {"action": "start_cleaning_robot", "room": "LivingRoom"}
    ]
    
    # Execute tasks
    for task in tasks:
        room_name = task["room"]
        room = get_room(home, room_name)
        if room:
            actuators = get_all_actuators(home, room_name)
            for actuator in actuators:
                if task["action"] == "turn_on_light" and isinstance(actuator, Light):
                    actuator.turn_on()
                    actuator.set_brightness_level(task["brightness"])
                elif task["action"] == "play_music" and isinstance(actuator, MusicPlayer):
                    actuator.turn_on()
                    actuator.play_music(task["playlist"])
                elif task["action"] == "make_coffee" and isinstance(actuator, CoffeeMachine):
                    actuator.turn_on()
                    actuator.make_coffee(task["coffee_type"])
                elif task["action"] == "set_ac_temperature" and isinstance(actuator, AC):
                    actuator.turn_on()
                    actuator.set_target_temperature(task["temperature"])
                elif task["action"] == "close_curtains" and isinstance(actuator, Curtain):
                    actuator.turn_off()  # Assuming closing curtains is turning them off
                elif task["action"] == "start_cleaning_robot" and isinstance(actuator, CleaningRobot):
                    actuator.turn_on()
                    actuator.daily_routine()

if __name__ == "__main__":
    main()