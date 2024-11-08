# Based on your functional description and the provided source code files for your smart home project, I will create a `function.py` file located in the `functions` folder. This file will include a main function that demonstrates how to use the classes defined in your project to control the smart home system.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, MusicPlayer, NotificationSender

def main():
    # Create the home layout
    home = home_plan()
    
    # Print the home plan
    print_home_plan(home)

    # Example: Controlling a specific room
    room_name = "LivingRoom"
    living_room = get_room(home, room_name)
    
    if living_room:
        # Get sensors in the living room
        sensors = get_room_sensors(home, room_name)
        print(f"Sensors in {room_name}: {[sensor.id for sensor in sensors]}")

        # Get actuators in the living room
        actuators = get_room_actuators(home, room_name)
        print(f"Actuators in {room_name}: {[actuator.id for actuator in actuators]}")

        # Example: Turn on the heater and set a target temperature
        heater = next((a for a in actuators if isinstance(a, Heater)), None)
        if heater:
            heater.turn_on()
            heater.set_target_temperature(22)  # Set to 22 degrees Celsius

        # Example: Turn on the light
        light = next((a for a in actuators if isinstance(a, Light)), None)
        if light:
            light.turn_on()
            light.set_brightness_level("high")  # Set light to high brightness

        # Example: Play music
        music_player = next((a for a in actuators if isinstance(a, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Chill Playlist")

        # Example: Send notification
        notification_sender = next((a for a in actuators if isinstance(a, NotificationSender)), None)
        if notification_sender:
            notification_sender.turn_on()
            notification_sender.notification_sender("Welcome to your smart home!")

if __name__ == "__main__":
    main()