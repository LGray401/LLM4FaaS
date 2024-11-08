from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.actuator import Light, CoffeeMachine, Curtain
from home.sensor import IndoorTemperatureSensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger

def morning_plan(home):
    """
    Morning plan:
        1. Turn on the lights in the living room to medium brightness
        2. Make a cup of coffee in the kitchen
    """
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        lights = get_room_actuators(home, "LivingRoom")
        if lights:
            for light in lights:
                if isinstance(light, Light):
                    light.turn_on()
                    light.set_brightness_level("medium")
        else:
            logger.warning("No lights found in the living room.")

    kitchen = get_room(home, "Kitchen")
    if kitchen is not None:
        coffee_machine = get_room_actuators(home, "Kitchen")
        if coffee_machine:
            for machine in coffee_machine:
                if isinstance(machine, CoffeeMachine):
                    machine.turn_on()
                    machine.make_coffee("Espresso")
        else:
            logger.warning("No coffee machine found in the kitchen.")

def leave_home_plan(home):
    """
    Leave home plan:
        1. Turn off all the lights in the home
    """
    all_lights = get_all_actuators(home, "Light")
    if all_lights:
        for light in all_lights:
            light.turn_off()
    else:
        logger.warning("No lights found in the home.")

def movie_plan(home):
    """
    Movie plan:
        1. Close the curtains in the living room
    """
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        curtains = get_room_actuators(home, "LivingRoom")
        if curtains:
            for curtain in curtains:
                if isinstance(curtain, Curtain):
                    curtain.turn_on()
        else:
            logger.warning("No curtains found in the living room.")

def temp_control(home):
    """
    Temperature control:
        1. Turn on the heater in the living room if the temperature is below 15 degrees Celsius
        2. Turn on the AC in the living room if the temperature is above 25 degrees Celsius
    """
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        temp_sensors = get_room_sensors(home, "LivingRoom")
        if temp_sensors:
            for sensor in temp_sensors:
                if isinstance(sensor, IndoorTemperatureSensor):
                    current_temp = sensor.get_reading()
                    if current_temp is not None:
                        heaters = get_room_actuators(home, "LivingRoom")
                        if heaters:
                            for heater in heaters:
                                if isinstance(heater, Heater):
                                    heater.set_target_temperature(TEMP_HIGH)
                                    heater.adjust_temperature(current_temp)

                        acs = get_room_actuators(home, "LivingRoom")
                        if acs:
                            for ac in acs:
                                if isinstance(ac, AC):
                                    ac.set_target_temperature(TEMP_LOW)
                                    ac.adjust_temperature(current_temp)
        else:
            logger.warning("No temperature sensors found in the living room.")

def humidity_control(home):
    """
    Humidity control:
        1. Turn on the humidifier in the living room if the humidity is below 30%
        2. Turn on the dehumidifier in the living room if the humidity is above 50%
    """
    # Add logic for humidifier and dehumidifier control
    # ...

def light_control(home):
    """
    Light control:
        1. Turn on the lights in the living room if the light intensity is below 300 lux
        2. Turn off the lights in the living room if the light intensity is above 900 lux
    """
    # Add logic for light control
    # ...

def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)
    # temp_control(home)
    # humidity_control(home)
    # light_control(home)

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions for managing rooms and devices.
#    - `home.actuator`: Contains classes for actuators like lights, coffee machines, etc.
#    - `home.sensor`: Contains classes for sensors like temperature sensors.
#    - `home.config`: Contains configuration values for thresholds and durations.
#    - `home.logger_config`: Handles logging for debugging.

# 2. **Define functions for each plan:**
#    - `morning_plan()`: Turns on lights in the living room and makes coffee in the kitchen.
#    - `leave_home_plan()`: Turns off all lights in the home.
#    - `movie_plan()`: Closes the curtains in the living room.
#    - `temp_control()`: Controls the heater and AC based on temperature.
#    - `humidity_control()`: **(Not implemented)** Controls the humidifier and dehumidifier.
#    - `light_control()`: **(Not implemented)** Controls the lights based on light intensity.

# 3. **Function Logic:**
#    - Each function uses the functions from `home.home_plan` to find specific rooms, devices, and sensors.
#    - The `isinstance` function checks if a device is of the correct type (e.g., `Light`, `CoffeeMachine`, etc.).
#    - The functions use the methods of the actuator classes (e.g., `turn_on()`, `make_coffee()`, `set_brightness_level()`) to control devices.

# 4. **`main()` Function:**
#    - Creates the `home` plan using `home_plan()`.
#    - Calls the plan functions: `morning_plan`, `leave_home_plan`, `movie_plan`.
#    - **(Uncommented)** Calls the `temp_control`, `humidity_control`, `light_control` functions, which are not fully implemented.

# **To use this code:**

# 1. Make sure you have all the files (`sensor.py`, `actuator.py`, `home_plan.py`, `config.py`, `logger_config.py`) in the correct directory structure.
# 2. Run the `function.py` file.
# 3. You can modify the plan functions and configuration values in `config.py` to customize the behavior.

# **Remember to implement the `humidity_control` and `light_control` functions based on your specific hardware and requirements.**
