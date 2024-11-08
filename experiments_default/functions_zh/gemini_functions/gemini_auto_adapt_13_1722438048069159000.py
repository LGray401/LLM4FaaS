from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, AC, Heater, CoffeeMachine, NotificationSender, MusicPlayer, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    DAILY_ROUTINE_DURATION
from home.logger_config import logger


def check_temperature(room_name):
    # 获取房间的温度传感器
    sensors = get_room_sensors(home_plan(), room_name)
    if sensors is None:
        return

    temperature_sensor = None
    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature_sensor = sensor
            break

    if temperature_sensor is None:
        logger.warning(f"No Indoor Temperature Sensor found in {room_name}")
        print(f"No Indoor Temperature Sensor found in {room_name}")
        return

    # 获取温度读数
    temperature = temperature_sensor.get_reading()
    if temperature is None:
        return

    # 检查温度是否超出阈值
    if temperature < TEMP_LOW:
        print(f"The temperature in {room_name} is too low. Turning on the heater.")
        logger.info(f"The temperature in {room_name} is too low. Turning on the heater.")
        # 获取房间的加热器
        heaters = get_room_actuators(home_plan(), room_name)
        if heaters is None:
            return

        for heater in heaters:
            if isinstance(heater, Heater):
                heater.turn_on()
                break

    elif temperature > TEMP_HIGH:
        print(f"The temperature in {room_name} is too high. Turning on the AC.")
        logger.info(f"The temperature in {room_name} is too high. Turning on the AC.")
        # 获取房间的空调
        acs = get_room_actuators(home_plan(), room_name)
        if acs is None:
            return

        for ac in acs:
            if isinstance(ac, AC):
                ac.turn_on()
                break


def check_humidity(room_name):
    # 获取房间的湿度传感器
    sensors = get_room_sensors(home_plan(), room_name)
    if sensors is None:
        return

    humidity_sensor = None
    for sensor in sensors:
        if isinstance(sensor, HumiditySensor):
            humidity_sensor = sensor
            break

    if humidity_sensor is None:
        logger.warning(f"No Humidity Sensor found in {room_name}")
        print(f"No Humidity Sensor found in {room_name}")
        return

    # 获取湿度读数
    humidity = humidity_sensor.get_reading()
    if humidity is None:
        return

    # 检查湿度是否超出阈值
    if humidity < HUMIDITY_LOW:
        print(f"The humidity in {room_name} is too low.")
        logger.info(f"The humidity in {room_name} is too low.")

    elif humidity > HUMIDITY_HIGH:
        print(f"The humidity in {room_name} is too high.")
        logger.info(f"The humidity in {room_name} is too high.")


def check_light_intensity(room_name):
    # 获取房间的光照强度传感器
    sensors = get_room_sensors(home_plan(), room_name)
    if sensors is None:
        return

    light_intensity_sensor = None
    for sensor in sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_intensity_sensor = sensor
            break

    if light_intensity_sensor is None:
        logger.warning(f"No Light Intensity Sensor found in {room_name}")
        print(f"No Light Intensity Sensor found in {room_name}")
        return

    # 获取光照强度读数
    light_intensity = light_intensity_sensor.get_reading()
    if light_intensity is None:
        return

    # 检查光照强度是否超出阈值
    if light_intensity < LIGHT_INTENSITY_LOW:
        print(f"The light intensity in {room_name} is too low. Turning on the lights.")
        logger.info(f"The light intensity in {room_name} is too low. Turning on the lights.")
        # 获取房间的灯光
        lights = get_room_actuators(home_plan(), room_name)
        if lights is None:
            return

        for light in lights:
            if isinstance(light, Light):
                light.turn_on()
                break

    elif light_intensity > LIGHT_INTENSITY_HIGH:
        print(f"The light intensity in {room_name} is too high.")
        logger.info(f"The light intensity in {room_name} is too high.")


def turn_on_lights_at_night(room_name):
    # 获取房间的灯光
    lights = get_room_actuators(home_plan(), room_name)
    if lights is None:
        return

    for light in lights:
        if isinstance(light, Light):
            light.turn_on()
            break


def turn_on_coffee_machine(room_name, coffee_type):
    # 获取房间的咖啡机
    coffee_machines = get_room_actuators(home_plan(), room_name)
    if coffee_machines is None:
        return

    for coffee_machine in coffee_machines:
        if isinstance(coffee_machine, CoffeeMachine):
            coffee_machine.make_coffee(coffee_type)
            break


def turn_on_music_player(room_name, playlist):
    # 获取房间的音乐播放器
    music_players = get_room_actuators(home_plan(), room_name)
    if music_players is None:
        return

    for music_player in music_players:
        if isinstance(music_player, MusicPlayer):
            music_player.play_music(playlist)
            break


def turn_on_tv(room_name, channel_name):
    # 获取房间的电视
    tvs = get_room_actuators(home_plan(), room_name)
    if tvs is None:
        return

    for tv in tvs:
        if isinstance(tv, SmartTV):
            tv.play_channel(channel_name)
            break


def send_notification(room_name, message):
    # 获取房间的通知发送器
    notification_senders = get_room_actuators(home_plan(), room_name)
    if notification_senders is None:
        return

    for notification_sender in notification_senders:
        if isinstance(notification_sender, NotificationSender):
            notification_sender.notification_sender(message)
            break


def run_daily_routine():
    # Get all cleaning robots
    cleaning_robots = get_all_actuators(home_plan(), "CleaningRobot")
    if cleaning_robots is None:
        return

    # Start daily routine for each cleaning robot
    for robot in cleaning_robots:
        robot.daily_routine()


def main():
    # Example usage:
    # check_temperature("LivingRoom")
    # check_humidity("LivingRoom")
    # check_light_intensity("LivingRoom")
    # turn_on_lights_at_night("LivingRoom")
    # turn_on_coffee_machine("Kitchen", "espresso")
    # turn_on_music_player("LivingRoom", "rock")
    # turn_on_tv("LivingRoom", "CNN")
    # send_notification("LivingRoom", "It's time for dinner!")
    run_daily_routine()


if __name__ == "__main__":
    main()
