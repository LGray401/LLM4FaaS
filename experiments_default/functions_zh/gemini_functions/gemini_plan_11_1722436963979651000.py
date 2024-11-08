from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import Light, AC, Heater, CleaningRobot, MusicPlayer, SmartTV, NotificationSender
from home.config import TEMP_LOW, TEMP_HIGH

from home.logger_config import logger

import time

# Global variable for home
home = home_plan()

def morning_plan():
    # Get the LivingRoom
    living_room = get_room(home, "LivingRoom")
    # Get the LivingRoom Light
    living_room_light = get_room_actuators(home, "LivingRoom")[0]
    # Turn on the LivingRoom light
    living_room_light.turn_on()
    print(f"Turned on the light in the {living_room.name}!")
    logger.info(f"Turned on the light in the {living_room.name}!")

def leave_home_plan():
    # Get the LivingRoom
    living_room = get_room(home, "LivingRoom")
    # Get the LivingRoom Curtain
    living_room_curtain = get_room_actuators(home, "LivingRoom")[4]
    # Open the LivingRoom Curtain
    living_room_curtain.turn_on()
    print(f"Opened the curtain in the {living_room.name}!")
    logger.info(f"Opened the curtain in the {living_room.name}!")

def movie_plan():
    # Get the LivingRoom
    living_room = get_room(home, "LivingRoom")
    # Get the LivingRoom SmartTV
    living_room_tv = get_room_actuators(home, "LivingRoom")[9]
    # Turn on the LivingRoom TV
    living_room_tv.turn_on()
    # Play the "TVB" channel on LivingRoom TV
    living_room_tv.play_channel("TVB")
    print(f"Turned on the TV and played TVB in the {living_room.name}!")
    logger.info(f"Turned on the TV and played TVB in the {living_room.name}!")


def adjust_room_temperature(room_name):
    # Get the room
    room = get_room(home, room_name)
    # Get the temperature sensor
    room_temp_sensor = get_room_sensors(home, room_name)[0]
    # Get the AC
    room_ac = get_room_actuators(home, room_name)[5]
    # Get the heater
    room_heater = get_room_actuators(home, room_name)[6]
    # Read the temperature
    temperature = room_temp_sensor.get_reading()
    
    # Adjust temperature
    if temperature < TEMP_LOW:
        print(f"It's too cold in {room_name}, turning on the heater.")
        logger.info(f"It's too cold in {room_name}, turning on the heater.")
        room_heater.turn_on()
    elif temperature > TEMP_HIGH:
        print(f"It's too hot in {room_name}, turning on the AC.")
        logger.info(f"It's too hot in {room_name}, turning on the AC.")
        room_ac.turn_on()
    else:
        print(f"The temperature in {room_name} is comfortable.")
        logger.info(f"The temperature in {room_name} is comfortable.")
        room_ac.turn_off()
        room_heater.turn_off()


def daily_cleaning_routine():
    # Get all cleaning robots
    cleaning_robots = get_all_actuators(home, "CleaningRobot")

    for robot in cleaning_robots:
        # Turn on the cleaning robot
        robot.turn_on()
        # Perform daily cleaning routine
        robot.daily_routine()

def play_music_in_living_room(playlist):
    # Get the LivingRoom
    living_room = get_room(home, "LivingRoom")
    # Get the LivingRoom MusicPlayer
    living_room_music_player = get_room_actuators(home, "LivingRoom")[5]
    # Play the playlist
    living_room_music_player.play_music(playlist)
    print(f"Playing {playlist} in the {living_room.name}!")
    logger.info(f"Playing {playlist} in the {living_room.name}!")

def turn_on_all_lights():
    # Get all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()
        print(f"Turned on the light in {light.room_name}")
        logger.info(f"Turned on the light in {light.room_name}")

def turn_off_all_lights():
    # Get all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
        print(f"Turned off the light in {light.room_name}")
        logger.info(f"Turned off the light in {light.room_name}")

def turn_on_all_acs():
    # Get all ACs
    acs = get_all_actuators(home, "AC")
    for ac in acs:
        ac.turn_on()
        print(f"Turned on the AC in {ac.room_name}")
        logger.info(f"Turned on the AC in {ac.room_name}")

def turn_off_all_acs():
    # Get all ACs
    acs = get_all_actuators(home, "AC")
    for ac in acs:
        ac.turn_off()
        print(f"Turned off the AC in {ac.room_name}")
        logger.info(f"Turned off the AC in {ac.room_name}")

def turn_on_all_heaters():
    # Get all heaters
    heaters = get_all_actuators(home, "Heater")
    for heater in heaters:
        heater.turn_on()
        print(f"Turned on the heater in {heater.room_name}")
        logger.info(f"Turned on the heater in {heater.room_name}")

def turn_off_all_heaters():
    # Get all heaters
    heaters = get_all_actuators(home, "Heater")
    for heater in heaters:
        heater.turn_off()
        print(f"Turned off the heater in {heater.room_name}")
        logger.info(f"Turned off the heater in {heater.room_name}")

def send_notification_to_all_rooms(message):
    # Get all notification senders
    notification_senders = get_all_actuators(home, "NotificationSender")
    for sender in notification_senders:
        sender.notification_sender(message)

def main():
    morning_plan()
    # leave_home_plan()
    # movie_plan()
    # while True:
    #     # Example usage of functions:
    #     morning_plan()
    #     leave_home_plan()
    #     movie_plan()
    #
    #     # Adjust temperature in LivingRoom
    #     adjust_room_temperature("LivingRoom")
    #
    #     # Daily cleaning routine
    #     daily_cleaning_routine()
    #
    #     # Play music in LivingRoom
    #     play_music_in_living_room("Classical Music")
    #
    #     # Turn on all lights
    #     turn_on_all_lights()
    #     time.sleep(5)
    #
    #     # Turn off all lights
    #     turn_off_all_lights()
    #     time.sleep(5)
    #
    #     # Turn on all ACs
    #     turn_on_all_acs()
    #     time.sleep(5)
    #
    #     # Turn off all ACs
    #     turn_off_all_acs()
    #     time.sleep(5)
    #
    #     # Turn on all heaters
    #     turn_on_all_heaters()
    #     time.sleep(5)
    #
    #     # Turn off all heaters
    #     turn_off_all_heaters()
    #     time.sleep(5)
    #
    #     # Send a notification to all rooms
    #     send_notification_to_all_rooms("Hello from the smart home!")
    #     time.sleep(5)
    #
    #     # Keep running the loop for testing
    #     time.sleep(10) # sleep for 10 seconds between each loop

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** Import necessary modules and functions from the other files in your project.
# 2. **Global Variable `home`:** Initialize the `home` variable by calling the `home_plan()` function from `home_plan.py`. This variable represents the entire home structure with rooms, sensors, and actuators.
# 3. **Plan Functions:**
#     - `morning_plan()`: Turns on the light in the living room.
#     - `leave_home_plan()`: Opens the curtains in the living room.
#     - `movie_plan()`: Turns on the TV and plays a specific channel in the living room.
# 4. **`adjust_room_temperature()`:** 
#     - Gets the room, temperature sensor, AC, and heater for a given room name.
#     - Reads the temperature using the temperature sensor.
#     - Adjusts the AC and heater based on the temperature to keep the room comfortable.
# 5. **`daily_cleaning_routine()`:**
#     - Gets all cleaning robots in the home.
#     - Turns on each cleaning robot and triggers its daily routine.
# 6. **`play_music_in_living_room()`:**
#     - Gets the music player in the living room.
#     - Plays the specified playlist.
# 7. **`turn_on_all_lights()`, `turn_off_all_lights()`:**
#     - Get all lights in the home.
#     - Turn on or off all lights.
# 8. **`turn_on_all_acs()`, `turn_off_all_acs()`:**
#     - Get all ACs in the home.
#     - Turn on or off all ACs.
# 9. **`turn_on_all_heaters()`, `turn_off_all_heaters()`:**
#     - Get all heaters in the home.
#     - Turn on or off all heaters.
# 10. **`send_notification_to_all_rooms()`:**
#     - Get all notification senders in the home.
#     - Send the specified message to all senders.
# 11. **`main()`:** 
#     - Contains the main loop for testing the functions.
#     - You can add more complex logic and event handling here to create more advanced scenarios for your smart home.

# **How to Use:**

# 1. **Save:** Save this code as `function.py` in the `functions` folder of your project.
# 2. **Run:** Run the `function.py` file. It will execute the example code and demonstrate how the functions work.
# 3. **Integrate:** Replace the example usage in the `main()` function with your own logic and event handlers to create your desired smart home functionality.

# **Important Notes:**

# - Ensure that all the necessary files (sensor.py, actuator.py, home_plan.py, and config.py) are in the correct locations and have the correct code.
# - Customize the code according to your specific smart home setup and desired functionalities.
# - This is a basic example, and you can expand upon it by adding more functionalities, event handling, and integration with external services or platforms.
