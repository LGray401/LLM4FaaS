from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

# Function to turn on all lights in a room
def turn_on_room_lights(home, room_name):
    """
    Turns on all lights in a specified room.

    Args:
        home: A list of Room objects representing the entire home.
        room_name: The name of the room to turn on the lights in.

    Returns:
        None.
    """

    lights = get_room_actuators(home, room_name)
    if lights:
        for light in lights:
            if light.actuator_type == "Light":
                if light.status == "off":
                    light.turn_on()
                    print(f"Turned on {light.id}")


# Function to turn off all lights in a room
def turn_off_room_lights(home, room_name):
    """
    Turns off all lights in a specified room.

    Args:
        home: A list of Room objects representing the entire home.
        room_name: The name of the room to turn off the lights in.

    Returns:
        None.
    """

    lights = get_room_actuators(home, room_name)
    if lights:
        for light in lights:
            if light.actuator_type == "Light":
                if light.status == "on":
                    light.turn_off()
                    print(f"Turned off {light.id}")


# Function to adjust the temperature of a room
def adjust_room_temperature(home, room_name, target_temperature):
    """
    Adjusts the temperature of a specified room using either a heater or AC.

    Args:
        home: A list of Room objects representing the entire home.
        room_name: The name of the room to adjust the temperature in.
        target_temperature: The desired temperature for the room.

    Returns:
        None.
    """

    room = get_room(home, room_name)
    if room:
        indoor_temp_sensors = get_room_sensors(home, room_name)
        if indoor_temp_sensors:
            for sensor in indoor_temp_sensors:
                if sensor.sensor_type == "IndoorTemperature":
                    current_temperature = sensor.get_reading()
                    if current_temperature is not None:
                        # Get heater and AC actuators in the room
                        heater = None
                        ac = None
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Heater":
                                heater = actuator
                            elif actuator.actuator_type == "AC":
                                ac = actuator
                        # Adjust temperature using heater or AC
                        if heater:
                            heater.set_target_temperature(target_temperature)
                            heater.adjust_temperature(current_temperature)
                        if ac:
                            ac.set_target_temperature(target_temperature)
                            ac.adjust_temperature(current_temperature)

# Function to play music in a room
def play_music_in_room(home, room_name, playlist_name):
    """
    Plays music in a specified room using a MusicPlayer.

    Args:
        home: A list of Room objects representing the entire home.
        room_name: The name of the room to play music in.
        playlist_name: The name of the playlist to play.

    Returns:
        None.
    """

    music_players = get_room_actuators(home, room_name)
    if music_players:
        for music_player in music_players:
            if music_player.actuator_type == "MusicPlayer":
                music_player.play_music(playlist_name)

# Function to send a notification to a room
def send_notification_to_room(home, room_name, message):
    """
    Sends a notification to a specified room using a NotificationSender.

    Args:
        home: A list of Room objects representing the entire home.
        room_name: The name of the room to send the notification to.
        message: The notification message to send.

    Returns:
        None.
    """

    notification_senders = get_room_actuators(home, room_name)
    if notification_senders:
        for notification_sender in notification_senders:
            if notification_sender.actuator_type == "NotificationSender":
                notification_sender.notification_sender(message)

# Function to open or close windows in a room based on temperature
def adjust_windows_for_temperature(home, room_name):
    """
    Adjusts the windows in a specified room based on the indoor temperature.

    Args:
        home: A list of Room objects representing the entire home.
        room_name: The name of the room to adjust the windows in.

    Returns:
        None.
    """

    room = get_room(home, room_name)
    if room:
        indoor_temp_sensors = get_room_sensors(home, room_name)
        if indoor_temp_sensors:
            for sensor in indoor_temp_sensors:
                if sensor.sensor_type == "IndoorTemperature":
                    current_temperature = sensor.get_reading()
                    if current_temperature is not None:
                        # Get windows in the room
                        windows = []
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Window":
                                windows.append(actuator)
                        # Adjust windows based on temperature
                        if current_temperature > TEMP_HIGH:
                            for window in windows:
                                if window.status == "off":
                                    window.turn_on()
                                    print(f"Opened {window.id}")
                        elif current_temperature < TEMP_LOW:
                            for window in windows:
                                if window.status == "on":
                                    window.turn_off()
                                    print(f"Closed {window.id}")

# Function to open or close curtains in a room based on light intensity
def adjust_curtains_for_light(home, room_name):
    """
    Adjusts the curtains in a specified room based on the light intensity.

    Args:
        home: A list of Room objects representing the entire home.
        room_name: The name of the room to adjust the curtains in.

    Returns:
        None.
    """

    room = get_room(home, room_name)
    if room:
        light_intensive_sensors = get_room_sensors(home, room_name)
        if light_intensive_sensors:
            for sensor in light_intensive_sensors:
                if sensor.sensor_type == "LightIntensive":
                    light_intensity = sensor.get_reading()
                    if light_intensity is not None:
                        # Get curtains in the room
                        curtains = []
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Curtain":
                                curtains.append(actuator)
                        # Adjust curtains based on light intensity
                        if light_intensity < LIGHT_INTENSITY_LOW:
                            for curtain in curtains:
                                if curtain.status == "off":
                                    curtain.turn_on()
                                    print(f"Opened {curtain.id}")
                        elif light_intensity > LIGHT_INTENSITY_HIGH:
                            for curtain in curtains:
                                if curtain.status == "on":
                                    curtain.turn_off()
                                    print(f"Closed {curtain.id}")

# Function to make coffee in the kitchen
def make_coffee_in_kitchen(home, coffee_type):
    """
    Makes coffee in the kitchen using a CoffeeMachine.

    Args:
        home: A list of Room objects representing the entire home.
        coffee_type: The type of coffee to make.

    Returns:
        None.
    """

    kitchen = get_room(home, "Kitchen")
    if kitchen:
        coffee_machines = get_room_actuators(home, "Kitchen")
        if coffee_machines:
            for coffee_machine in coffee_machines:
                if coffee_machine.actuator_type == "CoffeeMachine":
                    coffee_machine.make_coffee(coffee_type)

# Function to start the daily cleaning routine of the cleaning robot
def start_daily_cleaning_routine(home):
    """
    Starts the daily cleaning routine of all cleaning robots in the home.

    Args:
        home: A list of Room objects representing the entire home.

    Returns:
        None.
    """

    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    if cleaning_robots:
        for cleaning_robot in cleaning_robots:
            cleaning_robot.daily_routine()

# Function to turn on the TV in the living room and play a specific channel
def turn_on_tv_and_play_channel(home, channel_name):
    """
    Turns on the TV in the living room and plays a specific channel.

    Args:
        home: A list of Room objects representing the entire home.
        channel_name: The name of the channel to play.

    Returns:
        None.
    """

    living_room = get_room(home, "LivingRoom")
    if living_room:
        smart_tvs = get_room_actuators(home, "LivingRoom")
        if smart_tvs:
            for smart_tv in smart_tvs:
                if smart_tv.actuator_type == "SmartTV":
                    smart_tv.play_channel(channel_name)

# Main function to execute different smart home scenarios
def main():
    """
    Main function to execute different smart home scenarios.

    This function demonstrates how to use the defined functions to interact with the smart home system.
    """

    home = home_plan()
    
    print("\n--- Morning Plan ---")
    
    # Turn on lights in the kitchen and living room
    turn_on_room_lights(home, "Kitchen")
    turn_on_room_lights(home, "LivingRoom")

    # Make coffee in the kitchen
    make_coffee_in_kitchen(home, "Espresso")

    # Adjust temperature in the living room to 22 degrees
    adjust_room_temperature(home, "LivingRoom", 22)

    # Start daily cleaning routine
    start_daily_cleaning_routine(home)

    print("\n--- Leave Home Plan ---")

    # Turn off all lights in the home
    for room_name in ["Kitchen", "LivingRoom", "Bedroom", "Bathroom"]:
        turn_off_room_lights(home, room_name)

    # Lock the door in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        doors = get_room_actuators(home, "LivingRoom")
        if doors:
            for door in doors:
                if door.actuator_type == "Door":
                    door.lock()

    # Turn on the notification sender in the living room and send a message
    send_notification_to_room(home, "LivingRoom", "Leaving home now. Be back later!")

    print("\n--- Movie Plan ---")

    # Turn off lights in the living room
    turn_off_room_lights(home, "LivingRoom")

    # Turn on the TV and play Netflix
    turn_on_tv_and_play_channel(home, "Netflix")

if __name__ == "__main__":
    main()

# This `function.py` file contains functions that implement the functional descriptions you provided. It demonstrates how to interact with the smart home system using these functions.

# Here's a breakdown of the functions and how they relate to your descriptions:

# - **`turn_on_room_lights` and `turn_off_room_lights`:** These functions directly correspond to actions like turning on or off all lights in a specific room.
# - **`adjust_room_temperature`:**  This function demonstrates the temperature control functionality, adjusting the heater or AC based on the target temperature.
# - **`play_music_in_room`:** This function allows you to control the music player in a specific room.
# - **`send_notification_to_room`:** This function sends notifications using the notification sender in a specific room.
# - **`adjust_windows_for_temperature`:** This function demonstrates a more complex scenario where windows are automatically opened or closed based on temperature thresholds.
# - **`adjust_curtains_for_light`:** This function demonstrates automatic curtain control based on light intensity.
# - **`make_coffee_in_kitchen`:** This function allows you to control the coffee machine in the kitchen.
# - **`start_daily_cleaning_routine`:** This function triggers the daily cleaning routine of the cleaning robots in the home.
# - **`turn_on_tv_and_play_channel`:** This function turns on the TV in the living room and plays a specific channel.

# The `main` function demonstrates how to use these functions to execute different smart home scenarios based on the functional descriptions you provided.

# You can modify and add more functions to this file to implement additional features or scenarios for your smart home project.
