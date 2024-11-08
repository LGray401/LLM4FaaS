# Based on your functional description and provided source code, here is the `function.py` file for your smart home project. This file will implement the three plans: Morning, Leave Home, and Movie.
# 
# ### `functions/function.py`

from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import CoffeeMachine, MusicPlayer, Light
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor

def morning_plan(home):
    print("Executing Morning Plan...")
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        # Turn on the coffee machine
        coffee_machine = get_room_actuators(home, "CoffeeMachine")[0]
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

        # Adjust the light to a comfortable level
        light = get_room_actuators(home, "Light")[0]
        light.turn_on()
        light.set_brightness_level("high")

        # Get temperature and humidity readings
        temperature_sensor = get_room_sensors(home, "Bedroom")[0]
        humidity_sensor = get_room_sensors(home, "Bedroom")[1]
        temperature_sensor.get_reading()
        humidity_sensor.get_reading()

def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Lock the doors
        door = get_room_actuators(home, "Door")[0]
        door.lock()

        # Turn off all lights
        lights = get_room_actuators(home, "Light")
        for light in lights:
            light.turn_off()

        # Notify user
        notifier = get_room_actuators(home, "NotificationSender")[0]
        notifier.turn_on()
        notifier.notification_sender("All systems are set. You can leave home.")

def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Dim the lights
        light = get_room_actuators(home, "Light")[0]
        light.turn_on()
        light.set_brightness_level("low")

        # Turn on the Smart TV
        smart_tv = get_room_actuators(home, "SmartTV")[0]
        smart_tv.turn_on()
        smart_tv.play_channel("Netflix")

        # Play some music in the background
        music_player = get_room_actuators(home, "MusicPlayer")[0]
        music_player.turn_on()
        music_player.play_music("Chill Playlist")


def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()