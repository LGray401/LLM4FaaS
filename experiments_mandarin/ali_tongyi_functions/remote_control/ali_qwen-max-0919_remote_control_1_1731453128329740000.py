# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control the smart home devices as described. The main function will handle the following functionalities:
# 
# 1. **Vacuum Robot:**
#    - Start cleaning
#    - Spot cleaning
#    - Stop cleaning
# 
# 2. **Music Player:**
#    - Play a song
#    - Listen to an audiobook
# 
# 3. **Smart TV:**
#    - Change channel by voice
#    - Watch a movie or TV show
# 
# 4. **Bedroom Light:**
#    - Turn on
#    - Turn off
#    - Adjust brightness
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.config import DAILY_ROUTINE_DURATION

def find_device_by_type(room, device_type):
    for device in room.actuators:
        if device.actuator_type == device_type:
            return device
    return None

def main():
    home = home_plan()

    while True:
        print("\n--- Smart Home Control ---")
        print("1. Vacuum Robot")
        print("2. Music Player")
        print("3. Smart TV")
        print("4. Bedroom Light")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            # Vacuum Robot
            vacuum_robot = find_device_by_type(get_room(home, "LivingRoom"), "CleaningRobot")
            if vacuum_robot:
                print("\n--- Vacuum Robot Control ---")
                print("1. Start Cleaning")
                print("2. Spot Cleaning")
                print("3. Stop Cleaning")
                robot_choice = input("Choose an option: ")
                if robot_choice == '1':
                    vacuum_robot.turn_on()
                    vacuum_robot.daily_routine()
                elif robot_choice == '2':
                    vacuum_robot.turn_on()
                    print(f"Vacuum Robot {vacuum_robot.id} starts spot cleaning.")
                elif robot_choice == '3':
                    vacuum_robot.turn_off()
                    print(f"Vacuum Robot {vacuum_robot.id} stops cleaning.")
                else:
                    print("Invalid choice.")
            else:
                print("Vacuum Robot not found.")

        elif choice == '2':
            # Music Player
            music_player = find_device_by_type(get_room(home, "LivingRoom"), "MusicPlayer")
            if music_player:
                print("\n--- Music Player Control ---")
                print("1. Play a Song")
                print("2. Listen to an Audiobook")
                music_choice = input("Choose an option: ")
                if music_choice == '1':
                    song_name = input("Enter the song name: ")
                    music_player.turn_on()
                    music_player.play_music(song_name)
                elif music_choice == '2':
                    book_name = input("Enter the book name: ")
                    music_player.turn_on()
                    music_player.play_music(book_name)
                else:
                    print("Invalid choice.")
            else:
                print("Music Player not found.")

        elif choice == '3':
            # Smart TV
            smart_tv = find_device_by_type(get_room(home, "LivingRoom"), "SmartTV")
            if smart_tv:
                print("\n--- Smart TV Control ---")
                print("1. Change Channel by Voice")
                print("2. Watch a Movie or TV Show")
                tv_choice = input("Choose an option: ")
                if tv_choice == '1':
                    channel_name = input("Enter the channel name: ")
                    smart_tv.turn_on()
                    smart_tv.play_channel(channel_name)
                elif tv_choice == '2':
                    media_name = input("Enter the movie or TV show name: ")
                    smart_tv.turn_on()
                    smart_tv.play_channel(media_name)
                else:
                    print("Invalid choice.")
            else:
                print("Smart TV not found.")

        elif choice == '4':
            # Bedroom Light
            bedroom_light = find_device_by_type(zget_room(home, "Bedroom"), "Light")
            if bedroom_light:
                print("\n--- Bedroom Light Control ---")
                print("1. Turn On")
                print("2. Turn Off")
                print("3. Adjust Brightness")
                light_choice = input("Choose an option: ")
                if light_choice == '1':
                    bedroom_light.turn_on()
                elif light_choice == '2':
                    bedroom_light.turn_off()
                elif light_choice == '3':
                    level_name = input("Enter the brightness level (low, medium, high): ")
                    bedroom_light.set_brightness_level(level_name)
                else:
                    print("Invalid choice.")
            else:
                print("Bedroom Light not found.")

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()