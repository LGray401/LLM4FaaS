from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time

# Define functions for different actions

def adjust_temperature(home, room_name, target_temperature):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get heater and AC actuators for the room
    heater = get_room_actuators(home, room_name)[0]  # Assuming only one heater per room
    ac = get_room_actuators(home, room_name)[1]  # Assuming only one AC per room

    # Get temperature sensor reading
    temperature_sensor = get_room_sensors(home, room_name)[0]
    current_temperature = temperature_sensor.get_reading()

    # Adjust temperature
    if current_temperature < target_temperature:
        heater.turn_on()
        ac.turn_off()
        print(f"Turning on heater in {room_name} to reach {target_temperature}°C.")
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for some time for temperature to change
    elif current_temperature > target_temperature:
        heater.turn_off()
        ac.turn_on()
        print(f"Turning on AC in {room_name} to reach {target_temperature}°C.")
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for some time for temperature to change
    else:
        print(f"Temperature in {room_name} is already at {target_temperature}°C.")

    # Set target temperature for heater and AC
    heater.set_target_temperature(target_temperature)
    ac.set_target_temperature(target_temperature)


def adjust_humidity(home, room_name, target_humidity):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get humidifier
    humidifier = get_room_actuators(home, room_name)[0]  # Assuming only one humidifier per room

    # Get humidity sensor reading
    humidity_sensor = get_room_sensors(home, room_name)[1]
    current_humidity = humidity_sensor.get_reading()

    # Adjust humidity
    if current_humidity < target_humidity:
        humidifier.increase_humidity()
        print(f"Increasing humidity in {room_name} to reach {target_humidity}%")
    elif current_humidity > target_humidity:
        humidifier.decrease_humidity()
        print(f"Decreasing humidity in {room_name} to reach {target_humidity}%")
    else:
        print(f"Humidity in {room_name} is already at {target_humidity}%")


def turn_on_light(home, room_name, brightness_level):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get light actuator
    light = get_room_actuators(home, room_name)[0]  # Assuming only one light per room

    # Turn on light
    light.turn_on()
    light.set_brightness_level(brightness_level)
    print(f"Turning on light in {room_name} to {brightness_level.upper()} brightness.")


def turn_off_light(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get light actuator
    light = get_room_actuators(home, room_name)[0]  # Assuming only one light per room

    # Turn off light
    light.turn_off()
    print(f"Turning off light in {room_name}.")


def open_window(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get window actuator
    window = get_room_actuators(home, room_name)[1]  # Assuming only one window per room

    # Open window
    window.turn_on()
    print(f"Opening window in {room_name}.")


def close_window(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get window actuator
    window = get_room_actuators(home, room_name)[1]  # Assuming only one window per room

    # Close window
    window.turn_off()
    print(f"Closing window in {room_name}.")


def open_curtain(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get curtain actuator
    curtain = get_room_actuators(home, room_name)[2]  # Assuming only one curtain per room

    # Open curtain
    curtain.turn_on()
    print(f"Opening curtain in {room_name}.")


def close_curtain(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get curtain actuator
    curtain = get_room_actuators(home, room_name)[2]  # Assuming only one curtain per room

    # Close curtain
    curtain.turn_off()
    print(f"Closing curtain in {room_name}.")


def play_music(home, room_name, playlist):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get music player actuator
    music_player = get_room_actuators(home, room_name)[3]  # Assuming only one music player per room

    # Play music
    music_player.turn_on()
    music_player.play_music(playlist)
    print(f"Playing music in {room_name}: {playlist}.")


def stop_music(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get music player actuator
    music_player = get_room_actuators(home, room_name)[3]  # Assuming only one music player per room

    # Stop music
    music_player.turn_off()
    print(f"Stopping music in {room_name}.")


def make_coffee(home, room_name, coffee_type):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get coffee machine actuator
    coffee_machine = get_room_actuators(home, room_name)[0]  # Assuming only one coffee machine per room

    # Make coffee
    coffee_machine.turn_on()
    coffee_machine.make_coffee(coffee_type)
    print(f"Making {coffee_type} in {room_name}.")


def turn_on_tv(home, room_name, channel_name):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get Smart TV actuator
    tv = get_room_actuators(home, room_name)[4]  # Assuming only one Smart TV per room

    # Turn on TV and play channel
    tv.turn_on()
    tv.play_channel(channel_name)
    print(f"Turning on TV in {room_name} and playing {channel_name}.")


def turn_off_tv(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get Smart TV actuator
    tv = get_room_actuators(home, room_name)[4]  # Assuming only one Smart TV per room

    # Turn off TV
    tv.turn_off()
    print(f"Turning off TV in {room_name}.")


def start_cleaning_robot(home, room_name):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get cleaning robot actuator
    cleaning_robot = get_room_actuators(home, room_name)[5]  # Assuming only one cleaning robot per room

    # Start cleaning robot
    cleaning_robot.turn_on()
    cleaning_robot.daily_routine()
    print(f"Starting cleaning robot in {room_name}.")


def send_notification(home, room_name, message):
    room = get_room(home, room_name)
    if room is None:
        return

    # Get notification sender actuator
    notification_sender = get_room_actuators(home, room_name)[6]  # Assuming only one notification sender per room

    # Send notification
    notification_sender.turn_on()
    notification_sender.notification_sender(message)
    print(f"Sending notification in {room_name}: {message}.")

# Define the main function for handling user requests
def main():
    home = home_plan()
    print_home_plan(home)

    while True:
        user_input = input("\nWhat would you like to do? (Enter 'help' for commands): ")

        if user_input.lower() == "help":
            print("\nAvailable commands:")
            print("  - adjust_temperature [room_name] [target_temperature]")
            print("  - adjust_humidity [room_name] [target_humidity]")
            print("  - turn_on_light [room_name] [brightness_level]")
            print("  - turn_off_light [room_name]")
            print("  - open_window [room_name]")
            print("  - close_window [room_name]")
            print("  - open_curtain [room_name]")
            print("  - close_curtain [room_name]")
            print("  - play_music [room_name] [playlist]")
            print("  - stop_music [room_name]")
            print("  - make_coffee [room_name] [coffee_type]")
            print("  - turn_on_tv [room_name] [channel_name]")
            print("  - turn_off_tv [room_name]")
            print("  - start_cleaning_robot [room_name]")
            print("  - send_notification [room_name] [message]")
            print("  - exit")
        elif user_input.lower() == "exit":
            break
        elif "adjust_temperature" in user_input.lower():
            try:
                room_name, target_temperature = user_input.split()[1:]
                adjust_temperature(home, room_name, float(target_temperature))
            except (IndexError, ValueError):
                print("Invalid command format. Please use: adjust_temperature [room_name] [target_temperature]")
        elif "adjust_humidity" in user_input.lower():
            try:
                room_name, target_humidity = user_input.split()[1:]
                adjust_humidity(home, room_name, float(target_humidity))
            except (IndexError, ValueError):
                print("Invalid command format. Please use: adjust_humidity [room_name] [target_humidity]")
        elif "turn_on_light" in user_input.lower():
            try:
                room_name, brightness_level = user_input.split()[1:]
                turn_on_light(home, room_name, brightness_level.lower())
            except (IndexError, ValueError):
                print("Invalid command format. Please use: turn_on_light [room_name] [brightness_level]")
        elif "turn_off_light" in user_input.lower():
            try:
                room_name = user_input.split()[1]
                turn_off_light(home, room_name)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: turn_off_light [room_name]")
        elif "open_window" in user_input.lower():
            try:
                room_name = user_input.split()[1]
                open_window(home, room_name)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: open_window [room_name]")
        elif "close_window" in user_input.lower():
            try:
                room_name = user_input.split()[1]
                close_window(home, room_name)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: close_window [room_name]")
        elif "open_curtain" in user_input.lower():
            try:
                room_name = user_input.split()[1]
                open_curtain(home, room_name)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: open_curtain [room_name]")
        elif "close_curtain" in user_input.lower():
            try:
                room_name = user_input.split()[1]
                close_curtain(home, room_name)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: close_curtain [room_name]")
        elif "play_music" in user_input.lower():
            try:
                room_name, playlist = user_input.split()[1:]
                play_music(home, room_name, playlist)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: play_music [room_name] [playlist]")
        elif "stop_music" in user_input.lower():
            try:
                room_name = user_input.split()[1]
                stop_music(home, room_name)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: stop_music [room_name]")
        elif "make_coffee" in user_input.lower():
            try:
                room_name, coffee_type = user_input.split()[1:]
                make_coffee(home, room_name, coffee_type)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: make_coffee [room_name] [coffee_type]")
        elif "turn_on_tv" in user_input.lower():
            try:
                room_name, channel_name = user_input.split()[1:]
                turn_on_tv(home, room_name, channel_name)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: turn_on_tv [room_name] [channel_name]")
        elif "turn_off_tv" in user_input.lower():
            try:
                room_name = user_input.split()[1]
                turn_off_tv(home, room_name)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: turn_off_tv [room_name]")
        elif "start_cleaning_robot" in user_input.lower():
            try:
                room_name = user_input.split()[1]
                start_cleaning_robot(home, room_name)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: start_cleaning_robot [room_name]")
        elif "send_notification" in user_input.lower():
            try:
                room_name, message = user_input.split()[1:]
                send_notification(home, room_name, message)
            except (IndexError, ValueError):
                print("Invalid command format. Please use: send_notification [room_name] [message]")
        else:
            print("Invalid command. Please try again or enter 'help' for a list of commands.")

# Run the main function if the script is executed
if __name__ == "__main__":
    main()

# **Explanation of the Code:**

# 1. **Imports:** Necessary modules are imported, including:
#    - `home.home_plan`: For managing the home plan and accessing rooms, sensors, and actuators.
#    - `home.sensor`: For interacting with different sensor types.
#    - `home.actuator`: For interacting with different actuator types.
#    - `home.config`: For accessing configuration settings like temperature thresholds and wait durations.
#    - `time`: For pausing execution to simulate device actions.

# 2. **Functions:** Each function corresponds to a specific action the user can perform. Here's a breakdown:

#    - **`adjust_temperature(home, room_name, target_temperature)`:**
#      - Gets the room, heater, AC, and temperature sensor.
#      - Reads the current temperature.
#      - Turns on/off heater or AC based on the temperature difference.
#      - Sets the target temperature for both heater and AC.

#    - **`adjust_humidity(home, room_name, target_humidity)`:**
#      - Gets the room and humidifier.
#      - Reads the current humidity.
#      - Increases or decreases humidity using the humidifier.

#    - **`turn_on_light(home, room_name, brightness_level)`:**
#      - Gets the room and light.
#      - Turns on the light and sets the brightness level.

#    - **`turn_off_light(home, room_name)`:**
#      - Gets the room and light.
#      - Turns off the light.

#    - **`open_window(home, room_name)`:**
#      - Gets the room and window.
#      - Opens the window.

#    - **`close_window(home, room_name)`:**
#      - Gets the room and window.
#      - Closes the window.

#    - **`open_curtain(home, room_name)`:**
#      - Gets the room and curtain.
#      - Opens the curtain.

#    - **`close_curtain(home, room_name)`:**
#      - Gets the room and curtain.
#      - Closes the curtain.

#    - **`play_music(home, room_name, playlist)`:**
#      - Gets the room and music player.
#      - Turns on the music player and plays the playlist.

#    - **`stop_music(home, room_name)`:**
#      - Gets the room and music player.
#      - Turns off the music player.

#    - **`make_coffee(home, room_name, coffee_type)`:**
#      - Gets the room and coffee machine.
#      - Turns on the coffee machine and makes the requested coffee.

#    - **`turn_on_tv(home, room_name, channel_name)`:**
#      - Gets the room and Smart TV.
#      - Turns on the TV and plays the specified channel.

#    - **`turn_off_tv(home, room_name)`:**
#      - Gets the room and Smart TV.
#      - Turns off the TV.

#    - **`start_cleaning_robot(home, room_name)`:**
#      - Gets the room and cleaning robot.
#      - Turns on the cleaning robot and starts its daily routine.

#    - **`send_notification(home, room_name, message)`:**
#      - Gets the room and notification sender.
#      - Turns on the notification sender and sends the message.

# 3. **`main()` Function:**
#    - Creates the home plan using `home_plan()`.
#    - Prints the home plan using `print_home_plan()`.
#    - Enters an infinite loop for user interaction.
#    - Prompts the user for commands.
#    - Parses the user's input, extracting room names and other parameters.
#    - Calls the appropriate functions based on the command.
#    - Handles invalid commands and provides help information.

# **How to Use:**

# 1. **Run the `function.py` script:** This will start the interactive command prompt.
# 2. **Type commands:** Use the available commands (listed in the "help" command) to control your smart home.
# 3. **Exit:** Enter "exit" to terminate the program.

# **Example Interaction:**

# ```
# What would you like to do? (Enter 'help' for commands): help

# Available commands:
#   - adjust_temperature [room_name] [target_temperature]
#   - adjust_humidity [room_name] [target_humidity]
#   - turn_on_light [room_name] [brightness_level]
#   - turn_off_light [room_name]
#   - open_window [room_name]
#   - close_window [room_name]
#   - open_curtain [room_name]
#   - close_curtain [room_name]
#   - play_music [room_name] [playlist]
#   - stop_music [room_name]
#   - make_coffee [room_name] [coffee_type]
#   - turn_on_tv [room_name] [channel_name]
#   - turn_off_tv [room_name]
#   - start_cleaning_robot [room_name]
#   - send_notification [room_name] [message]
#   - exit

# What would you like to do? (Enter 'help' for commands): adjust_temperature LivingRoom 22

# Turning on AC in LivingRoom to reach 22.0°C.
# Temperature in LivingRoom is already at 22.0°C.

# What would you like to do? (Enter 'help' for commands): turn_on_light LivingRoom medium

# Turning on light in LivingRoom to MEDIUM brightness.

# What would you like to do? (Enter 'help' for commands): exit
# ```
