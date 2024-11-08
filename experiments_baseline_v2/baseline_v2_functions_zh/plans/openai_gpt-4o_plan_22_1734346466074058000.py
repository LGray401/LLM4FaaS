# To implement the functional description for the smart home application, we'll create a Python script that uses the existing classes from your source code files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`). The script will execute the specified plans: `MORNING PLAN`, `LEAVE HOME PLAN`, and `MOVIE PLAN`.
# 
# Below is the implementation of a new script, `smart_home.py`, which will use the classes and functions from your existing code to perform the actions described in the functional description.
# 
# ### `smart_home.py`
# ```python
from home.home_plan import home_plan, get_all_actuators

def morning_plan(home):
    print("\nExecuting Morning Plan...")
    # 打开卧室灯，打开窗帘，设置早六点音乐播放器，开启咖啡机制作咖啡
    bedroom_lights = get_all_actuators(home, "Light")
    bedroom_curtains = get_all_actuators(home, "Curtain")
    bedroom_music_players = get_all_actuators(home, "MusicPlayer")
    coffee_machines = get_all_actuators(home, "CoffeeMachine")

    # Open bedroom lights
    for light in bedroom_lights:
        if light.room_name == "Bedroom":
            light.turn_on()

    # Open bedroom curtains
    for curtain in bedroom_curtains:
        if curtain.room_name == "Bedroom":
            curtain.turn_on()
    
    # Set music player
    for player in bedroom_music_players:
        if player.room_name == "Bedroom":
            player.turn_on()
            player.play_music("Morning Playlist")

    # Start coffee machine
    for coffee_machine in coffee_machines:
        if coffee_machine.room_name == "Kitchen":
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

def leave_home_plan(home):
    print("\nExecuting Leave Home Plan...")
    # 关闭家中所有灯，入户门上锁，插座关闭
    all_lights = get_all_actuators(home, "Light")
    all_doors = get_all_actuators(home, "Door")
    all_sockets = get_all_actuators(home, "SmartSocket")

    # Turn off all lights
    for light in all_lights:
        light.turn_off()

    # Lock all doors
    for door in all_doors:
        door.lock()

    # Turn off all sockets
    for socket in all_sockets:
        socket.turn_off()

def movie_plan(home):
    print("\nExecuting Movie Plan...")
    # 拉上窗帘，调暗灯光，打开电视播放设置节目
    livingroom_curtains = get_all_actuators(home, "Curtain")
    livingroom_lights = get_all_actuators(home, "Light")
    livingroom_tv = get_all_actuators(home, "SmartTV")

    # Close curtains
    for curtain in livingroom_curtains:
        if curtain.room_name == "LivingRoom":
            curtain.turn_off()

    # Dim lights
    for light in livingroom_lights:
        if light.room_name == "LivingRoom":
            light.turn_on()
            light.set_brightness_level("low")

    # Turn on the TV
    for tv in livingroom_tv:
        if tv.room_name == "LivingRoom":
            tv.turn_on()
            tv.play_channel("Movie Channel")

def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Script
# To execute this script in a Linux terminal, you need to ensure that the `smart_home.py` file is in the same directory or properly referenced with the `home` module. You can run the script using the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Notes
# - Ensure that the `home` directory containing `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` is in the same directory as `smart_home.py` or is included in your Python path.
# - The script assumes that each of the described actions (e.g., turning on lights or making coffee) is adequately handled by the respective class methods.
# - You may need to update the logger and any other dependencies if they are not defined in the provided code snippets.