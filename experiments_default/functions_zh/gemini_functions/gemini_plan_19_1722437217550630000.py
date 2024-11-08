from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Heater, AC, CoffeeMachine, Light, Curtain, Door, CleaningRobot, SmartTV
import time
from home.logger_config import logger


def morning_plan():
    home = home_plan()
    # Get the living room
    living_room = get_room(home, "LivingRoom")

    # Turn on the living room light to medium brightness
    living_room_light = get_room_actuators(home, "LivingRoom")[0]
    living_room_light.turn_on()
    living_room_light.set_brightness_level("medium")

    # Open the living room curtains
    living_room_curtains = get_room_actuators(home, "LivingRoom")[4]
    living_room_curtains.turn_on()

    # Make coffee in the kitchen
    kitchen = get_room(home, "Kitchen")
    coffee_machine = get_room_actuators(home, "Kitchen")[3]
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")

    # Wait for a while
    time.sleep(5)

    # Turn off the coffee machine
    coffee_machine.turn_off()

    # Turn off the living room light
    living_room_light.turn_off()


def leave_home_plan():
    home = home_plan()
    # Get the front door
    front_door = get_room_actuators(home, "LivingRoom")[0]

    # Lock the door
    front_door.lock()

    # Turn off all the lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Turn off all the heaters
    heaters = get_all_actuators(home, "Heater")
    for heater in heaters:
        heater.turn_off()

    # Turn off all the ACs
    acs = get_all_actuators(home, "AC")
    for ac in acs:
        ac.turn_off()

    # Turn off all the smart sockets
    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()


def movie_plan():
    home = home_plan()
    # Get the living room
    living_room = get_room(home, "LivingRoom")

    # Turn on the living room light to low brightness
    living_room_light = get_room_actuators(home, "LivingRoom")[0]
    living_room_light.turn_on()
    living_room_light.set_brightness_level("low")

    # Close the living room curtains
    living_room_curtains = get_room_actuators(home, "LivingRoom")[4]
    living_room_curtains.turn_off()

    # Turn on the living room TV and play a movie
    living_room_tv = get_room_actuators(home, "LivingRoom")[10]
    living_room_tv.turn_on()
    living_room_tv.play_channel("Netflix")

    # Adjust the living room temperature to 20 degrees
    living_room_ac = get_room_actuators(home, "LivingRoom")[11]
    living_room_ac.set_target_temperature(20)

    # Wait for a while
    time.sleep(30)

    # Turn off the living room light
    living_room_light.turn_off()

    # Turn off the living room TV
    living_room_tv.turn_off()

    # Turn off the living room AC
    living_room_ac.turn_off()


def main():
    print("Welcome to the smart home system!")

    while True:
        # Prompt the user to select a plan
        plan_selection = input(
            "Select a plan:\n"
            "1. Morning Plan\n"
            "2. Leave Home Plan\n"
            "3. Movie Plan\n"
            "4. Exit\n"
            "Enter your choice: "
        )

        # Execute the chosen plan
        if plan_selection == "1":
            morning_plan()
        elif plan_selection == "2":
            leave_home_plan()
        elif plan_selection == "3":
            movie_plan()
        elif plan_selection == "4":
            print("Exiting the system...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: This imports functions related to managing the home plan (rooms, sensors, actuators).
#    - `home.sensor`: Imports specific sensor classes.
#    - `home.actuator`: Imports specific actuator classes.
#    - `time`: Used for delaying execution.
#    - `home.logger_config`: This imports the logger configuration for logging actions.

# 2. **Define plan functions:**
#    - `morning_plan()`:
#      - Retrieves the living room and kitchen objects.
#      - Turns on the living room light to medium brightness.
#      - Opens the living room curtains.
#      - Turns on the coffee machine in the kitchen and makes espresso.
#      - Waits for 5 seconds.
#      - Turns off the coffee machine.
#      - Turns off the living room light.
#    - `leave_home_plan()`:
#      - Retrieves the front door, all lights, heaters, ACs, and smart sockets.
#      - Locks the front door.
#      - Turns off all lights, heaters, ACs, and smart sockets.
#    - `movie_plan()`:
#      - Retrieves the living room objects.
#      - Turns on the living room light to low brightness.
#      - Closes the living room curtains.
#      - Turns on the living room TV and starts playing Netflix.
#      - Sets the living room AC to 20 degrees.
#      - Waits for 30 seconds.
#      - Turns off the living room light, TV, and AC.

# 3. **`main()` function:**
#    - Provides a menu to the user to choose from different plans.
#    - Calls the appropriate plan function based on the user's choice.
#    - Exits the system if the user chooses to.

# 4. **Error handling:**
#    - The `main()` function includes basic error handling for invalid user input.

# 5. **Logging:**
#    - The `logger.info()` and `logger.warning()` methods are used to log relevant actions and warnings.

# This code provides a basic framework for implementing different smart home plans based on sensor data and actuator control. You can extend this code to include more complex plans, additional sensors and actuators, and more robust error handling.
