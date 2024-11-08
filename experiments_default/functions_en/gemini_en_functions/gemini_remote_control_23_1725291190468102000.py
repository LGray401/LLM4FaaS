from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION

def main():
    """
    The main function of the smart home system.
    """
    home = home_plan()

    # Print the initial home plan
    print_home_plan(home)

    # Example usage of the functions
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        if living_room_sensors:
            print("\nSensors in Living Room:")
            for sensor in living_room_sensors:
                print(f"- {sensor.id}")

        living_room_actuators = get_room_actuators(home, "LivingRoom")
        if living_room_actuators:
            print("\nActuators in Living Room:")
            for actuator in living_room_actuators:
                print(f"- {actuator.id}")

    # Example usage of the sensor and actuator functions
    # Turn on the light in the living room
    living_room_light = get_all_actuators(home, "Light")[0]
    if living_room_light:
        living_room_light.turn_on()
        living_room_light.set_brightness_level("medium")

    # Get the temperature reading in the kitchen
    kitchen_temp_sensor = get_all_sensors(home, "IndoorTemperature")[0]
    if kitchen_temp_sensor:
        kitchen_temp_sensor.turn_on()
        kitchen_temperature = kitchen_temp_sensor.get_reading()

    # Control the heater based on the temperature
    kitchen_heater = get_all_actuators(home, "Heater")[0]
    if kitchen_heater:
        kitchen_heater.set_target_temperature(22)
        kitchen_heater.adjust_temperature(kitchen_temperature)

    # Example usage of the daily routine functionality
    cleaning_robot = get_all_actuators(home, "CleaningRobot")[0]
    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    # Example usage of the notification sender
    notification_sender = get_all_actuators(home, "NotificationSender")[0]
    if notification_sender:
        notification_sender.turn_on()
        notification_sender.notification_sender("The temperature in the kitchen is too low.")

    # Example of light intensity sensor usage
    living_room_light_sensor = get_all_sensors(home, "LightIntensive")[0]
    if living_room_light_sensor:
        living_room_light_sensor.turn_on()
        light_intensity = living_room_light_sensor.get_reading()
        if light_intensity < LIGHT_INTENSITY_LOW:
            print("Light intensity is low, turn on the light.")
            living_room_light.turn_on()
            living_room_light.set_brightness_level("medium")
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            print("Light intensity is high, turn off the light.")
            living_room_light.turn_off()
        else:
            print("Light intensity is normal.")

    # Example of temperature sensor usage
    living_room_temperature_sensor = get_all_sensors(home, "IndoorTemperature")[0]
    if living_room_temperature_sensor:
        living_room_temperature_sensor.turn_on()
        temperature = living_room_temperature_sensor.get_reading()
        if temperature < TEMP_LOW:
            print("Temperature is too low, turn on the heater.")
            living_room_heater = get_all_actuators(home, "Heater")[0]
            if living_room_heater:
                living_room_heater.turn_on()
                living_room_heater.set_target_temperature(22)
        elif temperature > TEMP_HIGH:
            print("Temperature is too high, turn on the AC.")
            living_room_ac = get_all_actuators(home, "AC")[0]
            if living_room_ac:
                living_room_ac.turn_on()
                living_room_ac.set_target_temperature(22)
        else:
            print("Temperature is normal.")

    # Example of humidity sensor usage
    living_room_humidity_sensor = get_all_sensors(home, "Humidity")[0]
    if living_room_humidity_sensor:
        living_room_humidity_sensor.turn_on()
        humidity = living_room_humidity_sensor.get_reading()
        if humidity < HUMIDITY_LOW:
            print("Humidity is too low, turn on the humidifier.")
            living_room_humidifier = get_all_actuators(home, "Humidifier")[0]
            if living_room_humidifier:
                living_room_humidifier.turn_on()
                living_room_humidifier.increase_humidity()
        elif humidity > HUMIDITY_HIGH:
            print("Humidity is too high, turn on the dehumidifier.")
            # add dehumidifier actuator here
        else:
            print("Humidity is normal.")

    # Example of smoke sensor usage
    kitchen_smoke_sensor = get_all_sensors(home, "Smoke")[0]
    if kitchen_smoke_sensor:
        kitchen_smoke_sensor.turn_on()
        smoke_level = kitchen_smoke_sensor.get_reading()
        if smoke_level > 0:
            print("Smoke detected! Turn on the ventilation fan and send a notification.")
            # add ventilation fan actuator here
            notification_sender.notification_sender("Smoke detected in the kitchen!")

    # Example of window and AC control
    living_room_window = get_all_actuators(home, "Window")[0]
    if living_room_window:
        living_room_window.turn_on()
        living_room_temperature_sensor.turn_on()
        for _ in range(TEMP_CHANGE_DURATION_WINDOW):
            temperature = living_room_temperature_sensor.get_reading()
            if temperature < TEMP_LOW:
                print("Temperature is too low, close the window.")
                living_room_window.turn_off()
                # Turn on the heater
                living_room_heater = get_all_actuators(home, "Heater")[0]
                if living_room_heater:
                    living_room_heater.turn_on()
                    living_room_heater.set_target_temperature(22)
            elif temperature > TEMP_HIGH:
                print("Temperature is too high, open the window and turn on the AC.")
                living_room_window.turn_on()
                # Turn on the AC
                living_room_ac = get_all_actuators(home, "AC")[0]
                if living_room_ac:
                    living_room_ac.turn_on()
                    living_room_ac.set_target_temperature(22)
            else:
                print("Temperature is normal, keep the window as it is.")
            time.sleep(1)

    # Example of door lock and unlock
    living_room_door = get_all_actuators(home, "Door")[0]
    if living_room_door:
        living_room_door.turn_on()
        living_room_door.lock()
        time.sleep(5)  # Wait for 5 seconds
        living_room_door.unlock()

    # Example of coffee machine
    kitchen_coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]
    if kitchen_coffee_machine:
        kitchen_coffee_machine.turn_on()
        kitchen_coffee_machine.make_coffee("Latte")
        time.sleep(5)  # Wait for 5 seconds
        kitchen_coffee_machine.turn_off()

    # Example of smart TV
    living_room_smart_tv = get_all_actuators(home, "SmartTV")[0]
    if living_room_smart_tv:
        living_room_smart_tv.turn_on()
        living_room_smart_tv.play_channel("Netflix")
        time.sleep(5)  # Wait for 5 seconds
        living_room_smart_tv.turn_off()

    # Example of music player
    living_room_music_player = get_all_actuators(home, "MusicPlayer")[0]
    if living_room_music_player:
        living_room_music_player.turn_on()
        living_room_music_player.play_music("Pop")
        time.sleep(5)  # Wait for 5 seconds
        living_room_music_player.turn_off()

    # Example of smart socket
    living_room_smart_socket = get_all_actuators(home, "SmartSocket")[0]
    if living_room_smart_socket:
        living_room_smart_socket.turn_on()
        time.sleep(5)  # Wait for 5 seconds
        living_room_smart_socket.turn_off()

    # Example of curtain control
    living_room_curtain = get_all_actuators(home, "Curtain")[0]
    if living_room_curtain:
        living_room_curtain.turn_on()
        # Open the curtain during the day
        living_room_curtain.turn_on()
        time.sleep(5)  # Wait for 5 seconds
        # Close the curtain at night
        living_room_curtain.turn_off()


if __name__ == '__main__':
    main()