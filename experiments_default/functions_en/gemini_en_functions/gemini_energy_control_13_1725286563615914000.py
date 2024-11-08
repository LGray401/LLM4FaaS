from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import Light, AC, Heater, Window, Door, Curtain, CoffeeMachine, CleaningRobot, NotificationSender, \
    MusicPlayer, SmartSocket, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time

# create home plan
home = home_plan()


def turn_off_lights_when_no_one_in_room(room_name):
    # get all light in the room
    lights = get_room_actuators(home, room_name)
    lights = [l for l in lights if isinstance(l, Light)]
    if lights:
        # get all light intensive sensor in the room
        light_intensive_sensors = get_room_sensors(home, room_name)
        light_intensive_sensors = [l for l in light_intensive_sensors if isinstance(l, LightIntensiveSensor)]
        if light_intensive_sensors:
            for sensor in light_intensive_sensors:
                reading = sensor.get_reading()
                if reading is not None and reading < LIGHT_INTENSITY_LOW:
                    print(f"Light intensity in {room_name} is low, turning off lights.")
                    for light in lights:
                        light.turn_off()
                else:
                    print(f"Light intensity in {room_name} is high, keeping lights on.")
        else:
            print(f"No Light Intensive sensor found in {room_name}, can't control lights.")


def turn_off_sockets_when_not_in_use(room_name):
    # get all SmartSocket in the room
    smart_sockets = get_room_actuators(home, room_name)
    smart_sockets = [s for s in smart_sockets if isinstance(s, SmartSocket)]
    if smart_sockets:
        # get all light intensive sensor in the room
        light_intensive_sensors = get_room_sensors(home, room_name)
        light_intensive_sensors = [l for l in light_intensive_sensors if isinstance(l, LightIntensiveSensor)]
        if light_intensive_sensors:
            for sensor in light_intensive_sensors:
                reading = sensor.get_reading()
                if reading is not None and reading < LIGHT_INTENSITY_LOW:
                    print(f"Light intensity in {room_name} is low, turning off smart sockets.")
                    for socket in smart_sockets:
                        socket.turn_off()
                else:
                    print(f"Light intensity in {room_name} is high, keeping smart sockets on.")
        else:
            print(f"No Light Intensive sensor found in {room_name}, can't control smart sockets.")


def adjust_heating_based_on_temperature(room_name):
    # get all heaters in the room
    heaters = get_room_actuators(home, room_name)
    heaters = [h for h in heaters if isinstance(h, Heater)]
    if heaters:
        # get all indoor temperature sensors in the room
        indoor_temp_sensors = get_room_sensors(home, room_name)
        indoor_temp_sensors = [t for t in indoor_temp_sensors if isinstance(t, IndoorTemperatureSensor)]
        if indoor_temp_sensors:
            for sensor in indoor_temp_sensors:
                reading = sensor.get_reading()
                if reading is not None:
                    for heater in heaters:
                        heater.adjust_temperature(reading)
                        if reading < TEMP_LOW:
                            print(f"Temperature in {room_name} is low, turning on heater.")
                            heater.turn_on()
                        else:
                            print(f"Temperature in {room_name} is above {TEMP_LOW}C, keeping heater off.")
                            heater.turn_off()
        else:
            print(f"No Indoor Temperature sensor found in {room_name}, can't control heater.")


def adjust_ac_based_on_temperature(room_name):
    # get all ACs in the room
    acs = get_room_actuators(home, room_name)
    acs = [a for a in acs if isinstance(a, AC)]
    if acs:
        # get all indoor temperature sensors in the room
        indoor_temp_sensors = get_room_sensors(home, room_name)
        indoor_temp_sensors = [t for t in indoor_temp_sensors if isinstance(t, IndoorTemperatureSensor)]
        if indoor_temp_sensors:
            for sensor in indoor_temp_sensors:
                reading = sensor.get_reading()
                if reading is not None:
                    for ac in acs:
                        ac.adjust_temperature(reading)
                        if reading > TEMP_HIGH:
                            print(f"Temperature in {room_name} is high, turning on AC.")
                            ac.turn_on()
                        else:
                            print(f"Temperature in {room_name} is below {TEMP_HIGH}C, keeping AC off.")
                            ac.turn_off()
        else:
            print(f"No Indoor Temperature sensor found in {room_name}, can't control AC.")


def adjust_ac_based_on_window_status(room_name):
    # get all ACs in the room
    acs = get_room_actuators(home, room_name)
    acs = [a for a in acs if isinstance(a, AC)]
    if acs:
        # get all windows in the room
        windows = get_room_actuators(home, room_name)
        windows = [w for w in windows if isinstance(w, Window)]
        if windows:
            for window in windows:
                if window.status == "on":
                    print(f"Window in {room_name} is open, turning off AC.")
                    for ac in acs:
                        ac.turn_off()
                else:
                    print(f"Window in {room_name} is closed, keeping AC status as it is.")
        else:
            print(f"No Window found in {room_name}, can't control AC based on window status.")


def adjust_ventilation_based_on_temperature(room_name):
    # get all windows in the room
    windows = get_room_actuators(home, room_name)
    windows = [w for w in windows if isinstance(w, Window)]
    if windows:
        # get all indoor temperature sensors in the room
        indoor_temp_sensors = get_room_sensors(home, room_name)
        indoor_temp_sensors = [t for t in indoor_temp_sensors if isinstance(t, IndoorTemperatureSensor)]
        if indoor_temp_sensors:
            for sensor in indoor_temp_sensors:
                reading = sensor.get_reading()
                if reading is not None:
                    for window in windows:
                        if reading > TEMP_HIGH:
                            print(f"Temperature in {room_name} is high, opening windows for ventilation.")
                            window.turn_on()
                        else:
                            print(f"Temperature in {room_name} is below {TEMP_HIGH}C, keeping windows closed.")
                            window.turn_off()
        else:
            print(f"No Indoor Temperature sensor found in {room_name}, can't control window ventilation.")


def close_windows_before_turning_on_ac(room_name):
    # get all ACs in the room
    acs = get_room_actuators(home, room_name)
    acs = [a for a in acs if isinstance(a, AC)]
    if acs:
        # get all windows in the room
        windows = get_room_actuators(home, room_name)
        windows = [w for w in windows if isinstance(w, Window)]
        if windows:
            for ac in acs:
                if ac.status == "on":
                    print(f"AC in {room_name} is on, closing all windows.")
                    for window in windows:
                        window.turn_off()
                else:
                    print(f"AC in {room_name} is off, keeping windows status as it is.")
        else:
            print(f"No Window found in {room_name}, can't control windows based on AC status.")


def adjust_humidity_based_on_humidity(room_name):
    # get all Humidifiers in the room
    humidifiers = get_room_actuators(home, room_name)
    humidifiers = [h for h in humidifiers if isinstance(h, Humidifier)]
    if humidifiers:
        # get all humidity sensors in the room
        humidity_sensors = get_room_sensors(home, room_name)
        humidity_sensors = [h for h in humidity_sensors if isinstance(h, HumiditySensor)]
        if humidity_sensors:
            for sensor in humidity_sensors:
                reading = sensor.get_reading()
                if reading is not None:
                    for humidifier in humidifiers:
                        if reading < HUMIDITY_LOW:
                            print(f"Humidity in {room_name} is low, increasing humidity.")
                            humidifier.increase_humidity()
                        elif reading > HUMIDITY_HIGH:
                            print(f"Humidity in {room_name} is high, decreasing humidity.")
                            humidifier.decrease_humidity()
                        else:
                            print(f"Humidity in {room_name} is within desired range, keeping humidity as it is.")
        else:
            print(f"No Humidity sensor found in {room_name}, can't control humidifier.")


def daily_cleaning_routine(room_name):
    # get cleaning robot in the room
    cleaning_robots = get_room_actuators(home, room_name)
    cleaning_robots = [c for c in cleaning_robots if isinstance(c, CleaningRobot)]
    if cleaning_robots:
        for robot in cleaning_robots:
            robot.daily_routine()
    else:
        print(f"No Cleaning Robot found in {room_name}, can't start cleaning routine.")


def main():
    while True:
        # Home Automation Functions
        turn_off_lights_when_no_one_in_room("LivingRoom")
        turn_off_sockets_when_not_in_use("LivingRoom")
        adjust_heating_based_on_temperature("LivingRoom")
        adjust_ac_based_on_temperature("LivingRoom")
        adjust_ac_based_on_window_status("LivingRoom")
        adjust_ventilation_based_on_temperature("LivingRoom")
        close_windows_before_turning_on_ac("LivingRoom")
        adjust_humidity_based_on_humidity("LivingRoom")
        daily_cleaning_routine("LivingRoom")

        # Add more automation functions here as needed

        # Wait for a short period before checking again
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Imports necessary modules from `home` package (home_plan, sensor, actuator, config).
#    - Imports `time` for sleep function.

# 2. **Global Variable:**
#    - `home`: A global variable representing the `home_plan` object created from the `home_plan` function.

# 3. **Functions:**
#    - **`turn_off_lights_when_no_one_in_room(room_name)`:**
#      - Gets all `Light` actuators in the specified room.
#      - Gets all `LightIntensiveSensor` sensors in the room.
#      - If both are found:
#        - Reads light intensity from the sensors.
#        - If intensity is below the `LIGHT_INTENSITY_LOW` threshold, turn off all lights in the room.
#    - **`turn_off_sockets_when_not_in_use(room_name)`:**
#      - Similar logic to `turn_off_lights_when_no_one_in_room`, but operates on `SmartSocket` actuators.
#    - **`adjust_heating_based_on_temperature(room_name)`:**
#      - Gets all `Heater` actuators in the room.
#      - Gets all `IndoorTemperatureSensor` sensors in the room.
#      - If both are found:
#        - Reads temperature from the sensors.
#        - If temperature is below `TEMP_LOW`, turn on the heater.
#        - If temperature is above `TEMP_LOW`, turn off the heater.
#    - **`adjust_ac_based_on_temperature(room_name)`:**
#      - Similar logic to `adjust_heating_based_on_temperature`, but operates on `AC` actuators and checks if the temperature is above `TEMP_HIGH`.
#    - **`adjust_ac_based_on_window_status(room_name)`:**
#      - Gets all `AC` actuators and `Window` actuators in the room.
#      - If a window is open, turn off the AC.
#    - **`adjust_ventilation_based_on_temperature(room_name)`:**
#      - Gets all `Window` actuators and `IndoorTemperatureSensor` sensors in the room.
#      - If temperature is above `TEMP_HIGH`, open the windows for ventilation.
#      - If temperature is below `TEMP_HIGH`, keep the windows closed.
#    - **`close_windows_before_turning_on_ac(room_name)`:**
#      - Gets all `AC` and `Window` actuators in the room.
#      - If the AC is on, close all windows.
#    - **`adjust_humidity_based_on_humidity(room_name)`:**
#      - Gets all `Humidifier` actuators and `HumiditySensor` sensors in the room.
#      - If humidity is below `HUMIDITY_LOW`, increase humidity.
#      - If humidity is above `HUMIDITY_HIGH`, decrease humidity.
#    - **`daily_cleaning_routine(room_name)`:**
#      - Gets all `CleaningRobot` actuators in the room.
#      - If found, start the robot's daily cleaning routine.

# 4. **`main()` Function:**
#    - Contains a loop that runs continuously:
#      - Calls all the automation functions defined above, focusing on the "LivingRoom" for now.
#      - Sleeps for a short duration defined by `TEMP_CHANGE_DURATION_WINDOW` before checking again.

# 5. **`if __name__ == "__main__":` Block:**
#    - Calls the `main()` function when the script is run directly.

# **Remember:**

# - Replace `"LivingRoom"` with other room names to apply the automation to different areas of your home.
# - Add more automation functions as per your project requirements.
# - Consider using a more robust scheduling mechanism instead of the simple `time.sleep` approach for better control over automation timings.
# - You can adjust the thresholds (`TEMP_LOW`, `TEMP_HIGH`, `HUMIDITY_LOW`, etc.) in the `config.py` file to fine-tune the automation behavior.
# - This code assumes sensors and actuators are working properly and provides basic logic. You might need additional error handling and communication logic for real-world implementation.
