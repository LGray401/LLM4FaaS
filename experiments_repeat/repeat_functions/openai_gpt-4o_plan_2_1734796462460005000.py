# To implement the desired functionality for your smart home project, we need to create a `function.py` file that defines the main functions corresponding to each of the plans: Morning Plan, Leave Home Plan, and Movie Plan. These functions will utilize the components defined in your existing code, such as sensors and actuators, to perform the required actions.
# 
# Here is the `function.py` file located in the `functions` folder:
# 
# ```python
from home.home_plan import home_plan, get_room_actuators, get_all_actuators
from home.actuator import Curtain, MusicPlayer, CoffeeMachine, Light, Door, SmartSocket, SmartTV

def morning_plan(home):
    # 拉开窗帘，音乐播放器开始播放，咖啡机制作咖啡
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    kitchen_actuators = get_room_actuators(home, "Kitchen")
    
    # Open curtains in all rooms
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Start playing music in the living room
    for actuator in living_room_actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")
    
    # Make coffee in the kitchen
    for actuator in kitchen_actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")

def leave_home_plan(home):
    # 灯和入户门关闭，除冰箱之外的插座断开
    all_lights = get_all_actuators(home, "Light")
    all_doors = get_all_actuators(home, "Door")
    all_sockets = get_all_actuators(home, "SmartSocket")
    
    # Turn off all lights
    for light in all_lights:
        light.turn_off()
    
    # Lock all doors
    for door in all_doors:
        door.lock()
    
    # Turn off all sockets except fridge (assuming fridge is on a specific socket)
    for socket in all_sockets:
        if "Fridge" not in socket.id:  # Assuming fridge has "Fridge" in its ID
            socket.turn_off()

def movie_plan(home):
    # 窗帘关闭，灯光调暗，开启电视播放喜爱的节目
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Close curtains
    for actuator in living_room_actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()
    
    # Dim lights
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("low")
    
    # Turn on TV and play favorite channel
    for actuator in living_room_actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Favorite Movie Channel")

def main():
    home = home_plan()
    print("Executing Morning Plan...")
    morning_plan(home)
    print("Executing Leave Home Plan...")
    leave_home_plan(home)
    print("Executing Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# - **morning_plan**: This function opens curtains, starts music, and makes coffee. It locates the `Curtain`, `MusicPlayer`, and `CoffeeMachine` actuators and performs the necessary actions.
# 
# - **leave_home_plan**: This function turns off all lights, locks all doors, and turns off all sockets except the one for the fridge. It assumes that the fridge socket has "Fridge" in its ID.
# 
# - **movie_plan**: This function closes curtains, dims lights to a low level, and starts playing the favorite channel on the TV.
# 
# - **main**: This function initializes the home plan and executes each of the plans in sequence.
# 
# This setup allows you to manage your smart home environment using predefined plans, leveraging the components and functionality defined in your existing codebase.