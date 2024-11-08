from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_actuators, \
    get_all_sensors
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor, HumiditySensor, \
    SmokeSensor
from home.actuator import Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, \
    CleaningRobot, NotificationSender, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

# from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
# from home.logger_config import logger
import time


def morning_plan(home):
    # print("Start Morning Plan")
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        music_player = get_all_actuators(home, "MusicPlayer")[0]
        music_player.turn_on()
        music_player.play_music("Morning Music Playlist")
        print("Start playing morning music in LivingRoom.")
        # time.sleep(10)


def leave_home_plan(home):
    # print("Start Leave Home Plan")
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        smart_socket = get_all_actuators(home, "SmartSocket")
        for s in smart_socket:
            s.turn_off()
            print(f"Unplug the socket {s.id}")
        # time.sleep(10)


def movie_plan(home):
    # print("Start Movie Plan")
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        curtain = get_all_actuators(home, "Curtain")[0]
        curtain.turn_on()
        print(f"Open the curtain {curtain.id}")
        # time.sleep(10)


def adjust_temperature(home):
    # print("Start Adjust Temperature")
    for room in home:
        # print(f"Checking Room {room.name}")
        temperature_sensors = get_room_sensors(home, room.name)
        if temperature_sensors is not None:
            for sensor in temperature_sensors:
                if sensor.sensor_type == "IndoorTemperature":
                    temperature = sensor.get_reading()
                    if temperature is not None:
                        heaters = get_room_actuators(home, room.name)
                        acs = get_room_actuators(home, room.name)
                        if heaters is not None and acs is not None:
                            for heater in heaters:
                                if heater.actuator_type == "Heater":
                                    heater.set_target_temperature(TEMP_HIGH)
                                    heater.adjust_temperature(temperature)
                            for ac in acs:
                                if ac.actuator_type == "AC":
                                    ac.set_target_temperature(TEMP_LOW)
                                    ac.adjust_temperature(temperature)
                        elif heaters is not None:
                            for heater in heaters:
                                if heater.actuator_type == "Heater":
                                    heater.set_target_temperature(TEMP_HIGH)
                                    heater.adjust_temperature(temperature)
                        elif acs is not None:
                            for ac in acs:
                                if ac.actuator_type == "AC":
                                    ac.set_target_temperature(TEMP_LOW)
                                    ac.adjust_temperature(temperature)
                        else:
                            print(f"No Heater or AC found in {room.name}")


def adjust_humidity(home):
    # print("Start Adjust Humidity")
    for room in home:
        # print(f"Checking Room {room.name}")
        humidity_sensors = get_room_sensors(home, room.name)
        if humidity_sensors is not None:
            for sensor in humidity_sensors:
                if sensor.sensor_type == "Humidity":
                    humidity = sensor.get_reading()
                    if humidity is not None:
                        humidifiers = get_room_actuators(home, room.name)
                        if humidifiers is not None:
                            for humidifier in humidifiers:
                                if humidifier.actuator_type == "Humidifier":
                                    if humidity < HUMIDITY_LOW:
                                        humidifier.increase_humidity()
                                    elif humidity > HUMIDITY_HIGH:
                                        humidifier.decrease_humidity()


def adjust_lighting(home):
    # print("Start Adjust Lighting")
    for room in home:
        # print(f"Checking Room {room.name}")
        light_sensors = get_room_sensors(home, room.name)
        if light_sensors is not None:
            for sensor in light_sensors:
                if sensor.sensor_type == "LightIntensive":
                    light_intensity = sensor.get_reading()
                    if light_intensity is not None:
                        lights = get_room_actuators(home, room.name)
                        if lights is not None:
                            for light in lights:
                                if light.actuator_type == "Light":
                                    if light_intensity < LIGHT_INTENSITY_LOW:
                                        light.turn_on()
                                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                                        light.turn_off()


def main():
    home = home_plan()

    # adjust_temperature(home)
    # adjust_humidity(home)
    # adjust_lighting(home)

    # Call your plans here
    morning_plan(home)
    # leave_home_plan(home)
    # movie_plan(home)
    while True:
        adjust_temperature(home)
        adjust_humidity(home)
        adjust_lighting(home)
        time.sleep(1)


if __name__ == "__main__":
    main()