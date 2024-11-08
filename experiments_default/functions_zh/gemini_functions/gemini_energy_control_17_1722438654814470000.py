from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import Heater, AC, Light, CleaningRobot, NotificationSender, MusicPlayer, SmartTV, \
    Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
import time


def energy_saving_mode(home):
    """
    Implements energy-saving mode for the smart home.

    This function analyzes sensor data and adjusts actuators to optimize energy consumption.
    """
    print("\nStarting Energy Saving Mode...")

    # 1. Temperature Control
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for indoor_temp_sensor in indoor_temp_sensors:
        indoor_temp_reading = indoor_temp_sensor.get_reading()
        if indoor_temp_reading is not None:
            if indoor_temp_reading < TEMP_LOW:
                print(f"Indoor temperature is below {TEMP_LOW}°C, turning on heater...")
                # Find the heater in the same room as the sensor
                room = get_room(home, indoor_temp_sensor.room_name)
                heater = None
                if room is not None:
                    heater = next(
                        (actor for actor in room.actuators if isinstance(actor, Heater)), None
                    )
                if heater is not None:
                    heater.turn_on()
                else:
                    print(f"No heater found in {indoor_temp_sensor.room_name}")

            elif indoor_temp_reading > TEMP_HIGH:
                print(f"Indoor temperature is above {TEMP_HIGH}°C, turning on AC...")
                # Find the AC in the same room as the sensor
                room = get_room(home, indoor_temp_sensor.room_name)
                ac = None
                if room is not None:
                    ac = next((actor for actor in room.actuators if isinstance(actor, AC)), None)
                if ac is not None:
                    ac.turn_on()
                else:
                    print(f"No AC found in {indoor_temp_sensor.room_name}")

    for outdoor_temp_sensor in outdoor_temp_sensors:
        outdoor_temp_reading = outdoor_temp_sensor.get_reading()
        if outdoor_temp_reading is not None:
            # Adjust AC based on outdoor temperature
            if outdoor_temp_reading < TEMP_LOW:
                print(f"Outdoor temperature is below {TEMP_LOW}°C, adjusting AC to higher temperature...")
                for ac in acs:
                    ac.set_target_temperature(TEMP_HIGH + 2)
            elif outdoor_temp_reading > TEMP_HIGH:
                print(f"Outdoor temperature is above {TEMP_HIGH}°C, adjusting AC to lower temperature...")
                for ac in acs:
                    ac.set_target_temperature(TEMP_HIGH - 2)

    # 2. Humidity Control
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for humidity_sensor in humidity_sensors:
        humidity_reading = humidity_sensor.get_reading()
        if humidity_reading is not None:
            if humidity_reading < HUMIDITY_LOW:
                print(f"Humidity is below {HUMIDITY_LOW}%, turning on humidifier...")
                room = get_room(home, humidity_sensor.room_name)
                humidifier = None
                if room is not None:
                    humidifier = next(
                        (actor for actor in room.actuators if isinstance(actor, Humidifier)), None
                    )
                if humidifier is not None:
                    humidifier.increase_humidity()
                else:
                    print(f"No humidifier found in {humidity_sensor.room_name}")
            elif humidity_reading > HUMIDITY_HIGH:
                print(f"Humidity is above {HUMIDITY_HIGH}%, turning off humidifier...")
                room = get_room(home, humidity_sensor.room_name)
                humidifier = None
                if room is not None:
                    humidifier = next(
                        (actor for actor in room.actuators if isinstance(actor, Humidifier)), None
                    )
                if humidifier is not None:
                    humidifier.decrease_humidity()
                else:
                    print(f"No humidifier found in {humidity_sensor.room_name}")

    # 3. Light Control
    light_intensive_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for light_intensive_sensor in light_intensive_sensors:
        light_intensity_reading = light_intensive_sensor.get_reading()
        if light_intensity_reading is not None:
            if light_intensity_reading < LIGHT_INTENSITY_LOW:
                print(f"Light intensity is below {LIGHT_INTENSITY_LOW} lux, turning on lights...")
                room = get_room(home, light_intensive_sensor.room_name)
                light = None
                if room is not None:
                    light = next((actor for actor in room.actuators if isinstance(actor, Light)), None)
                if light is not None:
                    light.turn_on()
                else:
                    print(f"No light found in {light_intensive_sensor.room_name}")
            elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                print(f"Light intensity is above {LIGHT_INTENSITY_HIGH} lux, turning off lights...")
                room = get_room(home, light_intensive_sensor.room_name)
                light = None
                if room is not None:
                    light = next((actor for actor in room.actuators if isinstance(actor, Light)), None)
                if light is not None:
                    light.turn_off()
                else:
                    print(f"No light found in {light_intensive_sensor.room_name}")

    # 4. Cleaning Robot Control
    cleaning_robots = get_all_actuators(home, "CleaningRobot")
    for cleaning_robot in cleaning_robots:
        # Schedule daily routine for cleaning robot
        cleaning_robot.daily_routine()

    # 5. Smart TV Control
    smart_tvs = get_all_actuators(home, "SmartTV")
    for smart_tv in smart_tvs:
        # Example: Automatically switch to energy-saving mode if no one is watching
        # if no one is watching (e.g., no motion detected for a certain time):
        #     print("No one is watching TV, switching to energy-saving mode...")
        #     smart_tv.set_energy_saving_mode(True)

    # 6. Other Energy Saving Features
    # - Automatically turn off lights when rooms are empty
    # - Use timers to control appliances (e.g., turn off heater when leaving home)
    # - Optimize appliance settings (e.g., adjust washing machine water level)
    # - Encourage energy-efficient habits (e.g., notifications for using energy-saving modes)

    print("Energy saving mode completed.")


if __name__ == "__main__":
    home = home_plan()
    while True:
        energy_saving_mode(home)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

# **Explanation of the Code:**

# 1. **Imports:**
#    - Imports necessary modules from `home_plan`, `sensor`, `actuator`, and `config`.
#    - Imports `time` for sleep functionality.

# 2. **`energy_saving_mode(home)` Function:**
#    - This is the core function that implements energy-saving logic.
#    - It takes `home` (representing the home plan) as input.
#    - Prints a message indicating the start of energy-saving mode.

# 3. **Temperature Control:**
#    - Retrieves all `IndoorTemperatureSensor` and `OutdoorTemperatureSensor` objects.
#    - Retrieves all `Heater` and `AC` objects.
#    - Iterates through the temperature sensors:
#      - Gets the current temperature reading.
#      - If the temperature is below `TEMP_LOW`, turns on the heater in the same room.
#      - If the temperature is above `TEMP_HIGH`, turns on the AC in the same room.
#    - Iterates through the outdoor temperature sensors:
#      - Gets the current outdoor temperature reading.
#      - Adjusts the target temperature of ACs based on the outdoor temperature.

# 4. **Humidity Control:**
#    - Retrieves all `HumiditySensor` and `Humidifier` objects.
#    - Iterates through humidity sensors:
#      - Gets the current humidity reading.
#      - If humidity is below `HUMIDITY_LOW`, turns on the humidifier in the same room.
#      - If humidity is above `HUMIDITY_HIGH`, turns off the humidifier in the same room.

# 5. **Light Control:**
#    - Retrieves all `LightIntensiveSensor` and `Light` objects.
#    - Iterates through light intensity sensors:
#      - Gets the current light intensity reading.
#      - If light intensity is below `LIGHT_INTENSITY_LOW`, turns on the light in the same room.
#      - If light intensity is above `LIGHT_INTENSITY_HIGH`, turns off the light in the same room.

# 6. **Cleaning Robot Control:**
#    - Retrieves all `CleaningRobot` objects.
#    - Calls the `daily_routine()` method for each cleaning robot to initiate daily cleaning.

# 7. **Smart TV Control (Example):**
#    - Retrieves all `SmartTV` objects.
#    - Provides an example of switching to energy-saving mode on the TV if no one is watching. This section needs further implementation based on how you detect if someone is watching TV.

# 8. **Other Energy Saving Features:**
#    - Lists other potential energy-saving features that you can implement:
#      - Automatically turning off lights when rooms are empty (requires presence detection).
#      - Using timers to control appliances.
#      - Optimizing appliance settings.
#      - Providing notifications for energy-saving modes.

# 9. **Loop and Sleep:**
#    - The `while True` loop ensures that energy-saving mode runs continuously.
#    - `time.sleep(TEMP_CHANGE_DURATION_WINDOW)` pauses execution for the specified duration before checking sensor readings and adjusting actuators again.

# **Key Considerations for Implementation:**

# - **Presence Detection:** To implement features like turning off lights when rooms are empty, you'll need to integrate some form of presence detection (e.g., motion sensors, occupancy sensors).
# - **Timer Control:** You can use libraries like `schedule` to schedule tasks like turning off heaters or appliances at specific times.
# - **Notifications:** Consider how you want to communicate energy-saving recommendations to users (e.g., using a smart home hub, app notifications).

# This code provides a foundation for implementing energy-saving mode in your smart home project. You can adapt and expand it to include additional features and functionality based on your specific requirements.
