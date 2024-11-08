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


def turn_on_all_lights():
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()


def turn_off_all_lights():
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()


def turn_on_lights_in_room(room_name):
    room = get_room(home, room_name)
    if room:
        lights = get_room_actuators(home, room_name)
        for light in lights:
            if light.actuator_type == "Light":
                light.turn_on()


def turn_off_lights_in_room(room_name):
    room = get_room(home, room_name)
    if room:
        lights = get_room_actuators(home, room_name)
        for light in lights:
            if light.actuator_type == "Light":
                light.turn_off()


def set_brightness_level(room_name, brightness_level):
    room = get_room(home, room_name)
    if room:
        lights = get_room_actuators(home, room_name)
        for light in lights:
            if light.actuator_type == "Light":
                light.set_brightness_level(brightness_level)


def open_windows_in_room(room_name):
    room = get_room(home, room_name)
    if room:
        windows = get_room_actuators(home, room_name)
        for window in windows:
            if window.actuator_type == "Window":
                window.turn_on()


def close_windows_in_room(room_name):
    room = get_room(home, room_name)
    if room:
        windows = get_room_actuators(home, room_name)
        for window in windows:
            if window.actuator_type == "Window":
                window.turn_off()


def open_curtains_in_room(room_name):
    room = get_room(home, room_name)
    if room:
        curtains = get_room_actuators(home, room_name)
        for curtain in curtains:
            if curtain.actuator_type == "Curtain":
                curtain.turn_on()


def close_curtains_in_room(room_name):
    room = get_room(home, room_name)
    if room:
        curtains = get_room_actuators(home, room_name)
        for curtain in curtains:
            if curtain.actuator_type == "Curtain":
                curtain.turn_off()


def play_music_in_room(room_name, playlist):
    room = get_room(home, room_name)
    if room:
        music_players = get_room_actuators(home, room_name)
        for music_player in music_players:
            if music_player.actuator_type == "MusicPlayer":
                music_player.play_music(playlist)


def adjust_temperature_in_room(room_name, target_temperature):
    room = get_room(home, room_name)
    if room:
        temperature_sensors = get_room_sensors(home, room_name)
        for temperature_sensor in temperature_sensors:
            if temperature_sensor.sensor_type == "IndoorTemperature":
                current_temperature = temperature_sensor.get_reading()
                heaters = get_room_actuators(home, room_name)
                for heater in heaters:
                    if heater.actuator_type == "Heater":
                        heater.set_target_temperature(target_temperature)
                        heater.adjust_temperature(current_temperature)

                acs = get_room_actuators(home, room_name)
                for ac in acs:
                    if ac.actuator_type == "AC":
                        ac.set_target_temperature(target_temperature)
                        ac.adjust_temperature(current_temperature)


def adjust_humidity_in_room(room_name, target_humidity):
    room = get_room(home, room_name)
    if room:
        humidity_sensors = get_room_sensors(home, room_name)
        for humidity_sensor in humidity_sensors:
            if humidity_sensor.sensor_type == "Humidity":
                current_humidity = humidity_sensor.get_reading()
                humidifiers = get_room_actuators(home, room_name)
                for humidifier in humidifiers:
                    if humidifier.actuator_type == "Humidifier":
                        if current_humidity < target_humidity:
                            humidifier.increase_humidity()
                        elif current_humidity > target_humidity:
                            humidifier.decrease_humidity()


def make_coffee(room_name, coffee_type):
    room = get_room(home, room_name)
    if room:
        coffee_machines = get_room_actuators(home, room_name)
        for coffee_machine in coffee_machines:
            if coffee_machine.actuator_type == "CoffeeMachine":
                coffee_machine.make_coffee(coffee_type)


def turn_on_cleaning_robot(room_name):
    room = get_room(home, room_name)
    if room:
        cleaning_robots = get_room_actuators(home, room_name)
        for cleaning_robot in cleaning_robots:
            if cleaning_robot.actuator_type == "CleaningRobot":
                cleaning_robot.turn_on()
                cleaning_robot.daily_routine()


def turn_on_smart_socket(room_name, socket_index):
    room = get_room(home, room_name)
    if room:
        smart_sockets = get_room_actuators(home, room_name)
        for i, smart_socket in enumerate(smart_sockets):
            if smart_socket.actuator_type == "SmartSocket" and i == socket_index:
                smart_socket.turn_on()


def turn_off_smart_socket(room_name, socket_index):
    room = get_room(home, room_name)
    if room:
        smart_sockets = get_room_actuators(home, room_name)
        for i, smart_socket in enumerate(smart_sockets):
            if smart_socket.actuator_type == "SmartSocket" and i == socket_index:
                smart_socket.turn_off()


def lock_door(room_name):
    room = get_room(home, room_name)
    if room:
        doors = get_room_actuators(home, room_name)
        for door in doors:
            if door.actuator_type == "Door":
                door.lock()


def unlock_door(room_name):
    room = get_room(home, room_name)
    if room:
        doors = get_room_actuators(home, room_name)
        for door in doors:
            if door.actuator_type == "Door":
                door.unlock()


def play_channel_on_tv(room_name, channel_name):
    room = get_room(home, room_name)
    if room:
        smart_tvs = get_room_actuators(home, room_name)
        for smart_tv in smart_tvs:
            if smart_tv.actuator_type == "SmartTV":
                smart_tv.play_channel(channel_name)


def send_notification(room_name, message):
    room = get_room(home, room_name)
    if room:
        notification_senders = get_room_actuators(home, room_name)
        for notification_sender in notification_senders:
            if notification_sender.actuator_type == "NotificationSender":
                notification_sender.notification_sender(message)


def check_and_adjust_temperature():
    for room in home:
        temperature_sensors = get_room_sensors(home, room.name)
        for temperature_sensor in temperature_sensors:
            if temperature_sensor.sensor_type == "IndoorTemperature":
                current_temperature = temperature_sensor.get_reading()
                heaters = get_room_actuators(home, room.name)
                for heater in heaters:
                    if heater.actuator_type == "Heater":
                        if current_temperature < TEMP_LOW:
                            heater.turn_on()
                        else:
                            heater.turn_off()

                acs = get_room_actuators(home, room.name)
                for ac in acs:
                    if ac.actuator_type == "AC":
                        if current_temperature > TEMP_HIGH:
                            ac.turn_on()
                        else:
                            ac.turn_off()

def check_and_adjust_humidity():
    for room in home:
        humidity_sensors = get_room_sensors(home, room.name)
        for humidity_sensor in humidity_sensors:
            if humidity_sensor.sensor_type == "Humidity":
                current_humidity = humidity_sensor.get_reading()
                humidifiers = get_room_actuators(home, room.name)
                for humidifier in humidifiers:
                    if humidifier.actuator_type == "Humidifier":
                        if current_humidity < HUMIDITY_LOW:
                            humidifier.increase_humidity()
                        elif current_humidity > HUMIDITY_HIGH:
                            humidifier.decrease_humidity()

def check_and_adjust_light():
    for room in home:
        light_intensity_sensors = get_room_sensors(home, room.name)
        for light_intensity_sensor in light_intensity_sensors:
            if light_intensity_sensor.sensor_type == "LightIntensive":
                current_light_intensity = light_intensity_sensor.get_reading()
                lights = get_room_actuators(home, room.name)
                for light in lights:
                    if light.actuator_type == "Light":
                        if current_light_intensity < LIGHT_INTENSITY_LOW:
                            light.turn_on()
                        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                            light.turn_off()

def check_and_open_window():
    for room in home:
        temperature_sensors = get_room_sensors(home, room.name)
        for temperature_sensor in temperature_sensors:
            if temperature_sensor.sensor_type == "IndoorTemperature":
                current_temperature = temperature_sensor.get_reading()
                if current_temperature > TEMP_HIGH:
                    windows = get_room_actuators(home, room.name)
                    for window in windows:
                        if window.actuator_type == "Window":
                            window.turn_on()
                            time.sleep(TEMP_CHANGE_DURATION_WINDOW)

def check_and_close_window():
    for room in home:
        temperature_sensors = get_room_sensors(home, room.name)
        for temperature_sensor in temperature_sensors:
            if temperature_sensor.sensor_type == "IndoorTemperature":
                current_temperature = temperature_sensor.get_reading()
                if current_temperature < TEMP_LOW:
                    windows = get_room_actuators(home, room.name)
                    for window in windows:
                        if window.actuator_type == "Window":
                            window.turn_off()
                            time.sleep(TEMP_CHANGE_DURATION_WINDOW)

def check_and_adjust_all():
    check_and_adjust_temperature()
    check_and_adjust_humidity()
    check_and_adjust_light()
    check_and_open_window()
    check_and_close_window()

if __name__ == "__main__":
    # turn_on_all_lights()
    # turn_off_all_lights()
    # turn_on_lights_in_room("LivingRoom")
    # turn_off_lights_in_room("LivingRoom")
    # set_brightness_level("LivingRoom", "medium")
    # open_windows_in_room("LivingRoom")
    # close_windows_in_room("LivingRoom")
    # open_curtains_in_room("LivingRoom")
    # close_curtains_in_room("LivingRoom")
    # play_music_in_room("LivingRoom", "Classical")
    # adjust_temperature_in_room("LivingRoom", 22)
    # adjust_humidity_in_room("LivingRoom", 40)
    # make_coffee("Kitchen", "Latte")
    # turn_on_cleaning_robot("LivingRoom")
    # turn_on_smart_socket("LivingRoom", 0)
    # turn_off_smart_socket("LivingRoom", 0)
    # lock_door("LivingRoom")
    # unlock_door("LivingRoom")
    # play_channel_on_tv("LivingRoom", "Discovery")
    # send_notification("LivingRoom", "Hello World!")
    check_and_adjust_all()