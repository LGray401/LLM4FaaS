# Based on the content of the markdown file, it appears that you are working on a smart home project and you need a new Python file named `function.py` to be created in the 'functions' folder. This file should contain the main function that controls the behavior of your smart home based on the functional description provided.
#
# The functional description is in Chinese, but it translates to: "When the kitchen smoke exceeds the standard, turn on the smoke alarm. In summer, when the indoor temperature is less than 20 degrees, automatically turn off the air conditioner. When the temperature is higher than 25 degrees, turn on the air conditioner. Set up a sensor light, the light is on when someone is there, and it automatically turns off when no one is there."
#
# The `function.py` file should interact with the existing Python files in your project: `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`, which are located in the 'home' folder.
#
# Here is a high-level pseudocode of what the `function.py` file might look like:
#
# 1. Import necessary modules and classes from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`.
# 2. Define the main function.
# 3. In the main function, create instances of the necessary sensors and actuators.
# 4. Implement the logic described in the functional description:
# - If the smoke sensor in the kitchen detects smoke above a certain level, turn on the smoke alarm.
# - If the indoor temperature sensor detects a temperature less than 20 degrees in summer, turn off the air conditioner.
# - If the indoor temperature sensor detects a temperature greater than 25 degrees in summer, turn on the air conditioner.
# - If the light sensor detects someone, turn on the light. If it doesn't detect anyone, turn off the light.
# 5. Call the main function.
#
# Here is a Python code snippet that implements the above pseudocode:
#
# ```python
from home.sensor import SmokeSensor, IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, Light, NotificationSender
from home.home_plan import get_room
from home.config import TEMP_LOW, TEMP_HIGH

def main():
    # Create instances of necessary sensors and actuators
    kitchen = get_room("Kitchen")
    living_room = get_room("LivingRoom")

    smoke_sensor = next((sensor for sensor in kitchen.sensors if isinstance(sensor, SmokeSensor)), None)
    temp_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    light_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)), None)

    ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
    light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)
    smoke_alarm = next((actuator for actuator in kitchen.actuators if isinstance(actuator, NotificationSender)), None)

    # Implement the logic described in the functional description
    if smoke_sensor.get_reading() > 50:  # Assuming 50 is the smoke level standard
        smoke_alarm.notification_sender("Smoke detected in the kitchen!")

    if temp_sensor.get_reading() < TEMP_LOW:
        ac.turn_off()
    elif temp_sensor.get_reading() > TEMP_HIGH:
        ac.turn_on()

    if light_sensor.get_reading() > 500:  # Assuming 500 is the light level indicating someone is there
        light.turn_on()
    else:
        light.turn_off()

if __name__ == "__main__":
    main()
# ```
#
# Please replace the thresholds in the code with the actual values you want to use. The code assumes that the `get_room` function returns a `Room` object with the specified name, and that the `Room` object has `sensors` and `actuators` attributes that are lists of `Sensor` and `Actuator` objects, respectively.