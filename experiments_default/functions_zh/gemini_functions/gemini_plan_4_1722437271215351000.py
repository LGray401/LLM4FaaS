from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Light, Curtain, AC, Heater, CoffeeMachine, NotificationSender, MusicPlayer, CleaningRobot, \
    SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger

# Function to turn on/off all lights in the house
def control_all_lights(home, status):
    lights = get_all_actuators(home, "Light")
    if lights:
        for light in lights:
            if status == "on":
                light.turn_on()
            elif status == "off":
                light.turn_off()
    else:
        print("There are no lights in the house.")
        logger.warning("There are no lights in the house.")


# Function to set the temperature in a room
def set_room_temperature(home, room_name, target_temperature):
    room = get_room(home, room_name)
    if room:
        ac = get_room_actuators(home, room_name)
        heater = get_room_actuators(home, room_name)
        if ac:
            ac[0].set_target_temperature(target_temperature)
        if heater:
            heater[0].set_target_temperature(target_temperature)
        print(f"Setting the target temperature in {room_name} to {target_temperature} degrees Celsius.")
        logger.info(f"Setting the target temperature in {room_name} to {target_temperature} degrees Celsius.")
    else:
        print(f"There is no room called {room_name}.")
        logger.warning(f"There is no room called {room_name}.")


# Function to open/close curtains in a room
def control_curtains(home, room_name, status):
    room = get_room(home, room_name)
    if room:
        curtains = get_room_actuators(home, room_name)
        if curtains:
            for curtain in curtains:
                if status == "open":
                    curtain.turn_on()
                elif status == "close":
                    curtain.turn_off()
            print(f"Curtains in {room_name} are now {status}.")
            logger.info(f"Curtains in {room_name} are now {status}.")
        else:
            print(f"There are no curtains in {room_name}.")
            logger.warning(f"There are no curtains in {room_name}.")
    else:
        print(f"There is no room called {room_name}.")
        logger.warning(f"There is no room called {room_name}.")


# Function to play music in a room
def play_music_in_room(home, room_name, playlist):
    room = get_room(home, room_name)
    if room:
        music_players = get_room_actuators(home, room_name)
        if music_players:
            for music_player in music_players:
                music_player.play_music(playlist)
            print(f"Playing {playlist} in {room_name}.")
            logger.info(f"Playing {playlist} in {room_name}.")
        else:
            print(f"There is no music player in {room_name}.")
            logger.warning(f"There is no music player in {room_name}.")
    else:
        print(f"There is no room called {room_name}.")
        logger.warning(f"There is no room called {room_name}.")


# Function to start the daily cleaning routine for a robot in a room
def start_cleaning_routine(home, room_name):
    room = get_room(home, room_name)
    if room:
        cleaning_robots = get_room_actuators(home, room_name)
        if cleaning_robots:
            for cleaning_robot in cleaning_robots:
                cleaning_robot.daily_routine()
            print(f"Cleaning robot in {room_name} has started its daily cleaning routine.")
            logger.info(f"Cleaning robot in {room_name} has started its daily cleaning routine.")
        else:
            print(f"There is no cleaning robot in {room_name}.")
            logger.warning(f"There is no cleaning robot in {room_name}.")
    else:
        print(f"There is no room called {room_name}.")
        logger.warning(f"There is no room called {room_name}.")

# Function to send a notification message to a room
def send_notification_to_room(home, room_name, message):
    room = get_room(home, room_name)
    if room:
        notification_senders = get_room_actuators(home, room_name)
        if notification_senders:
            for notification_sender in notification_senders:
                notification_sender.notification_sender(message)
            print(f"Notification sent to {room_name}: {message}")
            logger.info(f"Notification sent to {room_name}: {message}")
        else:
            print(f"There is no notification sender in {room_name}.")
            logger.warning(f"There is no notification sender in {room_name}.")
    else:
        print(f"There is no room called {room_name}.")
        logger.warning(f"There is no room called {room_name}.")

# Function to make coffee in the kitchen
def make_coffee(home, coffee_type):
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        coffee_machines = get_room_actuators(home, "Kitchen")
        if coffee_machines:
            for coffee_machine in coffee_machines:
                coffee_machine.make_coffee(coffee_type)
            print(f"Making {coffee_type} in the kitchen.")
            logger.info(f"Making {coffee_type} in the kitchen.")
        else:
            print("There is no coffee machine in the kitchen.")
            logger.warning("There is no coffee machine in the kitchen.")
    else:
        print("There is no kitchen in the house.")
        logger.warning("There is no kitchen in the house.")

# Function to adjust temperature based on sensor readings
def adjust_temperature_in_room(home, room_name):
    room = get_room(home, room_name)
    if room:
        # Get temperature sensor reading
        temp_sensor = get_room_sensors(home, room_name)
        if temp_sensor:
            current_temperature = temp_sensor[0].get_reading()
            print(f"Current temperature in {room_name}: {current_temperature} degrees Celsius.")
            logger.info(f"Current temperature in {room_name}: {current_temperature} degrees Celsius.")

            # Get AC and heater actuators
            ac = get_room_actuators(home, room_name)
            heater = get_room_actuators(home, room_name)

            # Adjust temperature based on sensor reading
            if ac:
                ac[0].adjust_temperature(current_temperature)
            if heater:
                heater[0].adjust_temperature(current_temperature)
        else:
            print(f"There is no temperature sensor in {room_name}.")
            logger.warning(f"There is no temperature sensor in {room_name}.")
    else:
        print(f"There is no room called {room_name}.")
        logger.warning(f"There is no room called {room_name}.")

# Function for morning plan
def morning_plan(home):
    print("\n--- Morning Plan ---")
    logger.info("Starting Morning Plan")
    
    # Open curtains in all rooms
    for room in home:
        control_curtains(home, room.name, "open")

    # Make coffee in the kitchen
    make_coffee(home, "espresso")

    # Turn on lights in the living room
    control_all_lights(home, "on")

# Function for leaving home plan
def leave_home_plan(home):
    print("\n--- Leaving Home Plan ---")
    logger.info("Starting Leaving Home Plan")

    # Turn off all lights
    control_all_lights(home, "off")

    # Close curtains in all rooms
    for room in home:
        control_curtains(home, room.name, "close")

    # Send a notification to the living room
    send_notification_to_room(home, "LivingRoom", "Leaving home now.")

    # Lock all doors in the house
    for room in home:
        doors = get_room_actuators(home, room.name)
        if doors:
            for door in doors:
                door.lock()

# Function for movie plan
def movie_plan(home, room_name):
    print(f"\n--- Movie Plan in {room_name} ---")
    logger.info(f"Starting Movie Plan in {room_name}")

    # Turn on the lights in the room and set them to low brightness
    room = get_room(home, room_name)
    if room:
        lights = get_room_actuators(home, room_name)
        if lights:
            for light in lights:
                light.turn_on()
                light.set_brightness_level("low")
        else:
            print(f"There are no lights in {room_name}.")
            logger.warning(f"There are no lights in {room_name}.")

    # Turn on the TV and play a movie channel
    smart_tv = get_room_actuators(home, room_name)
    if smart_tv:
        for tv in smart_tv:
            tv.turn_on()
            tv.play_channel("Movie Channel")
    else:
        print(f"There is no smart TV in {room_name}.")
        logger.warning(f"There is no smart TV in {room_name}.")

# Function for temperature control based on sensor readings
def temperature_control(home):
    print("\n--- Temperature Control ---")
    logger.info("Starting Temperature Control")

    # Iterate through all rooms
    for room in home:
        # Get temperature sensors and actuators
        temp_sensors = get_room_sensors(home, room.name)
        ac = get_room_actuators(home, room.name)
        heater = get_room_actuators(home, room.name)

        # Check if there are temperature sensors and actuators in the room
        if temp_sensors and (ac or heater):
            # Get temperature sensor reading
            current_temperature = temp_sensors[0].get_reading()
            print(f"Current temperature in {room.name}: {current_temperature} degrees Celsius.")
            logger.info(f"Current temperature in {room.name}: {current_temperature} degrees Celsius.")

            # Adjust temperature based on sensor reading and thresholds
            if ac:
                if current_temperature > TEMP_HIGH:
                    ac[0].turn_on()
                    print(f"Turning on AC in {room.name}.")
                    logger.info(f"Turning on AC in {room.name}.")
                elif current_temperature < TEMP_HIGH:
                    ac[0].turn_off()
                    print(f"Turning off AC in {room.name}.")
                    logger.info(f"Turning off AC in {room.name}.")

            if heater:
                if current_temperature < TEMP_LOW:
                    heater[0].turn_on()
                    print(f"Turning on heater in {room.name}.")
                    logger.info(f"Turning on heater in {room.name}.")
                elif current_temperature > TEMP_LOW:
                    heater[0].turn_off()
                    print(f"Turning off heater in {room.name}.")
                    logger.info(f"Turning off heater in {room.name}.")
        else:
            print(f"No temperature sensors or actuators found in {room.name}.")
            logger.warning(f"No temperature sensors or actuators found in {room.name}.")

# Function for humidity control based on sensor readings
def humidity_control(home):
    print("\n--- Humidity Control ---")
    logger.info("Starting Humidity Control")

    # Iterate through all rooms
    for room in home:
        # Get humidity sensors and actuators
        humidity_sensors = get_room_sensors(home, room.name)
        humidifiers = get_room_actuators(home, room.name)

        # Check if there are humidity sensors and actuators in the room
        if humidity_sensors and humidifiers:
            # Get humidity sensor reading
            current_humidity = humidity_sensors[0].get_reading()
            print(f"Current humidity in {room.name}: {current_humidity}%.")
            logger.info(f"Current humidity in {room.name}: {current_humidity}%.")

            # Adjust humidity based on sensor reading and thresholds
            if current_humidity < HUMIDITY_LOW:
                humidifiers[0].increase_humidity()
                print(f"Increasing humidity in {room.name}.")
                logger.info(f"Increasing humidity in {room.name}.")
            elif current_humidity > HUMIDITY_HIGH:
                humidifiers[0].decrease_humidity()
                print(f"Decreasing humidity in {room.name}.")
                logger.info(f"Decreasing humidity in {room.name}.")
        else:
            print(f"No humidity sensors or actuators found in {room.name}.")
            logger.warning(f"No humidity sensors or actuators found in {room.name}.")

# Function for light control based on sensor readings
def light_control(home):
    print("\n--- Light Control ---")
    logger.info("Starting Light Control")

    # Iterate through all rooms
    for room in home:
        # Get light intensive sensors and lights
        light_sensors = get_room_sensors(home, room.name)
        lights = get_room_actuators(home, room.name)

        # Check if there are light sensors and lights in the room
        if light_sensors and lights:
            # Get light sensor reading
            current_light_intensity = light_sensors[0].get_reading()
            print(f"Current light intensity in {room.name}: {current_light_intensity} lux.")
            logger.info(f"Current light intensity in {room.name}: {current_light_intensity} lux.")

            # Adjust lights based on sensor reading and thresholds
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                for light in lights:
                    light.turn_on()
                    print(f"Turning on lights in {room.name}.")
                    logger.info(f"Turning on lights in {room.name}.")
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    light.turn_off()
                    print(f"Turning off lights in {room.name}.")
                    logger.info(f"Turning off lights in {room.name}.")
        else:
            print(f"No light sensors or lights found in {room.name}.")
            logger.warning(f"No light sensors or lights found in {room.name}.")


if __name__ == "__main__":
    # Create home plan
    home = home_plan()

    # # Run morning plan
    # morning_plan(home)

    # Run leaving home plan
    leave_home_plan(home)

    # # Run movie plan in the living room
    # movie_plan(home, "LivingRoom")
    #
    # # Run temperature control for all rooms
    # temperature_control(home)
    #
    # # Run humidity control for all rooms
    # humidity_control(home)
    #
    # # Run light control for all rooms
    # light_control(home)