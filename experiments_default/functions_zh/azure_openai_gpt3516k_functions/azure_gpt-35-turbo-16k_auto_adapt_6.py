# Sure! Here is the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators

# Function to get the current temperature reading in a room
def get_temperature(room_name):
    sensors = get_all_sensors(home_plan(), "IndoorTemperatureSensor")
    for sensor in sensors:
        if sensor.room_name == room_name:
            return sensor.get_reading()

# Function to get the current humidity reading in a room
def get_humidity(room_name):
    sensors = get_all_sensors(home_plan(), "HumiditySensor")
    for sensor in sensors:
        if sensor.room_name == room_name:
            return sensor.get_reading()

# Function to get the current light intensity reading in a room
def get_light_intensity(room_name):
    sensors = get_all_sensors(home_plan(), "LightIntensiveSensor")
    for sensor in sensors:
        if sensor.room_name == room_name:
            return sensor.get_reading()

# Function to set the target temperature for a heater or AC in a room
def set_target_temperature(room_name, target_temperature):
    actuators = get_all_actuators(home_plan(), "Heater") + get_all_actuators(home_plan(), "AC")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.set_target_temperature(target_temperature)

# Function to adjust the temperature based on the target temperature in a room
def adjust_temperature(room_name, current_temperature):
    actuators = get_all_actuators(home_plan(), "Heater") + get_all_actuators(home_plan(), "AC")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.adjust_temperature(current_temperature)

# Function to set the brightness level for a light in a room
def set_brightness_level(room_name, brightness_level):
    actuators = get_all_actuators(home_plan(), "Light")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.set_brightness_level(brightness_level)

# Function to make coffee in a coffee machine in a room
def make_coffee(room_name, coffee_type):
    actuators = get_all_actuators(home_plan(), "CoffeeMachine")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.make_coffee(coffee_type)

# Function to lock a door in a room
def lock_door(room_name):
    actuators = get_all_actuators(home_plan(), "Door")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.lock()

# Function to unlock a door in a room
def unlock_door(room_name):
    actuators = get_all_actuators(home_plan(), "Door")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.unlock()

# Function to start the daily routine of a cleaning robot in a room
def start_cleaning_routine(room_name):
    actuators = get_all_actuators(home_plan(), "CleaningRobot")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.daily_routine()

# Function to send a notification message in a room
def send_notification(room_name, message):
    actuators = get_all_actuators(home_plan(), "NotificationSender")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.notification_sender(message)

# Function to play music in a music player in a room
def play_music(room_name, playlist):
    actuators = get_all_actuators(home_plan(), "MusicPlayer")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.play_music(playlist)

# Function to play a channel in a smart TV in a room
def play_channel(room_name, channel):
    actuators = get_all_actuators(home_plan(), "SmartTV")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.play_channel(channel)

# Function to increase the humidity in a room
def increase_humidity(room_name):
    actuators = get_all_actuators(home_plan(), "Humidifier")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.increase_humidity()

# Function to decrease the humidity in a room
def decrease_humidity(room_name):
    actuators = get_all_actuators(home_plan(), "Humidifier")
    for actuator in actuators:
        if actuator.room_name == room_name:
            actuator.decrease_humidity()