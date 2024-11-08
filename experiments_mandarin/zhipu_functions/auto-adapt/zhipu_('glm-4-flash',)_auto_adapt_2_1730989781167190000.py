# Based on the provided functional description and source code, here is the `function.py` file for your smart home project:

import time
from home.sensor import IndoorTemperatureSensor
from home.actuator import AC, Window, Humidifier
from home.logger_config import logger

# Assume home_plan() and get_room() functions are defined in home_plan.py
# Assume get_room_sensors() function is defined in home_plan.py

# Function to check and control the home based on temperature
def check_and_control_temperature(room_name):
    indoor_temp_sensor = get_room_sensors(room_name, "IndoorTemperature")
    if indoor_temp_sensor:
        current_temp = indoor_temp_sensor[0].get_reading()
        if current_temp is not None:
            if current_temp > 25:
                # Turn on AC and close the window
                ac = get_room_actuators(room_name, "AC")[0]
                window = get_room_actuators(room_name, "Window")[0]
                ac.turn_on()
                window.turn_off()
                logger.info(f"Turned on AC and closed the window in {room_name} due to high temperature.")
            else:
                # Turn off AC and open the window
                ac = get_room_actuators(room_name, "AC")[0]
                window = get_room_actuators(room_name, "Window")[0]
                ac.turn_off()
                window.turn_on()
                logger.info(f"Turned off AC and opened the window in {room_name} due to normal temperature.")

# Function to check and control the home based on humidity
def check_and_control_humidity(room_name):
    humidity_sensor = get_room_sensors(room_name, "Humidity")
    if humidity_sensor:
        current_humidity = humidity_sensor[0].get_reading()
        if current_humidity is not None:
            if current_humidity < 30:  # Assuming 30% is the low humidity threshold
                # Turn on humidifier
                humidifier = get_room_actuators(room_name, "Humidifier")[0]
                humidifier.increase_humidity()
                logger.info(f"Turned on humidifier in {room_name} due to low humidity.")
            else:
                # Turn off humidifier
                humidifier = get_room_actuators(room_name, "Humidifier")[0]
                humidifier.decrease_humidity()
                logger.info(f"Turned off humidifier in {room_name} due to normal humidity.")

# Main function to run the smart home system
def main():
    home = home_plan()
    # Example: Check and control the temperature in the LivingRoom
    check_and_control_temperature("LivingRoom")

    # You can add more conditions to control the home based on other sensors like light intensity, etc.

    # Sleep for a while before checking again
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Repeat the checks at regular intervals
    while True:
        check_and_control_temperature("LivingRoom")
        check_and_control_humidity("LivingRoom")
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()