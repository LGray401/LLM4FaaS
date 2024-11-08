from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import AC, Heater, Light, Curtain, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

# Function to check if the temperature is too low or too high
def check_temperature(room_name, home):
    indoor_temperature_sensors = get_room_sensors(home, room_name)
    if indoor_temperature_sensors:
        for sensor in indoor_temperature_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temperature = sensor.get_reading()
                if temperature is not None:
                    if temperature < TEMP_LOW:
                        print(f"The temperature in {room_name} is too low! Turning on heater.")
                        heaters = get_room_actuators(home, room_name)
                        if heaters:
                            for heater in heaters:
                                if isinstance(heater, Heater):
                                    heater.turn_on()
                                    heater.set_target_temperature(TEMP_HIGH)  # Set a comfortable temperature
                    elif temperature > TEMP_HIGH:
                        print(f"The temperature in {room_name} is too high! Turning on AC.")
                        acs = get_room_actuators(home, room_name)
                        if acs:
                            for ac in acs:
                                if isinstance(ac, AC):
                                    ac.turn_on()
                                    ac.set_target_temperature(TEMP_LOW)  # Set a comfortable temperature
    else:
        print(f"No indoor temperature sensor found in {room_name}.")

# Function to check if the humidity is too low or too high
def check_humidity(room_name, home):
    humidity_sensors = get_room_sensors(home, room_name)
    if humidity_sensors:
        for sensor in humidity_sensors:
            if isinstance(sensor, HumiditySensor):
                humidity = sensor.get_reading()
                if humidity is not None:
                    if humidity < HUMIDITY_LOW:
                        print(f"The humidity in {room_name} is too low! Turning on humidifier.")
                        humidifiers = get_room_actuators(home, room_name)
                        if humidifiers:
                            for humidifier in humidifiers:
                                if isinstance(humidifier, Humidifier):
                                    humidifier.increase_humidity()
                    elif humidity > HUMIDITY_HIGH:
                        print(f"The humidity in {room_name} is too high! Opening windows.")
                        windows = get_room_actuators(home, room_name)
                        if windows:
                            for window in windows:
                                if isinstance(window, Window):
                                    window.turn_on()
    else:
        print(f"No humidity sensor found in {room_name}.")

# Function to check if the light intensity is too high
def check_light_intensity(room_name, home):
    light_intensity_sensors = get_room_sensors(home, room_name)
    if light_intensity_sensors:
        for sensor in light_intensity_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                light_intensity = sensor.get_reading()
                if light_intensity is not None:
                    if light_intensity > LIGHT_INTENSITY_HIGH:
                        print(f"The light intensity in {room_name} is too high! Closing curtains.")
                        curtains = get_room_actuators(home, room_name)
                        if curtains:
                            for curtain in curtains:
                                if isinstance(curtain, Curtain):
                                    curtain.turn_on()
    else:
        print(f"No light intensity sensor found in {room_name}.")


# Function to control the lights based on the time of day
def control_lights(room_name, home, time_of_day):
    lights = get_room_actuators(home, room_name)
    if lights:
        for light in lights:
            if isinstance(light, Light):
                if time_of_day == "morning":
                    print(f"Turning on lights in {room_name} as it is morning.")
                    light.turn_on()
                    light.set_brightness_level("medium")
                elif time_of_day == "evening":
                    print(f"Turning on lights in {room_name} as it is evening.")
                    light.turn_on()
                    light.set_brightness_level("low")
                elif time_of_day == "night":
                    print(f"Turning off lights in {room_name} as it is night.")
                    light.turn_off()
    else:
        print(f"No lights found in {room_name}.")

# Main function to run the smart home automation logic
def main():
    home = home_plan()  # Initialize the home plan
    
    # Example usage:
    
    # Check temperature in LivingRoom
    check_temperature("LivingRoom", home)
    
    # Check humidity in Kitchen
    check_humidity("Kitchen", home)
    
    # Check light intensity in Bedroom
    check_light_intensity("Bedroom", home)
    
    # Control lights in LivingRoom based on time of day
    control_lights("LivingRoom", home, "evening")  # Example: It's evening now

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:** Imports relevant classes from `home.home_plan`, `home.sensor`, `home.actuator`, and `home.config`.
# 2. **Define helper functions:**
#    - `check_temperature(room_name, home)`: Checks the temperature in a room and adjusts heating or cooling accordingly.
#    - `check_humidity(room_name, home)`: Checks the humidity in a room and adjusts humidification or ventilation accordingly.
#    - `check_light_intensity(room_name, home)`: Checks the light intensity in a room and adjusts curtains if needed.
#    - `control_lights(room_name, home, time_of_day)`: Controls the lights in a room based on the time of day.
# 3. **Main function:**
#    - Creates the `home` object using `home_plan()`.
#    - Calls the helper functions for different rooms and actions:
#      - `check_temperature("LivingRoom", home)`
#      - `check_humidity("Kitchen", home)`
#      - `check_light_intensity("Bedroom", home)`
#      - `control_lights("LivingRoom", home, "evening")`
#    - Adjust these function calls to include all the rooms and actions you need to automate.

# **To use this code:**

# 1. Make sure you have the following files in your project:
#    - `functions/function.py` (this file)
#    - `home/sensor.py`
#    - `home/actuator.py`
#    - `home/home_plan.py`
#    - `home/config.py`
# 2. Replace the example calls in the `main()` function with the actual logic you want to implement for your smart home automation.
# 3. Run `function.py` to execute the automation.

# **Key points:**

# - The code uses the classes from `home.sensor` and `home.actuator` to interact with sensors and actuators.
# - The logic for each function is specific to the actions you want to automate.
# - The `main()` function is responsible for orchestrating the automation logic.
# - You can expand this code by adding more functions and logic to handle various other automation tasks.
