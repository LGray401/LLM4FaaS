from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, AC, Heater, MusicPlayer, CleaningRobot, SmartTV, NotificationSender
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Initialize home plan
    home = home_plan()

    # Example usage of functions:
    # Get living room
    living_room = get_room(home, "LivingRoom")

    # Get all light sensors
    all_light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all lights
    all_lights = get_all_actuators(home, "Light")

    # Turn on all lights in living room
    if living_room is not None:
        living_room_lights = get_room_actuators(home, "LivingRoom")
        for light in living_room_lights:
            if isinstance(light, Light):
                light.turn_on()

    # Check temperature in living room
    living_room_temperature_sensors = get_room_sensors(home, "LivingRoom")
    for sensor in living_room_temperature_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature = sensor.get_reading()
            if temperature is not None:
                if temperature < TEMP_LOW:
                    print(f"The temperature in the living room is too low. Turning on the heater.")
                    living_room_heater = get_room_actuators(home, "LivingRoom")
                    for heater in living_room_heater:
                        if isinstance(heater, Heater):
                            heater.turn_on()
                elif temperature > TEMP_HIGH:
                    print(f"The temperature in the living room is too high. Turning on the AC.")
                    living_room_ac = get_room_actuators(home, "LivingRoom")
                    for ac in living_room_ac:
                        if isinstance(ac, AC):
                            ac.turn_on()

    # Check humidity in living room
    living_room_humidity_sensors = get_room_sensors(home, "LivingRoom")
    for sensor in living_room_humidity_sensors:
        if isinstance(sensor, HumiditySensor):
            humidity = sensor.get_reading()
            if humidity is not None:
                if humidity < HUMIDITY_LOW:
                    print(f"The humidity in the living room is too low. Consider using a humidifier.")
                    logger.info(f"The humidity in the living room is too low. Consider using a humidifier.")
                elif humidity > HUMIDITY_HIGH:
                    print(f"The humidity in the living room is too high. Consider opening a window for ventilation.")
                    logger.info(f"The humidity in the living room is too high. Consider opening a window for ventilation.")

    # Check light intensity in living room
    living_room_light_intensity_sensors = get_room_sensors(home, "LivingRoom")
    for sensor in living_room_light_intensity_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                if light_intensity < LIGHT_INTENSITY_LOW:
                    print(f"The light intensity in the living room is too low. Consider turning on a light.")
                    logger.info(f"The light intensity in the living room is too low. Consider turning on a light.")
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    print(f"The light intensity in the living room is too high. Consider adjusting the brightness.")
                    logger.info(f"The light intensity in the living room is too high. Consider adjusting the brightness.")

    # Start daily cleaning routine in living room
    if living_room is not None:
        living_room_cleaning_robots = get_room_actuators(home, "LivingRoom")
        for robot in living_room_cleaning_robots:
            if isinstance(robot, CleaningRobot):
                robot.daily_routine()

    # Play music in living room
    if living_room is not None:
        living_room_music_players = get_room_actuators(home, "LivingRoom")
        for player in living_room_music_players:
            if isinstance(player, MusicPlayer):
                player.play_music("Relaxing Music")

    # Turn on the TV in living room
    if living_room is not None:
        living_room_smart_tvs = get_room_actuators(home, "LivingRoom")
        for tv in living_room_smart_tvs:
            if isinstance(tv, SmartTV):
                tv.turn_on()
                tv.play_channel("News Channel")

    # Send a notification to all notification senders
    all_notification_senders = get_all_actuators(home, "NotificationSender")
    for sender in all_notification_senders:
        if isinstance(sender, NotificationSender):
            sender.notification_sender("Reminder: Don't forget to water the plants!")

    # Add more functionality as needed
    # ...

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:** 
#    - Import `home_plan` functions for working with rooms, sensors, and actuators.
#    - Import sensor and actuator classes from `home.sensor` and `home.actuator`.
#    - Import temperature, humidity, and light intensity thresholds from `home.config`.
#    - Import `logger` from `home.logger_config` for logging.

# 2. **`main()` function:**
#    - **Initialize home plan:**  `home = home_plan()`.
#    - **Get specific rooms and components:**
#      - `living_room = get_room(home, "LivingRoom")` gets the living room object.
#      - `all_light_sensors = get_all_sensors(home, "LightIntensive")` gets all light intensity sensors.
#      - `all_lights = get_all_actuators(home, "Light")` gets all light actuators.

#    - **Control devices:**
#      - **Turn on lights in the living room:**
#        - Get living room lights using `get_room_actuators`.
#        - Iterate through the lights and turn them on if they are `Light` instances.
#      - **Temperature control in the living room:**
#        - Get the living room temperature sensor.
#        - Read the temperature and adjust the heater or AC based on the temperature thresholds.
#      - **Humidity control in the living room:**
#        - Get the living room humidity sensor.
#        - Read the humidity and print messages suggesting actions based on the humidity thresholds.
#      - **Light intensity control in the living room:**
#        - Get the living room light intensity sensor.
#        - Read the light intensity and print messages suggesting actions based on the light intensity thresholds.
#      - **Start daily cleaning routine:**
#        - Get the cleaning robot in the living room.
#        - Start the daily cleaning routine if a cleaning robot is found.
#      - **Play music:**
#        - Get the music player in the living room.
#        - Play relaxing music if a music player is found.
#      - **Turn on the TV:**
#        - Get the SmartTV in the living room.
#        - Turn on the TV and play a news channel if a SmartTV is found.
#      - **Send notifications:**
#        - Get all notification senders.
#        - Send a notification to each sender.

#    - **Add more functionality as needed:**
#      - You can easily expand this function to implement more complex actions based on sensor readings and user commands.

# **How to Use:**

# 1. Make sure you have the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files in the `home` folder.
# 2. Create a `functions` folder and place this `function.py` file inside.
# 3. Run `python functions/function.py` to execute the script.

# This will provide a basic example of how to use your sensor and actuator classes to create a smart home system that can react to changes in the environment and control devices.
