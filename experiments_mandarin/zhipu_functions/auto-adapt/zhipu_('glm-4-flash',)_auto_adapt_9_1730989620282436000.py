# Based on your functional description and the provided source code, I will create a `function.py` file that contains the `main` function. The `main` function will set up the smart home system by loading the home plan, sensors, and actuators. It will then simulate a day's operation of the smart home by adjusting the temperature, humidity, and light intensity according to predefined thresholds.
# 
# Here's the `function.py` file:

# function.py

from home.sensor import (IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, OutdoorTemperatureSensor,
                         SmokeSensor)
from home.actuator import (Heater, AC, Humidifier, Light, SmartSocket, SmartTV, Window, Curtain, MusicPlayer,
                           CleaningRobot, NotificationSender)
from home_plan import home_plan
from config import (TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH,
                   LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION)

# Define a function to simulate the smart home operation
def main():
    # Load the home plan
    home = home_plan()

    # Initialize the actuators
    # Example: Turn on the lights
    for room in home:
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()

    # Simulate the day's operation
    for _ in range(24):  # Simulate 24 hours
        # Example: Adjust the temperature
        for sensor in get_all_sensors(home, "IndoorTemperature"):
            current_temp = sensor.get_reading()
            if current_temp < TEMP_LOW or current_temp > TEMP_HIGH:
                # Turn on the heater or AC
                if current_temp < TEMP_LOW:
                    for actuator in get_all_actuators(home, "Heater"):
                        actuator.turn_on()
                elif current_temp > TEMP_HIGH:
                    for actuator in get_all_actuators(home, "AC"):
                        actuator.turn_on()

        # Example: Adjust the humidity
        for sensor in get_all_sensors(home, "Humidity"):
            current_humidity = sensor.get_reading()
            if current_humidity < HUMIDITY_LOW or current_humidity > HUMIDITY_HIGH:
                # Turn on the humidifier or dehumidifier
                if current_humidity < HUMIDITY_LOW:
                    for actuator in get_all_actuators(home, "Humidifier"):
                        actuator.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    for actuator in get_all_actuators(home, "Humidifier"):
                        actuator.decrease_humidity()

        # Example: Adjust the light intensity
        for sensor in get_all_sensors(home, "LightIntensive"):
            current_light_intensity = sensor.get_reading()
            if current_light_intensity < LIGHT_INTENSITY_LOW or current_light_intensity > LIGHT_INTENSITY_HIGH:
                # Adjust the light brightness
                for actuator in get_all_actuators(home, "Light"):
                    actuator.set_brightness_level("high" if current_light_intensity > LIGHT_INTENSITY_HIGH else "low")

        # Sleep for a while to simulate the passage of time
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

    # Clean up the home by turning off the actuators
    for room in home:
        for actuator in room.actuators:
            if actuator.status == "on":
                actuator.turn_off()

    # Example: Start the daily cleaning routine for the cleaning robot
    for actuator in get_all_actuators(home, "CleaningRobot"):
        actuator.daily_routine()

    # Send a notification
    for actuator in get_all_actuators(home, "NotificationSender"):
        actuator.notification_sender("Good night! The smart home is now in standby mode.")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()