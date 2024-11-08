# To create a smart home application based on your functional description, you'll need to implement functionalities for a cleaning robot, a music player, a smart TV, and bedroom lighting adjustment. Below is a Python script that utilizes the provided reference code to achieve these functionalities.
# 
# ### smart_home.py
# 
# ```python
from home.actuator import CleaningRobot, MusicPlayer, SmartTV, Light
from home.home_plan import home_plan, get_room_actuators

def start_cleaning(room_name):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    cleaning_robot = next((act for act in actuators if isinstance(act, CleaningRobot)), None)
    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

def play_music(room_name, playlist):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    music_player = next((act for act in actuators if isinstance(act, MusicPlayer)), None)
    if music_player:
        music_player.turn_on()
        music_player.play_music(playlist)

def play_tv(room_name, channel_name):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    tv = next((act for act in actuators if isinstance(act, SmartTV)), None)
    if tv:
        tv.turn_on()
        tv.play_channel(channel_name)

def adjust_light(room_name, action, brightness_level=None):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    lights = [act for act in actuators if isinstance(act, Light)]
    for light in lights:
        if action == "on":
            light.turn_on()
        elif action == "off":
            light.turn_off()
        elif action == "set_brightness" and brightness_level:
            light.turn_on()  # Ensure light is on before setting brightness
            light.set_brightness_level(brightness_level)

if __name__ == "__main__":
    # Example usage
    start_cleaning("LivingRoom")
    play_music("Bedroom", "Relaxing Playlist")
    play_tv("LivingRoom", "Channel 5")
    adjust_light("Bedroom", "on")
    adjust_light("Bedroom", "set_brightness", "medium")
# ```
# 
# ### Explanation
# 
# 1. **Cleaning Robot**: The `start_cleaning` function starts the cleaning routine for a specified room using the `CleaningRobot` actuator.
# 
# 2. **Music Player**: The `play_music` function plays music from a specified playlist in the given room using the `MusicPlayer` actuator.
# 
# 3. **Smart TV**: The `play_tv` function plays a specified TV channel in the given room using the `SmartTV` actuator.
# 
# 4. **Bedroom Lighting**: The `adjust_light` function turns on/off the lights or sets the brightness level in the specified room using the `Light` actuator.
# 
# ### Command to Run
# 
# To execute this script in a Linux terminal, ensure that the `home` directory is in your PYTHONPATH, and then run:
# 
# ```bash
# python smart_home.py
# ```
# 
# This script will perform example actions such as starting the cleaning routine in the living room, playing music in the bedroom, playing a TV channel in the living room, and adjusting the bedroom lights. You can modify the function calls in the `if __name__ == "__main__":` block to test different functionalities.