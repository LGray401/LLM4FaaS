import time
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Heater, AC, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger


def main():
    """
    Main function to implement the smart home logic.
    """

    # Initialize home plan
    home = home_plan()

    # Define working days
    working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

    # Simulation loop
    while True:
        # Get current day of the week
        current_day = time.strftime("%A")

        # Check for light intensity change
        light_sensors = get_all_sensors(home, "LightIntensive")
        for light_sensor in light_sensors:
            light_reading = light_sensor.get_reading()
            if light_reading is not None and light_reading > LIGHT_INTENSITY_HIGH:
                # Light intensity is high, turn off lights
                lights = get_all_actuators(home, "Light")
                for light in lights:
                    light.turn_off()
                logger.info(f"Light intensity is high. Turning off lights in {light_sensor.room_name}.")

        # Check for temperature changes
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        for temperature_sensor in temperature_sensors:
            temperature_reading = temperature_sensor.get_reading()
            if temperature_reading is not None:
                # Check for low temperature
                if temperature_reading < TEMP_LOW:
                    # Turn on heater
                    heater = get_room_actuators(home, temperature_sensor.room_name)[0]
                    heater.turn_on()
                    logger.info(f"Temperature is below {TEMP_LOW}°C. Turning on heater in {temperature_sensor.room_name}.")

                # Check for high temperature
                elif temperature_reading > TEMP_HIGH:
                    # Turn on AC
                    ac = get_room_actuators(home, temperature_sensor.room_name)[0]
                    ac.turn_on()
                    logger.info(f"Temperature is above {TEMP_HIGH}°C. Turning on AC in {temperature_sensor.room_name}.")

        # Check for humidity changes
        humidity_sensors = get_all_sensors(home, "Humidity")
        for humidity_sensor in humidity_sensors:
            humidity_reading = humidity_sensor.get_reading()
            if humidity_reading is not None:
                # Check for low humidity
                if humidity_reading < HUMIDITY_LOW:
                    # Turn on humidifier
                    humidifier = get_room_actuators(home, humidity_sensor.room_name)[0]
                    humidifier.increase_humidity()
                    logger.info(f"Humidity is below {HUMIDITY_LOW}%. Increasing humidity in {humidity_sensor.room_name}.")

        # Check for working days and cleaning robot routine
        if current_day in working_days:
            # Start cleaning robot daily routine
            cleaning_robots = get_all_actuators(home, "CleaningRobot")
            for cleaning_robot in cleaning_robots:
                cleaning_robot.turn_on()
                cleaning_robot.daily_routine()

        # Wait for a specified duration
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:** Import relevant classes and functions from `home_plan.py`, `sensor.py`, `actuator.py`, and `config.py`.
# 2. **Define working days:** Create a list of working days to trigger the cleaning robot routine.
# 3. **Simulation loop:** Create an infinite loop to continuously monitor sensors and control actuators.
# 4. **Light intensity check:**
#    - Retrieve all light intensity sensors.
#    - Get the reading from each sensor.
#    - If the reading exceeds `LIGHT_INTENSITY_HIGH`, turn off all lights in the room.
# 5. **Temperature check:**
#    - Retrieve all indoor temperature sensors.
#    - Get the reading from each sensor.
#    - If the temperature is below `TEMP_LOW`, turn on the heater.
#    - If the temperature is above `TEMP_HIGH`, turn on the AC.
# 6. **Humidity check:**
#    - Retrieve all humidity sensors.
#    - Get the reading from each sensor.
#    - If the humidity is below `HUMIDITY_LOW`, increase the humidity using the humidifier.
# 7. **Cleaning robot routine:**
#    - Check if the current day is a working day.
#    - If it is, turn on the cleaning robot and execute its daily routine.
# 8. **Wait duration:**
#    - Use `time.sleep()` to pause the execution for `TEMP_CHANGE_DURATION_WINDOW` seconds before the next loop iteration.

# **Key points:**

# - The code uses the `home_plan` object to access rooms, sensors, and actuators.
# - It iterates through sensors and actuators to check conditions and perform actions.
# - The logic is implemented using simple if-else statements and function calls.
# - The code logs events using the `logger` module.

# **To run the code:**

# 1. Make sure all the required files (sensor.py, actuator.py, home_plan.py, config.py, and function.py) are in the correct directory.
# 2. Execute the `function.py` file.

# The code will simulate the smart home logic and print log messages based on sensor readings and actuator actions.
