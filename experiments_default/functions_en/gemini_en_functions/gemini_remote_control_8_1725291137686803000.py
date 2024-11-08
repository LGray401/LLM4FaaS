from home.home_plan import home_plan, get_room, get_room_actuators
from home.actuator import AC, Light
from home.logger_config import logger

def main():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        living_room_actuators = get_room_actuators(home, "LivingRoom")
        # Find the AC and turn it on
        ac = next((actor for actor in living_room_actuators if isinstance(actor, AC)), None)
        if ac is not None:
            ac.turn_on()
            ac.set_target_temperature(17)
            logger.info("AC turned on and set to 17 degrees.")
            print("AC turned on and set to 17 degrees.")
        else:
            logger.warning("No AC found in the Living Room.")
            print("No AC found in the Living Room.")

        # Find the light and turn it on
        light = next((actor for actor in living_room_actuators if isinstance(actor, Light)), None)
        if light is not None:
            light.turn_on()
            logger.info("Living room light turned on.")
            print("Living room light turned on.")
        else:
            logger.warning("No light found in the Living Room.")
            print("No light found in the Living Room.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`:  Import functions to get the home plan, find specific rooms, and get actuators in a room.
#    - `home.actuator`: Import `AC` and `Light` classes to work with air conditioning and lights.
#    - `home.logger_config`: Import the logger for logging events.

# 2. **`main()` function:**
#    - **Get the home plan:** Call `home_plan()` to create the home structure.
#    - **Find the Living Room:** Use `get_room()` to locate the "LivingRoom" in the home plan.
#    - **Get Living Room actuators:** If the "LivingRoom" is found, get its actuators using `get_room_actuators()`.
#    - **Find AC and turn it on:** Use a generator expression to find the AC actuator in the room. If found, turn it on and set the target temperature to 17 degrees. Log and print the actions.
#    - **Find the light and turn it on:** Similar to the AC logic, find the light, turn it on, and log/print.

# 3. **`if __name__ == "__main__":`:**
#    - This ensures that the `main()` function runs only when the script is executed directly (not imported as a module).

# **How to use:**

# 1. **Place `function.py`:** Make sure this file is located in the `functions` folder of your project.
# 2. **Run the script:** Execute `function.py` from your terminal. This will turn on the AC and the light in the Living Room.

# **Important notes:**

# - **Error handling:** The code checks if the Living Room, AC, and light are found. If not, it logs warnings and prints messages to the console.
# - **Logger:** The code uses the `logger` to log events, which can be helpful for debugging and tracking actions in your smart home system.
# - **Extensibility:** This code can be easily extended to control other actuators or sensors by adding more classes and logic.
# - **Integration:** Make sure to integrate this file with your other smart home system components for a cohesive solution.
