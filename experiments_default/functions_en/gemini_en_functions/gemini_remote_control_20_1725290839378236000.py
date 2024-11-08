from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_actuators, \
    get_all_sensors
from home.sensor import IndoorTemperatureSensor, HumiditySensor
from home.actuator import AC, CleaningRobot
from home.config import TEMP_HIGH, TEMP_LOW, DAILY_ROUTINE_DURATION
import time
from home.logger_config import logger

def main():
    # Load the home plan
    home = home_plan()

    # Get the living room
    living_room = get_room(home, "LivingRoom")

    # Get the air conditioner and cleaning robot in the living room
    ac = get_room_actuators(home, "LivingRoom")[10]
    cleaning_robot = get_room_actuators(home, "LivingRoom")[9]

    # Get the temperature sensor in the living room
    temp_sensor = get_room_sensors(home, "LivingRoom")[1]

    # Turn on the cleaning robot when no one is home
    cleaning_robot.turn_on()
    cleaning_robot.daily_routine()

    # Turn on the air conditioner 10 minutes before going home
    time.sleep(600)  # Simulate 10 minutes
    ac.turn_on()

    # Set the target temperature of the air conditioner
    ac.set_target_temperature(TEMP_HIGH)

    # Continuously monitor the temperature and adjust the air conditioner accordingly
    while True:
        # Get the current temperature
        current_temperature = temp_sensor.get_reading()

        # Adjust the air conditioner based on the target temperature
        ac.adjust_temperature(current_temperature)

        # Wait for a short time before checking the temperature again
        time.sleep(1)

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import Necessary Modules:**
#    - Import `home_plan` functions to access the home plan, rooms, sensors, and actuators.
#    - Import `IndoorTemperatureSensor` and `HumiditySensor` from `home.sensor`.
#    - Import `AC` and `CleaningRobot` from `home.actuator`.
#    - Import `TEMP_HIGH`, `TEMP_LOW`, and `DAILY_ROUTINE_DURATION` from `home.config`.
#    - Import `time` for simulating time delays.
#    - Import `logger` from `home.logger_config` for logging.

# 2. **Define `main()` Function:**
#    - This function contains the main logic for the smart home system.

# 3. **Load the Home Plan:**
#    - `home = home_plan()` loads the home plan from `home.home_plan`.

# 4. **Get Living Room and Devices:**
#    - `living_room = get_room(home, "LivingRoom")` retrieves the living room from the home plan.
#    - `ac = get_room_actuators(home, "LivingRoom")[10]` gets the air conditioner from the living room's actuators.
#    - `cleaning_robot = get_room_actuators(home, "LivingRoom")[9]` gets the cleaning robot.
#    - `temp_sensor = get_room_sensors(home, "LivingRoom")[1]` gets the temperature sensor.

# 5. **Cleaning Robot Logic:**
#    - `cleaning_robot.turn_on()` turns on the cleaning robot.
#    - `cleaning_robot.daily_routine()` starts the cleaning robot's routine.

# 6. **Air Conditioner Logic:**
#    - **Simulate Delay:** `time.sleep(600)` simulates a 10-minute delay before turning on the AC (adjust as needed).
#    - `ac.turn_on()` turns on the air conditioner.
#    - `ac.set_target_temperature(TEMP_HIGH)` sets the target temperature.

# 7. **Temperature Monitoring Loop:**
#    - `while True:` creates an infinite loop to continuously monitor the temperature.
#    - `current_temperature = temp_sensor.get_reading()` reads the current temperature.
#    - `ac.adjust_temperature(current_temperature)` adjusts the AC based on the target temperature.
#    - `time.sleep(1)` waits for 1 second before checking the temperature again.

# **How to Use:**

# 1.  **Save the Code:** Save the code as `function.py` in the `functions` folder.
# 2.  **Run the Code:** Execute the `function.py` file. This will start the smart home system, simulating the actions described in the functional description.

# **Key Points:**

# - The code assumes that you have the `home` folder with the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files in the same directory as `function.py`.
# - Adjust the time delays and thresholds in the `config.py` file as needed for your project.
# - You can add more sensors, actuators, and logic to this code to further customize your smart home system.
