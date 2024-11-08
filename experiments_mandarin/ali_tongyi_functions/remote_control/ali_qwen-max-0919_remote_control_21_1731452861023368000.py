# 根据你的功能描述和提供的代码文件，我将为你创建一个 `function.py` 文件。这个文件将会实现你所要求的功能：当你回家时，自动打开灯光并调整到中等亮度、播放一首缓解压力的歌曲、煮一杯咖啡、设置空调温度为22°C、关闭窗帘，并启动扫地机器人。
# 
# ### function.py

import time
from home.actuator import Light, MusicPlayer, CoffeeMachine, AC, Curtain, CleaningRobot
from home.home_plan import home_plan, get_room_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Define the room where the actions will take place (e.g., LivingRoom)
    room_name = "LivingRoom"
    
    # Get all actuators in the specified room
    actuators = get_room_actuators(home, room_name)
    
    # Find and control specific actuators
    for actuator in actuators:
        if isinstance(actuator, Light):
            # Turn on the light and set to medium brightness
            actuator.turn_on()
            actuator.set_brightness_level("medium")
            print(f"Light in {room_name} is turned on and set to medium brightness.")
        
        elif isinstance(actuator, MusicPlayer):
            # Turn on the music player and play a relaxing song
            actuator.turn_on()
            actuator.play_music("Relaxing Songs")
            print(f"Music player in {room_name} is playing 'Relaxing Songs'.")
        
        elif isinstance(actuator, CoffeeMachine):
            # Turn on the coffee machine and make a cup of coffee
            actuator.turn_on()
            actuator.make_coffee("Espresso")
            print(f"Coffee machine in {room_name} is making an Espresso.")
        
        elif isinstance(actuator, AC):
            # Turn on the AC and set the temperature to 22°C
            actuator.turn_on()
            actuator.set_target_temperature(22)
            print(f"AC in {room_name} is set to 22°C.")
        
        elif isinstance(actuator, Curtain):
            # Close the curtains
            actuator.turn_off()
            print(f"Curtains in {room_name} are closed.")
        
        elif isinstance(actuator, CleaningRobot):
            # Start the cleaning robot's daily routine
            actuator.turn_on()
            actuator.daily_routine()
            print(f"Cleaning robot in {room_name} has started its daily routine.")

if __name__ == "__main__":
    main()