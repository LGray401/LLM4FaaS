from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator, CoffeeMachine, MusicPlayer, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time
import random

# Function.py in functions folder


def check_and_adjust_temperature(home, room_name, target_temperature):
    """
    Checks the temperature in a room and adjusts the heater or AC accordingly.
    """
    room = get_room_sensors(home, room_name)
    if room is None:
        return
    temperature_sensors = [sensor for sensor in room if sensor.sensor_type == "IndoorTemperature"]
    if len(temperature_sensors) == 0:
        logger.warning(format("There is no Indoor Temperature sensor in " + room_name))
        print("There is no Indoor Temperature sensor in ", room_name)
        return

    temperature_sensor = temperature_sensors[0]  # Assuming only one indoor temperature sensor per room
    current_temperature = temperature_sensor.get_reading()

    if current_temperature is not None:
        room = get_room_actuators(home, room_name)
        if room is None:
            return

        heater = [actuator for actuator in room if actuator.actuator_type == "Heater"]
        if len(heater) > 0:
            heater[0].set_target_temperature(target_temperature)
            heater[0].adjust_temperature(current_temperature)

        ac = [actuator for actuator in room if actuator.actuator_type == "AC"]
        if len(ac) > 0:
            ac[0].set_target_temperature(target_temperature)
            ac[0].adjust_temperature(current_temperature)


def check_and_adjust_humidity(home, room_name, target_humidity):
    """
    Checks the humidity in a room and adjusts the humidifier accordingly.
    """
    room = get_room_sensors(home, room_name)
    if room is None:
        return
    humidity_sensors = [sensor for sensor in room if sensor.sensor_type == "Humidity"]
    if len(humidity_sensors) == 0:
        logger.warning(format("There is no humidity sensor in " + room_name))
        print("There is no humidity sensor in ", room_name)
        return

    humidity_sensor = humidity_sensors[0]  # Assuming only one humidity sensor per room
    current_humidity = humidity_sensor.get_reading()

    if current_humidity is not None:
        room = get_room_actuators(home, room_name)
        if room is None:
            return

        humidifier = [actuator for actuator in room if actuator.actuator_type == "Humidifier"]
        if len(humidifier) > 0:
            if current_humidity < target_humidity:
                humidifier[0].increase_humidity()
            elif current_humidity > target_humidity:
                humidifier[0].decrease_humidity()


def check_and_adjust_light(home, room_name, target_brightness):
    """
    Checks the light intensity in a room and adjusts the lights accordingly.
    """
    room = get_room_sensors(home, room_name)
    if room is None:
        return
    light_intensity_sensors = [sensor for sensor in room if sensor.sensor_type == "LightIntensive"]
    if len(light_intensity_sensors) == 0:
        logger.warning(format("There is no light intensity sensor in " + room_name))
        print("There is no light intensity sensor in ", room_name)
        return

    light_intensity_sensor = light_intensity_sensors[0]  # Assuming only one light intensity sensor per room
    current_light_intensity = light_intensity_sensor.get_reading()

    if current_light_intensity is not None:
        room = get_room_actuators(home, room_name)
        if room is None:
            return

        lights = [actuator for actuator in room if actuator.actuator_type == "Light"]
        if len(lights) > 0:
            if target_brightness == "low":
                lights[0].set_brightness_level("low")
            elif target_brightness == "medium":
                lights[0].set_brightness_level("medium")
            elif target_brightness == "high":
                lights[0].set_brightness_level("high")


def turn_on_all_lights_in_room(home, room_name):
    """
    Turns on all the lights in a given room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    lights = [actuator for actuator in room if actuator.actuator_type == "Light"]
    for light in lights:
        light.turn_on()


def turn_off_all_lights_in_room(home, room_name):
    """
    Turns off all the lights in a given room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    lights = [actuator for actuator in room if actuator.actuator_type == "Light"]
    for light in lights:
        light.turn_off()


def open_all_windows_in_room(home, room_name):
    """
    Opens all the windows in a given room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    windows = [actuator for actuator in room if actuator.actuator_type == "Window"]
    for window in windows:
        window.turn_on()


def close_all_windows_in_room(home, room_name):
    """
    Closes all the windows in a given room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    windows = [actuator for actuator in room if actuator.actuator_type == "Window"]
    for window in windows:
        window.turn_off()


def open_curtain_in_room(home, room_name):
    """
    Opens the curtain in a given room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    curtains = [actuator for actuator in room if actuator.actuator_type == "Curtain"]
    if len(curtains) > 0:
        curtains[0].turn_on()


def close_curtain_in_room(home, room_name):
    """
    Closes the curtain in a given room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    curtains = [actuator for actuator in room if actuator.actuator_type == "Curtain"]
    if len(curtains) > 0:
        curtains[0].turn_off()


def play_music_in_room(home, room_name, playlist):
    """
    Plays music in a given room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    music_players = [actuator for actuator in room if actuator.actuator_type == "MusicPlayer"]
    if len(music_players) > 0:
        music_players[0].play_music(playlist)


def play_channel_on_tv(home, room_name, channel_name):
    """
    Plays a channel on the TV in a given room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    smart_tvs = [actuator for actuator in room if actuator.actuator_type == "SmartTV"]
    if len(smart_tvs) > 0:
        smart_tvs[0].play_channel(channel_name)


def make_coffee_in_room(home, room_name, coffee_type):
    """
    Makes coffee in the kitchen.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    coffee_machines = [actuator for actuator in room if actuator.actuator_type == "CoffeeMachine"]
    if len(coffee_machines) > 0:
        coffee_machines[0].make_coffee(coffee_type)


def turn_on_cleaning_robot(home, room_name):
    """
    Turns on the cleaning robot in the room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    cleaning_robots = [actuator for actuator in room if actuator.actuator_type == "CleaningRobot"]
    if len(cleaning_robots) > 0:
        cleaning_robots[0].turn_on()
        cleaning_robots[0].daily_routine()
    else:
        logger.warning(f"Cleaning Robot not found in {room_name}")
        print(f"Cleaning Robot not found in {room_name}")


def get_sensor_reading(home, room_name, sensor_type):
    """
    Gets the reading from a specific sensor type in a room.
    """
    room = get_room_sensors(home, room_name)
    if room is None:
        return
    sensors = [sensor for sensor in room if sensor.sensor_type == sensor_type]
    if len(sensors) > 0:
        return sensors[0].get_reading()
    else:
        logger.warning(f"Sensor {sensor_type} not found in {room_name}")
        print(f"Sensor {sensor_type} not found in {room_name}")
        return None


def get_actuator_status(home, room_name, actuator_type):
    """
    Gets the status of a specific actuator type in a room.
    """
    room = get_room_actuators(home, room_name)
    if room is None:
        return
    actuators = [actuator for actuator in room if actuator.actuator_type == actuator_type]
    if len(actuators) > 0:
        return actuators[0].get_status()
    else:
        logger.warning(f"Actuator {actuator_type} not found in {room_name}")
        print(f"Actuator {actuator_type} not found in {room_name}")
        return None


def smart_home_scenario(home):
    """
    Example scenario for the smart home system.
    """
    # Turn on lights and AC in the living room
    turn_on_all_lights_in_room(home, "LivingRoom")
    check_and_adjust_temperature(home, "LivingRoom", 22)

    # Play music in the living room
    play_music_in_room(home, "LivingRoom", "Pop")

    # Check and adjust temperature in the bedroom
    check_and_adjust_temperature(home, "Bedroom", 20)

    # Turn on lights in the kitchen
    turn_on_all_lights_in_room(home, "Kitchen")

    # Make coffee in the kitchen
    make_coffee_in_room(home, "Kitchen", "Espresso")

    # Check and adjust humidity in the bathroom
    check_and_adjust_humidity(home, "Bathroom", 40)

    # Turn on the TV in the living room
    play_channel_on_tv(home, "LivingRoom", "News")

    # Check for smoke in the kitchen
    smoke_sensor_reading = get_sensor_reading(home, "Kitchen", "Smoke")
    if smoke_sensor_reading is not None and smoke_sensor_reading > 50:
        # Send notification if smoke is detected
        print("Smoke detected in the kitchen! Sending notification...")
        logger.warning(format("Smoke detected in the kitchen!"))

    # Turn on the cleaning robot in the living room
    turn_on_cleaning_robot(home, "LivingRoom")

    # Simulate changes in temperature and light intensity for demonstration purposes
    while True:
        # Simulate temperature changes in the living room
        temperature_reading = get_sensor_reading(home, "LivingRoom", "IndoorTemperature")
        if temperature_reading is not None:
            if temperature_reading < TEMP_LOW:
                print(f"Living room temperature is low: {temperature_reading}°C")
                check_and_adjust_temperature(home, "LivingRoom", 22)
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            elif temperature_reading > TEMP_HIGH:
                print(f"Living room temperature is high: {temperature_reading}°C")
                check_and_adjust_temperature(home, "LivingRoom", 20)
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            else:
                print(f"Living room temperature is comfortable: {temperature_reading}°C")
                time.sleep(1)

        # Simulate light intensity changes in the living room
        light_intensity_reading = get_sensor_reading(home, "LivingRoom", "LightIntensive")
        if light_intensity_reading is not None:
            if light_intensity_reading < LIGHT_INTENSITY_LOW:
                print(f"Living room light intensity is low: {light_intensity_reading} lux")
                turn_on_all_lights_in_room(home, "LivingRoom")
                time.sleep(1)
            elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                print(f"Living room light intensity is high: {light_intensity_reading} lux")
                turn_off_all_lights_in_room(home, "LivingRoom")
                time.sleep(1)

        # Simulate humidity changes in the bathroom
        humidity_reading = get_sensor_reading(home, "Bathroom", "Humidity")
        if humidity_reading is not None:
            if humidity_reading < HUMIDITY_LOW:
                print(f"Bathroom humidity is low: {humidity_reading}%")
                check_and_adjust_humidity(home, "Bathroom", 40)
                time.sleep(1)
            elif humidity_reading > HUMIDITY_HIGH:
                print(f"Bathroom humidity is high: {humidity_reading}%")
                check_and_adjust_humidity(home, "Bathroom", 40)
                time.sleep(1)

        # Simulate random events
        if random.random() < 0.05:  # 5% chance of an event occurring
            # Simulate a guest arriving
            print("Guest arriving! Opening the door and playing welcome music...")
            room = get_room_actuators(home, "LivingRoom")
            if room is not None:
                doors = [actuator for actuator in room if actuator.actuator_type == "Door"]
                if len(doors) > 0:
                    doors[0].unlock()
            play_music_in_room(home, "LivingRoom", "Welcome")
            time.sleep(5)

        if random.random() < 0.02:  # 2% chance of an event occurring
            # Simulate a power outage
            print("Power outage! Turning off all lights and appliances...")
            for room in home:
                for actuator in room.actuators:
                    actuator.turn_off()
            time.sleep(10)  # Simulate power outage duration

        # ... continue simulating changes and events as needed ...


if __name__ == "__main__":
    home = home_plan()
    smart_home_scenario(home)

# This `function.py` file includes several functions that provide the core functionalities of your smart home project, including:

# - **Temperature control:** Adjust the heater or AC based on temperature readings.
# - **Humidity control:** Adjust the humidifier based on humidity readings.
# - **Light control:** Adjust the light brightness level or turn lights on/off.
# - **Window and curtain control:** Open/close windows and curtains.
# - **Music playback:** Play music in a room.
# - **TV control:** Play a channel on the TV.
# - **Coffee machine control:** Make coffee.
# - **Cleaning robot control:** Start the cleaning robot's daily routine.
# - **Sensor reading:** Get readings from specific sensors.
# - **Actuator status:** Get the status of specific actuators.

# The `smart_home_scenario` function demonstrates how these functions can be used to create a basic smart home scenario. The function includes simulated changes in temperature, light intensity, and humidity, as well as random events like guests arriving or a power outage.

# **To use this file:**

# 1. **Place `function.py` in the `functions` folder.**
# 2. **Import the necessary functions into your other Python files (`sensor.py`, `actuator.py`, `home_plan.py`, etc.).**
# 3. **Call the functions from your main script or other modules as needed.**

# Remember to adapt the scenario and functions to your specific project needs. You can add more features, functionalities, and events to create a more sophisticated and personalized smart home experience.
