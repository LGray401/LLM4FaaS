from home.home_plan import get_room, get_room_sensors, get_room_actuators, get_all_actuators, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def morning_plan(home):
    """
    Execute the morning plan for the smart home.

    Args:
        home: The smart home plan.

    Returns:
        None
    """
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        coffee_machine = get_room_actuators(home, "Kitchen")[0]
        if coffee_machine:
            print("Making coffee...")
            coffee_machine.turn_on()
            coffee_machine.make_coffee("Espresso")
            print("Coffee is ready!")
            coffee_machine.turn_off()
        else:
            logger.error("No coffee machine found in the kitchen!")

def leave_home_plan(home):
    """
    Execute the leave home plan for the smart home.

    Args:
        home: The smart home plan.

    Returns:
        None
    """
    all_lights = get_all_actuators(home, "Light")
    if all_lights:
        print("Turning off all lights...")
        for light in all_lights:
            light.turn_off()
        print("All lights are off!")
    else:
        logger.error("No lights found in the home!")
    # Add additional actions for leaving home, like locking doors, etc.

def movie_plan(home):
    """
    Execute the movie plan for the smart home.

    Args:
        home: The smart home plan.

    Returns:
        None
    """
    living_room = get_room(home, "LivingRoom")
    if living_room:
        curtain = get_room_actuators(home, "LivingRoom")[0]
        if curtain:
            print("Closing curtains...")
            curtain.turn_on()
            print("Curtains are closed!")
        else:
            logger.error("No curtains found in the living room!")
    else:
        logger.error("No living room found in the home!")
    # Add additional actions for movie plan, like adjusting lighting, turning on TV, etc.

def temperature_control(home):
    """
    Control temperature based on sensor readings and predefined thresholds.

    Args:
        home: The smart home plan.

    Returns:
        None
    """
    all_indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    all_heaters = get_all_actuators(home, "Heater")
    all_acs = get_all_actuators(home, "AC")

    if all_indoor_temperature_sensors and (all_heaters or all_acs):
        for sensor in all_indoor_temperature_sensors:
            current_temperature = sensor.get_reading()
            if current_temperature is not None:
                print(f"Current temperature in {sensor.room_name}: {current_temperature}°C")

                if current_temperature < TEMP_LOW and all_heaters:
                    print("Turning on heater...")
                    for heater in all_heaters:
                        heater.turn_on()
                        heater.set_target_temperature(TEMP_HIGH)

                elif current_temperature > TEMP_HIGH and all_acs:
                    print("Turning on AC...")
                    for ac in all_acs:
                        ac.turn_on()
                        ac.set_target_temperature(TEMP_LOW)

                else:
                    print("Temperature is within acceptable range.")
    else:
        if not all_indoor_temperature_sensors:
            logger.error("No indoor temperature sensors found!")
        if not (all_heaters or all_acs):
            logger.error("No heaters or AC units found!")

def humidity_control(home):
    """
    Control humidity based on sensor readings and predefined thresholds.

    Args:
        home: The smart home plan.

    Returns:
        None
    """
    all_humidity_sensors = get_all_sensors(home, "Humidity")
    # Assuming no specific actuators for humidity control yet.
    # Implement logic to control humidifiers or dehumidifiers based on humidity readings and thresholds.

    if all_humidity_sensors:
        for sensor in all_humidity_sensors:
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                print(f"Current humidity in {sensor.room_name}: {current_humidity}%")

                if current_humidity < HUMIDITY_LOW:
                    print("Humidity is too low. Consider adding a humidifier.")

                elif current_humidity > HUMIDITY_HIGH:
                    print("Humidity is too high. Consider adding a dehumidifier.")

                else:
                    print("Humidity is within acceptable range.")
    else:
        logger.error("No humidity sensors found!")

def light_control(home):
    """
    Control light intensity based on sensor readings and predefined thresholds.

    Args:
        home: The smart home plan.

    Returns:
        None
    """
    all_light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    all_lights = get_all_actuators(home, "Light")

    if all_light_intensive_sensors and all_lights:
        for sensor in all_light_intensive_sensors:
            current_intensity = sensor.get_reading()
            if current_intensity is not None:
                print(f"Current light intensity in {sensor.room_name}: {current_intensity} lux")

                if current_intensity < LIGHT_INTENSITY_LOW:
                    print("Light intensity is low. Turning on lights...")
                    for light in all_lights:
                        light.turn_on()
                        light.set_brightness_level("high")

                elif current_intensity > LIGHT_INTENSITY_HIGH:
                    print("Light intensity is high. Dimming lights...")
                    for light in all_lights:
                        light.turn_on()
                        light.set_brightness_level("low")

                else:
                    print("Light intensity is within acceptable range.")
    else:
        if not all_light_intensive_sensors:
            logger.error("No light intensive sensors found!")
        if not all_lights:
            logger.error("No lights found!")

if __name__ == "__main__":
    home = home_plan()
    # morning_plan(home)
    # leave_home_plan(home)
    # movie_plan(home)
    temperature_control(home)
    humidity_control(home)
    light_control(home)

# This file defines several functions for executing different smart home plans:

# - `morning_plan`: Turns on the coffee machine in the kitchen and makes coffee.
# - `leave_home_plan`: Turns off all lights in the house.
# - `movie_plan`: Closes the curtains in the living room.
# - `temperature_control`:  Controls the temperature based on sensor readings.
# - `humidity_control`: Controls the humidity based on sensor readings. (Currently a placeholder as no humidity control actuators are defined.)
# - `light_control`: Controls the light intensity based on sensor readings.

# **Key features:**

# - **Uses functions from `home_plan.py`:** Imports functions to retrieve rooms, sensors, and actuators based on their names and types.
# - **Uses constants from `config.py`:**  Imports thresholds for temperature, humidity, and light intensity.
# - **Logs actions:** Uses the logger from `logger_config.py` to log actions and errors.

# **To run this code:**

# 1. Make sure you have `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` in the `home` folder.
# 2. Create a `functions` folder and place `function.py` in it.
# 3. Run `function.py`.

# **Note:** This is a basic example, and you can expand it with more complex plans and features. You can also add more sensor and actuator types to the project as needed.
