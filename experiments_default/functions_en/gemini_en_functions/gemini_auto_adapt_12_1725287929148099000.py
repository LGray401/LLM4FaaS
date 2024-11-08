from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import Light, AC, Heater, CoffeeMachine, Window, Curtain, CleaningRobot, NotificationSender, MusicPlayer, \
    Door, SmartTV, SmartSocket, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time

# function.py

def main():
    home = home_plan()  # Get the home plan

    # Example: Adjusting temperature in the Living Room based on temperature and humidity
    living_room = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    while True:
        for sensor in living_room:
            if isinstance(sensor, IndoorTemperatureSensor):
                temperature = sensor.get_reading()
                if temperature is not None:
                    for actuator in living_room_actuators:
                        if isinstance(actuator, Heater):
                            actuator.adjust_temperature(temperature)
                            if temperature < TEMP_LOW:
                                print(f"Turning on heater in Living Room because temperature is {temperature}°C.")
                                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                        elif isinstance(actuator, AC):
                            actuator.adjust_temperature(temperature)
                            if temperature > TEMP_HIGH:
                                print(f"Turning on AC in Living Room because temperature is {temperature}°C.")
                                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            elif isinstance(sensor, HumiditySensor):
                humidity = sensor.get_reading()
                if humidity is not None:
                    for actuator in living_room_actuators:
                        if isinstance(actuator, Humidifier):
                            if humidity < HUMIDITY_LOW:
                                print(f"Increasing humidity in Living Room because humidity is {humidity}%.")
                                actuator.increase_humidity()
                                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                            elif humidity > HUMIDITY_HIGH:
                                print(f"Decreasing humidity in Living Room because humidity is {humidity}%.")
                                actuator.decrease_humidity()
                                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
            elif isinstance(sensor, LightIntensiveSensor):
                light_intensity = sensor.get_reading()
                if light_intensity is not None:
                    for actuator in living_room_actuators:
                        if isinstance(actuator, Light):
                            if light_intensity < LIGHT_INTENSITY_LOW:
                                print(f"Turning on light in Living Room because light intensity is {light_intensity} lux.")
                                actuator.turn_on()
                                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                            elif light_intensity > LIGHT_INTENSITY_HIGH:
                                print(f"Turning off light in Living Room because light intensity is {light_intensity} lux.")
                                actuator.turn_off()
                                time.sleep(TEMP_CHANGE_DURATION_WINDOW)

        # Example: Coffee machine automation
        kitchen = get_room_actuators(home, "Kitchen")
        for actuator in kitchen:
            if isinstance(actuator, CoffeeMachine):
                if time.strftime("%H") == "08":  # Make coffee at 8:00 AM
                    print("It's 8:00 AM, time for coffee!")
                    actuator.make_coffee("Cappuccino")
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

        # Example: Cleaning robot automation
        for room in home:
            for actuator in room.actuators:
                if isinstance(actuator, CleaningRobot):
                    if time.strftime("%H") == "17":  # Start daily cleaning routine at 5:00 PM
                        print(f"It's 5:00 PM, time for daily cleaning routine in {room.name}.")
                        actuator.daily_routine()
                        time.sleep(DAILY_ROUTINE_DURATION)

        time.sleep(10)  # Check sensors and actuators every 10 seconds

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:** Import modules from `home_plan.py`, `sensor.py`, `actuator.py`, and `config.py`.
# 2. **Define `main()` function:**
#     - Get the home plan using `home = home_plan()`.
#     - **Temperature and Humidity Control:**
#         - Get sensors and actuators for the "LivingRoom."
#         - Iterate through sensors and actuators:
#             - If the sensor is an `IndoorTemperatureSensor`:
#                 - Get the temperature reading.
#                 - If the temperature is below `TEMP_LOW`, turn on the `Heater`.
#                 - If the temperature is above `TEMP_HIGH`, turn on the `AC`.
#             - If the sensor is a `HumiditySensor`:
#                 - Get the humidity reading.
#                 - If the humidity is below `HUMIDITY_LOW`, increase humidity using the `Humidifier`.
#                 - If the humidity is above `HUMIDITY_HIGH`, decrease humidity using the `Humidifier`.
#             - If the sensor is a `LightIntensiveSensor`:
#                 - Get the light intensity reading.
#                 - If the light intensity is below `LIGHT_INTENSITY_LOW`, turn on the `Light`.
#                 - If the light intensity is above `LIGHT_INTENSITY_HIGH`, turn off the `Light`.
#     - **Coffee Machine Automation:**
#         - Get actuators for the "Kitchen."
#         - Iterate through actuators:
#             - If the actuator is a `CoffeeMachine`, make a "Cappuccino" at 8:00 AM.
#     - **Cleaning Robot Automation:**
#         - Iterate through rooms in the home plan and actuators in each room:
#             - If the actuator is a `CleaningRobot`, start the daily cleaning routine at 5:00 PM.
#     - **Sleep:** Sleep for 10 seconds before repeating the cycle.
# 3. **Run `main()` function:** Run the `main()` function when the script is executed.

# **Remember to:**

# - **Install the required libraries:** `pip install python-dotenv`
# - **Adjust the configuration settings:** Change the values in `config.py` to suit your specific needs.
# - **Implement more automation logic:** This code provides a basic example. Add more conditions, actions, and actuators to build a comprehensive smart home system.
# - **Add error handling:** Consider adding error handling for situations like sensor failures or actuator errors.

# This code provides a starting point for building a smart home system with Python. Feel free to expand upon it and customize it to your liking.
