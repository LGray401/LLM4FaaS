from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Light, Curtain, MusicPlayer, CoffeeMachine
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

# Define functions for each plan

def morning_plan(home):
    """Executes the morning plan."""
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Open curtains
        curtains = get_room_actuators(home, "LivingRoom")
        for curtain in curtains:
            if curtain.actuator_type == "Curtain":
                curtain.turn_on()
        # Turn on lights
        lights = get_room_actuators(home, "LivingRoom")
        for light in lights:
            if light.actuator_type == "Light":
                light.turn_on()
                light.set_brightness_level("medium")

        # Play music
        music_player = get_room_actuators(home, "LivingRoom")
        for player in music_player:
            if player.actuator_type == "MusicPlayer":
                player.play_music("Soothing Music")

        # Make coffee
        kitchen = get_room(home, "Kitchen")
        if kitchen:
            coffee_machine = get_room_actuators(home, "Kitchen")
            for machine in coffee_machine:
                if machine.actuator_type == "CoffeeMachine":
                    machine.make_coffee("Espresso")
                    logger.info("Morning plan executed successfully.")
                    print("Morning plan executed successfully.")
    else:
        logger.error("Living Room not found in Home Plan.")
        print("Living Room not found in Home Plan.")

def leave_home_plan(home):
    """Executes the leave home plan."""
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Close the door
        door = get_room_actuators(home, "LivingRoom")
        for d in door:
            if d.actuator_type == "Door":
                d.lock()
        # Turn off lights
        lights = get_room_actuators(home, "LivingRoom")
        for light in lights:
            if light.actuator_type == "Light":
                light.turn_off()
        logger.info("Leave home plan executed successfully.")
        print("Leave home plan executed successfully.")
    else:
        logger.error("Living Room not found in Home Plan.")
        print("Living Room not found in Home Plan.")

def movie_plan(home):
    """Executes the movie plan."""
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Turn on TV
        tv = get_room_actuators(home, "LivingRoom")
        for t in tv:
            if t.actuator_type == "SmartTV":
                t.turn_on()
                t.play_channel("Netflix")
        # Close curtains
        curtains = get_room_actuators(home, "LivingRoom")
        for curtain in curtains:
            if curtain.actuator_type == "Curtain":
                curtain.turn_on()
        # Dim the lights
        lights = get_room_actuators(home, "LivingRoom")
        for light in lights:
            if light.actuator_type == "Light":
                light.turn_on()
                light.set_brightness_level("low")
        logger.info("Movie plan executed successfully.")
        print("Movie plan executed successfully.")
    else:
        logger.error("Living Room not found in Home Plan.")
        print("Living Room not found in Home Plan.")

def check_and_adjust_temperature(home):
    """Checks temperature sensors and adjusts heaters/ACs accordingly."""
    # Check temperature in each room
    for room in home:
        temp_sensors = get_room_sensors(home, room.name)
        for temp_sensor in temp_sensors:
            if temp_sensor.sensor_type == "IndoorTemperature":
                temperature_reading = temp_sensor.get_reading()
                if temperature_reading is not None:
                    # Adjust heater/AC based on temperature
                    actuators = get_room_actuators(home, room.name)
                    for actuator in actuators:
                        if actuator.actuator_type == "Heater":
                            actuator.adjust_temperature(temperature_reading)
                        elif actuator.actuator_type == "AC":
                            actuator.adjust_temperature(temperature_reading)

def check_and_adjust_humidity(home):
    """Checks humidity sensors and adjusts humidifiers accordingly."""
    # Check humidity in each room
    for room in home:
        humidity_sensors = get_room_sensors(home, room.name)
        for humidity_sensor in humidity_sensors:
            if humidity_sensor.sensor_type == "Humidity":
                humidity_reading = humidity_sensor.get_reading()
                if humidity_reading is not None:
                    # Adjust humidifier based on humidity
                    actuators = get_room_actuators(home, room.name)
                    for actuator in actuators:
                        if actuator.actuator_type == "Humidifier":
                            if humidity_reading < HUMIDITY_LOW:
                                actuator.increase_humidity()
                            elif humidity_reading > HUMIDITY_HIGH:
                                actuator.decrease_humidity()

def check_and_adjust_light(home):
    """Checks light intensity sensors and adjusts lights accordingly."""
    # Check light intensity in each room
    for room in home:
        light_sensors = get_room_sensors(home, room.name)
        for light_sensor in light_sensors:
            if light_sensor.sensor_type == "LightIntensive":
                light_intensity_reading = light_sensor.get_reading()
                if light_intensity_reading is not None:
                    # Adjust lights based on light intensity
                    actuators = get_room_actuators(home, room.name)
                    for actuator in actuators:
                        if actuator.actuator_type == "Light":
                            if light_intensity_reading < LIGHT_INTENSITY_LOW:
                                actuator.turn_on()
                            elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                                actuator.turn_off()

def main():
    """Main function to manage smart home functions."""
    home = home_plan()

    # Example usage of plans
    # morning_plan(home)
    # leave_home_plan(home)
    # movie_plan(home)

    while True:
        # Check and adjust temperature
        check_and_adjust_temperature(home)
        # Check and adjust humidity
        check_and_adjust_humidity(home)
        # Check and adjust light intensity
        check_and_adjust_light(home)

        # Add other logic or functions as needed
        # ...

        # Example to get all sensors of a specific type
        # all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        # print(all_temperature_sensors)

        # Example to get all actuators of a specific type
        # all_lights = get_all_actuators(home, "Light")
        # print(all_lights)

        # Example to manually control a specific actuator
        # living_room = get_room(home, "LivingRoom")
        # if living_room:
        #     lights = get_room_actuators(home, "LivingRoom")
        #     for light in lights:
        #         if light.actuator_type == "Light":
        #             light.turn_on()
        #             light.set_brightness_level("high")

        # Wait for a while before checking again
        # time.sleep(1)

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** The code imports necessary modules from the `home` package, including `home_plan` for accessing home information, `sensor` for sensor types, `actuator` for actuator types, and `config` for configuration values.

# 2. **Plan Functions:**
#    - `morning_plan()`:  Opens curtains, turns on lights (medium brightness), plays soothing music, and makes espresso in the kitchen.
#    - `leave_home_plan()`: Closes the door and turns off the lights in the living room.
#    - `movie_plan()`: Turns on the TV, closes curtains, and dims the lights in the living room.

# 3. **Utility Functions:**
#    - `check_and_adjust_temperature()`: Iterates through rooms, checks indoor temperature sensors, and adjusts heaters/ACs based on temperature thresholds.
#    - `check_and_adjust_humidity()`: Iterates through rooms, checks humidity sensors, and adjusts humidifiers based on humidity thresholds.
#    - `check_and_adjust_light()`: Iterates through rooms, checks light intensity sensors, and adjusts lights based on light intensity thresholds.

# 4. **`main()` Function:**
#    - Creates a `home` object using `home_plan()`.
#    - Contains a loop that runs indefinitely:
#      - Calls the utility functions to check and adjust temperature, humidity, and light.
#      - You can add more logic or functions inside the loop.
#      - Includes examples of how to:
#        - Get all sensors of a specific type
#        - Get all actuators of a specific type
#        - Manually control a specific actuator

# 5. **Example Usage:**
#    - You can uncomment the lines in `main()` to execute the example plans.
#    - You can add your own logic and functions to `main()` to implement more complex smart home features.

# **To use this code:**

# 1. Make sure you have the `home` package (containing the files you provided) in your project.
# 2. Save this code as `function.py` in a `functions` folder within your project.
# 3. Run `function.py` to start the smart home system.

# **Improvements:**

# - Add error handling to functions to gracefully handle situations where components are not found.
# - Implement more complex plans and functionalities.
# - Integrate with real-world sensors and actuators using libraries like `RPi.GPIO` or other hardware-specific libraries.
# - Explore using a database or message queue to store and share home data.
# - Consider using a web server or other interface to remotely control your smart home. 
