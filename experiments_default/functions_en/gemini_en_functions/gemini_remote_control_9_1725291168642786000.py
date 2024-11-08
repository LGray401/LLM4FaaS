from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.logger_config import logger
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH

# Function to turn up the air conditioner
def turn_up_ac(room_name, target_temperature):
    room = get_room(home_plan(), room_name)
    if room is not None:
        acs = get_room_actuators(home_plan(), room_name)
        if acs is not None:
            for ac in acs:
                if ac.actuator_type == "AC":
                    ac.set_target_temperature(target_temperature)
                    print(f"Turned up the AC in {room_name} to {target_temperature}°C.")
                    logger.info(f"Turned up the AC in {room_name} to {target_temperature}°C.")
        else:
            print(f"No AC found in {room_name}.")
            logger.warning(f"No AC found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")

# Function to turn up the TV volume
def turn_up_tv_volume(room_name, volume_increase):
    room = get_room(home_plan(), room_name)
    if room is not None:
        tvs = get_room_actuators(home_plan(), room_name)
        if tvs is not None:
            for tv in tvs:
                if tv.actuator_type == "SmartTV":
                    # Assuming a TV has a volume property. 
                    # You'll need to add volume functionality to your SmartTV class.
                    # Replace this with your TV volume adjustment code
                    tv.volume += volume_increase
                    print(f"Turned up the TV volume in {room_name} by {volume_increase} degrees.")
                    logger.info(f"Turned up the TV volume in {room_name} by {volume_increase} degrees.")
        else:
            print(f"No TV found in {room_name}.")
            logger.warning(f"No TV found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")

# Function to heat the kettle
def heat_kettle(room_name, target_temperature):
    room = get_room(home_plan(), room_name)
    if room is not None:
        kettles = get_room_actuators(home_plan(), room_name)
        if kettles is not None:
            for kettle in kettles:
                if kettle.actuator_type == "SmartSocket":
                    # Assuming the kettle is connected to a SmartSocket. 
                    # You'll need to implement kettle functionality in your SmartSocket class.
                    # Replace this with your kettle heating logic
                    kettle.target_temperature = target_temperature
                    print(f"Heating the kettle in {room_name} to {target_temperature}°C.")
                    logger.info(f"Heating the kettle in {room_name} to {target_temperature}°C.")
        else:
            print(f"No kettle found in {room_name}.")
            logger.warning(f"No kettle found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")


def adjust_temperature(room_name):
    room = get_room(home_plan(), room_name)
    if room is not None:
        temp_sensors = get_room_sensors(home_plan(), room_name)
        if temp_sensors is not None:
            for sensor in temp_sensors:
                if sensor.sensor_type == "IndoorTemperature":
                    current_temperature = sensor.get_reading()
                    if current_temperature is not None:
                        acs = get_room_actuators(home_plan(), room_name)
                        if acs is not None:
                            for ac in acs:
                                if ac.actuator_type == "AC":
                                    ac.adjust_temperature(current_temperature)
                        heaters = get_room_actuators(home_plan(), room_name)
                        if heaters is not None:
                            for heater in heaters:
                                if heater.actuator_type == "Heater":
                                    heater.adjust_temperature(current_temperature)
        else:
            print(f"No Temperature Sensor found in {room_name}.")
            logger.warning(f"No Temperature Sensor found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")


def adjust_humidity(room_name):
    room = get_room(home_plan(), room_name)
    if room is not None:
        humidity_sensors = get_room_sensors(home_plan(), room_name)
        if humidity_sensors is not None:
            for sensor in humidity_sensors:
                if sensor.sensor_type == "Humidity":
                    current_humidity = sensor.get_reading()
                    if current_humidity is not None:
                        humidifiers = get_room_actuators(home_plan(), room_name)
                        if humidifiers is not None:
                            for humidifier in humidifiers:
                                if humidifier.actuator_type == "Humidifier":
                                    if current_humidity < HUMIDITY_LOW:
                                        humidifier.increase_humidity()
                                    elif current_humidity > HUMIDITY_HIGH:
                                        humidifier.decrease_humidity()
        else:
            print(f"No Humidity Sensor found in {room_name}.")
            logger.warning(f"No Humidity Sensor found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")


def adjust_light(room_name):
    room = get_room(home_plan(), room_name)
    if room is not None:
        light_sensors = get_room_sensors(home_plan(), room_name)
        if light_sensors is not None:
            for sensor in light_sensors:
                if sensor.sensor_type == "LightIntensive":
                    current_light_intensity = sensor.get_reading()
                    if current_light_intensity is not None:
                        lights = get_room_actuators(home_plan(), room_name)
                        if lights is not None:
                            for light in lights:
                                if light.actuator_type == "Light":
                                    if current_light_intensity < LIGHT_INTENSITY_LOW:
                                        light.turn_on()
                                        light.set_brightness_level("high")
                                    elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                                        light.turn_off()
        else:
            print(f"No Light Sensor found in {room_name}.")
            logger.warning(f"No Light Sensor found in {room_name}.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")


def main():
    home = home_plan()

    # Example usage:
    # Turn up the AC in the LivingRoom to 26°C
    turn_up_ac("LivingRoom", 26)

    # Turn up the TV volume in the LivingRoom by 3 degrees
    turn_up_tv_volume("LivingRoom", 3)

    # Heat the kettle in the Kitchen to 100°C
    heat_kettle("Kitchen", 100)

    # Example of adjusting temperature, humidity and light in different rooms
    while True:
        adjust_temperature("LivingRoom")
        adjust_temperature("Bedroom")
        adjust_temperature("Kitchen")
        adjust_temperature("Bathroom")

        adjust_humidity("LivingRoom")
        adjust_humidity("Bedroom")
        adjust_humidity("Kitchen")
        adjust_humidity("Bathroom")

        adjust_light("LivingRoom")
        adjust_light("Bedroom")
        adjust_light("Kitchen")
        adjust_light("Bathroom")

        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: This imports the functions for interacting with the home plan (rooms, sensors, actuators).
#    - `home.logger_config`: This imports the logger for logging information and events.
#    - `home.config`: This imports configuration settings like temperature thresholds, humidity thresholds, light intensity thresholds, and daily routine duration.

# 2. **Define functions for each command:**
#    - **`turn_up_ac(room_name, target_temperature)`:**
#      - Gets the room object using `get_room`.
#      - Gets the ACs in the room using `get_room_actuators`.
#      - Sets the target temperature of the AC using `ac.set_target_temperature`.
#    - **`turn_up_tv_volume(room_name, volume_increase)`:**
#      - Gets the room and TV objects similarly to the AC function.
#      - Increases the TV volume. You'll need to implement volume adjustment in your `SmartTV` class.
#    - **`heat_kettle(room_name, target_temperature)`:**
#      - Gets the room and SmartSocket objects (assuming the kettle is connected to it).
#      - Sets the target temperature for the kettle. You'll need to implement kettle functionality in your `SmartSocket` class.
#    - **`adjust_temperature(room_name)`:**
#      - Gets the room, temperature sensor, and AC/heater objects.
#      - Reads the current temperature.
#      - Turns on/off the AC or heater based on the target temperature (which should be set in another function like `turn_up_ac` or `heat_kettle`).
#    - **`adjust_humidity(room_name)`:**
#      - Gets the room, humidity sensor, and humidifier objects.
#      - Reads the current humidity.
#      - Increases/decreases humidity using the humidifier based on the thresholds defined in `home.config`.
#    - **`adjust_light(room_name)`:**
#      - Gets the room, light sensor, and light objects.
#      - Reads the current light intensity.
#      - Turns on/off the light and sets the brightness level based on the light intensity thresholds.

# 3. **`main()` function:**
#    - Creates the `home` object using `home_plan()`.
#    - Provides example calls to the functions to demonstrate their usage.
#    - The `while True` loop calls `adjust_temperature`, `adjust_humidity`, and `adjust_light` for each room continuously, simulating automatic environmental adjustments.

# **Important Notes:**

# - **Implement the missing functionality:** You'll need to implement volume adjustment for `SmartTV` and heating functionality for `SmartSocket` (to control the kettle) in your respective classes.
# - **Adjust configuration:** Customize the thresholds and other settings in `home.config` as needed for your specific smart home setup.
# - **Consider adding error handling:** The code currently assumes things will work correctly. You should add error handling to handle cases like:
#     - Not finding a room, sensor, or actuator.
#     - Unexpected values from sensors.
# - **Add other functionality:**  You can expand this by adding more functions to interact with other actuators and sensors in your smart home system.

# This provides a solid foundation for your smart home project. You can now build upon this by adding more specific commands, sensors, actuators, and logic to control your home environment.