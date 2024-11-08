from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_actuators, \
    get_all_sensors
from home.actuator import Light, MusicPlayer, Window, Heater, AC


def main():
    home = home_plan()

    # 调亮客厅的灯
    living_room = get_room(home, "LivingRoom")
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("high")

    # 调暗卧室的灯
    bedroom = get_room(home, "Bedroom")
    bedroom_lights = get_room_actuators(home, "Bedroom")
    for light in bedroom_lights:
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("low")

    # 打开厨房窗户
    kitchen = get_room(home, "Kitchen")
    kitchen_windows = get_room_actuators(home, "Kitchen")
    for window in kitchen_windows:
        if window.actuator_type == "Window":
            window.turn_on()

    # 让客厅的音乐播放器播放歌曲
    living_room_music_players = get_room_actuators(home, "LivingRoom")
    for music_player in living_room_music_players:
        if music_player.actuator_type == "MusicPlayer":
            music_player.turn_on()
            music_player.play_music("Pop")

    # Example of controlling temperature
    # Get all heaters
    all_heaters = get_all_actuators(home, "Heater")
    for heater in all_heaters:
        heater.set_target_temperature(22)  # Set target temperature to 22 degrees Celsius

    # Get all ACs
    all_acs = get_all_actuators(home, "AC")
    for ac in all_acs:
        ac.set_target_temperature(25)  # Set target temperature to 25 degrees Celsius

    # Get all indoor temperature sensors
    all_indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in all_indoor_temp_sensors:
        sensor.turn_on()  # Turn on the sensors to get readings


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:** The code imports modules from `home.home_plan` and `home.actuator` to interact with the home plan and actuators.
# 2. **Create home plan:** It initializes the `home` variable using `home_plan()`, which represents your smart home setup.
# 3. **Execute actions:**
#     * **Dimming and brightening lights:** It finds the living room and bedroom, then iterates through the lights in each room to adjust their brightness.
#     * **Opening kitchen window:** It locates the kitchen and opens its windows.
#     * **Playing music in the living room:** It finds the living room's music player and plays a pop music playlist.
# 4. **Temperature control (example):** The code demonstrates setting target temperatures for heaters and AC units. It also turns on indoor temperature sensors to get readings.

# **Key Points:**

# * **Room and Actuator Access:** The code uses functions like `get_room`, `get_room_actuators`, and `get_all_actuators` to easily find and interact with specific rooms and devices.
# * **Device-Specific Actions:** It utilizes methods like `turn_on`, `turn_off`, `set_brightness_level`, `play_music`, and `set_target_temperature` to control individual devices.
# * **Clarity and Structure:** The code is organized and well-commented, making it easy to understand and modify.

# **Integration with your project:**

# This `function.py` file provides a starting point for defining your smart home functions. You can:

# * Add more functions based on your desired functionality.
# * Extend the code to handle more complex scenarios, like responding to sensor readings or implementing automated tasks.
# * Customize the code to match your specific smart home configuration and device names.

# Remember to adjust the code to align with the classes and functionality defined in your `sensor.py`, `actuator.py`, and `home_plan.py` files.