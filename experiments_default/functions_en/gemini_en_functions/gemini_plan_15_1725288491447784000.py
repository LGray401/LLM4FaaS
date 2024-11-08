from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION


def morning_plan(home):
    # 1. Turn on the lights in the living room and bedroom to 60% brightness
    living_room = get_room(home, "LivingRoom")
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("medium")
    bedroom = get_room(home, "Bedroom")
    bedroom_lights = get_room_actuators(home, "Bedroom")
    for light in bedroom_lights:
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("medium")

    # 2. Turn on the coffee machine in the kitchen and make a cup of coffee
    kitchen = get_room(home, "Kitchen")
    kitchen_coffee_machine = get_room_actuators(home, "Kitchen")
    for coffee_machine in kitchen_coffee_machine:
        if coffee_machine.actuator_type == "CoffeeMachine":
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")

    # 3. Turn on the music player in the living room and play a morning playlist
    living_room_music_player = get_room_actuators(home, "LivingRoom")
    for music_player in living_room_music_player:
        if music_player.actuator_type == "MusicPlayer":
            music_player.turn_on()
            music_player.play_music("Morning Playlist")

    # 4. Adjust the temperature in the living room and bedroom to 20 degrees Celsius
    living_room_heater = get_room_actuators(home, "LivingRoom")
    for heater in living_room_heater:
        if heater.actuator_type == "Heater":
            heater.turn_on()
            heater.set_target_temperature(20)
    bedroom_heater = get_room_actuators(home, "Bedroom")
    for heater in bedroom_heater:
        if heater.actuator_type == "Heater":
            heater.turn_on()
            heater.set_target_temperature(20)

    # 5. Open the window in the living room and bedroom for fresh air
    living_room_windows = get_room_actuators(home, "LivingRoom")
    for window in living_room_windows:
        if window.actuator_type == "Window":
            window.turn_on()
    bedroom_windows = get_room_actuators(home, "Bedroom")
    for window in bedroom_windows:
        if window.actuator_type == "Window":
            window.turn_on()


def leave_home_plan(home):
    # 1. Turn off all lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    # 2. Turn off the music player
    all_music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in all_music_players:
        music_player.turn_off()

    # 3. Close all windows
    all_windows = get_all_actuators(home, "Window")
    for window in all_windows:
        window.turn_off()

    # 4. Lock all doors
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.lock()

    # 5. Turn off the coffee machine
    all_coffee_machines = get_all_actuators(home, "CoffeeMachine")
    for coffee_machine in all_coffee_machines:
        coffee_machine.turn_off()

    # 6. Turn off the heater and AC
    all_heaters = get_all_actuators(home, "Heater")
    for heater in all_heaters:
        heater.turn_off()

    all_acs = get_all_actuators(home, "AC")
    for ac in all_acs:
        ac.turn_off()

    # 7. Turn off the cleaning robot
    all_cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for cleaning_robot in all_cleaning_robots:
        cleaning_robot.turn_off()

    # 8. Set the smart TV to standby mode
    all_smart_tvs = get_all_actuators(home, "SmartTV")
    for smart_tv in all_smart_tvs:
        smart_tv.turn_off()

    # 9. Close all curtains
    all_curtains = get_all_actuators(home, "Curtain")
    for curtain in all_curtains:
        curtain.turn_off()


def movie_plan(home):
    # 1. Turn on the lights in the living room to 30% brightness
    living_room = get_room(home, "LivingRoom")
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("low")

    # 2. Turn on the smart TV and play Netflix
    living_room_smart_tv = get_room_actuators(home, "LivingRoom")
    for smart_tv in living_room_smart_tv:
        if smart_tv.actuator_type == "SmartTV":
            smart_tv.turn_on()
            smart_tv.play_channel("Netflix")

    # 3. Turn off the music player
    all_music_players = get_all_actuators(home, "MusicPlayer")
    for music_player in all_music_players:
        music_player.turn_off()

    # 4. Close all windows
    all_windows = get_all_actuators(home, "Window")
    for window in all_windows:
        window.turn_off()

    # 5. Close all curtains
    all_curtains = get_all_actuators(home, "Curtain")
    for curtain in all_curtains:
        curtain.turn_off()

    # 6. Adjust the temperature in the living room to 22 degrees Celsius
    living_room_heater = get_room_actuators(home, "LivingRoom")
    for heater in living_room_heater:
        if heater.actuator_type == "Heater":
            heater.turn_on()
            heater.set_target_temperature(22)


def check_temp(home):
    all_indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for temp_sensor in all_indoor_temp_sensors:
        temp_reading = temp_sensor.get_reading()
        if temp_reading is not None:
            if temp_reading < TEMP_LOW:
                room = get_room(home, temp_sensor.room_name)
                heater = get_room_actuators(home, temp_sensor.room_name)
                for heater in heater:
                    if heater.actuator_type == "Heater":
                        heater.turn_on()
                        heater.set_target_temperature(TEMP_HIGH)
            elif temp_reading > TEMP_HIGH:
                room = get_room(home, temp_sensor.room_name)
                ac = get_room_actuators(home, temp_sensor.room_name)
                for ac in ac:
                    if ac.actuator_type == "AC":
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_LOW)


def check_humidity(home):
    all_humidity_sensors = get_all_sensors(home, "Humidity")
    for humidity_sensor in all_humidity_sensors:
        humidity_reading = humidity_sensor.get_reading()
        if humidity_reading is not None:
            if humidity_reading < HUMIDITY_LOW:
                room = get_room(home, humidity_sensor.room_name)
                humidifier = get_room_actuators(home, humidity_sensor.room_name)
                for humidifier in humidifier:
                    if humidifier.actuator_type == "Humidifier":
                        humidifier.increase_humidity()
            elif humidity_reading > HUMIDITY_HIGH:
                room = get_room(home, humidity_sensor.room_name)
                humidifier = get_room_actuators(home, humidity_sensor.room_name)
                for humidifier in humidifier:
                    if humidifier.actuator_type == "Humidifier":
                        humidifier.decrease_humidity()


def check_light_intensity(home):
    all_light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    for light_intensity_sensor in all_light_intensity_sensors:
        light_intensity_reading = light_intensity_sensor.get_reading()
        if light_intensity_reading is not None:
            if light_intensity_reading < LIGHT_INTENSITY_LOW:
                room = get_room(home, light_intensity_sensor.room_name)
                lights = get_room_actuators(home, light_intensity_sensor.room_name)
                for light in lights:
                    if light.actuator_type == "Light":
                        light.turn_on()
                        light.set_brightness_level("high")
            elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                room = get_room(home, light_intensity_sensor.room_name)
                lights = get_room_actuators(home, light_intensity_sensor.room_name)
                for light in lights:
                    if light.actuator_type == "Light":
                        light.turn_on()
                        light.set_brightness_level("low")


def main():
    home = home_plan()

    # Example plan execution
    morning_plan(home)
    # leave_home_plan(home)
    # movie_plan(home)

    # Continuous monitoring and adjustment
    while True:
        check_temp(home)
        check_humidity(home)
        check_light_intensity(home)

        # Add other sensor checks and actuator control logic here as needed
        # Example:
        # if time.time() - last_cleaning_time > CLEANING_INTERVAL:
        #     clean_house()

        # Wait for a short duration before checking again
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Adjust the delay based on your needs


if __name__ == "__main__":
    main()