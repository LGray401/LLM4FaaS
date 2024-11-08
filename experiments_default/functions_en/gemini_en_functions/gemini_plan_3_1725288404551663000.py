from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION

from home.logger_config import logger

# functions.py

def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    kitchen = get_room(home, "Kitchen")

    # make coffee
    if kitchen is not None:
        coffee_machine = get_room_actuators(home, "Kitchen")[0]
        if coffee_machine is not None and coffee_machine.status == "off":
            coffee_machine.turn_on()
        if coffee_machine is not None:
            coffee_machine.make_coffee("Espresso")

    # turn on lights
    if living_room is not None:
        lights = get_room_actuators(home, "LivingRoom")
        for light in lights:
            if light is not None and light.status == "off":
                light.turn_on()
                light.set_brightness_level("medium")

    print("\n---Morning Plan Completed---")
    logger.info("---Morning Plan Completed---")


def leave_home_plan(home):
    # turn off all lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        if light.status == "on":
            light.turn_off()

    # lock all doors
    doors = get_all_actuators(home, "Door")
    for door in doors:
        door.lock()

    print("\n---Leave Home Plan Completed---")
    logger.info("---Leave Home Plan Completed---")


def movie_plan(home):
    living_room = get_room(home, "LivingRoom")

    # close the curtains
    curtains = get_room_actuators(home, "LivingRoom")
    for curtain in curtains:
        if curtain.actuator_type == "Curtain":
            curtain.turn_on()  # Assuming 'turn_on' closes the curtains in this context

    # turn on the TV and play a movie
    if living_room is not None:
        tv = get_room_actuators(home, "LivingRoom")[0]
        if tv is not None and tv.status == "off":
            tv.turn_on()
        if tv is not None:
            tv.play_channel("Netflix")

    print("\n---Movie Plan Completed---")
    logger.info("---Movie Plan Completed---")


def adjust_temperature(home):
    # Adjust the temperature in each room according to the sensors
    for room in home:
        # Get sensors and actuators for each room
        sensors = room.sensors
        heaters = get_room_actuators(room, "Heater")
        acs = get_room_actuators(room, "AC")

        for sensor in sensors:
            if sensor.sensor_type == "IndoorTemperature":
                # Get temperature reading
                temp_reading = sensor.get_reading()

                # Adjust temperature based on reading
                for heater in heaters:
                    heater.adjust_temperature(temp_reading)

                for ac in acs:
                    ac.adjust_temperature(temp_reading)


def adjust_humidity(home):
    # Adjust humidity in each room according to the sensors
    for room in home:
        # Get sensors and actuators for each room
        sensors = room.sensors
        humidifiers = get_room_actuators(room, "Humidifier")

        for sensor in sensors:
            if sensor.sensor_type == "Humidity":
                # Get humidity reading
                humidity_reading = sensor.get_reading()

                # Adjust humidity based on reading
                for humidifier in humidifiers:
                    if humidity_reading < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif humidity_reading > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()


def adjust_light_intensity(home):
    # Adjust light intensity in each room according to the sensors
    for room in home:
        # Get sensors and actuators for each room
        sensors = room.sensors
        lights = get_room_actuators(room, "Light")

        for sensor in sensors:
            if sensor.sensor_type == "LightIntensive":
                # Get light intensity reading
                light_intensity_reading = sensor.get_reading()

                # Adjust light intensity based on reading
                for light in lights:
                    if light_intensity_reading < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                        light.turn_off()


def daily_routine(home):
    # Run daily routines, like cleaning, for each room
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for robot in cleaning_robots:
        if robot.status == "off":
            robot.turn_on()
        robot.daily_routine()


def main():
    home = home_plan()

    # Example usage of functions
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)
    daily_routine(home)

    # Simulate sensor readings and adjust temperature, humidity, and light
    for _ in range(10):  # Run for 10 iterations
        adjust_temperature(home)
        adjust_humidity(home)
        adjust_light_intensity(home)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for some time


if __name__ == "__main__":
    main()

# **Explanation of Changes**

# 1. **Imports:**
#    - The `function.py` file now imports all necessary classes and functions from other files in your project:
#      - `home_plan` for managing the home layout and accessing rooms/devices
#      - `sensor` for accessing sensors and their readings
#      - `actuator` for controlling actuators
#      - `config` for settings and thresholds
#      - `logger_config` for logging

# 2. **Function Definitions:**
#    - **`morning_plan(home)`:**
#      - Gets the living room and kitchen.
#      - Turns on the coffee machine in the kitchen and makes coffee.
#      - Turns on lights in the living room and sets their brightness to "medium".
#    - **`leave_home_plan(home)`:**
#      - Turns off all lights.
#      - Locks all doors.
#    - **`movie_plan(home)`:**
#      - Closes the curtains in the living room.
#      - Turns on the TV and starts playing a movie on Netflix.
#    - **`adjust_temperature(home)`:**
#      - Iterates through each room in the home.
#      - Gets indoor temperature sensors and heaters/ACs for each room.
#      - Reads the temperature from the sensor and adjusts the heater or AC based on the target temperature set in the `actuator.py` file.
#    - **`adjust_humidity(home)`:**
#      - Iterates through each room in the home.
#      - Gets humidity sensors and humidifiers for each room.
#      - Reads the humidity from the sensor and adjusts the humidifier based on pre-defined thresholds.
#    - **`adjust_light_intensity(home)`:**
#      - Iterates through each room in the home.
#      - Gets light intensity sensors and lights for each room.
#      - Reads the light intensity from the sensor and adjusts the light brightness based on pre-defined thresholds.
#    - **`daily_routine(home)`:**
#      - Gets all cleaning robots in the home.
#      - Turns on each robot if it's off and starts the daily cleaning routine.

# 3. **`main()` Function:**
#    - Creates a home plan using `home_plan()`.
#    - Calls the plan functions (`morning_plan`, `leave_home_plan`, `movie_plan`, `daily_routine`) to simulate the scenarios.
#    - Includes a loop to simulate sensor readings and adjust temperature, humidity, and light intensity over time.

# **How to Use:**

# 1. **Save `function.py` in the `functions` folder of your project.**
# 2. **Ensure that the other files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`, `logger_config.py`) are correctly located in the `home` folder.**
# 3. **Run `function.py` to execute the code.**

# **Remember to:**

# - Adjust the `config.py` file to modify thresholds and other settings according to your project needs.
# - Implement additional functions in `function.py` to handle more smart home scenarios.
# - Connect your real-world sensors and actuators to the code to make your smart home functional.
