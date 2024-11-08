# Great! Based on your functional description and the provided source code, I'll create the `function.py` file for your smart home project. This file will contain the main function and implement the described plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.
# 
# Here's the `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators, get_room, get_room_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import CoffeeMachine, MusicPlayer, Curtain, Light, Door, SmartSocket

def morning_plan(home):
    print("Executing MORNING PLAN...")
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # 拉开窗帘
    curtains = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_on()

    # 阴天的话开灯
    light_sensors = [sensor for sensor in get_room(home, "LivingRoom").sensors if isinstance(sensor, LightIntensiveSensor)]
    for sensor in light_sensors:
        sensor.turn_on()
        if sensor.get_reading() < 900:  # 阴天的光强度假设为小于900
            lights = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)]
            for light in lights:
                light.turn_on()

    # 做咖啡
    coffee_machines = [actuator for actuator in get_room_actuators(home, "Kitchen") if isinstance(actuator, CoffeeMachine)]
    for coffee_machine in coffee_machines:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # 咖啡做好了放音乐
    music_players = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, MusicPlayer)]
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Morning Playlist")


def leave_home_plan(home):
    print("Executing LEAVE HOME PLAN...")
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # 晴天的话拉开窗帘
    outdoor_sensors = get_all_actuators(home, "OutdoorTemperature")
    if outdoor_sensors:
        for sensor in outdoor_sensors:
            sensor.turn_on()
            if sensor.get_reading() > 15:  # 晴天的温度假设为大于15度
                curtains = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)]
                for curtain in curtains:
                    curtain.turn_on()

    # 关闭灯，插座，锁门
    lights = [actuator for actuator in get_all_actuators(home, "Light")]
    for light in lights:
        light.turn_off()

    smart_sockets = [actuator for actuator in get_all_actuators(home, "SmartSocket")]
    for socket in smart_sockets:
        socket.turn_off()

    doors = [actuator for actuator in get_all_actuators(home, "Door")]
    for door in doors:
        door.lock()


def movie_plan(home):
    print("Executing MOVIE PLAN...")
    living_room = get_room(home, "LivingRoom")
    if not living_room:
        return

    # 合上窗帘，关灯
    curtains = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Curtain)]
    for curtain in curtains:
        curtain.turn_off()

    lights = [actuator for actuator in get_room_actuators(home, "LivingRoom") if isinstance(actuator, Light)]
    for light in lights:
        light.turn_off()


def main():
    home = home_plan()
    print("Welcome to Smart Home System!")
    while True:
        print("\nChoose a plan to execute:")
        print("1. MORNING PLAN")
        print("2. LEAVE HOME PLAN")
        print("3. MOVIE PLAN")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            morning_plan(home)
        elif choice == '2':
            leave_home_plan(home)
        elif choice == '3':
            movie_plan(home)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()