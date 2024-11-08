from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION, TEMP_CHANGE_DURATION_WINDOW
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Curtain, CleaningRobot
import time

def energy_saving_function(home):
    """
    This function implements the energy saving function.
    It checks the temperature, humidity and light intensity in each room.
    If the temperature is too high or too low, it adjusts the AC or heater accordingly.
    If the humidity is too high or too low, it adjusts the humidifier or dehumidifier accordingly.
    If the light intensity is too high, it adjusts the curtains accordingly.
    It also schedules the cleaning robot to perform its daily routine.
    """

    print_home_plan(home)
    while True:
        for room_name in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom"]:
            room = get_room(home, room_name)
            if room is not None:
                # Check temperature and adjust AC or heater
                temperature_sensors = get_room_sensors(home, room_name)
                if temperature_sensors is not None:
                    for sensor in temperature_sensors:
                        if isinstance(sensor, IndoorTemperatureSensor):
                            temperature = sensor.get_reading()
                            if temperature is not None:
                                heaters = get_room_actuators(home, room_name, "Heater")
                                acs = get_room_actuators(home, room_name, "AC")
                                if heaters is not None:
                                    for heater in heaters:
                                        heater.set_target_temperature(TEMP_HIGH)
                                        heater.adjust_temperature(temperature)
                                if acs is not None:
                                    for ac in acs:
                                        ac.set_target_temperature(TEMP_LOW)
                                        ac.adjust_temperature(temperature)

                # Check humidity and adjust humidifier or dehumidifier
                humidity_sensors = get_room_sensors(home, room_name)
                if humidity_sensors is not None:
                    for sensor in humidity_sensors:
                        if isinstance(sensor, HumiditySensor):
                            humidity = sensor.get_reading()
                            if humidity is not None:
                                # TODO: Add humidifier and dehumidifier actuators and adjust them based on humidity
                                pass

                # Check light intensity and adjust curtains
                light_intensity_sensors = get_room_sensors(home, room_name)
                if light_intensity_sensors is not None:
                    for sensor in light_intensity_sensors:
                        if isinstance(sensor, LightIntensiveSensor):
                            light_intensity = sensor.get_reading()
                            if light_intensity is not None:
                                curtains = get_room_actuators(home, room_name, "Curtain")
                                if curtains is not None:
                                    for curtain in curtains:
                                        if light_intensity > LIGHT_INTENSITY_HIGH:
                                            curtain.turn_on()
                                        else:
                                            curtain.turn_off()

        # Schedule cleaning robot daily routine
        cleaning_robots = get_all_actuators(home, "CleaningRobot")
        if cleaning_robots is not None:
            for cleaning_robot in cleaning_robots:
                if cleaning_robot.get_status() == "off":
                    cleaning_robot.turn_on()
                    cleaning_robot.daily_routine()

        # Wait for some time before checking again
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    home = home_plan()
    energy_saving_function(home)

# **Explanation:**

# 1. **Imports:** Imports necessary classes and constants from `home_plan`, `config`, `sensor`, and `actuator`.
# 2. **`energy_saving_function`:** This function implements the core logic of the energy-saving system. It iterates through each room in the `home` object:
#    - **Temperature:**
#      - Retrieves temperature sensors in the room.
#      - If a temperature sensor is found, it gets the current temperature reading.
#      - Adjusts the heater or AC based on the target temperature and the current temperature.
#    - **Humidity:**
#      - Retrieves humidity sensors in the room.
#      - If a humidity sensor is found, it gets the current humidity reading.
#      - **(TODO):** Placeholder for adjusting humidifier or dehumidifier based on the humidity.
#    - **Light Intensity:**
#      - Retrieves light intensity sensors in the room.
#      - If a light intensity sensor is found, it gets the current light intensity reading.
#      - Adjusts the curtains based on the light intensity.
#    - **Cleaning Robot:**
#      - Retrieves all cleaning robots in the home.
#      - If any cleaning robot is off, it turns it on and starts its daily routine.
# 3. **Sleep:** The function waits for `TEMP_CHANGE_DURATION_WINDOW` seconds before checking the conditions again.
# 4. **Main Execution:**
#    - Calls `home_plan()` to create the `home` object.
#    - Starts the `energy_saving_function` to run the energy-saving system.

# **Additional Notes:**

# - **Placeholder for Humidity:** The humidity control logic is commented out as a placeholder. You need to add:
#     - **Actuators:** Implement `Humidifier` and `Dehumidifier` actuators.
#     - **Logic:** Add code to adjust the humidifier or dehumidifier based on the humidity reading and thresholds.
# - **Error Handling:** Consider adding error handling to catch potential issues with sensor readings, actuator controls, or other unexpected situations.

# This is a basic implementation of the energy-saving function. You can customize it by adding more features, optimizing the logic, and integrating with real-world devices.
