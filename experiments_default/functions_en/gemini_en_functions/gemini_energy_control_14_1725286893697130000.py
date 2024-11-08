from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION
from home.logger_config import logger

def main():
    """
    Main function for smart home system.
    """
    home = home_plan()

    # Example scenarios
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Get sensors and actuators
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        living_room_actuators = get_room_actuators(home, "LivingRoom")

        # Check sensors
        indoor_temp_sensor = get_all_sensors(home, "IndoorTemperature")[0]
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_on()
            current_temp = indoor_temp_sensor.get_reading()
            print(f"Current temperature in Living Room is: {current_temp}°C")
            if current_temp < TEMP_LOW:
                print(f"Temperature is too low, turn on heater.")
                heater = get_all_actuators(home, "Heater")[0]
                if heater:
                    heater.turn_on()
                    heater.set_target_temperature(TEMP_HIGH)
            elif current_temp > TEMP_HIGH:
                print(f"Temperature is too high, turn on AC.")
                ac = get_all_actuators(home, "AC")[0]
                if ac:
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_LOW)

        # Control actuators
        light = get_all_actuators(home, "Light")[0]
        if light:
            light.turn_on()
            light.set_brightness_level("medium")
        # ... other actuator control logic

    # ... other scenarios

    # Example daily routine
    cleaning_robot = get_all_actuators(home, "CleaningRobot")[0]
    if cleaning_robot:
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    # ... other routines

if __name__ == "__main__":
    main()


# **Explanation:**

# 1. **Import necessary modules:**
#    - Import relevant functions and classes from `home.home_plan`, `home.sensor`, `home.actuator`, `home.config`, and `home.logger_config`.

# 2. **`main()` function:**
#    - This function contains the logic for your smart home system.
#    - **Get home plan:** `home = home_plan()` creates the home structure with rooms and components.
#    - **Example scenarios:** This section demonstrates how to interact with the home plan.
#      - **Get a room:** `living_room = get_room(home, "LivingRoom")` retrieves the Living Room object.
#      - **Get sensors and actuators:**  Retrieve lists of sensors and actuators from the Living Room using `get_room_sensors` and `get_room_actuators`.
#      - **Check sensors:** 
#        - Get the Indoor Temperature sensor (`indoor_temp_sensor`).
#        - Turn it on, get its reading, and use the reading to trigger actions (turning on the heater or AC based on temperature thresholds).
#      - **Control actuators:** 
#        - Get the Light actuator (`light`).
#        - Turn it on and set its brightness.
#        - **... other actuator control logic** (Add your own logic here for controlling other actuators like curtains, music player, etc.).

#    - **Example daily routine:** 
#      - Get the Cleaning Robot (`cleaning_robot`).
#      - Turn it on and trigger its daily routine (`daily_routine()`).
#      - **... other routines** (Add other routines as needed).

# 3. **`if __name__ == "__main__":` block:**
#    - This block ensures that the `main()` function is executed only when the script is run directly (not when it's imported as a module). 

# **To use this `function.py` file:**

# 1. **Place it in the `functions` folder.**
# 2. **Make sure the other files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) are in the `home` folder.**
# 3. **Run `function.py` from the command line.** 

# This will execute the `main()` function and run your smart home scenarios. You can add more scenarios and routines in the `main()` function to customize your smart home logic. 
