from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger

# function.py

def main():
    home = home_plan()
    print("Welcome to Smart Home System! \n")
    # Example Usage (Replace with your desired functionality)
    while True:
        try:
            action = input(
                "Please input your action: 'status', 'temp', 'humidity', 'light', 'clean', 'coffee', 'music', 'tv', 'exit': ")
            if action == "status":
                room_name = input("Please enter the room name: ")
                status(home, room_name)
            elif action == "temp":
                room_name = input("Please enter the room name: ")
                target_temp = float(input("Please enter the target temperature: "))
                adjust_temperature(home, room_name, target_temp)
            elif action == "humidity":
                room_name = input("Please enter the room name: ")
                humidity_level = input("Please enter the humidity level: ")
                adjust_humidity(home, room_name, humidity_level)
            elif action == "light":
                room_name = input("Please enter the room name: ")
                light_level = input("Please enter the light level (low, medium, high): ")
                adjust_light(home, room_name, light_level)
            elif action == "clean":
                room_name = input("Please enter the room name: ")
                clean_room(home, room_name)
            elif action == "coffee":
                room_name = input("Please enter the room name: ")
                coffee_type = input("Please enter the coffee type: ")
                make_coffee(home, room_name, coffee_type)
            elif action == "music":
                room_name = input("Please enter the room name: ")
                playlist = input("Please enter the playlist: ")
                play_music(home, room_name, playlist)
            elif action == "tv":
                room_name = input("Please enter the room name: ")
                channel_name = input("Please enter the channel name: ")
                play_tv(home, room_name, channel_name)
            elif action == "exit":
                print("Exiting the Smart Home System. Goodbye!")
                break
            else:
                print("Invalid action. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")


def status(home, room_name):
    room = get_room(home, room_name)
    if room:
        sensors = get_room_sensors(home, room_name)
        for sensor in sensors:
            sensor.turn_on()
            print(f"Sensor {sensor.id} reading: {sensor.get_reading()}")
            sensor.turn_off()
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            print(f"Actuator {actuator.id} status: {actuator.get_status()}")


def adjust_temperature(home, room_name, target_temp):
    room = get_room(home, room_name)
    if room:
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        heaters = get_all_actuators(home, "Heater")
        acs = get_all_actuators(home, "AC")
        for sensor in temperature_sensors:
            sensor.turn_on()
            current_temp = sensor.get_reading()
            sensor.turn_off()
            for heater in heaters:
                heater.set_target_temperature(target_temp)
                heater.adjust_temperature(current_temp)
            for ac in acs:
                ac.set_target_temperature(target_temp)
                ac.adjust_temperature(current_temp)
            if current_temp < TEMP_LOW:
                print("The temperature is too low. Turning on the heater.")
                logger.info(f"The temperature is too low. Turning on the heater.")
                for heater in heaters:
                    heater.turn_on()
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            elif current_temp > TEMP_HIGH:
                print("The temperature is too high. Turning on the AC.")
                logger.info(f"The temperature is too high. Turning on the AC.")
                for ac in acs:
                    ac.turn_on()
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            else:
                print(f"The temperature is comfortable at {current_temp}°C.")
                logger.info(f"The temperature is comfortable at {current_temp}°C.")
                for heater in heaters:
                    heater.turn_off()
                for ac in acs:
                    ac.turn_off()


def adjust_humidity(home, room_name, humidity_level):
    room = get_room(home, room_name)
    if room:
        humidity_sensors = get_all_sensors(home, "Humidity")
        humidifiers = get_all_actuators(home, "Humidifier")
        for sensor in humidity_sensors:
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            sensor.turn_off()
            if current_humidity < HUMIDITY_LOW and humidity_level == "increase":
                print("The humidity is too low. Increasing humidity.")
                logger.info(f"The humidity is too low. Increasing humidity.")
                for humidifier in humidifiers:
                    humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH and humidity_level == "decrease":
                print("The humidity is too high. Decreasing humidity.")
                logger.info(f"The humidity is too high. Decreasing humidity.")
                for humidifier in humidifiers:
                    humidifier.decrease_humidity()
            else:
                print(f"The humidity is comfortable at {current_humidity}%.")
                logger.info(f"The humidity is comfortable at {current_humidity}%.")


def adjust_light(home, room_name, light_level):
    room = get_room(home, room_name)
    if room:
        light_sensors = get_all_sensors(home, "LightIntensive")
        lights = get_all_actuators(home, "Light")
        for sensor in light_sensors:
            sensor.turn_on()
            current_light_intensity = sensor.get_reading()
            sensor.turn_off()
            for light in lights:
                if current_light_intensity < LIGHT_INTENSITY_LOW and light_level == "high":
                    print("The light is too dim. Increasing light intensity.")
                    logger.info(f"The light is too dim. Increasing light intensity.")
                    light.turn_on()
                    light.set_brightness_level("high")
                elif current_light_intensity > LIGHT_INTENSITY_HIGH and light_level == "low":
                    print("The light is too bright. Decreasing light intensity.")
                    logger.info(f"The light is too bright. Decreasing light intensity.")
                    light.turn_on()
                    light.set_brightness_level("low")
                else:
                    print(f"The light intensity is comfortable at {current_light_intensity} lux.")
                    logger.info(f"The light intensity is comfortable at {current_light_intensity} lux.")
                    light.turn_on()
                    light.set_brightness_level("medium")


def clean_room(home, room_name):
    room = get_room(home, room_name)
    if room:
        cleaning_robots = get_all_actuators(home, "CleaningRobot")
        for robot in cleaning_robots:
            robot.turn_on()
            robot.daily_routine()
            print(f"The cleaning robot in {room_name} is now cleaning.")
            logger.info(f"The cleaning robot in {room_name} is now cleaning.")


def make_coffee(home, room_name, coffee_type):
    room = get_room(home, room_name)
    if room:
        coffee_machines = get_all_actuators(home, "CoffeeMachine")
        for machine in coffee_machines:
            machine.turn_on()
            machine.make_coffee(coffee_type)
            print(f"The coffee machine in {room_name} is now making {coffee_type}.")
            logger.info(f"The coffee machine in {room_name} is now making {coffee_type}.")


def play_music(home, room_name, playlist):
    room = get_room(home, room_name)
    if room:
        music_players = get_all_actuators(home, "MusicPlayer")
        for player in music_players:
            player.turn_on()
            player.play_music(playlist)
            print(f"The music player in {room_name} is now playing {playlist}.")
            logger.info(f"The music player in {room_name} is now playing {playlist}.")


def play_tv(home, room_name, channel_name):
    room = get_room(home, room_name)
    if room:
        smart_tvs = get_all_actuators(home, "SmartTV")
        for tv in smart_tvs:
            tv.turn_on()
            tv.play_channel(channel_name)
            print(f"The smart TV in {room_name} is now playing channel {channel_name}.")
            logger.info(f"The smart TV in {room_name} is now playing channel {channel_name}.")


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Import necessary classes and functions from `home_plan.py`, `config.py`, and `logger_config.py`.

# 2. **`main()` Function:**
#    - The core function to handle user interaction and execute commands.
#    - Uses a `while True` loop for continuous interaction.
#    - Takes user input for actions like `status`, `temp`, `humidity`, `light`, `clean`, `coffee`, `music`, `tv`, and `exit`.
#    - Calls relevant functions based on the user's input.

# 3. **Action Functions:**
#    - `status(home, room_name)`: Gets status of sensors and actuators in a specified room.
#    - `adjust_temperature(home, room_name, target_temp)`: Adjusts temperature in a room based on target temperature.
#    - `adjust_humidity(home, room_name, humidity_level)`: Adjusts humidity in a room based on desired level.
#    - `adjust_light(home, room_name, light_level)`: Adjusts light intensity in a room based on desired level.
#    - `clean_room(home, room_name)`: Starts cleaning routine in a specified room.
#    - `make_coffee(home, room_name, coffee_type)`: Makes coffee using the coffee machine in a specified room.
#    - `play_music(home, room_name, playlist)`: Plays music on the music player in a specified room.
#    - `play_tv(home, room_name, channel_name)`: Plays a channel on the Smart TV in a specified room.

# 4. **Helper Functions:**
#    - The code leverages functions from `home_plan.py` to:
#      - Get the `home` object representing the house layout.
#      - Get a specific `room` by name.
#      - Get all sensors or actuators of a specific type.

# 5. **Logging:**
#    - Uses the `logger` object from `logger_config.py` to log actions and events for debugging and monitoring.

# **How to Use:**

# 1. **Place the code:** Create a `functions` folder in your project and save this code as `function.py` inside it.
# 2. **Run the code:** Execute `function.py` to start the smart home system.
# 3. **Interact:** Follow the prompts to enter commands and control your smart home devices.

# **Important Notes:**

# - This code provides a framework for interacting with the smart home system. You need to adapt the logic and actions to match the specific requirements of your project.
# - Replace the placeholder comments with your actual device control logic.
# - Ensure that the `home.py`, `config.py`, and `logger_config.py` files are in the correct location and import them appropriately.
# - Consider error handling and input validation for a more robust system.
