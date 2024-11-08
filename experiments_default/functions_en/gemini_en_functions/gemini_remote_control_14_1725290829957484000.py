from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import Light
from home.logger_config import logger

def main():
    home = home_plan()

    # Parse the user's request
    request = "Xiaog, turn on the lights in the living room"
    words = request.split()

    # Extract relevant information
    room_name = words[-2]
    action = " ".join(words[-3:])  # "turn on the lights"

    # Find the specified room
    room = get_room(home, room_name)

    if room:
        # Get the actuators in the room
        actuators = get_room_actuators(home, room_name)
        # Find the light actuators
        lights = [actuator for actuator in actuators if isinstance(actuator, Light)]

        # Perform the requested action
        if lights:
            for light in lights:
                light.turn_on()
            logger.info(f"Turned on the lights in {room_name}")
        else:
            logger.warning(f"No lights found in {room_name}")
    else:
        logger.error(f"Room '{room_name}' not found.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions to create the home plan and retrieve rooms and actuators.
#    - `home.actuator`: Contains the `Light` class representing a light actuator.
#    - `home.logger_config`: Provides the `logger` object for logging information and errors.

# 2. **Define the `main` function:**
#    - This function handles the main logic of the application.

# 3. **Parse the user's request:**
#    - The code splits the user's request into words and extracts the room name (using the last word before "in") and the action (using the last three words).

# 4. **Find the specified room:**
#    - It calls `get_room` from `home.home_plan` to retrieve the room object based on the extracted room name.

# 5. **Get the actuators in the room:**
#    - If the room is found, it calls `get_room_actuators` to obtain a list of all actuators in that room.

# 6. **Find the light actuators:**
#    - The code filters the actuators to find those that are instances of the `Light` class, representing light actuators.

# 7. **Perform the requested action:**
#    - If lights are found:
#      - It iterates through the `lights` list and calls `turn_on()` for each light to switch them on.
#      - It logs the successful action.
#    - If no lights are found:
#      - It logs a warning message.
#    - If the room is not found:
#      - It logs an error message.

# 8. **Run the `main` function if the script is executed directly:**
#    - `if __name__ == "__main__":` ensures the `main` function is executed only when the script is run directly, not when imported as a module.

# **To use this code:**

# 1. Make sure you have the `home` folder with the required files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) in the same directory as `function.py`.
# 2. Execute `function.py` from your terminal or Python environment.
# 3. The script will parse the provided request and attempt to turn on the lights in the specified room.
# 4. The `logger` will print output to the console, including information, warnings, and errors.

# **Note:** This is a basic implementation. You can extend this code to handle various other requests, such as turning off lights, adjusting brightness, controlling other actuators, and using more complex logic to respond to user commands.
