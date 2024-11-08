from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, NotificationSender, MusicPlayer, \
    Light, SmartTV, SmartSocket, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time
from home.logger_config import logger

home = home_plan()


def main():
    # Example usage of functions
    # Adjust temperature in LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_temperature_sensor = get_room_sensors(home, "LivingRoom")[0]
        living_room_heater = get_room_actuators(home, "LivingRoom")[0]
        living_room_ac = get_room_actuators(home, "LivingRoom")[1]

        # Turn on heater/AC based on temperature
        if living_room_temperature_sensor.get_reading() < TEMP_LOW:
            living_room_heater.turn_on()
        elif living_room_temperature_sensor.get_reading() > TEMP_HIGH:
            living_room_ac.turn_on()
        else:
            living_room_heater.turn_off()
            living_room_ac.turn_off()

    # Turn on the light in Bedroom if light intensity is low
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        bedroom_light_sensor = get_room_sensors(home, "Bedroom")[0]
        bedroom_light = get_room_actuators(home, "Bedroom")[0]

        if bedroom_light_sensor.get_reading() < LIGHT_INTENSITY_LOW:
            bedroom_light.turn_on()
        else:
            bedroom_light.turn_off()

    # Turn on CoffeeMachine in Kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        kitchen_coffee_machine = get_room_actuators(home, "Kitchen")[0]
        kitchen_coffee_machine.turn_on()
        kitchen_coffee_machine.make_coffee("Cappuccino")

    # Turn on CleaningRobot in LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_cleaning_robot = get_room_actuators(home, "LivingRoom")[9]
        living_room_cleaning_robot.turn_on()
        living_room_cleaning_robot.daily_routine()

    # Example to adjust humidity in Bathroom
    bathroom = get_room(home, "Bathroom")
    if bathroom:
        bathroom_humidity_sensor = get_room_sensors(home, "Bathroom")[0]
        bathroom_humidifier = get_room_actuators(home, "Bathroom")[4]

        # Turn on humidifier if humidity is below the threshold
        if bathroom_humidity_sensor.get_reading() < HUMIDITY_LOW:
            bathroom_humidifier.increase_humidity()
        elif bathroom_humidity_sensor.get_reading() > HUMIDITY_HIGH:
            bathroom_humidifier.decrease_humidity()
        else:
            # Keep humidity at desired level
            pass

    # Example to control the temperature based on external temperature
    balcony = get_room(home, "Balcony")
    if balcony:
        balcony_temperature_sensor = get_room_sensors(home, "Balcony")[0]
        living_room = get_room(home, "LivingRoom")
        living_room_heater = get_room_actuators(home, "LivingRoom")[0]
        living_room_ac = get_room_actuators(home, "LivingRoom")[1]

        # Turn on heater/AC in LivingRoom based on external temperature
        if balcony_temperature_sensor.get_reading() < TEMP_LOW:
            living_room_heater.turn_on()
            # Wait for a short time to allow temperature change
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
        elif balcony_temperature_sensor.get_reading() > TEMP_HIGH:
            living_room_ac.turn_on()
            # Wait for a short time to allow temperature change
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
        else:
            living_room_heater.turn_off()
            living_room_ac.turn_off()


if __name__ == "__main__":
    main()

# **Explanation of the Code:**

# 1. **Imports:**
#    - Imports necessary classes and functions from `home.home_plan`, `home.sensor`, `home.actuator`, and `home.config`.
#    - Imports `time` for pausing execution and `logger` for logging information.

# 2. **`home` Variable:**
#    - Creates an instance of the `home` variable using `home_plan()` to represent the entire smart home layout.

# 3. **`main()` Function:**
#    - Contains the logic for controlling the smart home components.
#    - **Temperature Control:**
#      - Retrieves the `LivingRoom` and its `IndoorTemperatureSensor`, `Heater`, and `AC`.
#      - Turns on the heater if the temperature is below the `TEMP_LOW` threshold, turns on the AC if the temperature is above the `TEMP_HIGH` threshold, and turns off both if the temperature is within the desired range.
#    - **Light Control:**
#      - Retrieves the `Bedroom` and its `LightIntensiveSensor` and `Light`.
#      - Turns on the bedroom light if the light intensity is below the `LIGHT_INTENSITY_LOW` threshold.
#    - **Coffee Machine:**
#      - Retrieves the `Kitchen` and its `CoffeeMachine`.
#      - Turns on the coffee machine and makes a "Cappuccino".
#    - **Cleaning Robot:**
#      - Retrieves the `LivingRoom` and its `CleaningRobot`.
#      - Turns on the cleaning robot and starts its daily routine.
#    - **Humidity Control:**
#      - Retrieves the `Bathroom` and its `HumiditySensor` and `Humidifier`.
#      - Turns on the humidifier if the humidity is below the `HUMIDITY_LOW` threshold and turns off if the humidity is above the `HUMIDITY_HIGH` threshold.
#    - **External Temperature Control:**
#      - Retrieves the `Balcony` and its `OutdoorTemperatureSensor` and the `LivingRoom` with its `Heater` and `AC`.
#      - Turns on the living room heater/AC based on the external temperature, waiting for a short duration to allow temperature changes to take effect.

# 4. **`if __name__ == "__main__":` Block:**
#    - Calls the `main()` function to execute the smart home control logic.

# **Key Points:**

# - The code demonstrates how to interact with sensors and actuators within different rooms of the smart home.
# - It showcases examples of common control scenarios, such as temperature regulation, light adjustment, appliance usage, cleaning, and humidity management.
# - The code utilizes thresholds and waiting durations to provide realistic control mechanisms.
# - The `logger` is used to log various events and actions for debugging and monitoring purposes.
# - This code serves as a foundation for building more complex and sophisticated smart home applications.

# **Enhancements:**

# - **User Interaction:** Implement user interfaces (e.g., voice commands, mobile apps) to allow for more interactive control.
# - **Automation:** Add more advanced automation rules based on sensor data and user preferences.
# - **Integration:** Connect to real-world hardware (sensors, actuators) via APIs or communication protocols.
# - **Security:** Implement security measures to protect the smart home system from unauthorized access.
