from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import Sensor
from home.actuator import Actuator
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW


def main():
    home = home_plan()
    # print(home)
    # get_room(home, "LivingRoom").print_info()
    # print(get_room_actuators(home, "LivingRoom"))
    # print(get_room_sensors(home, "LivingRoom"))

    # turn_on_all_lights(home)

    # Example for turning on lights in "LivingRoom"
    living_room = get_room(home, "LivingRoom")
    # print(living_room.actuators)
    living_room_lights = get_room_actuators(home, "LivingRoom")
    if living_room_lights:
        for light in living_room_lights:
            if light.actuator_type == "Light":
                light.turn_on()
                light.set_brightness_level("high")

    # Example for controlling the AC in the "LivingRoom"
    living_room_ac = get_room_actuators(home, "LivingRoom")
    # print(living_room_ac)
    if living_room_ac:
        for ac in living_room_ac:
            if ac.actuator_type == "AC":
                ac.set_target_temperature(22)  # Set desired temperature
                # Get temperature sensor readings and adjust the AC accordingly
                temperature_sensors = get_room_sensors(home, "LivingRoom")
                # print(temperature_sensors)
                if temperature_sensors:
                    for temperature_sensor in temperature_sensors:
                        if temperature_sensor.sensor_type == "IndoorTemperature":
                            current_temperature = temperature_sensor.get_reading()
                            if current_temperature:
                                ac.adjust_temperature(current_temperature)

    # Example for managing coffee machine in "Kitchen"
    kitchen = get_room(home, "Kitchen")
    # print(kitchen.actuators)
    kitchen_coffee_machine = get_room_actuators(home, "Kitchen")
    if kitchen_coffee_machine:
        for coffee_machine in kitchen_coffee_machine:
            if coffee_machine.actuator_type == "CoffeeMachine":
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Cappuccino")

    # Example for checking and managing smoke sensor in "Kitchen"
    kitchen = get_room(home, "Kitchen")
    kitchen_smoke_sensors = get_room_sensors(home, "Kitchen")
    if kitchen_smoke_sensors:
        for smoke_sensor in kitchen_smoke_sensors:
            if smoke_sensor.sensor_type == "Smoke":
                smoke_reading = smoke_sensor.get_reading()
                if smoke_reading > 50:
                    # Trigger alarm or notification
                    print(f"Smoke detected in {kitchen.name}!")
                    # Example: send notification
                    kitchen_notification_sender = get_room_actuators(home, "Kitchen")
                    if kitchen_notification_sender:
                        for notification_sender in kitchen_notification_sender:
                            if notification_sender.actuator_type == "NotificationSender":
                                notification_sender.notification_sender(
                                    f"Smoke detected in {kitchen.name}! Please check!")

    # Example for checking and managing temperature in "LivingRoom"
    living_room_temp_sensors = get_room_sensors(home, "LivingRoom")
    # print(living_room_temp_sensors)
    if living_room_temp_sensors:
        for temperature_sensor in living_room_temp_sensors:
            if temperature_sensor.sensor_type == "IndoorTemperature":
                temperature = temperature_sensor.get_reading()
                if temperature:
                    if temperature < TEMP_LOW:
                        print(
                            f"Temperature in {living_room.name} is too low. Turn on heater for {TEMP_CHANGE_DURATION_WINDOW} seconds.")
                        # Example: turn on heater
                        living_room_heater = get_room_actuators(home, "LivingRoom")
                        if living_room_heater:
                            for heater in living_room_heater:
                                if heater.actuator_type == "Heater":
                                    heater.turn_on()
                                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                                    heater.turn_off()
                    elif temperature > TEMP_HIGH:
                        print(
                            f"Temperature in {living_room.name} is too high. Turn on AC for {TEMP_CHANGE_DURATION_WINDOW} seconds.")
                        # Example: turn on AC
                        living_room_ac = get_room_actuators(home, "LivingRoom")
                        if living_room_ac:
                            for ac in living_room_ac:
                                if ac.actuator_type == "AC":
                                    ac.turn_on()
                                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                                    ac.turn_off()

    # Example for checking and managing humidity in "Bathroom"
    bathroom_humidity_sensors = get_room_sensors(home, "Bathroom")
    # print(bathroom_humidity_sensors)
    if bathroom_humidity_sensors:
        for humidity_sensor in bathroom_humidity_sensors:
            if humidity_sensor.sensor_type == "Humidity":
                humidity = humidity_sensor.get_reading()
                if humidity:
                    if humidity < HUMIDITY_LOW:
                        print(
                            f"Humidity in {living_room.name} is too low. Turn on humidifier for {TEMP_CHANGE_DURATION_WINDOW} seconds.")
                        # Example: turn on humidifier
                        bathroom_humidifier = get_room_actuators(home, "Bathroom")
                        if bathroom_humidifier:
                            for humidifier in bathroom_humidifier:
                                if humidifier.actuator_type == "Humidifier":
                                    humidifier.increase_humidity()
                                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                                    # humidifier.turn_off()
                    elif humidity > HUMIDITY_HIGH:
                        print(
                            f"Humidity in {living_room.name} is too high. Turn on dehumidifier for {TEMP_CHANGE_DURATION_WINDOW} seconds.")
                        # Example: turn on dehumidifier
                        bathroom_humidifier = get_room_actuators(home, "Bathroom")
                        if bathroom_humidifier:
                            for humidifier in bathroom_humidifier:
                                if humidifier.actuator_type == "Humidifier":
                                    humidifier.decrease_humidity()
                                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                                    # humidifier.turn_off()

    # Example for checking and managing light intensity in "LivingRoom"
    living_room_light_sensors = get_room_sensors(home, "LivingRoom")
    if living_room_light_sensors:
        for light_sensor in living_room_light_sensors:
            if light_sensor.sensor_type == "LightIntensive":
                light_intensity = light_sensor.get_reading()
                if light_intensity:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        print(
                            f"Light intensity in {living_room.name} is too low. Turn on light for {TEMP_CHANGE_DURATION_WINDOW} seconds.")
                        # Example: turn on light
                        living_room_light = get_room_actuators(home, "LivingRoom")
                        if living_room_light:
                            for light in living_room_light:
                                if light.actuator_type == "Light":
                                    light.turn_on()
                                    # time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                                    # light.turn_off()
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        print(
                            f"Light intensity in {living_room.name} is too high. Turn off light for {TEMP_CHANGE_DURATION_WINDOW} seconds.")
                        # Example: turn off light
                        living_room_light = get_room_actuators(home, "LivingRoom")
                        if living_room_light:
                            for light in living_room_light:
                                if light.actuator_type == "Light":
                                    light.turn_off()
                                    # time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                                    # light.turn_off()

    # Example for triggering daily cleaning routine for cleaning robot in "LivingRoom"
    living_room_cleaning_robot = get_room_actuators(home, "LivingRoom")
    if living_room_cleaning_robot:
        for cleaning_robot in living_room_cleaning_robot:
            if cleaning_robot.actuator_type == "CleaningRobot":
                cleaning_robot.turn_on()
                cleaning_robot.daily_routine()

    # Example for playing a specific playlist on the music player in "LivingRoom"
    living_room_music_player = get_room_actuators(home, "LivingRoom")
    if living_room_music_player:
        for music_player in living_room_music_player:
            if music_player.actuator_type == "MusicPlayer":
                music_player.turn_on()
                music_player.play_music("Jazz")

    # Example for playing a specific channel on the SmartTV in "LivingRoom"
    living_room_smart_tv = get_room_actuators(home, "LivingRoom")
    if living_room_smart_tv:
        for smart_tv in living_room_smart_tv:
            if smart_tv.actuator_type == "SmartTV":
                smart_tv.turn_on()
                smart_tv.play_channel("CNN")


def turn_on_all_lights(home):
    for room in home:
        # print(room)
        for actor in room.actuators:
            if actor.actuator_type == "Light":
                actor.turn_on()
                actor.set_brightness_level("high")


if __name__ == "__main__":
    main()
