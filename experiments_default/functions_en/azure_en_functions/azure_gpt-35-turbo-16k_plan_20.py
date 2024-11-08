# Sure, I will create the 'function.py' file for your smart home project based on the given functional description. 
# 
# Here is the 'function.py' file:

from home.home_plan import get_room_actuators, get_room_sensors, print_home_plan, get_room
from home.actuator import Light, NotificationSender
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor


def morning_plan(home):
    room = get_room(home, "LivingRoom")
    sensors = get_room_sensors(home, "LivingRoom")
    actuators = get_room_actuators(home, "LivingRoom")

    # Open the curtains
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.turn_on()
            actuator.set_brightness_level("high")
        elif isinstance(actuator, NotificationSender):
            actuator.notification_sender("Good morning! The curtains have been opened.")

    # Additional actions based on the sensors' readings
    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            reading = sensor.get_reading()
            if reading is not None:
                if reading < 20:
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.set_brightness_level("high")
                            actuator.turn_on()
                elif reading > 25:
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.set_brightness_level("low")
                            actuator.turn_on()

    print_home_plan(home)


def leave_home_plan(home):
    room = get_room(home, "LivingRoom")
    actuators = get_room_actuators(home, "LivingRoom")

    # Turn off the lights
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

    print_home_plan(home)


def movie_plan(home):
    room = get_room(home, "LivingRoom")
    sensors = get_room_sensors(home, "LivingRoom")
    actuators = get_room_actuators(home, "LivingRoom")

    # Adjust light brightness
    for actuator in actuators:
        if isinstance(actuator, Light):
            actuator.set_brightness_level("low")
            actuator.turn_on()

    # Additional actions based on the sensors' readings
    for sensor in sensors:
        if isinstance(sensor, LightIntensiveSensor):
            reading = sensor.get_reading()
            if reading is not None:
                if reading < 500:
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.set_brightness_level("high")
                            actuator.turn_on()
                elif reading > 800:
                    for actuator in actuators:
                        if isinstance(actuator, Light):
                            actuator.set_brightness_level("low")
                            actuator.turn_on()

    print_home_plan(home)


if __name__ == "__main__":
    home = home_plan()
    morning_plan(home)