from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_actuators, \
    get_all_sensors
from home.actuator import Heater, AC, CoffeeMachine, Curtain, Door, Light, MusicPlayer, NotificationSender
from home.sensor import LightIntensiveSensor, OutdoorTemperatureSensor
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")

    if living_room is not None:
        # open curtains
        curtains = get_room_actuators(home, "LivingRoom")
        if curtains is not None:
            for curtain in curtains:
                if curtain.actuator_type == "Curtain":
                    curtain.turn_on()

        # turn on lights if cloudy
        light_sensor = get_room_sensors(home, "LivingRoom")
        if light_sensor is not None:
            for sensor in light_sensor:
                if sensor.sensor_type == "LightIntensive":
                    light_reading = sensor.get_reading()
                    if light_reading is not None and light_reading < LIGHT_INTENSITY_HIGH:
                        lights = get_room_actuators(home, "LivingRoom")
                        if lights is not None:
                            for light in lights:
                                if light.actuator_type == "Light":
                                    light.turn_on()
                                    light.set_brightness_level("medium")

    if kitchen is not None:
        # make coffee
        coffee_machine = get_room_actuators(home, "Kitchen")
        if coffee_machine is not None:
            for machine in coffee_machine:
                if machine.actuator_type == "CoffeeMachine":
                    machine.turn_on()
                    machine.make_coffee("Espresso")
                    # Play music when coffee is ready
                    music_player = get_room_actuators(home, "LivingRoom")
                    if music_player is not None:
                        for player in music_player:
                            if player.actuator_type == "MusicPlayer":
                                player.turn_on()
                                player.play_music("Coffee Music")


def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")

    if living_room is not None:
        # open curtains if sunny
        light_sensor = get_room_sensors(home, "LivingRoom")
        if light_sensor is not None:
            for sensor in light_sensor:
                if sensor.sensor_type == "LightIntensive":
                    light_reading = sensor.get_reading()
                    if light_reading is not None and light_reading > LIGHT_INTENSITY_LOW:
                        curtains = get_room_actuators(home, "LivingRoom")
                        if curtains is not None:
                            for curtain in curtains:
                                if curtain.actuator_type == "Curtain":
                                    curtain.turn_on()

        # turn off lights and sockets
        lights = get_room_actuators(home, "LivingRoom")
        if lights is not None:
            for light in lights:
                if light.actuator_type == "Light":
                    light.turn_off()

        sockets = get_room_actuators(home, "LivingRoom")
        if sockets is not None:
            for socket in sockets:
                if socket.actuator_type == "SmartSocket":
                    socket.turn_off()

        # lock the door
        door = get_room_actuators(home, "LivingRoom")
        if door is not None:
            for d in door:
                if d.actuator_type == "Door":
                    d.lock()

    if bedroom is not None:
        # turn off lights and sockets
        lights = get_room_actuators(home, "Bedroom")
        if lights is not None:
            for light in lights:
                if light.actuator_type == "Light":
                    light.turn_off()

        sockets = get_room_actuators(home, "Bedroom")
        if sockets is not None:
            for socket in sockets:
                if socket.actuator_type == "SmartSocket":
                    socket.turn_off()

    if kitchen is not None:
        # turn off lights and sockets
        lights = get_room_actuators(home, "Kitchen")
        if lights is not None:
            for light in lights:
                if light.actuator_type == "Light":
                    light.turn_off()

        sockets = get_room_actuators(home, "Kitchen")
        if sockets is not None:
            for socket in sockets:
                if socket.actuator_type == "SmartSocket":
                    socket.turn_off()


def movie_plan(home):
    living_room = get_room(home, "LivingRoom")

    if living_room is not None:
        # close curtains
        curtains = get_room_actuators(home, "LivingRoom")
        if curtains is not None:
            for curtain in curtains:
                if curtain.actuator_type == "Curtain":
                    curtain.turn_off()

        # turn off lights
        lights = get_room_actuators(home, "LivingRoom")
        if lights is not None:
            for light in lights:
                if light.actuator_type == "Light":
                    light.turn_off()


def main():
    home = home_plan()

    # Example invocation of plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()