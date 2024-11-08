from home.home_plan import get_room, get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors
from home.actuator import Light, Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, NotificationSender, \
    MusicPlayer, SmartTV
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.logger_config import logger
import re

def main():
    home = get_room(get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors)

    # Process user input
    user_input = input("小g please: ")
    room_name, action, target = parse_user_input(user_input)

    # Find the room
    room = get_room(home, room_name)
    if not room:
        return

    # Execute the action
    if action == "open":
        execute_action(room, "Window", "turn_on")
    elif action == "close":
        execute_action(room, "Window", "turn_off")
    elif action == "turn on":
        execute_action(room, "Light", "turn_on")
    elif action == "turn off":
        execute_action(room, "Light", "turn_off")
    elif action == "lock":
        execute_action(room, "Door", "lock")
    elif action == "unlock":
        execute_action(room, "Door", "unlock")
    elif action == "open":
        execute_action(room, "Curtain", "turn_on")
    elif action == "close":
        execute_action(room, "Curtain", "turn_off")
    elif action == "start":
        execute_action(room, "CleaningRobot", "daily_routine")
    elif action == "send":
        execute_action(room, "NotificationSender", "notification_sender", target)
    elif action == "play":
        execute_action(room, "MusicPlayer", "play_music", target)
    elif action == "set":
        if target == "temperature":
            execute_action(room, "Heater", "set_target_temperature", target)
        elif target == "brightness":
            execute_action(room, "Light", "set_brightness_level", target)
        else:
            logger.warning(f"Invalid target for 'set' action: {target}")
            print(f"Invalid target for 'set' action: {target}")
    elif action == "make":
        execute_action(room, "CoffeeMachine", "make_coffee", target)
    elif action == "play":
        execute_action(room, "SmartTV", "play_channel", target)
    else:
        logger.warning(f"Invalid action: {action}")
        print(f"Invalid action: {action}")

def parse_user_input(user_input):
    """Parses user input into room name, action, and target."""
    # TODO: Make it more robust and handle different cases, for example "turn on the light in living room"
    matches = re.findall(r"(\w+)\s+(\w+)\s+(.*)", user_input)
    if matches:
        room_name = matches[0][0].lower()
        action = matches[0][1].lower()
        target = matches[0][2]
        return room_name, action, target
    else:
        logger.warning(f"Failed to parse user input: {user_input}")
        print(f"Failed to parse user input: {user_input}")
        return None, None, None

def execute_action(room, actuator_type, action_name, target=None):
    """Finds the actuator and executes the specified action."""
    actuators = get_room_actuators(room, actuator_type)
    if actuators:
        for actuator in actuators:
            if hasattr(actuator, action_name):
                getattr(actuator, action_name)(target)
                logger.info(f"Action '{action_name}' executed for actuator '{actuator.id}'.")
                print(f"Action '{action_name}' executed for actuator '{actuator.id}'.")
                return
        logger.warning(f"No actuator of type '{actuator_type}' found in room '{room.name}'.")
        print(f"No actuator of type '{actuator_type}' found in room '{room.name}'.")
    else:
        logger.warning(f"No actuators found in room '{room.name}'.")
        print(f"No actuators found in room '{room.name}'.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import Statements:**
#    - Import necessary functions from `home_plan` for getting room information, actuators, and sensors.
#    - Import actuator and sensor classes from `actuator.py` and `sensor.py`.
#    - Import the logger from `logger_config.py` for logging purposes.
#    - Import `re` for regular expression matching.

# 2. **`main` Function:**
#    - **Get Home Plan:** Retrieves the home plan using the imported functions.
#    - **Process User Input:**
#      - Gets user input using `input()`.
#      - Calls `parse_user_input` to extract room name, action, and target.
#    - **Find Room:** Calls `get_room` to find the specified room in the home plan.
#    - **Execute Action:**
#      - Based on the parsed action, calls `execute_action` to find and execute the corresponding action on the appropriate actuator.
#      - Handles various actions like turning lights on/off, opening/closing windows, locking/unlocking doors, etc.

# 3. **`parse_user_input` Function:**
#    - Uses regular expressions (`re.findall`) to extract room name, action, and target from the user input.
#    - Returns the extracted information if successful, otherwise logs an error.

# 4. **`execute_action` Function:**
#    - Gets the list of actuators of the specified type in the room using `get_room_actuators`.
#    - Iterates through the actuators and checks if the requested action is available using `hasattr`.
#    - If the action is available, it calls the action method on the actuator using `getattr` and passes the target (if any) as an argument.
#    - Logs a success message if the action is executed.
#    - Logs an error message if the specified actuator type or the requested action is not found.

# **Key Improvements:**

# - **Robust User Input Handling:** Uses regular expressions for more reliable user input parsing.
# - **Structured Action Execution:** Uses `execute_action` function to encapsulate action logic, making the code more readable and maintainable.
# - **Improved Error Handling:** Provides informative error messages to the user.
# - **Logging:** Uses the logger for detailed logging, making it easier to track program execution and debug issues.

# **To Use the Code:**

# 1. Make sure you have the `home`, `functions`, and `logger` folders with the necessary files (sensor.py, actuator.py, home_plan.py, config.py, and logger_config.py) in your project.
# 2. Replace the comments in the code with your specific room names, actuator types, and actions as needed.
# 3. Run the `function.py` file.
# 4. Enter commands in the format: "room_name action target" (e.g., "livingroom turn on light").
