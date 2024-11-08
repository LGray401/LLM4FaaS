# Sure! Here is the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def check_temperature():
    sensors = get_all_sensors(home_plan(), "IndoorTemperature")

    for sensor in sensors:
        temperature = sensor.get_reading()
        
        if temperature is not None:
            if temperature > TEMP_HIGH:
                notification_sender = NotificationSender(sensor.room_name)
                notification_sender.turn_on()
                notification_sender.notification_sender("Temperature is too high!")
            elif temperature < TEMP_LOW:
                notification_sender = NotificationSender(sensor.room_name)
                notification_sender.turn_on()
                notification_sender.notification_sender("Temperature is too low!")


def check_humidity():
    sensors = get_all_sensors(home_plan(), "Humidity")

    for sensor in sensors:
        humidity = sensor.get_reading()
        
        if humidity is not None:
            if humidity > HUMIDITY_HIGH:
                notification_sender = NotificationSender(sensor.room_name)
                notification_sender.turn_on()
                notification_sender.notification_sender("Humidity is too high!")
            elif humidity < HUMIDITY_LOW:
                notification_sender = NotificationSender(sensor.room_name)
                notification_sender.turn_on()
                notification_sender.notification_sender("Humidity is too low!")


def check_light_intensity():
    sensors = get_all_sensors(home_plan(), "LightIntensive")

    for sensor in sensors:
        light_intensity = sensor.get_reading()
        
        if light_intensity is not None:
            if light_intensity > LIGHT_INTENSITY_HIGH:
                notification_sender = NotificationSender(sensor.room_name)
                notification_sender.turn_on()
                notification_sender.notification_sender("Light intensity is too high!")
            elif light_intensity < LIGHT_INTENSITY_LOW:
                notification_sender = NotificationSender(sensor.room_name)
                notification_sender.turn_on()
                notification_sender.notification_sender("Light intensity is too low!")


def main():
    check_temperature()
    check_humidity()
    check_light_intensity()


if __name__ == "__main__":
    main()