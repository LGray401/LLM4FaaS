# Based on your functional description and the provided source code files, I will create a `function.py` file that includes a main function to manage the different plans for your smart home system: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN". I will assume typical actions for these plans based on common smart home functionalities.
# 
# Here's the content for the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.actuator import CoffeeMachine, Light, AC, Heater, MusicPlayer, SmartTV, Door, Curtain
from home.sensor import IndoorTemperatureSensor, HumiditySensor

def morning_plan(home):
    print("\n--- Morning Plan ---")
    # Turn on lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        light.set_brightness_level("medium")

    # Prepare coffee
    coffee_makers = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_makers:
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # Adjust temperature
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    for heater in heaters:
        heater.set_target_temperature(22)
        heater.adjust_temperature(20)  # Assuming current temp is 20 for example
    for ac in acs:
        ac.set_target_temperature(22)
        ac.adjust_temperature(25)  # Assuming current temp is 25 for example

def leave_home_plan(home):
    print("\n--- Leave Home Plan ---")
    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Lock doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()

    # Turn off all coffee machines
    coffee_makers = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in coffee_makers:
        coffee_machine.turn_off()

    # Send notification
    notification_sender = get_all_actuators(home, "NotificationSender")
    for ns in notification_sender:
        ns.turn_on()
        ns.notification_sender("All systems are set. You can leave home safely.")

def movie_plan(home):
    print("\n--- Movie Plan ---")
    # Dim lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.set_brightness_level("low")

    # Turn on the Smart TV
    smart_tvs = get_all_actuators(home, "SmartTV")
    for smart_tv in smart_tvs:
        smart_tv.turn_on()
        smart_tv.play_channel("Netflix")

    # Play music
    music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Chill Vibes Playlist")

def main():
    home = home_plan()

    # Execute plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()