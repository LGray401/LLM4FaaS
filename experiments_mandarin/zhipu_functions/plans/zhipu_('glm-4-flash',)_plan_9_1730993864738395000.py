# Based on the provided functional description and the existing code in the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files, I will now provide you with the `function.py` file. This file will contain a `main` function that integrates the given plans and configurations to control the smart home system according to the specified plans.
# 
# The `main` function will initialize the home plan, then check the current time and trigger the appropriate plan (Morning, Leave Home, Movie). It will also handle the configuration parameters for temperature, humidity, and light intensity thresholds, which will be used by the actuators.
# 
# Here's the `function.py` file:

# function.py
import datetime
from home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Get the current time
    now = datetime.datetime.now()

    # Check for the Morning plan
    if now.hour == 7 and now.minute == 40:
        # Turn on the Coffee Machine to make coffee
        coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]
        coffee_machine.make_coffee("Espresso")

    # Check for the Leave Home plan
    elif now.hour == 8:
        # Lock the door
        door = get_all_actuators(home, "Door")[0]
        door.lock()

    # Check for the Movie plan
    elif now.hour == 19:
        # Turn on the SmartTV and select a channel
        smart_tv = get_all_actuators(home, "SmartTV")[0]
        smart_tv.play_channel("HBO")

    # Example of handling sensor readings and adjusting actuators based on thresholds
    # Get all Indoor Temperature Sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Check each sensor and adjust the Heater or AC if necessary
    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        if current_temp is not None:
            if current_temp < TEMP_LOW:
                # Turn on the Heater
                heater = get_all_actuators(home, "Heater")[0]
                heater.turn_on()
            elif current_temp > TEMP_HIGH:
                # Turn on the AC
                ac = get_all_actuators(home, "AC")[0]
                ac.turn_on()

    # You can add more conditions for other sensors and actuators as needed

    # Print the home plan for debugging purposes
    print_home_plan(home)

if __name__ == "__main__":
    main()