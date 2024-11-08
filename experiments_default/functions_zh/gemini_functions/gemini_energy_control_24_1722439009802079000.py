from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, Curtain, AC
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def energy_saving_mode():
    home = home_plan()

    # Get all indoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all outdoor temperature sensors
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")

    # Get all light intensity sensors
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")

    # Get all windows
    windows = get_all_actuators(home, "Window")

    # Get all curtains
    curtains = get_all_actuators(home, "Curtain")

    # Get all AC units
    ac_units = get_all_actuators(home, "AC")

    # Loop through each room and apply energy-saving logic
    for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
        # Get the current indoor temperature
        indoor_temp = None
        for sensor in indoor_temp_sensors:
            if sensor.room_name == room_name:
                indoor_temp = sensor.get_reading()
                break

        # Get the current outdoor temperature
        outdoor_temp = None
        for sensor in outdoor_temp_sensors:
            if sensor.room_name == room_name:
                outdoor_temp = sensor.get_reading()
                break

        # Get the current light intensity
        light_intensity = None
        for sensor in light_intensive_sensors:
            if sensor.room_name == room_name:
                light_intensity = sensor.get_reading()
                break

        # Get the room's windows and curtains
        room_windows = []
        room_curtains = []
        for window in windows:
            if window.room_name == room_name:
                room_windows.append(window)
        for curtain in curtains:
            if curtain.room_name == room_name:
                room_curtains.append(curtain)

        # Get the room's AC unit
        room_ac = None
        for ac in ac_units:
            if ac.room_name == room_name:
                room_ac = ac
                break

        # Energy-saving logic
        if indoor_temp is not None and outdoor_temp is not None:
            # 降温1
            if outdoor_temp < indoor_temp:
                # Open the windows
                for window in room_windows:
                    window.turn_on()
                logger.info(f"Open windows in {room_name} as outdoor temperature is lower than indoor temperature.")
            # 降温2
            elif indoor_temp < outdoor_temp and light_intensity > LIGHT_INTENSITY_HIGH:
                # Close the curtains
                for curtain in room_curtains:
                    curtain.turn_on()
                logger.info(f"Close curtains in {room_name} as indoor temperature is lower than outdoor temperature and light intensity is high.")
            # Adjust AC temperature
            if room_ac is not None:
                if indoor_temp > TEMP_HIGH:
                    room_ac.set_target_temperature(TEMP_HIGH)
                    logger.info(f"Set AC target temperature to {TEMP_HIGH}°C in {room_name} as indoor temperature is higher than {TEMP_HIGH}°C.")
                elif indoor_temp < TEMP_LOW:
                    room_ac.set_target_temperature(TEMP_LOW)
                    logger.info(f"Set AC target temperature to {TEMP_LOW}°C in {room_name} as indoor temperature is lower than {TEMP_LOW}°C.")

# Main function
if __name__ == "__main__":
    energy_saving_mode()

# This file defines a `energy_saving_mode` function that implements the logic described in the functional description. Here's a breakdown of the code:

# 1. **Imports:** It imports necessary modules like `home_plan`, `sensor`, `actuator`, `config`, and `logger_config`.
# 2. **`energy_saving_mode` function:**
#    - **Gets room data:** It gets all the sensors and actuators from the `home_plan` using helper functions from `home_plan.py`.
#    - **Iterates through rooms:** It loops through the rooms defined in the `home_plan` to apply the energy-saving logic.
#    - **Reads sensor data:** It reads the current indoor, outdoor temperatures, and light intensity for each room.
#    - **Applies logic:** 
#       - **降温1:** If the outdoor temperature is lower than the indoor temperature, it opens the windows in the room.
#       - **降温2:** If the indoor temperature is lower than the outdoor temperature and light intensity is high, it closes the curtains in the room.
#       - **AC adjustment:** If the room has an AC unit, it adjusts the target temperature based on the indoor temperature and thresholds defined in `config.py`.
# 3. **Main function:** If the script is run directly, it calls the `energy_saving_mode` function.

# This file uses the data from `home_plan.py`, `sensor.py`, and `actuator.py` to implement the logic. It leverages the thresholds defined in `config.py` to control the actuators based on the sensor readings. The `logger_config` module is used for logging relevant information.
