# To implement the `function.py` file as per your requirements, the main function should be capable of executing three plans: `MORNING PLAN`, `LEAVE HOME PLAN`, and `MOVIE PLAN`. To achieve this, I'll use the classes and methods defined in your existing code files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) to control the actuators as needed for each plan.
# 
# Below is the code for `function.py`:
# 
# ```python
from home.home_plan import home_plan, get_all_actuators

def morning_plan():
    # 拉开窗帘，音乐播放器开始播放，咖啡机制作咖啡
    home = home_plan()
    
    # Open curtains in all rooms
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()
    
    # Start playing music in the living room
    music_players = get_all_actuators(home, "MusicPlayer")
    for player in music_players:
        if player.room_name == "LivingRoom":
            player.turn_on()
            player.play_music("Morning Playlist")
    
    # Make coffee in the kitchen
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for machine in coffee_machines:
        machine.turn_on()
        machine.make_coffee("Espresso")


def leave_home_plan():
    # 灯和入户门关闭，除冰箱之外的插座断开
    home = home_plan()
    
    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    
    # Close all doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.turn_off()
    
    # Turn off all sockets except the fridge
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        # Assuming fridge is on a specific socket, skip it
        if "Fridge" not in socket.id:
            socket.turn_off()


def movie_plan():
    # 窗帘关闭，灯光调暗，开启电视播放喜爱的节目
    home = home_plan()
    
    # Close curtains in the living room
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        if curtain.room_name == "LivingRoom":
            curtain.turn_off()
    
    # Dim lights in the living room
    lights = get_all_actuators(home, "Light")
    for light in lights:
        if light.room_name == "LivingRoom":
            light.turn_on()
            light.set_brightness_level("low")
    
    # Turn on TV and play a favorite program
    tvs = get_all_actuators(home, "SmartTV")
    for tv in tvs:
        if tv.room_name == "LivingRoom":
            tv.turn_on()
            tv.play_channel("Favorite Movie Channel")


def main():
    # Execute desired plans
    print("Executing Morning Plan...")
    morning_plan()
    
    print("\nExecuting Leave Home Plan...")
    leave_home_plan()
    
    print("\nExecuting Movie Plan...")
    movie_plan()
    

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation
# 
# - **Morning Plan**: 
#   - Opens all curtains using `Curtain` actuators.
#   - Starts playing music in the living room using `MusicPlayer`.
#   - Makes coffee using the `CoffeeMachine` in the kitchen.
# 
# - **Leave Home Plan**:
#   - Turns off all `Light` actuators.
#   - Turns off all `Door` actuators.
#   - Turns off all `SmartSocket` actuators except the one designated for the fridge.
# 
# - **Movie Plan**:
#   - Closes curtains in the living room using `Curtain` actuators.
#   - Dims the lights in the living room to a low brightness using `Light` actuators.
#   - Turns on the `SmartTV` and plays a favorite channel.
# 
# This `function.py` file assumes that all actuators are properly defined in your home configuration and that the logging setup in `logger_config` is functioning correctly to capture the logs of these actions. Adjust the playlist name, coffee type, and TV channel as needed for your specific setup.