# Here is the 'function.py' file for your smart home project:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.logger_config import logger

def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Example usage of functions to access room, sensors, and actuators
    room = get_room(home, "LivingRoom")
    sensors = get_room_sensors(home, "LivingRoom")
    actuators = get_room_actuators(home, "LivingRoom")
    all_sensors = get_all_sensors(home, "IndoorTemperature")
    all_actuators = get_all_actuators(home, "Light")

    # Example usage of individual sensors and actuators
    indoor_temp_sensor = IndoorTemperatureSensor("LivingRoom")
    indoor_temp_sensor.turn_on()
    print(indoor_temp_sensor.get_reading())

    light = Light("LivingRoom")
    light.turn_on()
    light.set_brightness_level("medium")

    music_player = MusicPlayer("LivingRoom")
    music_player.turn_on()
    music_player.play_music("playlist")

    heater = Heater("LivingRoom")
    heater.turn_on()
    heater.set_target_temperature(25)
    heater.adjust_temperature(20)

    ac = AC("LivingRoom")
    ac.turn_on()
    ac.set_target_temperature(20)
    ac.adjust_temperature(25)

    coffee_machine = CoffeeMachine("Kitchen")
    coffee_machine.turn_on()
    coffee_machine.make_coffee("espresso")

    door = Door("LivingRoom")
    door.lock()
    door.unlock()

    curtain = Curtain("LivingRoom")
    curtain.turn_on()

    cleaning_robot = CleaningRobot("LivingRoom")
    cleaning_robot.turn_on()
    cleaning_robot.daily_routine()

    notification_sender = NotificationSender("LivingRoom")
    notification_sender.turn_on()
    notification_sender.notification_sender("message")

    smart_tv = SmartTV("LivingRoom")
    smart_tv.turn_on()
    smart_tv.play_channel("channel")

    smart_socket = SmartSocket("LivingRoom")
    smart_socket.turn_on()

if __name__ == "__main__":
    main()