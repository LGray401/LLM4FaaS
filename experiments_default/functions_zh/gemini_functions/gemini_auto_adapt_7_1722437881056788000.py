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
    home = home_plan()
    print_home_plan(home)

    # Example usage of functions
    # living_room = get_room(home, "LivingRoom")
    # sensors = get_room_sensors(home, "LivingRoom")
    # actuators = get_room_actuators(home, "LivingRoom")
    # all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    # all_lights = get_all_actuators(home, "Light")
    # print(all_temperature_sensors)

    while True:
        # Get all sensors and their readings
        all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        all_humidity_sensors = get_all_sensors(home, "Humidity")
        all_light_sensors = get_all_sensors(home, "LightIntensive")

        # Check Temperature
        for sensor in all_temperature_sensors:
            sensor.turn_on()
            temp = sensor.get_reading()
            if temp is not None:
                # Get all heaters in the room
                room = get_room(home, sensor.room_name)
                heaters = get_room_actuators(room, "Heater")

                if temp < TEMP_LOW:
                    for heater in heaters:
                        heater.turn_on()
                        heater.set_target_temperature(temp + 5)
                        print(
                            f"It's cold in {sensor.room_name}. Turning on heater to {heater.target_temperature}°C")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                elif temp > TEMP_HIGH:
                    for heater in heaters:
                        heater.turn_on()
                        heater.set_target_temperature(temp - 5)
                        print(
                            f"It's hot in {sensor.room_name}. Turning on heater to {heater.target_temperature}°C")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

                # Get all ACs in the room
                acs = get_room_actuators(room, "AC")
                if temp > TEMP_HIGH:
                    for ac in acs:
                        ac.turn_on()
                        ac.set_target_temperature(temp - 5)
                        print(f"It's hot in {sensor.room_name}. Turning on AC to {ac.target_temperature}°C")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                elif temp < TEMP_LOW:
                    for ac in acs:
                        ac.turn_on()
                        ac.set_target_temperature(temp + 5)
                        print(f"It's cold in {sensor.room_name}. Turning on AC to {ac.target_temperature}°C")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            sensor.turn_off()

        # Check Humidity
        for sensor in all_humidity_sensors:
            sensor.turn_on()
            humidity = sensor.get_reading()
            if humidity is not None:
                # Get all humidifiers in the room
                room = get_room(home, sensor.room_name)
                humidifiers = get_room_actuators(room, "Humidifier")

                if humidity < HUMIDITY_LOW:
                    for humidifier in humidifiers:
                        humidifier.increase_humidity()
                        print(f"The humidity in {sensor.room_name} is low, increasing humidity")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                elif humidity > HUMIDITY_HIGH:
                    for humidifier in humidifiers:
                        humidifier.decrease_humidity()
                        print(f"The humidity in {sensor.room_name} is high, decreasing humidity")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            sensor.turn_off()

        # Check Light Intensity
        for sensor in all_light_sensors:
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                # Get all lights in the room
                room = get_room(home, sensor.room_name)
                lights = get_room_actuators(room, "Light")

                if light_intensity < LIGHT_INTENSITY_LOW:
                    for light in lights:
                        light.turn_on()
                        print(f"It's dark in {sensor.room_name}. Turning on light.")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    for light in lights:
                        light.turn_off()
                        print(f"It's bright in {sensor.room_name}. Turning off light.")
                        time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            sensor.turn_off()

        # Example: Daily cleaning routine
        # This section is for testing purposes
        all_cleaning_robots = get_all_actuators(home, "CleaningRobot")
        for robot in all_cleaning_robots:
            robot.turn_on()
            robot.daily_routine()
            time.sleep(DAILY_ROUTINE_DURATION)

        time.sleep(5)  # Adjust the sleep duration as needed

        # # Example: Turning on Music player in the living room
        # living_room = get_room(home, "LivingRoom")
        # music_players = get_room_actuators(living_room, "MusicPlayer")
        # for player in music_players:
        #     player.turn_on()
        #     player.play_music("Classical")
        #     time.sleep(5)

        # Example: Playing TV in the living room
        # living_room = get_room(home, "LivingRoom")
        # TVs = get_room_actuators(living_room, "SmartTV")
        # for TV in TVs:
        #     TV.turn_on()
        #     TV.play_channel("BBC")
        #     time.sleep(5)

        # Example: Making coffee in the kitchen
        # kitchen = get_room(home, "Kitchen")
        # coffee_machines = get_room_actuators(kitchen, "CoffeeMachine")
        # for machine in coffee_machines:
        #     machine.turn_on()
        #     machine.make_coffee("Espresso")
        #     time.sleep(5)

        # Example: Turning on the light in the bathroom
        # bathroom = get_room(home, "Bathroom")
        # lights = get_room_actuators(bathroom, "Light")
        # for light in lights:
        #     light.turn_on()
        #     time.sleep(5)

        # Example: Sending a notification to the living room
        # living_room = get_room(home, "LivingRoom")
        # notification_senders = get_room_actuators(living_room, "NotificationSender")
        # for sender in notification_senders:
        #     sender.turn_on()
        #     sender.notification_sender("The door is open")
        #     time.sleep(5)

        # Example: Turning on the heater in the bedroom
        # bedroom = get_room(home, "Bedroom")
        # heaters = get_room_actuators(bedroom, "Heater")
        # for heater in heaters:
        #     heater.turn_on()
        #     heater.set_target_temperature(22)
        #     time.sleep(5)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Necessary imports from `home_plan.py`, `sensor.py`, `actuator.py`, and `config.py` files.
#    - `time` module for sleep functions.

# 2. **`main()` function:**
#    - Calls `home_plan()` to create the home structure.
#    - Prints the home plan using `print_home_plan()`.
#    - Contains a `while True` loop to continuously monitor and control the smart home.

# 3. **Sensor Readings and Control:**
#    - Gets all temperature sensors (`all_temperature_sensors`), humidity sensors (`all_humidity_sensors`), and light intensity sensors (`all_light_sensors`).
#    - Iterates through each sensor type:
#      - Turns the sensor on (`sensor.turn_on()`).
#      - Gets the sensor reading.
#      - Based on the reading and configured thresholds:
#        - Activates/deactivates relevant actuators (heaters, ACs, humidifiers, lights).
#        - Provides informative messages to the user.
#        - Uses `time.sleep()` for pauses between actions.

# 4. **Example Usage:**
#    - Demonstrates how to access rooms, sensors, and actuators using the functions provided in `home_plan.py`.
#    - Includes examples of:
#      - Daily cleaning routine with `CleaningRobot`.
#      - Playing music, TV, and making coffee.
#      - Turning on lights and sending notifications.
#      - Turning on heaters.

# **Key Improvements:**

# - **Sensor Reading and Control:**  The code now actively reads sensor values and triggers actuators based on thresholds.
# - **Real-time Monitoring:** The `while True` loop allows for continuous monitoring and control of the smart home.
# - **User Messages:** The code provides user-friendly messages about actions being taken.
# - **Example Usage:** The example sections demonstrate how to interact with the smart home functions.

# **To Run This Code:**

# 1. Make sure you have the `home` folder containing the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files.
# 2. Create a `functions` folder.
# 3. Save this code as `function.py` inside the `functions` folder.
# 4. Run `function.py` from your terminal: `python functions/function.py`

# This will simulate the smart home behavior, logging messages and taking actions based on the sensor readings and configured thresholds. Remember to customize the thresholds, actions, and sleep durations in the `config.py` file and within the `main()` function for your specific needs.
