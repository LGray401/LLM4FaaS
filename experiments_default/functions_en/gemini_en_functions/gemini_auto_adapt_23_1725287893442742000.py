# functions/function.py
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time


def main():
    """
    This function demonstrates the basic functionality of the smart home system.
    It interacts with sensors, actuators, and the home plan to simulate real-world scenarios.
    """
    # Initialize the home plan
    home = home_plan()
    print_home_plan(home)

    # Example scenario: Adjusting temperature in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        living_room_actuators = get_room_actuators(home, "LivingRoom")

        # Get the temperature sensor in the living room
        temp_sensor = None
        for sensor in living_room_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temp_sensor = sensor
                break

        if temp_sensor:
            # Turn on the temperature sensor
            temp_sensor.turn_on()

            # Get the current temperature
            current_temperature = temp_sensor.get_reading()

            # Adjust the temperature using the heater
            heater = None
            for actuator in living_room_actuators:
                if isinstance(actuator, Heater):
                    heater = actuator
                    break

            if heater:
                # Set the target temperature
                target_temperature = 23  # Example target temperature
                heater.set_target_temperature(target_temperature)

                # Simulate temperature adjustment
                while True:
                    current_temperature = temp_sensor.get_reading()
                    heater.adjust_temperature(current_temperature)
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                    if abs(current_temperature - target_temperature) < 0.5:
                        break
        else:
            print("Temperature sensor not found in LivingRoom.")

    # Example scenario: Turn on the lights in the Bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        bedroom_actuators = get_room_actuators(home, "Bedroom")
        # Find the light in Bedroom
        light = None
        for actuator in bedroom_actuators:
            if isinstance(actuator, Light):
                light = actuator
                break

        if light:
            # Turn on the light
            light.turn_on()
            light.set_brightness_level("medium")
        else:
            print("Light not found in Bedroom.")

    # Example scenario: Play music in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        music_player = None
        for actuator in living_room_actuators:
            if isinstance(actuator, MusicPlayer):
                music_player = actuator
                break
        if music_player:
            music_player.turn_on()
            music_player.play_music("Classical")
        else:
            print("Music Player not found in LivingRoom.")

    # Example scenario: Trigger daily cleaning routine in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        cleaning_robot = None
        for actuator in living_room_actuators:
            if isinstance(actuator, CleaningRobot):
                cleaning_robot = actuator
                break

        if cleaning_robot:
            cleaning_robot.turn_on()
            cleaning_robot.daily_routine()

    # Example scenario: Watch TV in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        smart_tv = None
        for actuator in living_room_actuators:
            if isinstance(actuator, SmartTV):
                smart_tv = actuator
                break

        if smart_tv:
            smart_tv.turn_on()
            smart_tv.play_channel("News")
        else:
            print("Smart TV not found in LivingRoom.")

    # Example scenario: Make coffee in the Kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        kitchen_actuators = get_room_actuators(home, "Kitchen")
        coffee_machine = None
        for actuator in kitchen_actuators:
            if isinstance(actuator, CoffeeMachine):
                coffee_machine = actuator
                break

        if coffee_machine:
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")
        else:
            print("Coffee Machine not found in Kitchen.")

    # Example scenario: Turn on the light in the Bathroom
    bathroom = get_room(home, "Bathroom")
    if bathroom:
        bathroom_actuators = get_room_actuators(home, "Bathroom")
        light = None
        for actuator in bathroom_actuators:
            if isinstance(actuator, Light):
                light = actuator
                break

        if light:
            light.turn_on()
        else:
            print("Light not found in Bathroom.")

    # Example scenario: Get the humidity in the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        humidity_sensor = None
        for sensor in living_room_sensors:
            if isinstance(sensor, HumiditySensor):
                humidity_sensor = sensor
                break

        if humidity_sensor:
            humidity_sensor.turn_on()
            humidity_reading = humidity_sensor.get_reading()
            print(f"Humidity in LivingRoom: {humidity_reading}%")
        else:
            print("Humidity sensor not found in LivingRoom.")

    # Example scenario: Check if the smoke sensor in the Kitchen is triggered
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        kitchen_sensors = get_room_sensors(home, "Kitchen")
        smoke_sensor = None
        for sensor in kitchen_sensors:
            if isinstance(sensor, SmokeSensor):
                smoke_sensor = sensor
                break

        if smoke_sensor:
            smoke_sensor.turn_on()
            smoke_reading = smoke_sensor.get_reading()
            print(f"Smoke sensor in Kitchen reading: {smoke_reading}")
            if smoke_reading > 50:  # Example threshold for smoke alarm
                print("Smoke alarm triggered!")
                notification_sender = None
                for actuator in kitchen_actuators:
                    if isinstance(actuator, NotificationSender):
                        notification_sender = actuator
                        break

                if notification_sender:
                    notification_sender.turn_on()
                    notification_sender.notification_sender(
                        "Smoke detected in the Kitchen! Please evacuate the house.")
        else:
            print("Smoke sensor not found in Kitchen.")

    # Example scenario: Check if the light in the Bedroom is too bright
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        bedroom_sensors = get_room_sensors(home, "Bedroom")
        light_intensive_sensor = None
        for sensor in bedroom_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                light_intensive_sensor = sensor
                break

        if light_intensive_sensor:
            light_intensive_sensor.turn_on()
            light_intensity_reading = light_intensive_sensor.get_reading()
            print(f"Light intensity in Bedroom: {light_intensity_reading} lux")

            bedroom_actuators = get_room_actuators(home, "Bedroom")
            light = None
            for actuator in bedroom_actuators:
                if isinstance(actuator, Light):
                    light = actuator
                    break

            if light:
                if light_intensity_reading > LIGHT_INTENSITY_HIGH:
                    print("Light in Bedroom is too bright. Dimming the light.")
                    light.set_brightness_level("low")
        else:
            print("Light intensive sensor not found in Bedroom.")

    # Example scenario: Open the windows in the LivingRoom if the temperature is too high
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        temp_sensor = None
        for sensor in living_room_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temp_sensor = sensor
                break

        if temp_sensor:
            temp_sensor.turn_on()
            current_temperature = temp_sensor.get_reading()

            living_room_actuators = get_room_actuators(home, "LivingRoom")
            window = None
            for actuator in living_room_actuators:
                if isinstance(actuator, Window):
                    window = actuator
                    break

            if window:
                if current_temperature > TEMP_HIGH:
                    print(f"The temperature in LivingRoom is too high ({current_temperature}°C). Opening the windows.")
                    window.turn_on()
        else:
            print("Temperature sensor not found in LivingRoom.")

    # Example scenario: Close the curtains in the Bedroom if the light intensity is too high
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        bedroom_sensors = get_room_sensors(home, "Bedroom")
        light_intensive_sensor = None
        for sensor in bedroom_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                light_intensive_sensor = sensor
                break

        if light_intensive_sensor:
            light_intensive_sensor.turn_on()
            light_intensity_reading = light_intensive_sensor.get_reading()

            bedroom_actuators = get_room_actuators(home, "Bedroom")
            curtain = None
            for actuator in bedroom_actuators:
                if isinstance(actuator, Curtain):
                    curtain = actuator
                    break

            if curtain:
                if light_intensity_reading > LIGHT_INTENSITY_HIGH:
                    print(f"Light intensity in Bedroom is too high ({light_intensity_reading} lux). Closing the curtains.")
                    curtain.turn_on()
        else:
            print("Light intensive sensor not found in Bedroom.")

    # Example scenario: Check the humidity in the Bathroom and turn on the humidifier if it's too low
    bathroom = get_room(home, "Bathroom")
    if bathroom:
        bathroom_sensors = get_room_sensors(home, "Bathroom")
        humidity_sensor = None
        for sensor in bathroom_sensors:
            if isinstance(sensor, HumiditySensor):
                humidity_sensor = sensor
                break

        if humidity_sensor:
            humidity_sensor.turn_on()
            humidity_reading = humidity_sensor.get_reading()

            bathroom_actuators = get_room_actuators(home, "Bathroom")
            humidifier = None
            for actuator in bathroom_actuators:
                if isinstance(actuator, Humidifier):
                    humidifier = actuator
                    break

            if humidifier:
                if humidity_reading < HUMIDITY_LOW:
                    print(
                        f"Humidity in Bathroom is too low ({humidity_reading}%). Turning on the humidifier to increase humidity.")
                    humidifier.increase_humidity()
        else:
            print("Humidity sensor not found in Bathroom.")

    # Example scenario: Turn on the AC in the LivingRoom if the temperature is too high
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        temp_sensor = None
        for sensor in living_room_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temp_sensor = sensor
                break

        if temp_sensor:
            temp_sensor.turn_on()
            current_temperature = temp_sensor.get_reading()

            living_room_actuators = get_room_actuators(home, "LivingRoom")
            ac = None
            for actuator in living_room_actuators:
                if isinstance(actuator, AC):
                    ac = actuator
                    break

            if ac:
                if current_temperature > TEMP_HIGH:
                    print(f"The temperature in LivingRoom is too high ({current_temperature}°C). Turning on the AC.")
                    ac.turn_on()
        else:
            print("Temperature sensor not found in LivingRoom.")

    # Example scenario: Get the temperature in the Balcony
    balcony = get_room(home, "Balcony")
    if balcony:
        balcony_sensors = get_room_sensors(home, "Balcony")
        temp_sensor = None
        for sensor in balcony_sensors:
            if isinstance(sensor, OutdoorTemperatureSensor):
                temp_sensor = sensor
                break

        if temp_sensor:
            temp_sensor.turn_on()
            current_temperature = temp_sensor.get_reading()
            print(f"The temperature in Balcony is: {current_temperature}°C")
        else:
            print("Temperature sensor not found in Balcony.")


if __name__ == "__main__":
    main()