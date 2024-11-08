from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, AC, Heater, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def main():
    # Initialize the home plan
    home = home_plan()

    # Example usage of functions to access and interact with home components
    # Get the LivingRoom
    living_room = get_room(home, "LivingRoom")

    # Get all lights
    all_lights = get_all_actuators(home, "Light")

    # Get all indoor temperature sensors
    all_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all humidity sensors
    all_humidity_sensors = get_all_sensors(home, "Humidity")

    # Get all light intensity sensors
    all_light_sensors = get_all_sensors(home, "LightIntensive")

    # Example: Turn on all lights in the LivingRoom
    if living_room:
        living_room_lights = get_room_actuators(home, "LivingRoom")
        if living_room_lights:
            for light in living_room_lights:
                if isinstance(light, Light):
                    light.turn_on()

    # Example: Adjust AC temperature in the LivingRoom
    if living_room:
        living_room_ac = get_room_actuators(home, "LivingRoom")
        if living_room_ac:
            for ac in living_room_ac:
                if isinstance(ac, AC):
                    current_temp = get_current_temp(living_room)
                    ac.adjust_temperature(current_temp)

    # Example: Adjust heater temperature in the LivingRoom
    if living_room:
        living_room_heater = get_room_actuators(home, "LivingRoom")
        if living_room_heater:
            for heater in living_room_heater:
                if isinstance(heater, Heater):
                    current_temp = get_current_temp(living_room)
                    heater.adjust_temperature(current_temp)

    # Example: Adjust humidifier in the LivingRoom
    if living_room:
        living_room_humidifier = get_room_actuators(home, "LivingRoom")
        if living_room_humidifier:
            for humidifier in living_room_humidifier:
                if isinstance(humidifier, Humidifier):
                    current_humidity = get_current_humidity(living_room)
                    humidifier.adjust_humidity(current_humidity)

    # Example: Set light brightness level in the LivingRoom
    if living_room:
        living_room_lights = get_room_actuators(home, "LivingRoom")
        if living_room_lights:
            for light in living_room_lights:
                if isinstance(light, Light):
                    current_light_intensity = get_current_light_intensity(living_room)
                    light.set_brightness_level(get_brightness_level(current_light_intensity))

    # Example: Get and print sensor readings
    if living_room:
        print(f"LivingRoom temperature: {get_current_temp(living_room)}°C")
        print(f"LivingRoom humidity: {get_current_humidity(living_room)}%")
        print(f"LivingRoom light intensity: {get_current_light_intensity(living_room)} lux")


def get_current_temp(room):
    if room:
        temp_sensors = get_room_sensors(home_plan(), room.name)
        if temp_sensors:
            for sensor in temp_sensors:
                if isinstance(sensor, IndoorTemperatureSensor):
                    return sensor.get_reading()
    return None


def get_current_humidity(room):
    if room:
        humidity_sensors = get_room_sensors(home_plan(), room.name)
        if humidity_sensors:
            for sensor in humidity_sensors:
                if isinstance(sensor, HumiditySensor):
                    return sensor.get_reading()
    return None


def get_current_light_intensity(room):
    if room:
        light_sensors = get_room_sensors(home_plan(), room.name)
        if light_sensors:
            for sensor in light_sensors:
                if isinstance(sensor, LightIntensiveSensor):
                    return sensor.get_reading()
    return None


def get_brightness_level(light_intensity):
    if light_intensity is not None:
        if light_intensity <= LIGHT_INTENSITY_LOW:
            return "low"
        elif LIGHT_INTENSITY_LOW < light_intensity <= LIGHT_INTENSITY_HIGH:
            return "medium"
        else:
            return "high"
    return None


if __name__ == "__main__":
    main()

# **Explanation of the 'function.py' file:**

# 1. **Import necessary modules:**
#    - Imports functions from `home.home_plan` to manage the home structure.
#    - Imports sensor classes (`IndoorTemperatureSensor`, `HumiditySensor`, `LightIntensiveSensor`) from `home.sensor`.
#    - Imports actuator classes (`Light`, `AC`, `Heater`, `Humidifier`) from `home.actuator`.
#    - Imports constants for temperature, humidity, and light intensity thresholds from `home.config`.

# 2. **`main()` function:**
#    - Initializes the `home` structure using `home_plan()`.
#    - Demonstrates how to use functions to access and interact with home components:
#      - **Getting rooms:** `get_room(home, "LivingRoom")` to get the LivingRoom object.
#      - **Getting actuators:** `get_all_actuators(home, "Light")` to get a list of all `Light` actuators.
#      - **Getting sensors:** `get_all_sensors(home, "IndoorTemperature")` to get a list of all `IndoorTemperatureSensor`s.
#    - Example scenarios:
#      - Turn on all lights in the LivingRoom.
#      - Adjust AC temperature based on the current temperature.
#      - Adjust heater temperature based on the current temperature.
#      - Adjust humidifier based on the current humidity.
#      - Set light brightness level based on the current light intensity.
#    - Gets and prints sensor readings for the LivingRoom.

# 3. **Helper functions:**
#    - `get_current_temp(room)`: Returns the current temperature reading from the LivingRoom.
#    - `get_current_humidity(room)`: Returns the current humidity reading from the LivingRoom.
#    - `get_current_light_intensity(room)`: Returns the current light intensity reading from the LivingRoom.
#    - `get_brightness_level(light_intensity)`: Determines the appropriate light brightness level based on the intensity reading.

# **How to use this 'function.py' file:**

# 1. Make sure you have the `home` folder with the necessary files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) in the same directory as `function.py`.
# 2. Run `function.py` from your terminal: `python function.py`
# 3. This will execute the example scenarios and print sensor readings.

# **Key improvements:**

# - **Organized functions:** Provides functions to access and interact with home components, making the code cleaner and easier to understand.
# - **Helper functions:** The helper functions make it easier to get sensor readings and adjust actuator settings based on specific conditions.
# - **Comments:** Includes comments to explain the purpose of each function and section.
# - **Example scenarios:** Provides clear examples of how to use the functions to control different home components.

# **Remember to customize this code:**

# - Add more example scenarios and functions to control other devices and sensors in your smart home.
# - Adjust the constants in `config.py` to match your specific requirements.
# - Adapt the logic in `function.py` to create your desired smart home automation rules.
