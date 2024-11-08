# To create the `function.py` file for your smart home project, we'll implement the main function that orchestrates the "Morning Plan", "Leave Home Plan", and "Movie Plan" based on the functional description you provided. This function will utilize the classes and methods from your existing code files: `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 
# Here's how the `function.py` file may look:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Light, Door, SmartSocket, SmartTV

def morning_plan(home):
    # 拉开窗帘，音乐播放器开始播放，咖啡机制作咖啡
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    kitchen_actuators = get_room_actuators(home, "Kitchen")

    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
        elif isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("morning_playlist")

    for actuator in kitchen_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("espresso")

def leave_home_plan(home):
    # 灯和入户门关闭，除冰箱之外的插座断开
    for room in home:
        actuators = get_room_actuators(home, room.name)
        for actuator in actuators:
            if isinstance(actuator, Light) or isinstance(actuator, Door):
                actuator.turn_off()
            elif isinstance(actuator, SmartSocket):
                if not ('Refrigerator' in actuator.id):  # Assuming refrigerator sockets are named distinctly
                    actuator.turn_off()

def movie_plan(home):
    # 窗帘关闭，灯光调暗，开启电视播放喜爱的节目
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
        elif isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
        elif isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("favorite_show")

def main():
    home = home_plan()
    print("Executing Morning Plan")
    morning_plan(home)
    
    print("Executing Leave Home Plan")
    leave_home_plan(home)
    
    print("Executing Movie Plan")
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Morning Plan**: Turn on the curtain and music player in the living room, and make coffee using the coffee machine in the kitchen.
# - **Leave Home Plan**: Turn off all lights and doors in every room, and also turn off all smart sockets except those that are presumed to be for refrigerators.
# - **Movie Plan**: Close curtains, set lights to a low brightness, and turn on the TV to play a favorite show in the living room.
# 
# This script assumes that each actuator type has a clear action like `turn_on`, `turn_off`, `play_music`, etc., and that the home plan is correctly set up with the appropriate rooms and devices.
# 
# Make sure that the `function.py` file is located in the `functions` folder and that it can access the `home` package appropriately. Adjust any import paths if necessary based on your project's folder structure.