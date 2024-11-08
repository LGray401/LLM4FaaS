from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import AC, Heater, CoffeeMachine, Light, Window, Curtain, MusicPlayer, CleaningRobot, NotificationSender, \
    SmartTV, SmartSocket, Door, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
import time
from home.logger_config import logger


def main():
    home = home_plan()
    # Example usage:
    # print_home_plan(home)

    # 1. Get sensors in "LivingRoom"
    living_room = get_room(home, "LivingRoom")
    if living_room is None:
        return
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # 2. Get all "IndoorTemperature" sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # 3. Get all "Light" actuators
    lights = get_all_actuators(home, "Light")
    # print(lights)

    # 4. Control room temperature
    for sensor in indoor_temp_sensors:
        temperature = sensor.get_reading()
        if temperature is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room is not None:
                for actuator in room.actuators:
                    if isinstance(actuator, Heater):
                        actuator.adjust_temperature(temperature)
                    elif isinstance(actuator, AC):
                        actuator.adjust_temperature(temperature)

    # 5. Control room humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room is not None:
                for actuator in room.actuators:
                    if isinstance(actuator, Humidifier):
                        if humidity < HUMIDITY_LOW:
                            actuator.increase_humidity()
                        elif humidity > HUMIDITY_HIGH:
                            actuator.decrease_humidity()

    # 6. Control room light intensity
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_intensity_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room is not None:
                for actuator in room.actuators:
                    if isinstance(actuator, Light):
                        if light_intensity < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()
                            actuator.set_brightness_level("high")
                        elif light_intensity > LIGHT_INTENSITY_HIGH:
                            actuator.set_brightness_level("low")

    # 7. Control window based on temperature
    # Get all "IndoorTemperature" sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        temperature = sensor.get_reading()
        if temperature is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room is not None:
                for actuator in room.actuators:
                    if isinstance(actuator, Window):
                        if temperature < TEMP_LOW:
                            actuator.turn_on()
                            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                            actuator.turn_off()
                        elif temperature > TEMP_HIGH:
                            actuator.turn_off()
                            time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                            actuator.turn_on()

    # 8. Control curtain based on time
    # Example: Close curtains in the evening
    current_hour = time.localtime().tm_hour
    if 18 <= current_hour <= 22:
        for room in home:
            for actuator in room.actuators:
                if isinstance(actuator, Curtain):
                    actuator.turn_off()

    # 9. Control music player based on time
    current_hour = time.localtime().tm_hour
    if 7 <= current_hour <= 9:
        for room in home:
            for actuator in room.actuators:
                if isinstance(actuator, MusicPlayer):
                    actuator.turn_on()
                    actuator.play_music("Morning Playlist")
                    time.sleep(30)
                    actuator.turn_off()
                    # TODO: need to check music player API

    # 10. Control Cleaning Robot based on time
    current_hour = time.localtime().tm_hour
    if current_hour == 10:
        for room in home:
            for actuator in room.actuators:
                if isinstance(actuator, CleaningRobot):
                    actuator.turn_on()
                    actuator.daily_routine()


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** Necessary imports are made from the `home` package, including `home_plan` (for home layout), `sensor` (for sensor classes), `actuator` (for actuator classes), and `config` (for configuration settings).
# 2. **`main()` Function:**
#    - This function is the entry point for the script.
#    - **Home Plan:** Creates the `home` structure using the `home_plan()` function.
#    - **Sensor and Actuator Access:** 
#       - Gets sensors and actuators using functions from `home_plan`.
#    - **Temperature Control:** 
#       - Retrieves readings from `IndoorTemperatureSensor`s.
#       - Adjusts `Heater` and `AC` based on the readings.
#    - **Humidity Control:**
#       - Retrieves readings from `HumiditySensor`s.
#       - Adjusts `Humidifier` based on the readings.
#    - **Light Intensity Control:**
#       - Retrieves readings from `LightIntensiveSensor`s.
#       - Adjusts `Light` brightness levels based on the readings.
#    - **Window Control:**
#       - Retrieves readings from `IndoorTemperatureSensor`s.
#       - Adjusts `Window` state (open/closed) based on the readings.
#    - **Curtain Control:**
#       - Controls curtains based on time.
#    - **Music Player Control:**
#       - Controls music player based on time.
#    - **Cleaning Robot Control:**
#       - Controls cleaning robot based on time.
# 3. **Conditional Logic:**
#    - The code includes `if` statements to control actuators based on time or sensor readings.
#    - This allows for more sophisticated control scenarios.
# 4. **Time Management:**
#    - `time.sleep()` is used to introduce delays into the control logic.
#    - This allows for more realistic control behavior.

# **To use this script:**

# 1. **Set up your `home` package:** Make sure your project has a `home` package with the files `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` as provided.
# 2. **Run `function.py`:** Execute the `function.py` script. The script will then interact with your smart home setup based on the logic defined within.

# **Key Points:**

# - **Modular Design:** The code is organized into functions and classes for better readability and maintainability.
# - **Configuration:** The `config.py` file allows you to easily adjust thresholds and time settings.
# - **Extensible:** The framework can be easily expanded to include additional sensors, actuators, and control logic.
# - **Realistic Simulation:** The use of `time.sleep()` provides a more realistic simulation of smart home behavior.
