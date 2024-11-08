# Based on the provided functional description and source code, I will create a `function.py` file that includes the main function to handle the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. This file will be placed in the `functions` folder.
# 
# Here is the `function.py`:

# functions/function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def morning_plan(home):
    print("Starting Morning Plan")
    
    # 7点叫我起床
    notification_sender = get_room_actuators(home, "LivingRoom")[0]
    if isinstance(notification_sender, NotificationSender):
        notification_sender.turn_on()
        notification_sender.notification_sender("Time to wake up!")
        time.sleep(1)  # Wait for 1 second
        notification_sender.turn_off()
    
    # 7点零五把音乐大开，播放周杰伦歌单
    music_player = get_room_actuators(home, "LivingRoom")[4]
    if isinstance(music_player, MusicPlayer):
        music_player.turn_on()
        music_player.play_music("Jay Chou Playlist")
    
    # 7:20做好咖啡
    coffee_machine = get_room_actuators(home, "Kitchen")[3]
    if isinstance(coffee_machine, CoffeeMachine):
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

def leave_home_plan(home):
    print("Starting Leave Home Plan")
    
    # 7:30之后我离开家后自动锁门
    door_living_room = get_room_actuators(home, "LivingRoom")[0]
    door_kitchen = get_room_actuators(home, "Kitchen")[4]
    door_bathroom = get_room_actuators(home, "Bathroom")[3]
    door_balcony = get_room_actuators(home, "Balcony")[0]
    
    if isinstance(door_living_room, Door):
        door_living_room.lock()
    if isinstance(door_kitchen, Door):
        door_kitchen.lock()
    if isinstance(door_bathroom, Door):
        door_bathroom.lock()
    if isinstance(door_balcony, Door):
        door_balcony.lock()
    
    # 关闭家中灯光插座
    for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            if isinstance(actuator, (Light, SmartSocket)):
                actuator.turn_off()

def movie_plan(home):
    print("Starting Movie Plan")
    
    # 我开始播放电影时，关闭窗帘，调暗灯光
    curtain_living_room = get_room_actuators(home, "LivingRoom")[3]
    light_living_room = get_room_actuators(home, "LivingRoom")[1]
    
    if isinstance(curtain_living_room, Curtain):
        curtain_living_room.turn_on()  # Assuming turning on means closing the curtain
        curtain_living_room.turn_off()  # Turn off after closing
    
    if isinstance(light_living_room, Light):
        light_living_room.turn_on()
        light_living_room.set_brightness_level("low")

def main():
    home = home_plan()
    
    # Simulate the time for the plans
    current_time = 7 * 60  # 7:00 AM in minutes
    while True:
        if current_time == 7 * 60:  # 7:00 AM
            morning_plan(home)
        elif current_time == 7 * 60 + 30:  # 7:30 AM
            leave_home_plan(home)
        elif current_time == 8 * 60:  # 8:00 PM
            movie_plan(home)
        
        # Increment time by 1 minute
        current_time += 1
        time.sleep(60)  # Sleep for 1 minute

if __name__ == "__main__":
    main()