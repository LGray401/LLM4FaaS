from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
import time

# Define global variable for home plan
home = home_plan()


def morning_plan():
    # Get Living Room
    living_room = get_room(home, "LivingRoom")

    # Open curtains
    curtains = get_room_actuators(home, "LivingRoom")
    for curtain in curtains:
        if curtain.actuator_type == "Curtain":
            curtain.turn_on()

    # Make coffee
    coffee_machine = get_room_actuators(home, "Kitchen")
    for cm in coffee_machine:
        if cm.actuator_type == "CoffeeMachine":
            cm.turn_on()
            cm.make_coffee("Latte")


def leave_home_plan():
    # Get Living Room
    living_room = get_room(home, "LivingRoom")
    living_room_door = get_room_actuators(home, "LivingRoom")

    # Find and Lock Door
    for door in living_room_door:
        if door.actuator_type == "Door":
            door.lock()
            # Turn off power after locking door
            power_sockets = get_room_actuators(living_room, "LivingRoom")
            for power_socket in power_sockets:
                if power_socket.actuator_type == "SmartSocket":
                    power_socket.turn_off()


def movie_plan():
    # Get Living Room
    living_room = get_room(home, "LivingRoom")

    # Dim the lights
    lights = get_room_actuators(living_room, "LivingRoom")
    for light in lights:
        if light.actuator_type == "Light":
            light.set_brightness_level("low")

    # Turn on TV and play a movie
    tv = get_room_actuators(living_room, "LivingRoom")
    for t in tv:
        if t.actuator_type == "SmartTV":
            t.turn_on()
            t.play_channel("Netflix")

    # Turn on music player
    music_player = get_room_actuators(living_room, "LivingRoom")
    for mp in music_player:
        if mp.actuator_type == "MusicPlayer":
            mp.turn_on()
            mp.play_music("Movie Soundtrack")


def auto_adjust_temperature():
    # Adjust temperature for each room
    for room in home:
        # Check if heater or AC is available in the room
        if any(actuator.actuator_type in ["Heater", "AC"] for actuator in room.actuators):
            temperature_sensors = get_room_sensors(home, room.name)
            # Get indoor temperature
            for sensor in temperature_sensors:
                if sensor.sensor_type == "IndoorTemperature":
                    temperature = sensor.get_reading()

                    # Adjust heater/AC based on temperature
                    heaters = get_room_actuators(home, room.name)
                    acs = get_room_actuators(home, room.name)

                    for heater in heaters:
                        if heater.actuator_type == "Heater":
                            heater.adjust_temperature(temperature)
                    for ac in acs:
                        if ac.actuator_type == "AC":
                            ac.adjust_temperature(temperature)

                    # Wait for a specified duration before checking temperature again
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def auto_adjust_humidity():
    # Adjust humidity for each room
    for room in home:
        # Check if humidifier is available in the room
        if any(actuator.actuator_type == "Humidifier" for actuator in room.actuators):
            humidity_sensors = get_room_sensors(home, room.name)
            # Get indoor humidity
            for sensor in humidity_sensors:
                if sensor.sensor_type == "Humidity":
                    humidity = sensor.get_reading()

                    # Adjust humidifier based on humidity
                    humidifiers = get_room_actuators(home, room.name)
                    for humidifier in humidifiers:
                        if humidifier.actuator_type == "Humidifier":
                            if humidity < HUMIDITY_LOW:
                                humidifier.increase_humidity()
                            elif humidity > HUMIDITY_HIGH:
                                humidifier.decrease_humidity()

                    # Wait for a specified duration before checking humidity again
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def auto_adjust_light():
    # Adjust light for each room
    for room in home:
        # Check if light is available in the room
        if any(actuator.actuator_type == "Light" for actuator in room.actuators):
            light_intensity_sensors = get_room_sensors(home, room.name)
            # Get light intensity
            for sensor in light_intensity_sensors:
                if sensor.sensor_type == "LightIntensive":
                    light_intensity = sensor.get_reading()

                    # Adjust light based on light intensity
                    lights = get_room_actuators(home, room.name)
                    for light in lights:
                        if light.actuator_type == "Light":
                            if light_intensity < LIGHT_INTENSITY_LOW:
                                light.turn_on()
                            elif light_intensity > LIGHT_INTENSITY_HIGH:
                                light.turn_off()

                    # Wait for a specified duration before checking light intensity again
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)


def main():
    while True:
        # Check for temperature changes and adjust heater/AC accordingly
        auto_adjust_temperature()

        # Check for humidity changes and adjust humidifier accordingly
        auto_adjust_humidity()

        # Check for light intensity changes and adjust light accordingly
        auto_adjust_light()

        # # Example: Trigger Morning Plan at 7:30 AM
        # current_time = time.strftime("%H:%M")
        # if current_time == "07:30":
        #     morning_plan()

        # # Example: Trigger Leave Home Plan when door is locked
        # if door_status == "locked":
        #     leave_home_plan()

        # Example: Trigger Movie Plan
        # movie_plan()

        # Wait for a specified duration before checking again
        time.sleep(1)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** Import necessary modules from your `home` package.
# 2. **Global `home` variable:**  Define a global variable `home` to store the home plan structure created using `home_plan()`.
# 3. **Plan functions:**
#    - `morning_plan()`: Opens curtains in the Living Room and makes coffee in the Kitchen.
#    - `leave_home_plan()`: Locks the Living Room door and turns off smart sockets in the Living Room.
#    - `movie_plan()`: Dims lights, turns on TV to Netflix, and plays movie soundtrack in the Living Room.
# 4. **Auto-adjust functions:**
#    - `auto_adjust_temperature()`: Iterates through rooms, checks for temperature sensors and heaters/ACs. Adjusts heaters/ACs based on temperature readings.
#    - `auto_adjust_humidity()`: Iterates through rooms, checks for humidity sensors and humidifiers. Adjusts humidifiers based on humidity readings.
#    - `auto_adjust_light()`: Iterates through rooms, checks for light intensity sensors and lights. Adjusts lights based on light intensity readings.
# 5. **`main()` function:**
#    - Contains the main control loop.
#    - Calls `auto_adjust_temperature`, `auto_adjust_humidity`, and `auto_adjust_light` functions repeatedly.
#    - **(Optional):**  Add logic to trigger plans based on time or events (e.g., door lock status).
#    - **(Optional):** Implement more complex logic for interaction with actuators and sensors based on your specific smart home requirements.

# **Key points:**

# - The code provides a basic framework for implementing smart home functionality.
# - You can customize the plans and auto-adjust functions to match your specific home setup and desired actions.
# - Consider adding more sophisticated logic for decision-making, event handling, and interaction with other devices.

# **Remember:**

# - Replace the placeholder comments in the `main()` function with your specific logic for triggering plans and handling events.
# - Ensure that the `home.config.py` file contains the correct thresholds and durations for your smart home devices.
# - Modify the sensor and actuator code to match the specific capabilities of your actual devices.
