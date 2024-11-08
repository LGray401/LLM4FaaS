from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

import time


def main():
    """
    This function contains the main logic of the smart home system. It includes:
        1. Initializing the home plan and getting references to sensors and actuators.
        2. Running an infinite loop to constantly monitor sensor readings and adjust actuators accordingly.
        3. Implementing various functionalities based on user requests.
    """
    home = home_plan()
    print_home_plan(home)

    # Get references to sensors and actuators
    living_room = get_room(home, "LivingRoom")
    living_room_temp_sensor = get_room_sensors(home, "LivingRoom")[0]
    living_room_humidity_sensor = get_room_sensors(home, "LivingRoom")[1]
    living_room_light_sensor = get_room_sensors(home, "LivingRoom")[2]
    living_room_light = get_room_actuators(home, "LivingRoom")[0]
    living_room_ac = get_room_actuators(home, "LivingRoom")[10]
    living_room_heater = get_room_actuators(home, "LivingRoom")[11]
    notification_sender = get_all_actuators(home, "NotificationSender")[0]

    # Turn on the sensors and actuators
    living_room_temp_sensor.turn_on()
    living_room_humidity_sensor.turn_on()
    living_room_light_sensor.turn_on()
    living_room_light.turn_on()
    notification_sender.turn_on()

    while True:
        # Monitor sensor readings
        temperature = living_room_temp_sensor.get_reading()
        humidity = living_room_humidity_sensor.get_reading()
        light_intensity = living_room_light_sensor.get_reading()

        # Adjust actuators based on sensor readings
        if temperature < TEMP_LOW:
            living_room_heater.turn_on()
            notification_sender.notification_sender("The temperature is too low. The heater has been turned on.")
        elif temperature > TEMP_HIGH:
            living_room_ac.turn_on()
            notification_sender.notification_sender("The temperature is too high. The AC has been turned on.")
        else:
            living_room_heater.turn_off()
            living_room_ac.turn_off()

        if humidity < HUMIDITY_LOW:
            # TODO: Add humidifier functionality
            notification_sender.notification_sender("The humidity is too low. Consider using a humidifier.")
        elif humidity > HUMIDITY_HIGH:
            # TODO: Add dehumidifier functionality
            notification_sender.notification_sender("The humidity is too high. Consider using a dehumidifier.")

        if light_intensity < LIGHT_INTENSITY_LOW:
            living_room_light.set_brightness_level("high")
        elif light_intensity > LIGHT_INTENSITY_HIGH:
            living_room_light.set_brightness_level("low")

        # Implement functionalities based on user requests (TODO)
        # Example:
        # if user_input == "turn_on_lights":
        #     living_room_light.turn_on()
        # elif user_input == "turn_off_lights":
        #     living_room_light.turn_off()

        # Wait for a short period before checking sensor readings again
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:** Imports relevant modules from `home` package and `time` for delays.
# 2. **`main()` function:**
#    - **Initialization:**
#      - Creates a home plan using `home_plan()`.
#      - Prints the home plan using `print_home_plan()`.
#      - Gets references to specific sensors and actuators in the living room using functions like `get_room()`, `get_room_sensors()`, and `get_room_actuators()`.
#      - Turns on the necessary sensors and actuators (you can adjust this based on your needs).
#    - **Infinite loop:**
#      - Continuously monitors sensor readings for temperature, humidity, and light intensity.
#      - Adjusts actuators based on sensor readings:
#        - Turns on the heater if the temperature is below `TEMP_LOW`.
#        - Turns on the AC if the temperature is above `TEMP_HIGH`.
#        - Sends notifications using `notification_sender.notification_sender()` if necessary.
#        - Adjusts the light brightness based on light intensity.
#      - Implements user functionalities (TODO).
#      - Waits for `TEMP_CHANGE_DURATION_WINDOW` seconds before checking sensor readings again.

# **To use this function.py:**

# 1. **Save this code in a file named `function.py` within the `functions` folder of your project.**
# 2. **Ensure that the other required files (sensor.py, actuator.py, home_plan.py, and config.py) are in the `home` folder.**
# 3. **Run `function.py` to start the smart home system.**

# **Remember to:**

# - **Fill in the TODOs to implement additional functionalities based on user input.**
# - **Adjust the configuration values in `config.py` according to your specific requirements.**
# - **Add error handling and logging for robustness.**
# - **Consider integrating with other smart home platforms for wider functionality.**