import time
from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_actuators, \
    get_all_sensors
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger


def main():
    home = home_plan()  # Create the home plan

    # Example usage:
    # open the window in living room
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        for actuator in living_room.actuators:
            if isinstance(actuator, Window):
                actuator.turn_on()
                print(f"{actuator.id} is now on")
                logger.info(f"{actuator.id} is turned on")
                break

    # Turn on the light in the bedroom to medium brightness
    bedroom = get_room(home, "Bedroom")
    if bedroom is not None:
        for actuator in bedroom.actuators:
            if isinstance(actuator, Light):
                actuator.turn_on()
                actuator.set_brightness_level("medium")
                break

    # Play music in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        for actuator in living_room.actuators:
            if isinstance(actuator, MusicPlayer):
                actuator.turn_on()
                actuator.play_music("Relaxing Music")
                break

    # Make coffee in the kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen is not None:
        for actuator in kitchen.actuators:
            if isinstance(actuator, CoffeeMachine):
                actuator.turn_on()
                actuator.make_coffee("Espresso")
                break

    # Turn on the AC in the living room to 22 degrees Celsius
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        for actuator in living_room.actuators:
            if isinstance(actuator, AC):
                actuator.turn_on()
                actuator.set_target_temperature(22)
                break

    # Close the curtains in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        for actuator in living_room.actuators:
            if isinstance(actuator, Curtain):
                actuator.turn_off()
                break

    # Start the cleaning robot in the living room
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        for actuator in living_room.actuators:
            if isinstance(actuator, CleaningRobot):
                actuator.turn_on()
                actuator.daily_routine()
                break

    # Automatic temperature and humidity control:
    while True:
        # Check all indoor temperature sensors
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in indoor_temp_sensors:
            temp_reading = sensor.get_reading()
            if temp_reading is not None:
                room_name = sensor.room_name
                # Get the heater and AC in the room
                room = get_room(home, room_name)
                if room is not None:
                    heater = get_all_actuators(home, "Heater")[0]
                    ac = get_all_actuators(home, "AC")[0]
                    if heater is not None and ac is not None:
                        if temp_reading < TEMP_LOW:
                            heater.turn_on()
                            heater.set_target_temperature(TEMP_LOW + 1)
                            ac.turn_off()
                            print(f"Heater in {room_name} turned ON to {TEMP_LOW + 1}°C.")
                            logger.info(f"Heater in {room_name} turned ON to {TEMP_LOW + 1}°C.")
                        elif temp_reading > TEMP_HIGH:
                            ac.turn_on()
                            ac.set_target_temperature(TEMP_HIGH - 1)
                            heater.turn_off()
                            print(f"AC in {room_name} turned ON to {TEMP_HIGH - 1}°C.")
                            logger.info(f"AC in {room_name} turned ON to {TEMP_HIGH - 1}°C.")
                        else:
                            heater.turn_off()
                            ac.turn_off()
                            print(f"Both heater and AC in {room_name} turned OFF.")
                            logger.info(f"Both heater and AC in {room_name} turned OFF.")

        # Check all humidity sensors
        humidity_sensors = get_all_sensors(home, "Humidity")
        for sensor in humidity_sensors:
            humidity_reading = sensor.get_reading()
            if humidity_reading is not None:
                room_name = sensor.room_name
                # Get the humidifier in the room
                room = get_room(home, room_name)
                if room is not None:
                    humidifier = get_all_actuators(home, "Humidifier")[0]
                    if humidifier is not None:
                        if humidity_reading < HUMIDITY_LOW:
                            humidifier.increase_humidity()
                            print(f"Humidifier in {room_name} is increasing humidity.")
                            logger.info(f"Humidifier in {room_name} is increasing humidity.")
                        elif humidity_reading > HUMIDITY_HIGH:
                            humidifier.decrease_humidity()
                            print(f"Humidifier in {room_name} is decreasing humidity.")
                            logger.info(f"Humidifier in {room_name} is decreasing humidity.")

        # Check all light intensive sensors
        light_intensive_sensors = get_all_sensors(home, "LightIntensive")
        for sensor in light_intensive_sensors:
            light_intensity_reading = sensor.get_reading()
            if light_intensity_reading is not None:
                room_name = sensor.room_name
                # Get the light in the room
                room = get_room(home, room_name)
                if room is not None:
                    light = get_all_actuators(home, "Light")[0]
                    if light is not None:
                        if light_intensity_reading < LIGHT_INTENSITY_LOW:
                            light.turn_on()
                            light.set_brightness_level("high")
                            print(f"Light in {room_name} turned ON to high brightness.")
                            logger.info(f"Light in {room_name} turned ON to high brightness.")
                        elif light_intensity_reading > LIGHT_INTENSITY_HIGH:
                            light.turn_off()
                            print(f"Light in {room_name} turned OFF.")
                            logger.info(f"Light in {room_name} turned OFF.")

        # Simulate a slow change in temperature
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** Import necessary modules from `home` package.
# 2. **`main()` Function:**
#     - Creates the `home` object using `home_plan()`.
#     - Provides example usage for interacting with sensors and actuators.
#     - Implements a loop for automatic temperature and humidity control:
#         - Retrieves all sensors of a specific type using `get_all_sensors()`.
#         - Gets readings from each sensor and checks if they are within the defined thresholds.
#         - If necessary, turns on/off actuators like heaters, ACs, and humidifiers to adjust the environment.
#         - Simulates a slow change in temperature using `time.sleep()`.

# 3. **Automatic Control:**
#     - **Temperature:** The code checks indoor temperature sensors, and based on readings:
#         - If temperature is below `TEMP_LOW`, it turns on the heater to a target temperature slightly above `TEMP_LOW`.
#         - If temperature is above `TEMP_HIGH`, it turns on the AC to a target temperature slightly below `TEMP_HIGH`.
#         - If temperature is within the range, both heater and AC are turned off.
#     - **Humidity:** The code checks humidity sensors and:
#         - If humidity is below `HUMIDITY_LOW`, it increases humidity using the humidifier.
#         - If humidity is above `HUMIDITY_HIGH`, it decreases humidity using the humidifier.
#     - **Light Intensity:** The code checks light intensive sensors and:
#         - If light intensity is below `LIGHT_INTENSITY_LOW`, it turns on the light to high brightness.
#         - If light intensity is above `LIGHT_INTENSITY_HIGH`, it turns off the light.

# 4. **`if __name__ == "__main__":` Block:** Calls the `main()` function to run the code when the script is executed directly.

# This script showcases a basic implementation of how to use sensors and actuators to create a smart home system. You can expand upon this by adding more features, like voice control, scheduling, and more advanced control logic based on your project requirements.
