from home.home_plan import get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators, \
    print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Heater, AC, CoffeeMachine, MusicPlayer, SmartTV, Light, Humidifier, NotificationSender, \
    CleaningRobot
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION
import time

# Global variable to store the home plan
home = None


def initialize_home():
    """Initializes the home plan.

    This function should be called once at the beginning of the program.
    """
    global home
    home = print_home_plan(home)

def handle_temperature_request(room_name, target_temperature):
    """Handles requests to adjust the temperature in a room.

    Args:
        room_name (str): The name of the room.
        target_temperature (float): The desired temperature in degrees Celsius.
    """
    room = get_room(home, room_name)
    if room is not None:
        temperature_sensors = get_room_sensors(home, room_name)
        if temperature_sensors is not None:
            current_temperature = temperature_sensors[0].get_reading()
            # Check if a heater or AC is available in the room
            heaters = get_room_actuators(home, room_name, 'Heater')
            acs = get_room_actuators(home, room_name, 'AC')
            if heaters:
                heater = heaters[0]
                heater.set_target_temperature(target_temperature)
                heater.adjust_temperature(current_temperature)
            elif acs:
                ac = acs[0]
                ac.set_target_temperature(target_temperature)
                ac.adjust_temperature(current_temperature)
            else:
                print(
                    f"No heater or AC found in {room_name}. Cannot adjust temperature. ")

def handle_light_request(room_name, brightness_level):
    """Handles requests to adjust the brightness of lights in a room.

    Args:
        room_name (str): The name of the room.
        brightness_level (str): The desired brightness level ("low", "medium", or "high").
    """
    room = get_room(home, room_name)
    if room is not None:
        lights = get_room_actuators(home, room_name, 'Light')
        if lights is not None:
            for light in lights:
                light.set_brightness_level(brightness_level)
        else:
            print(f"No lights found in {room_name}. Cannot adjust brightness.")

def handle_music_request(room_name, playlist):
    """Handles requests to play music in a room.

    Args:
        room_name (str): The name of the room.
        playlist (str): The name of the playlist to play.
    """
    room = get_room(home, room_name)
    if room is not None:
        music_players = get_room_actuators(home, room_name, 'MusicPlayer')
        if music_players is not None:
            music_player = music_players[0]
            music_player.play_music(playlist)
        else:
            print(f"No music player found in {room_name}. Cannot play music.")

def handle_tv_request(room_name, channel_name):
    """Handles requests to play a channel on a TV in a room.

    Args:
        room_name (str): The name of the room.
        channel_name (str): The name of the channel to play.
    """
    room = get_room(home, room_name)
    if room is not None:
        tvs = get_room_actuators(home, room_name, 'SmartTV')
        if tvs is not None:
            tv = tvs[0]
            tv.play_channel(channel_name)
        else:
            print(f"No SmartTV found in {room_name}. Cannot play channel.")

def handle_coffee_request(room_name, coffee_type):
    """Handles requests to make coffee in a room.

    Args:
        room_name (str): The name of the room.
        coffee_type (str): The type of coffee to make.
    """
    room = get_room(home, room_name)
    if room is not None:
        coffee_machines = get_room_actuators(home, room_name, 'CoffeeMachine')
        if coffee_machines is not None:
            coffee_machine = coffee_machines[0]
            coffee_machine.make_coffee(coffee_type)
        else:
            print(f"No coffee machine found in {room_name}. Cannot make coffee.")

def handle_notification_request(room_name, message):
    """Handles requests to send notifications in a room.

    Args:
        room_name (str): The name of the room.
        message (str): The message to send.
    """
    room = get_room(home, room_name)
    if room is not None:
        notification_senders = get_room_actuators(home, room_name, 'NotificationSender')
        if notification_senders is not None:
            notification_sender = notification_senders[0]
            notification_sender.notification_sender(message)
        else:
            print(f"No notification sender found in {room_name}. Cannot send notification.")

def handle_cleaning_robot_request(room_name):
    """Handles requests to start the daily cleaning routine of a cleaning robot in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        cleaning_robots = get_room_actuators(home, room_name, 'CleaningRobot')
        if cleaning_robots is not None:
            cleaning_robot = cleaning_robots[0]
            cleaning_robot.daily_routine()
        else:
            print(f"No cleaning robot found in {room_name}. Cannot start cleaning.")

def handle_humidity_request(room_name, action):
    """Handles requests to adjust the humidity in a room.

    Args:
        room_name (str): The name of the room.
        action (str): The desired action ("increase" or "decrease").
    """
    room = get_room(home, room_name)
    if room is not None:
        humidity_sensors = get_room_sensors(home, room_name, 'HumiditySensor')
        if humidity_sensors is not None:
            current_humidity = humidity_sensors[0].get_reading()
            humidifiers = get_room_actuators(home, room_name, 'Humidifier')
            if humidifiers is not None:
                humidifier = humidifiers[0]
                if action == "increase":
                    humidifier.increase_humidity()
                elif action == "decrease":
                    humidifier.decrease_humidity()
                else:
                    print(f"Invalid action: {action}. Please use 'increase' or 'decrease'.")
            else:
                print(f"No humidifier found in {room_name}. Cannot adjust humidity.")
        else:
            print(f"No humidity sensor found in {room_name}. Cannot adjust humidity.")

def main():
    """Main function of the program."""
    initialize_home()

    while True:
        user_input = input("Enter a command (e.g., 'set temperature LivingRoom 26', 'play music LivingRoom playlist1'): ")
        # print("Starting processing now")
        # if "exit" in user_input:
        #     print("Exiting...")
        #     break
        command, room_name, *args = user_input.split()
        if command == 'set':
            if args[0] == 'temperature':
                handle_temperature_request(room_name, float(args[1]))
            elif args[0] == 'light':
                handle_light_request(room_name, args[1])
        elif command == 'play':
            if args[0] == 'music':
                handle_music_request(room_name, args[1])
            elif args[0] == 'channel':
                handle_tv_request(room_name, args[1])
        elif command == 'make':
            if args[0] == 'coffee':
                handle_coffee_request(room_name, args[1])
        elif command == 'send':
            if args[0] == 'notification':
                handle_notification_request(room_name, ' '.join(args[1:]))
        elif command == 'clean':
            if args[0] == 'robot':
                handle_cleaning_robot_request(room_name)
        elif command == 'adjust':
            if args[0] == 'humidity':
                handle_humidity_request(room_name, args[1])
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **`function.py` Structure:**
#    - Imports necessary functions and classes from other files (`home_plan.py`, `sensor.py`, `actuator.py`, `config.py`).
#    - Defines a global `home` variable to store the home plan.
#    - Defines `initialize_home` function to create and store the home plan.
#    - Defines functions for handling user commands, each function corresponding to a specific action:
#      - `handle_temperature_request`: Adjusts room temperature using a heater or AC.
#      - `handle_light_request`: Adjusts light brightness in a room.
#      - `handle_music_request`: Plays music in a room.
#      - `handle_tv_request`: Plays a channel on a TV.
#      - `handle_coffee_request`: Makes coffee in a room.
#      - `handle_notification_request`: Sends notifications.
#      - `handle_cleaning_robot_request`: Starts the cleaning robot's daily routine.
#      - `handle_humidity_request`: Adjusts humidity in a room.
#    - Defines a `main` function to:
#      - Call `initialize_home` to set up the home plan.
#      - Enter a loop to repeatedly:
#        - Get user input.
#        - Parse the input to extract the command, room name, and arguments.
#        - Call the appropriate handler function based on the command.

# 2. **Function Implementation:**
#    - Each handler function:
#      - Retrieves the specified room using `get_room`.
#      - Finds relevant actuators or sensors using `get_room_actuators` or `get_room_sensors`.
#      - Performs the desired action based on the command arguments.
#      - Handles potential errors (e.g., room not found, actuator not found) by printing informative messages.

# 3. **Command Handling:**
#    - The `main` function uses a simple string split to parse user input.
#    - It uses `if` statements to determine the command type and call the corresponding handler function.
#    - This allows for flexibility in handling different commands and actions.

# 4. **Integration with `home_plan.py` and Other Files:**
#    - `function.py` effectively acts as a bridge between the user interface and the smart home functionality.
#    - It uses functions from `home_plan.py` to access and manipulate the home plan.
#    - It uses classes from `sensor.py` and `actuator.py` to interact with devices.
#    - It leverages configuration values from `config.py`.

# **To use this code:**

# 1. Make sure you have all the files in the correct directory structure:
#    - `home` folder:
#      - `sensor.py`
#      - `actuator.py`
#      - `home_plan.py`
#      - `config.py`
#    - `functions` folder:
#      - `function.py`

# 2. Run `function.py` to start the program.

# 3. Enter commands like:
#    - `set temperature LivingRoom 26`
#    - `play music Bedroom playlist2`
#    - `make coffee Kitchen Americano`

# **Remember to:**

# - Replace example playlist names, coffee types, etc., with actual values.
# - Customize `home_plan.py` to define the layout of your home and its devices.
# - Adjust `config.py` to set appropriate threshold values and other parameters.
