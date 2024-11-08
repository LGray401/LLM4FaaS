from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, Light, Window, MusicPlayer, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    home = home_plan()

    # Automatically close windows when the air conditioner is turned on
    ac = get_all_actuators(home, "AC")[0]  # Assume only one AC in the house
    windows = get_all_actuators(home, "Window")
    if ac.status == "on":
        for window in windows:
            window.turn_off()
            logger.info(f"Window {window.id} closed because AC is on.")

    # Automatically turn off the air conditioner when the indoor temperature is below 20 degrees
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        if sensor.get_reading() < TEMP_LOW and ac.status == "on":
            ac.turn_off()
            logger.info(f"AC turned off because indoor temperature is below {TEMP_LOW}°C.")

    # Automatically turn off or dim the lights when the light is strong
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    for sensor in light_sensors:
        if sensor.get_reading() > LIGHT_INTENSITY_HIGH:
            for light in lights:
                light.turn_off()
                logger.info(f"Light {light.id} turned off because light intensity is above {LIGHT_INTENSITY_HIGH} lux.")
        elif sensor.get_reading() > LIGHT_INTENSITY_LOW and sensor.get_reading() <= LIGHT_INTENSITY_HIGH:
            for light in lights:
                light.set_brightness_level("low")
                logger.info(f"Light {light.id} dimmed to low because light intensity is between {LIGHT_INTENSITY_LOW} lux and {LIGHT_INTENSITY_HIGH} lux.")

    # Automatically turn off the music player and TV when people leave the house
    # (This is tricky without motion sensors, you'll need a way to detect people leaving)
    # You could use a presence sensor or a door sensor to trigger this behavior.
    # Example using a hypothetical 'PresenceSensor' class:
    # presence_sensors = get_all_sensors(home, "PresenceSensor")
    # for sensor in presence_sensors:
    #     if sensor.get_reading() == "absent":
    #         music_players = get_all_actuators(home, "MusicPlayer")
    #         for player in music_players:
    #             player.turn_off()
    #             logger.info(f"Music player {player.id} turned off because no one is present.")
    #         tvs = get_all_actuators(home, "SmartTV")
    #         for tv in tvs:
    #             tv.turn_off()
    #             logger.info(f"TV {tv.id} turned off because no one is present.")


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - We import necessary components from `home_plan`, `sensor`, `actuator`, and `config` modules.

# 2. **`main()` Function:**
#    - The main function encapsulates all the automation logic.
#    - **Get Home Plan:** Retrieves the home plan using `home_plan()`.
#    - **Find Devices:** Uses helper functions from `home_plan` to find specific devices:
#      - `get_all_actuators(home, "AC")`  to find the air conditioner.
#      - `get_all_actuators(home, "Window")` to find all windows.
#      - `get_all_sensors(home, "IndoorTemperature")` to find indoor temperature sensors.
#      - `get_all_sensors(home, "LightIntensive")` to find light intensity sensors.
#      - **Automations:** Implements the automation logic:
#        - **AC & Windows:** If the AC is on, close all windows using a loop.
#        - **AC & Temperature:** If the indoor temperature is below the threshold (`TEMP_LOW`) and the AC is on, turn off the AC.
#        - **Lights & Light Intensity:** Based on the light intensity readings, turn off lights if the intensity is too high or dim them if it's moderately high.
#        - **Music Player & TV (Placeholder):** This section is commented out as it requires a presence detection mechanism, which is not implemented in the provided code. 

# 3. **Logging:**
#    - The code includes `logger.info()` calls to log relevant actions, such as turning devices on/off.

# **To use this code:**

# 1. **Ensure you have the `home`, `sensor`, `actuator`, `config`, and `logger_config` modules properly defined and working in your project.**
# 2. **Replace the placeholder comments in the "Automatically turn off the music player and TV when people leave the house" section with your own logic for detecting presence or absence.**
# 3. **Run the `function.py` file.**

# **Remember:** This code provides a basic framework. You can expand it by adding more automation rules, integrating with different sensors and actuators, and implementing a robust presence detection mechanism.
