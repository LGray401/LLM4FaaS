# Given your functional description and the provided source code, I'll create the `function.py` file that will contain the main function to execute the different home automation plans: Morning Plan, Leave Home Plan, and Movie Plan. The `function.py` file will be located in the 'functions' folder and will import the necessary modules from the 'home' folder.
# 
# Here's the `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, Door, SmartSocket, Window
from home.sensor import LightIntensiveSensor

def morning_plan(home):
    # 早晨拉开窗帘，阴天的话开灯，做咖啡，咖啡做好了放音乐
    print("Executing Morning Plan...")
    
    # 拉开窗帘
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

    # Check if it's cloudy (based on LightIntensiveSensor)
    light_sensors = get_all_sensors(home, "LightIntensive")
    cloudy = False
    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading < 900:
            cloudy = True
    
    # 阴天的话开灯
    if cloudy:
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_on()
    
    # 做咖啡
    coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")
    
    # 咖啡做好了放音乐
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Morning Playlist")

def leave_home_plan(home):
    # 晴天的话拉开窗帘，关闭灯，插座，锁门
    print("Executing Leave Home Plan...")
    
    # Check if it's sunny (based on OutdoorTemperatureSensor)
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    sunny = False
    for sensor in outdoor_temp_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading > 0:
            sunny = True
    
    # 晴天的话拉开窗帘
    if sunny:
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()
    
    # 关闭灯
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
    
    # 关闭插座
    smart_sockets = get_all_actuators(home, "SmartSocket")
    for socket in smart_sockets:
        socket.turn_off()
    
    # 锁门
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()

def movie_plan(home):
    # 合上窗帘，关灯
    print("Executing Movie Plan...")
    
    # 合上窗帘
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_off()
    
    # 关灯
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def main():
    home = home_plan()
    
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()