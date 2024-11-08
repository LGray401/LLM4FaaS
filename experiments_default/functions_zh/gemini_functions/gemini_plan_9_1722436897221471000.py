from home.home_plan import home_plan, get_room, get_room_actuators, get_all_actuators
from home.actuator import Door, CoffeeMachine, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def morning_plan(home):
    # Turn on coffee machine in kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        coffee_machine = get_room_actuators(home, "Kitchen")[0]  # Assuming only one coffee machine in the kitchen
        if coffee_machine and isinstance(coffee_machine, CoffeeMachine):
            print("Turning on coffee machine in the kitchen.")
            logger.info("Turning on coffee machine in the kitchen.")
            coffee_machine.turn_on()
            # You can add more actions here like specifying coffee type, etc.


def leave_home_plan(home):
    # Lock the door in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        door = get_room_actuators(home, "LivingRoom")[0]  # Assuming only one door in the living room
        if door and isinstance(door, Door):
            print("Locking the door in the living room.")
            logger.info("Locking the door in the living room.")
            door.lock()


def movie_plan(home):
    # Turn on TV in the living room and play a channel
    living_room = get_room(home, "LivingRoom")
    if living_room:
        tv = get_room_actuators(home, "LivingRoom")[0]  # Assuming only one TV in the living room
        if tv and isinstance(tv, SmartTV):
            print("Turning on TV in the living room and playing a channel.")
            logger.info("Turning on TV in the living room and playing a channel.")
            tv.turn_on()
            # You can add more actions here like specifying a specific channel or movie


def main():
    home = home_plan()

    # Example usage of plans
    # morning_plan(home)
    # leave_home_plan(home)
    movie_plan(home)

    # You can add more functions and plans as needed
    # ...


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - Import `home_plan` for working with the home layout.
#    - Import `Door`, `CoffeeMachine`, `SmartTV` from `actuator` to access those specific actuators.
#    - Import `TEMP_LOW`, `TEMP_HIGH`, etc. from `config` for any temperature or other thresholds used in your plans.
#    - Import `logger` for logging actions.

# 2. **Define Plan Functions:**
#    - **`morning_plan(home)`:**
#      - Gets the "Kitchen" room using `get_room`.
#      - Retrieves the first actuator from the kitchen (assuming it's the coffee machine) using `get_room_actuators`.
#      - Checks if the actuator is indeed a `CoffeeMachine`.
#      - Turns on the coffee machine.
#    - **`leave_home_plan(home)`:**
#      - Gets the "LivingRoom" room.
#      - Retrieves the first actuator from the living room (assuming it's the door).
#      - Checks if the actuator is a `Door`.
#      - Locks the door.
#    - **`movie_plan(home)`:**
#      - Gets the "LivingRoom" room.
#      - Retrieves the first actuator (TV).
#      - Checks if the actuator is a `SmartTV`.
#      - Turns on the TV.

# 3. **`main()` Function:**
#    - Creates the home plan using `home_plan()`.
#    - Calls the plan functions to demonstrate their usage.
#    - You can add more plan functions and actions as needed.

# 4. **Running the script:**
#    - When you run `function.py`, it will execute the `main()` function, which will in turn call your defined plan functions and perform the actions specified within them.

# **Important Notes:**

# - **Error Handling:**
#    - This code assumes the existence of specific actuators in each room. You should add error handling to gracefully handle cases where rooms or actuators might be missing.
# - **Assumptions:**
#    - The code assumes that there's only one coffee machine in the kitchen, one door in the living room, and one TV in the living room. You might need to modify this based on your home layout.
# - **Real-World Implementation:**
#    - This is a basic example. In a real-world smart home, you would need to connect these functions to your actual hardware (sensors and actuators) using communication protocols like MQTT, HTTP, etc.

# Remember to customize this code according to your specific smart home setup and desired functionalities.
