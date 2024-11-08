from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, \
    CleaningRobot, SmartTV, NotificationSender, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
import time

def morning_plan(home):
    print("Good Morning!")
    # Turn on the lights in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_lights = get_room_actuators(home, "LivingRoom")
        for light in living_room_lights:
            if light.actuator_type == "Light":
                light.turn_on()
                light.set_brightness_level("medium")

    # Open the curtains in the living room
    living_room_curtains = get_room_actuators(home, "LivingRoom")
    for curtain in living_room_curtains:
        if curtain.actuator_type == "Curtain":
            curtain.turn_on()

    # Turn on the AC in the living room and set the temperature
    living_room_ac = get_room_actuators(home, "LivingRoom")
    for ac in living_room_ac:
        if ac.actuator_type == "AC":
            ac.turn_on()
            ac.set_target_temperature(22)

    # Make coffee in the kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen is not None:
        kitchen_coffee_machine = get_room_actuators(home, "Kitchen")
        for coffee_machine in kitchen_coffee_machine:
            if coffee_machine.actuator_type == "CoffeeMachine":
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Espresso")

    # Play some music in the living room
    living_room_music_player = get_room_actuators(home, "LivingRoom")
    for music_player in living_room_music_player:
        if music_player.actuator_type == "MusicPlayer":
            music_player.turn_on()
            music_player.play_music("Morning Jazz")

    print("Morning Plan Completed!")

def leave_home_plan(home):
    print("Leaving Home!")
    # Turn off all the lights
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        light.turn_off()

    # Close all the curtains
    all_curtains = get_all_actuators(home, "Curtain")
    for curtain in all_curtains:
        curtain.turn_off()

    # Turn off the AC in the living room
    living_room_ac = get_room_actuators(home, "LivingRoom")
    for ac in living_room_ac:
        if ac.actuator_type == "AC":
            ac.turn_off()

    # Lock all the doors
    all_doors = get_all_actuators(home, "Door")
    for door in all_doors:
        door.lock()

    # Start the cleaning robot in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_cleaning_robot = get_room_actuators(home, "LivingRoom")
        for cleaning_robot in living_room_cleaning_robot:
            if cleaning_robot.actuator_type == "CleaningRobot":
                cleaning_robot.turn_on()
                cleaning_robot.daily_routine()

    print("Leaving Home Plan Completed!")

def movie_plan(home):
    print("Movie Time!")
    # Turn on the TV in the living room and play a movie
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_tv = get_room_actuators(home, "LivingRoom")
        for tv in living_room_tv:
            if tv.actuator_type == "SmartTV":
                tv.turn_on()
                tv.play_channel("Netflix")

    # Dim the lights in the living room
    living_room_lights = get_room_actuators(home, "LivingRoom")
    for light in living_room_lights:
        if light.actuator_type == "Light":
            light.turn_on()
            light.set_brightness_level("low")

    # Close the curtains in the living room
    living_room_curtains = get_room_actuators(home, "LivingRoom")
    for curtain in living_room_curtains:
        if curtain.actuator_type == "Curtain":
            curtain.turn_off()

    # Turn on the AC in the living room and set the temperature
    living_room_ac = get_room_actuators(home, "LivingRoom")
    for ac in living_room_ac:
        if ac.actuator_type == "AC":
            ac.turn_on()
            ac.set_target_temperature(20)

    print("Movie Plan Completed!")

def auto_adjust_temperature(home):
    # Check the temperature in each room
    all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in all_temperature_sensors:
        current_temperature = sensor.get_reading()
        room_name = sensor.room_name
        # Adjust the temperature based on the room and the sensor reading
        if current_temperature < TEMP_LOW:
            # Turn on the heater
            room_heaters = get_room_actuators(home, room_name)
            for heater in room_heaters:
                if heater.actuator_type == "Heater":
                    heater.turn_on()
                    heater.set_target_temperature(TEMP_HIGH)
            # Notify user
            notification_sender = get_room_actuators(home, room_name)
            for sender in notification_sender:
                if sender.actuator_type == "NotificationSender":
                    sender.notification_sender(f"The temperature in {room_name} is below {TEMP_LOW} degrees, turning on the heater.")
        elif current_temperature > TEMP_HIGH:
            # Turn on the AC
            room_acs = get_room_actuators(home, room_name)
            for ac in room_acs:
                if ac.actuator_type == "AC":
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_LOW)
            # Notify user
            notification_sender = get_room_actuators(home, room_name)
            for sender in notification_sender:
                if sender.actuator_type == "NotificationSender":
                    sender.notification_sender(f"The temperature in {room_name} is above {TEMP_HIGH} degrees, turning on the AC.")
        else:
            # Turn off the heater and AC
            room_heaters = get_room_actuators(home, room_name)
            for heater in room_heaters:
                if heater.actuator_type == "Heater":
                    heater.turn_off()
            room_acs = get_room_actuators(home, room_name)
            for ac in room_acs:
                if ac.actuator_type == "AC":
                    ac.turn_off()

def auto_adjust_humidity(home):
    # Check the humidity in each room
    all_humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in all_humidity_sensors:
        current_humidity = sensor.get_reading()
        room_name = sensor.room_name
        # Adjust the humidity based on the room and the sensor reading
        if current_humidity < HUMIDITY_LOW:
            # Turn on the humidifier
            room_humidifiers = get_room_actuators(home, room_name)
            for humidifier in room_humidifiers:
                if humidifier.actuator_type == "Humidifier":
                    humidifier.increase_humidity()
            # Notify user
            notification_sender = get_room_actuators(home, room_name)
            for sender in notification_sender:
                if sender.actuator_type == "NotificationSender":
                    sender.notification_sender(f"The humidity in {room_name} is below {HUMIDITY_LOW}%, turning on the humidifier.")
        elif current_humidity > HUMIDITY_HIGH:
            # Turn on the dehumidifier (not implemented in this example)
            # Notify user
            notification_sender = get_room_actuators(home, room_name)
            for sender in notification_sender:
                if sender.actuator_type == "NotificationSender":
                    sender.notification_sender(f"The humidity in {room_name} is above {HUMIDITY_HIGH}%, considering using a dehumidifier.")
        else:
            # Turn off the humidifier and dehumidifier (not implemented in this example)
            room_humidifiers = get_room_actuators(home, room_name)
            for humidifier in room_humidifiers:
                if humidifier.actuator_type == "Humidifier":
                    humidifier.turn_off()

def auto_adjust_light(home):
    # Check the light intensity in each room
    all_light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in all_light_intensity_sensors:
        current_light_intensity = sensor.get_reading()
        room_name = sensor.room_name
        # Adjust the light based on the room and the sensor reading
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            # Turn on the lights
            room_lights = get_room_actuators(home, room_name)
            for light in room_lights:
                if light.actuator_type == "Light":
                    light.turn_on()
                    light.set_brightness_level("medium")
            # Notify user
            notification_sender = get_room_actuators(home, room_name)
            for sender in notification_sender:
                if sender.actuator_type == "NotificationSender":
                    sender.notification_sender(f"The light intensity in {room_name} is below {LIGHT_INTENSITY_LOW} lux, turning on the lights.")
        else:
            # Turn off the lights (if they are already on)
            room_lights = get_room_actuators(home, room_name)
            for light in room_lights:
                if light.actuator_type == "Light":
                    light.turn_off()

def main():
    home = home_plan()

    # Example usage of functions:
    morning_plan(home)
    time.sleep(5)
    leave_home_plan(home)
    time.sleep(5)
    movie_plan(home)

    while True:
        # Auto-adjust temperature, humidity and light
        auto_adjust_temperature(home)
        auto_adjust_humidity(home)
        auto_adjust_light(home)

        # Check for smoke
        all_smoke_sensors = get_all_sensors(home, "Smoke")
        for sensor in all_smoke_sensors:
            smoke_level = sensor.get_reading()
            if smoke_level > 50:
                room_name = sensor.room_name
                # Notify user
                notification_sender = get_room_actuators(home, room_name)
                for sender in notification_sender:
                    if sender.actuator_type == "NotificationSender":
                        sender.notification_sender(f"Smoke detected in {room_name}, please check!")
                # Open windows
                room_windows = get_room_actuators(home, room_name)
                for window in room_windows:
                    if window.actuator_type == "Window":
                        window.turn_on()

        time.sleep(1)

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions for creating the home plan, accessing rooms, sensors, and actuators.
#    - `home.sensor`: Contains classes for different sensor types.
#    - `home.actuator`: Contains classes for different actuator types.
#    - `home.config`: Contains configuration values for thresholds, durations, etc.
#    - `time`: For pausing execution.

# 2. **Define functions for each plan:**
#    - **`morning_plan(home)`:**
#      - Turns on lights, opens curtains, turns on AC, makes coffee, and plays music in the living room.
#    - **`leave_home_plan(home)`:**
#      - Turns off all lights, closes curtains, locks doors, turns on the cleaning robot in the living room.
#    - **`movie_plan(home)`:**
#      - Turns on the TV and plays Netflix, dims the lights, closes curtains, and adjusts the AC temperature in the living room.

# 3. **Define functions for auto-adjustment:**
#    - **`auto_adjust_temperature(home)`:**
#      - Reads temperature from all indoor temperature sensors.
#      - Turns on heaters or ACs based on the temperature thresholds.
#      - Sends notifications to the user.
#    - **`auto_adjust_humidity(home)`:**
#      - Reads humidity from all humidity sensors.
#      - Turns on humidifiers based on humidity thresholds.
#      - Sends notifications to the user.
#    - **`auto_adjust_light(home)`:**
#      - Reads light intensity from all light intensity sensors.
#      - Turns on lights based on light intensity thresholds.

# 4. **Define `main()` function:**
#    - Creates the home plan using `home_plan()`.
#    - Executes the `morning_plan`, `leave_home_plan`, and `movie_plan` functions as examples.
#    - Enters a loop that continuously calls `auto_adjust_temperature`, `auto_adjust_humidity`, and `auto_adjust_light` functions to maintain the desired environment.
#    - Checks for smoke detection and performs actions like sending notifications and opening windows if necessary.

# **Key improvements:**

# - **Clearer organization:** Functions are defined for each plan and auto-adjustment, making the code more readable and modular.
# - **Enhanced functionality:** The code now includes smoke detection and auto-adjustment for humidity and light intensity.
# - **User notifications:** The code sends notifications to the user through a `NotificationSender` actuator when certain conditions are met.
# - **Error handling:** The code gracefully handles cases where rooms or devices are not found.

# **Remember:**
# - This is a basic example. You can extend the functionality by adding more sensors, actuators, plans, and conditions.
# - You can customize the thresholds, durations, and other configuration values to suit your specific needs.
# - Consider using a real-time data source like an IoT platform to provide actual sensor readings instead of random values generated in the code.
