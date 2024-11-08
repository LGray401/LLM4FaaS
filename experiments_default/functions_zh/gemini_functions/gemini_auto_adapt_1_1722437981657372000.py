from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.actuator import Light, Heater, AC, CoffeeMachine, CleaningRobot, NotificationSender, MusicPlayer, Humidifier
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
import time

def handle_temperature_command(home, room_name, target_temperature):
    room = get_room(home, room_name)
    if room:
        temperature_sensors = get_room_sensors(home, room_name)
        heaters = get_room_actuators(home, room_name, "Heater")
        acs = get_room_actuators(home, room_name, "AC")

        if temperature_sensors and (heaters or acs):
            # Get the current temperature reading
            current_temperature = temperature_sensors[0].get_reading()  # Assuming only one temperature sensor in the room

            if current_temperature is not None:
                # Adjust the temperature based on the target temperature
                if target_temperature > current_temperature:
                    if heaters:
                        for heater in heaters:
                            heater.turn_on()
                            heater.set_target_temperature(target_temperature)
                            print(f"Turning on heater in {room_name} to {target_temperature}°C.")
                elif target_temperature < current_temperature:
                    if acs:
                        for ac in acs:
                            ac.turn_on()
                            ac.set_target_temperature(target_temperature)
                            print(f"Turning on AC in {room_name} to {target_temperature}°C.")
                else:
                    print(f"Temperature in {room_name} is already at the desired temperature.")
            else:
                print(f"Error getting temperature reading in {room_name}.")
        else:
            print(f"No temperature sensors or temperature control actuators found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")

def handle_humidity_command(home, room_name, target_humidity):
    room = get_room(home, room_name)
    if room:
        humidity_sensors = get_room_sensors(home, room_name, "Humidity")
        humidifiers = get_room_actuators(home, room_name, "Humidifier")

        if humidity_sensors and humidifiers:
            # Get the current humidity reading
            current_humidity = humidity_sensors[0].get_reading()  # Assuming only one humidity sensor in the room

            if current_humidity is not None:
                # Adjust the humidity based on the target humidity
                if target_humidity > current_humidity:
                    for humidifier in humidifiers:
                        humidifier.increase_humidity()
                        print(f"Increasing humidity in {room_name}.")
                elif target_humidity < current_humidity:
                    for humidifier in humidifiers:
                        humidifier.decrease_humidity()
                        print(f"Decreasing humidity in {room_name}.")
                else:
                    print(f"Humidity in {room_name} is already at the desired level.")
            else:
                print(f"Error getting humidity reading in {room_name}.")
        else:
            print(f"No humidity sensors or humidifiers found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")

def handle_light_intensity_command(home, room_name, light_intensity_level):
    room = get_room(home, room_name)
    if room:
        lights = get_room_actuators(home, room_name, "Light")
        if lights:
            for light in lights:
                light.turn_on()
                light.set_brightness_level(light_intensity_level)
                print(f"Setting light intensity in {room_name} to {light_intensity_level.upper()}.")
        else:
            print(f"No lights found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")


def handle_coffee_command(home, room_name, coffee_type):
    room = get_room(home, room_name)
    if room:
        coffee_machines = get_room_actuators(home, room_name, "CoffeeMachine")
        if coffee_machines:
            for coffee_machine in coffee_machines:
                coffee_machine.turn_on()
                coffee_machine.make_coffee(coffee_type)
                print(f"Making {coffee_type} coffee in {room_name}.")
        else:
            print(f"No coffee machine found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")

def handle_cleaning_robot_command(home, room_name):
    room = get_room(home, room_name)
    if room:
        cleaning_robots = get_room_actuators(home, room_name, "CleaningRobot")
        if cleaning_robots:
            for cleaning_robot in cleaning_robots:
                cleaning_robot.turn_on()
                cleaning_robot.daily_routine()
                print(f"Starting daily cleaning routine in {room_name}.")
        else:
            print(f"No cleaning robot found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")

def handle_music_command(home, room_name, playlist):
    room = get_room(home, room_name)
    if room:
        music_players = get_room_actuators(home, room_name, "MusicPlayer")
        if music_players:
            for music_player in music_players:
                music_player.turn_on()
                music_player.play_music(playlist)
                print(f"Playing {playlist} in {room_name}.")
        else:
            print(f"No music player found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")

def handle_notification_command(home, room_name, message):
    room = get_room(home, room_name)
    if room:
        notification_senders = get_room_actuators(home, room_name, "NotificationSender")
        if notification_senders:
            for notification_sender in notification_senders:
                notification_sender.turn_on()
                notification_sender.notification_sender(message)
                print(f"Sending notification in {room_name}: {message}")
        else:
            print(f"No notification sender found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")

def handle_command(command):
    home = home_plan()
    command_parts = command.split()
    
    if command_parts[0].lower() == "temperature":
        room_name = command_parts[1]
        target_temperature = float(command_parts[2])
        handle_temperature_command(home, room_name, target_temperature)

    elif command_parts[0].lower() == "humidity":
        room_name = command_parts[1]
        target_humidity = float(command_parts[2])
        handle_humidity_command(home, room_name, target_humidity)
    
    elif command_parts[0].lower() == "light":
        room_name = command_parts[1]
        light_intensity_level = command_parts[2].lower()  # Convert to lowercase for comparison
        handle_light_intensity_command(home, room_name, light_intensity_level)

    elif command_parts[0].lower() == "coffee":
        room_name = command_parts[1]
        coffee_type = command_parts[2]
        handle_coffee_command(home, room_name, coffee_type)

    elif command_parts[0].lower() == "clean":
        room_name = command_parts[1]
        handle_cleaning_robot_command(home, room_name)

    elif command_parts[0].lower() == "music":
        room_name = command_parts[1]
        playlist = command_parts[2]
        handle_music_command(home, room_name, playlist)

    elif command_parts[0].lower() == "notify":
        room_name = command_parts[1]
        message = " ".join(command_parts[2:])
        handle_notification_command(home, room_name, message)

    else:
        print("Invalid command.")


if __name__ == "__main__":
    while True:
        command = input("Enter a command: ")
        handle_command(command)

# **Explanation:**

# 1. **Import Necessary Modules:**
#    - `home.home_plan`: Contains functions to work with the home plan (rooms, sensors, actuators).
#    - `home.actuator`: Contains classes for different actuator types (lights, heaters, etc.).
#    - `home.sensor`: Contains classes for different sensor types (temperature, humidity, etc.).
#    - `time`: Used for pausing execution during actions like cleaning.

# 2. **`handle_temperature_command(home, room_name, target_temperature)`:**
#    - Gets the `room` from the `home` plan based on `room_name`.
#    - Retrieves temperature sensors and heaters/ACs from the room.
#    - If both sensors and actuators exist:
#      - Reads the current temperature using the first temperature sensor.
#      - Turns on heaters/ACs and sets the target temperature if needed.

# 3. **`handle_humidity_command(home, room_name, target_humidity)`:**
#    - Similar to `handle_temperature_command` but for humidity.
#    - Uses humidifiers to adjust humidity levels.

# 4. **`handle_light_intensity_command(home, room_name, light_intensity_level)`:**
#    - Turns on lights in the specified room and sets the brightness level.

# 5. **`handle_coffee_command(home, room_name, coffee_type)`:**
#    - Turns on the coffee machine in the specified room and makes coffee of the specified type.

# 6. **`handle_cleaning_robot_command(home, room_name)`:**
#    - Turns on the cleaning robot in the specified room and starts its daily routine.

# 7. **`handle_music_command(home, room_name, playlist)`:**
#    - Turns on the music player in the specified room and starts playing the given playlist.

# 8. **`handle_notification_command(home, room_name, message)`:**
#    - Turns on the notification sender in the specified room and sends the given message.

# 9. **`handle_command(command)`:**
#    - Parses the user input command.
#    - Calls the appropriate handler function based on the command type.
#    - Handles invalid commands gracefully.

# 10. **Main Loop:**
#    - Continuously prompts the user for a command.
#    - Calls `handle_command` to process the command.

# **Key Improvements:**

# - **Clear Function Separation:** Each function handles a specific command, making the code more organized and easier to understand.
# - **Error Handling:** Each handler function checks for the presence of necessary sensors and actuators, and provides appropriate feedback to the user.
# - **User-Friendly Output:** The code provides informative messages to the user, indicating what actions are being performed.
# - **Consistent Command Structure:** The command format is consistent, requiring room name and other relevant information.

# **To Run This Code:**

# 1. **Save:** Save the above code as `function.py` in the `functions` folder of your project.
# 2. **Run:** Execute the `function.py` file from your terminal using: `python functions/function.py`

# Now, when you run the code, it will continuously prompt you for commands, and you can use the commands outlined in the explanation to interact with your smart home. 
