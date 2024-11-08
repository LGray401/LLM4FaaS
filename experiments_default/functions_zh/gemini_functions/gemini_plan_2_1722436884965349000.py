from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_actuators, \
    get_all_sensors
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import Light, Door, Window, Curtain, MusicPlayer, CoffeeMachine, CleaningRobot, SmartTV, Heater, AC, \
    Humidifier, NotificationSender
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def morning_plan(home):
    print(f"-------- Morning Plan --------")
    living_room = get_room(home, "LivingRoom")
    # if living_room is None:
    #     return

    # Open curtains
    curtains = get_room_actuators(living_room, "Curtain")
    if curtains is not None:
        for curtain in curtains:
            curtain.turn_on()

    # Play music
    music_player = get_room_actuators(living_room, "MusicPlayer")
    if music_player is not None:
        for player in music_player:
            player.play_music("Morning Music")

    # Make coffee
    kitchen = get_room(home, "Kitchen")
    coffee_machine = get_room_actuators(kitchen, "CoffeeMachine")
    if coffee_machine is not None:
        for machine in coffee_machine:
            machine.make_coffee("Espresso")

    print("Morning Plan Completed")
    logger.info("Morning Plan Completed")


def leave_home_plan(home):
    print(f"-------- Leave Home Plan --------")
    # Turn off all lights
    lights = get_all_actuators(home, "Light")
    if lights is not None:
        for light in lights:
            light.turn_off()

    # Close all doors
    doors = get_all_actuators(home, "Door")
    if doors is not None:
        for door in doors:
            door.lock()

    # Turn off all sockets except for the refrigerator
    sockets = get_all_actuators(home, "SmartSocket")
    if sockets is not None:
        for socket in sockets:
            if socket.room_name == "Kitchen":
                continue
            else:
                socket.turn_off()

    print("Leave Home Plan Completed")
    logger.info("Leave Home Plan Completed")


def movie_plan(home):
    print(f"-------- Movie Plan --------")
    living_room = get_room(home, "LivingRoom")
    if living_room is None:
        return

    # Close curtains
    curtains = get_room_actuators(living_room, "Curtain")
    if curtains is not None:
        for curtain in curtains:
            curtain.turn_off()

    # Dim lights
    lights = get_room_actuators(living_room, "Light")
    if lights is not None:
        for light in lights:
            light.set_brightness_level("low")

    # Turn on TV and play favorite channel
    tv = get_room_actuators(living_room, "SmartTV")
    if tv is not None:
        for t in tv:
            t.play_channel("Netflix")

    print("Movie Plan Completed")
    logger.info("Movie Plan Completed")


def temperature_control(home):
    # Check indoor temperature in all rooms
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    if indoor_temp_sensors is not None:
        for sensor in indoor_temp_sensors:
            # if sensor.status == "off":
            #     sensor.turn_on()
            temp = sensor.get_reading()
            if temp is not None:
                room_name = sensor.room_name
                room = get_room(home, room_name)
                heaters = get_room_actuators(room, "Heater")
                acs = get_room_actuators(room, "AC")
                if heaters is not None:
                    for heater in heaters:
                        heater.adjust_temperature(temp)
                if acs is not None:
                    for ac in acs:
                        ac.adjust_temperature(temp)

    # Check outdoor temperature
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    if outdoor_temp_sensors is not None:
        for sensor in outdoor_temp_sensors:
            # if sensor.status == "off":
            #     sensor.turn_on()
            temp = sensor.get_reading()
            if temp is not None:
                if temp < TEMP_LOW:
                    # Trigger notification
                    notification_sender = get_all_actuators(home, "NotificationSender")
                    if notification_sender is not None:
                        for sender in notification_sender:
                            sender.notification_sender("Outdoor temperature is low! Please consider wearing warm clothes.")

    print("Temperature Control Completed")
    logger.info("Temperature Control Completed")


def humidity_control(home):
    # Check humidity in all rooms
    humidity_sensors = get_all_sensors(home, "Humidity")
    if humidity_sensors is not None:
        for sensor in humidity_sensors:
            # if sensor.status == "off":
            #     sensor.turn_on()
            humidity = sensor.get_reading()
            if humidity is not None:
                room_name = sensor.room_name
                room = get_room(home, room_name)
                humidifiers = get_room_actuators(room, "Humidifier")
                if humidifiers is not None:
                    for humidifier in humidifiers:
                        if humidity < HUMIDITY_LOW:
                            humidifier.increase_humidity()
                        elif humidity > HUMIDITY_HIGH:
                            humidifier.decrease_humidity()

    print("Humidity Control Completed")
    logger.info("Humidity Control Completed")


def light_intensity_control(home):
    # Check light intensity in all rooms
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    if light_intensity_sensors is not None:
        for sensor in light_intensity_sensors:
            # if sensor.status == "off":
            #     sensor.turn_on()
            intensity = sensor.get_reading()
            if intensity is not None:
                room_name = sensor.room_name
                room = get_room(home, room_name)
                lights = get_room_actuators(room, "Light")
                if lights is not None:
                    for light in lights:
                        if intensity < LIGHT_INTENSITY_LOW:
                            light.turn_on()
                        elif intensity > LIGHT_INTENSITY_HIGH:
                            light.turn_off()

    print("Light Intensity Control Completed")
    logger.info("Light Intensity Control Completed")


def smoke_detection(home):
    # Check smoke levels in all rooms
    smoke_sensors = get_all_sensors(home, "Smoke")
    if smoke_sensors is not None:
        for sensor in smoke_sensors:
            # if sensor.status == "off":
            #     sensor.turn_on()
            smoke_level = sensor.get_reading()
            if smoke_level is not None:
                if smoke_level > 50:
                    # Trigger alarm
                    notification_sender = get_all_actuators(home, "NotificationSender")
                    if notification_sender is not None:
                        for sender in notification_sender:
                            sender.notification_sender(
                                "Smoke detected! Please evacuate the premises immediately.")
                    # Open windows
                    room_name = sensor.room_name
                    room = get_room(home, room_name)
                    windows = get_room_actuators(room, "Window")
                    if windows is not None:
                        for window in windows:
                            window.turn_on()

    print("Smoke Detection Completed")
    logger.info("Smoke Detection Completed")


def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)
    temperature_control(home)
    humidity_control(home)
    light_intensity_control(home)
    smoke_detection(home)


if __name__ == "__main__":
    main()