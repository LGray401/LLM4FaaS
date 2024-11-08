from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
import time


def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        for curtain in get_room_actuators(home, "LivingRoom"):
            if curtain.actuator_type == "Curtain":
                curtain.turn_on()
                print(f"Open the curtain in {living_room.name}")

    print("Finish Morning Plan!")


def leave_home_plan(home):
    # Turn off all the lights
    lights = get_all_actuators(home, "Light")
    if lights is not None:
        for light in lights:
            light.turn_off()
            print(f"Turn off the light in {light.room_name}")

    # Lock all doors
    doors = get_all_actuators(home, "Door")
    if doors is not None:
        for door in doors:
            door.lock()
            print(f"Lock the door in {door.room_name}")

    # Close all windows
    windows = get_all_actuators(home, "Window")
    if windows is not None:
        for window in windows:
            window.turn_off()
            print(f"Close the window in {window.room_name}")

    print("Finish Leave Home Plan!")


def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        tv = get_room_actuators(home, "LivingRoom")
        if tv is not None:
            for tv in tv:
                if tv.actuator_type == "SmartTV":
                    tv.turn_on()
                    tv.play_channel("Netflix")
                    print("Turn on the TV and play Netflix")

    print("Finish Movie Plan!")


def adjust_temperature(home):
    for room in home:
        # Get temperature sensors for each room
        temperature_sensors = get_room_sensors(home, room.name)
        if temperature_sensors is not None:
            for temperature_sensor in temperature_sensors:
                if temperature_sensor.sensor_type == "IndoorTemperature":
                    current_temperature = temperature_sensor.get_reading()
                    # Check if temperature sensor is ON
                    if temperature_sensor.get_status() == "on":
                        # Find heaters and ACs in the same room
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Heater":
                                actuator.adjust_temperature(current_temperature)
                            elif actuator.actuator_type == "AC":
                                actuator.adjust_temperature(current_temperature)
                    else:
                        print(
                            f"Temperature Sensor {temperature_sensor.id} is currently OFF, Cannot Adjust Temperature")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def adjust_humidity(home):
    for room in home:
        # Get humidity sensors for each room
        humidity_sensors = get_room_sensors(home, room.name)
        if humidity_sensors is not None:
            for humidity_sensor in humidity_sensors:
                if humidity_sensor.sensor_type == "Humidity":
                    current_humidity = humidity_sensor.get_reading()
                    # Check if humidity sensor is ON
                    if humidity_sensor.get_status() == "on":
                        # Find Humidifiers in the same room
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Humidifier":
                                if current_humidity < HUMIDITY_LOW:
                                    actuator.increase_humidity()
                                elif current_humidity > HUMIDITY_HIGH:
                                    actuator.decrease_humidity()
                    else:
                        print(
                            f"Humidity Sensor {humidity_sensor.id} is currently OFF, Cannot Adjust Humidity")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def adjust_light(home):
    for room in home:
        light_intensity_sensors = get_room_sensors(home, room.name)
        if light_intensity_sensors is not None:
            for light_intensity_sensor in light_intensity_sensors:
                if light_intensity_sensor.sensor_type == "LightIntensive":
                    current_light_intensity = light_intensity_sensor.get_reading()
                    # Check if light_intensity sensor is ON
                    if light_intensity_sensor.get_status() == "on":
                        # Find lights in the same room
                        for actuator in room.actuators:
                            if actuator.actuator_type == "Light":
                                if current_light_intensity < LIGHT_INTENSITY_LOW:
                                    actuator.turn_on()
                                    actuator.set_brightness_level("high")
                                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                                    actuator.turn_off()
                    else:
                        print(
                            f"Light Intensity Sensor {light_intensity_sensor.id} is currently OFF, Cannot Adjust Light")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def main():
    home = home_plan()
    print(f"Home Plan created, it includes:\n")
    # Example invocation of the function
    # morning_plan(home)
    # leave_home_plan(home)
    # movie_plan(home)

    # while True:
    adjust_temperature(home)
    adjust_humidity(home)
    adjust_light(home)
    time.sleep(1)  # Wait for 1 second before checking again


if __name__ == "__main__":
    main()
