from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_actuators, \
    get_all_sensors
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

import time


def morning_plan(home):
    living_room = get_room(home, "LivingRoom")
    coffee_machine = get_room_actuators(living_room, "CoffeeMachine")[0]
    coffee_machine.turn_on()
    coffee_machine.make_coffee("7.40 degree coffee")


def leave_home_plan(home):
    living_room = get_room(home, "LivingRoom")
    door = get_room_actuators(living_room, "Door")[0]
    door.lock()


def movie_plan(home):
    living_room = get_room(home, "LivingRoom")
    tv = get_room_actuators(living_room, "SmartTV")[0]
    tv.turn_on()
    tv.play_channel("Channel 7")


def main():
    home = home_plan()

    # Example: Execute morning plan
    morning_plan(home)
    time.sleep(1)  # Simulate time passing

    # Example: Execute leave home plan
    leave_home_plan(home)
    time.sleep(1)

    # Example: Execute movie plan
    movie_plan(home)

    # Example: Turn on lights in the bedroom
    bedroom = get_room(home, "Bedroom")
    lights = get_room_actuators(bedroom, "Light")
    for light in lights:
        light.turn_on()

    # Example: Set AC temperature in the living room
    living_room = get_room(home, "LivingRoom")
    ac = get_room_actuators(living_room, "AC")[0]
    ac.set_target_temperature(22)  # Set target temperature to 22 degrees Celsius

    # Example: Adjust heating in the bathroom based on temperature sensor reading
    bathroom = get_room(home, "Bathroom")
    heater = get_room_actuators(bathroom, "Heater")[0]
    temperature_sensor = get_room_sensors(bathroom, "IndoorTemperature")[0]

    while True:
        current_temperature = temperature_sensor.get_reading()
        if current_temperature < TEMP_LOW:
            heater.turn_on()
            print(f"Heating on in the bathroom. Current temperature is {current_temperature}°C.")
        elif current_temperature > TEMP_HIGH:
            heater.turn_off()
            print(f"Heating off in the bathroom. Current temperature is {current_temperature}°C.")
        time.sleep(1)  # Simulate time passing

    # ... continue with more logic and automation tasks ...


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** The code imports necessary modules like `home_plan`, `sensor`, `actuator`, and `config`.
# 2. **Plan Functions:** The code defines functions for different plans:
#    - `morning_plan()`: Turns on the coffee machine and makes coffee.
#    - `leave_home_plan()`: Locks the door in the living room.
#    - `movie_plan()`: Turns on the TV in the living room and starts playing a channel.
# 3. **`main()` Function:**
#    - Creates a home plan using `home_plan()`.
#    - Executes the `morning_plan()`, `leave_home_plan()`, and `movie_plan()`.
#    - Demonstrates turning on lights in the bedroom and setting the AC temperature in the living room.
#    - Includes a loop to demonstrate adjusting the bathroom heater based on temperature sensor readings.
# 4. **Temperature Control:**
#    - The `while True` loop constantly checks the bathroom temperature using `get_reading()`.
#    - If the temperature is below `TEMP_LOW`, the heater is turned on.
#    - If the temperature is above `TEMP_HIGH`, the heater is turned off.
#    - The loop includes a `time.sleep(1)` to simulate time passing.

# **How to Use:**

# 1. **Run the code:** Execute `function.py` using `python function.py`.
# 2. **Modify Plans:** You can adjust the plan functions to add more actions or change existing ones based on your smart home needs.
# 3. **Extend Logic:** Implement more automation tasks by adding logic to the `main()` function using the functions provided by `home_plan`, `sensor`, and `actuator`.

# **Key Points:**

# - The code uses the classes and functions provided in `home_plan`, `sensor`, and `actuator` to interact with the smart home components.
# - The `config.py` file contains configuration parameters like temperature thresholds and device names.
# - The `main()` function serves as the entry point for your smart home automation logic.
