from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger

home = home_plan()

def adjust_temperature(room_name, target_temperature):
    """Adjusts the temperature in a room using heaters and ACs.

    Args:
        room_name (str): The name of the room.
        target_temperature (float): The desired temperature in Celsius.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find heaters and ACs in the room
        heaters = get_room_actuators(home, room_name, Heater)
        acs = get_room_actuators(home, room_name, AC)
        # Get current temperature
        temp_sensors = get_room_sensors(home, room_name, IndoorTemperatureSensor)
        if temp_sensors:
            current_temperature = temp_sensors[0].get_reading()
        else:
            logger.warning(f"No temperature sensor found in {room_name}. Cannot adjust temperature.")
            return
        # Adjust temperature using heaters and ACs
        if current_temperature < target_temperature:
            # Turn on heaters
            for heater in heaters:
                heater.turn_on()
                heater.set_target_temperature(target_temperature)
        elif current_temperature > target_temperature:
            # Turn on ACs
            for ac in acs:
                ac.turn_on()
                ac.set_target_temperature(target_temperature)
        else:
            # Turn off heaters and ACs
            for heater in heaters:
                heater.turn_off()
            for ac in acs:
                ac.turn_off()
        # Log the temperature adjustment
        logger.info(f"Adjusted temperature in {room_name} to {target_temperature}°C.")
        print(f"Adjusted temperature in {room_name} to {target_temperature}°C.")
    else:
        logger.warning(f"Room {room_name} not found.")

def adjust_humidity(room_name, target_humidity):
    """Adjusts the humidity in a room using humidifiers.

    Args:
        room_name (str): The name of the room.
        target_humidity (float): The desired humidity level in percentage.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find humidifiers in the room
        humidifiers = get_room_actuators(home, room_name, Humidifier)
        # Get current humidity
        humidity_sensors = get_room_sensors(home, room_name, HumiditySensor)
        if humidity_sensors:
            current_humidity = humidity_sensors[0].get_reading()
        else:
            logger.warning(f"No humidity sensor found in {room_name}. Cannot adjust humidity.")
            return
        # Adjust humidity using humidifiers
        if current_humidity < target_humidity:
            # Increase humidity
            for humidifier in humidifiers:
                humidifier.increase_humidity()
        elif current_humidity > target_humidity:
            # Decrease humidity
            for humidifier in humidifiers:
                humidifier.decrease_humidity()
        else:
            # No action required
            logger.info(f"Humidity in {room_name} is already at the desired level.")
        # Log the humidity adjustment
        logger.info(f"Adjusted humidity in {room_name} to {target_humidity}%.")
        print(f"Adjusted humidity in {room_name} to {target_humidity}%.")
    else:
        logger.warning(f"Room {room_name} not found.")

def adjust_light_intensity(room_name, target_intensity):
    """Adjusts the light intensity in a room using lights.

    Args:
        room_name (str): The name of the room.
        target_intensity (float): The desired light intensity in lux.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find lights in the room
        lights = get_room_actuators(home, room_name, Light)
        # Get current light intensity
        light_sensors = get_room_sensors(home, room_name, LightIntensiveSensor)
        if light_sensors:
            current_intensity = light_sensors[0].get_reading()
        else:
            logger.warning(f"No light intensity sensor found in {room_name}. Cannot adjust light intensity.")
            return
        # Adjust light intensity using lights
        if current_intensity < target_intensity:
            # Turn on lights
            for light in lights:
                light.turn_on()
                if target_intensity < LIGHT_INTENSITY_HIGH:
                    light.set_brightness_level("medium")
                else:
                    light.set_brightness_level("high")
        elif current_intensity > target_intensity:
            # Turn off lights
            for light in lights:
                light.turn_off()
        else:
            # No action required
            logger.info(f"Light intensity in {room_name} is already at the desired level.")
        # Log the light intensity adjustment
        logger.info(f"Adjusted light intensity in {room_name} to {target_intensity} lux.")
        print(f"Adjusted light intensity in {room_name} to {target_intensity} lux.")
    else:
        logger.warning(f"Room {room_name} not found.")

def open_windows(room_name):
    """Opens the windows in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find windows in the room
        windows = get_room_actuators(home, room_name, Window)
        # Open windows
        for window in windows:
            window.turn_on()
        # Log the window opening
        logger.info(f"Opened windows in {room_name}.")
        print(f"Opened windows in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def close_windows(room_name):
    """Closes the windows in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find windows in the room
        windows = get_room_actuators(home, room_name, Window)
        # Close windows
        for window in windows:
            window.turn_off()
        # Log the window closing
        logger.info(f"Closed windows in {room_name}.")
        print(f"Closed windows in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def open_curtains(room_name):
    """Opens the curtains in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find curtains in the room
        curtains = get_room_actuators(home, room_name, Curtain)
        # Open curtains
        for curtain in curtains:
            curtain.turn_on()
        # Log the curtain opening
        logger.info(f"Opened curtains in {room_name}.")
        print(f"Opened curtains in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def close_curtains(room_name):
    """Closes the curtains in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find curtains in the room
        curtains = get_room_actuators(home, room_name, Curtain)
        # Close curtains
        for curtain in curtains:
            curtain.turn_off()
        # Log the curtain closing
        logger.info(f"Closed curtains in {room_name}.")
        print(f"Closed curtains in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def play_music(room_name, playlist):
    """Plays music in a room.

    Args:
        room_name (str): The name of the room.
        playlist (str): The name of the playlist to play.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find music players in the room
        music_players = get_room_actuators(home, room_name, MusicPlayer)
        # Play music
        for music_player in music_players:
            music_player.play_music(playlist)
        # Log the music playing
        logger.info(f"Playing music in {room_name}.")
        print(f"Playing music in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def turn_on_lights(room_name):
    """Turns on the lights in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find lights in the room
        lights = get_room_actuators(home, room_name, Light)
        # Turn on lights
        for light in lights:
            light.turn_on()
        # Log the light turning on
        logger.info(f"Turned on lights in {room_name}.")
        print(f"Turned on lights in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def turn_off_lights(room_name):
    """Turns off the lights in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find lights in the room
        lights = get_room_actuators(home, room_name, Light)
        # Turn off lights
        for light in lights:
            light.turn_off()
        # Log the light turning off
        logger.info(f"Turned off lights in {room_name}.")
        print(f"Turned off lights in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def send_notification(room_name, message):
    """Sends a notification in a room.

    Args:
        room_name (str): The name of the room.
        message (str): The message to send.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find notification senders in the room
        notification_senders = get_room_actuators(home, room_name, NotificationSender)
        # Send notification
        for notification_sender in notification_senders:
            notification_sender.notification_sender(message)
        # Log the notification sending
        logger.info(f"Sent notification in {room_name}: {message}.")
        print(f"Sent notification in {room_name}: {message}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def start_cleaning_robot(room_name):
    """Starts the cleaning robot in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find cleaning robots in the room
        cleaning_robots = get_room_actuators(home, room_name, CleaningRobot)
        # Start cleaning robots
        for cleaning_robot in cleaning_robots:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()
        # Log the cleaning robot starting
        logger.info(f"Started cleaning robot in {room_name}.")
        print(f"Started cleaning robot in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def turn_on_coffee_machine(room_name):
    """Turns on the coffee machine in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find coffee machines in the room
        coffee_machines = get_room_actuators(home, room_name, CoffeeMachine)
        # Turn on coffee machines
        for coffee_machine in coffee_machines:
            coffee_machine.turn_on()
        # Log the coffee machine turning on
        logger.info(f"Turned on coffee machine in {room_name}.")
        print(f"Turned on coffee machine in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def make_coffee(room_name, coffee_type):
    """Makes coffee using the coffee machine in a room.

    Args:
        room_name (str): The name of the room.
        coffee_type (str): The type of coffee to make.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find coffee machines in the room
        coffee_machines = get_room_actuators(home, room_name, CoffeeMachine)
        # Make coffee
        for coffee_machine in coffee_machines:
            coffee_machine.make_coffee(coffee_type)
        # Log the coffee making
        logger.info(f"Made {coffee_type} coffee in {room_name}.")
        print(f"Made {coffee_type} coffee in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def turn_on_tv(room_name):
    """Turns on the TV in a room.

    Args:
        room_name (str): The name of the room.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find TVs in the room
        tvs = get_room_actuators(home, room_name, SmartTV)
        # Turn on TVs
        for tv in tvs:
            tv.turn_on()
        # Log the TV turning on
        logger.info(f"Turned on TV in {room_name}.")
        print(f"Turned on TV in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def play_channel(room_name, channel_name):
    """Plays a channel on the TV in a room.

    Args:
        room_name (str): The name of the room.
        channel_name (str): The name of the channel to play.
    """
    room = get_room(home, room_name)
    if room is not None:
        # Find TVs in the room
        tvs = get_room_actuators(home, room_name, SmartTV)
        # Play channel
        for tv in tvs:
            tv.play_channel(channel_name)
        # Log the channel playing
        logger.info(f"Playing channel {channel_name} on TV in {room_name}.")
        print(f"Playing channel {channel_name} on TV in {room_name}.")
    else:
        logger.warning(f"Room {room_name} not found.")

def main():
    # Example usage
    adjust_temperature("LivingRoom", 20)
    adjust_humidity("Bathroom", 40)
    adjust_light_intensity("Bedroom", 500)
    open_windows("LivingRoom")
    close_windows("Kitchen")
    open_curtains("Bedroom")
    close_curtains("LivingRoom")
    play_music("LivingRoom", "Pop Hits")
    turn_on_lights("Kitchen")
    turn_off_lights("Bathroom")
    send_notification("LivingRoom", "Reminder: Don't forget to take out the trash.")
    start_cleaning_robot("Bedroom")
    turn_on_coffee_machine("Kitchen")
    make_coffee("Kitchen", "Espresso")
    turn_on_tv("LivingRoom")
    play_channel("LivingRoom", "CNN")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions for managing the home plan (rooms, sensors, actuators).
#    - `home.sensor`: Contains sensor classes (IndoorTemperatureSensor, HumiditySensor, etc.).
#    - `home.actuator`: Contains actuator classes (Light, Heater, AC, etc.).
#    - `home.config`: Contains configuration settings (temperature thresholds, etc.).
#    - `home.logger_config`: Contains logging configuration to write messages to a file.

# 2. **Create the home plan:**
#    - `home = home_plan()`: Calls the `home_plan` function to create the home plan, which initializes rooms and their components (sensors and actuators).

# 3. **Define functions for interacting with the smart home:**
#    - **`adjust_temperature(room_name, target_temperature)`:**
#      - Retrieves the room using `get_room`.
#      - Finds heaters and ACs in the room using `get_room_actuators`.
#      - Gets the current temperature from the temperature sensor using `get_room_sensors`.
#      - Turns on heaters or ACs based on the target temperature and the current temperature.
#      - Logs the temperature adjustment.
#    - **`adjust_humidity(room_name, target_humidity)`:**
#      - Similar to `adjust_temperature`, but uses humidifiers to adjust humidity.
#    - **`adjust_light_intensity(room_name, target_intensity)`:**
#      - Similar to `adjust_temperature`, but uses lights to adjust light intensity.
#    - **`open_windows(room_name)`:**
#      - Finds windows in the room and turns them on.
#      - Logs the window opening.
#    - **`close_windows(room_name)`:**
#      - Finds windows in the room and turns them off.
#      - Logs the window closing.
#    - **`open_curtains(room_name)`:**
#      - Finds curtains in the room and turns them on.
#      - Logs the curtain opening.
#    - **`close_curtains(room_name)`:**
#      - Finds curtains in the room and turns them off.
#      - Logs the curtain closing.
#    - **`play_music(room_name, playlist)`:**
#      - Finds music players in the room and plays the specified playlist.
#      - Logs the music playing.
#    - **`turn_on_lights(room_name)`:**
#      - Finds lights in the room and turns them on.
#      - Logs the light turning on.
#    - **`turn_off_lights(room_name)`:**
#      - Finds lights in the room and turns them off.
#      - Logs the light turning off.
#    - **`send_notification(room_name, message)`:**
#      - Finds notification senders in the room and sends the message.
#      - Logs the notification sending.
#    - **`start_cleaning_robot(room_name)`:**
#      - Finds cleaning robots in the room, turns them on, and starts the cleaning routine.
#      - Logs the cleaning robot starting.
#    - **`turn_on_coffee_machine(room_name)`:**
#      - Finds coffee machines in the room and turns them on.
#      - Logs the coffee machine turning on.
#    - **`make_coffee(room_name, coffee_type)`:**
#      - Finds coffee machines in the room and makes the specified coffee.
#      - Logs the coffee making.
#    - **`turn_on_tv(room_name)`:**
#      - Finds TVs in the room and turns them on.
#      - Logs the TV turning on.
#    - **`play_channel(room_name, channel_name)`:**
#      - Finds TVs in the room and plays the specified channel.
#      - Logs the channel playing.

# 4. **`main()` function:**
#    - Contains example usage of the functions to demonstrate how to interact with the smart home.

# **Remember:** This is a basic example. You can extend it by adding more sensors, actuators, functions, and logic to create a more comprehensive and intelligent smart home system.
