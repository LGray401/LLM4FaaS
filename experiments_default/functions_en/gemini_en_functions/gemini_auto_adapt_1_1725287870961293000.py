from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW

import time


def main():
    home = home_plan()

    # Example usage of functions:
    # Get the living room
    living_room = get_room(home, "LivingRoom")

    # Get all sensors in the living room
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get all lights in the home
    lights = get_all_actuators(home, "Light")

    # Turn on all lights
    for light in lights:
        light.turn_on()

    # Get all indoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Check temperature and adjust AC or heater
    for sensor in indoor_temp_sensors:
        temperature = sensor.get_reading()
        if temperature is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room is not None:
                heater = get_room_actuators(room, "Heater")[0]
                ac = get_room_actuators(room, "AC")[0]
                if temperature < TEMP_LOW:
                    print(f"Temperature in {room_name} is too low, turning on heater.")
                    heater.turn_on()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for the heater to warm up
                    heater.turn_off()
                elif temperature > TEMP_HIGH:
                    print(f"Temperature in {room_name} is too high, turning on AC.")
                    ac.turn_on()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for the AC to cool down
                    ac.turn_off()

    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Check humidity and adjust humidifier
    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room is not None:
                humidifier = get_room_actuators(room, "Humidifier")[0]
                if humidity < HUMIDITY_LOW:
                    print(f"Humidity in {room_name} is too low, turning on humidifier.")
                    humidifier.increase_humidity()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for the humidifier to increase humidity
                elif humidity > HUMIDITY_HIGH:
                    print(f"Humidity in {room_name} is too high, turning off humidifier.")
                    humidifier.decrease_humidity()
                    time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for the humidifier to decrease humidity

    # Get all light intensity sensors
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    # Check light intensity and adjust lights
    for sensor in light_intensity_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            room_name = sensor.room_name
            room = get_room(home, room_name)
            if room is not None:
                lights = get_room_actuators(room, "Light")
                for light in lights:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        print(f"Light intensity in {room_name} is too low, turning on lights.")
                        light.turn_on()
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        print(f"Light intensity in {room_name} is too high, turning off lights.")
                        light.turn_off()

    # Other smart home logic can be implemented here, such as:
    # - Controlling smart sockets based on usage patterns
    # - Playing music based on user preferences
    # - Sending notifications based on events

    # Example: Play music in the living room
    living_room_music_player = get_room_actuators(living_room, "MusicPlayer")[0]
    living_room_music_player.play_music("Relaxing Music")

    print("Smart home system running...")
    time.sleep(5)  # Simulate system running for 5 seconds

    # Clean up by turning off all lights
    for light in lights:
        light.turn_off()

    print("Smart home system shutting down.")


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Imports necessary modules from `home` package.
#    - Imports `time` for delays.

# 2. **`main()` function:**
#    - Creates a `home` object using `home_plan()`.
#    - **Example Usage:**
#      - Gets the `living_room` using `get_room()`.
#      - Gets `living_room_sensors` using `get_room_sensors()`.
#      - Gets all `lights` using `get_all_actuators()`.
#    - **Control Lights:**
#      - Turns on all lights.
#    - **Control Temperature:**
#      - Gets all `indoor_temp_sensors` using `get_all_sensors()`.
#      - Iterates through sensors, gets temperature readings, and adjusts `heater` or `ac` in the corresponding room based on the temperature.
#    - **Control Humidity:**
#      - Gets all `humidity_sensors` using `get_all_sensors()`.
#      - Iterates through sensors, gets humidity readings, and adjusts `humidifier` in the corresponding room based on the humidity.
#    - **Control Light Intensity:**
#      - Gets all `light_intensity_sensors` using `get_all_sensors()`.
#      - Iterates through sensors, gets light intensity readings, and adjusts lights in the corresponding room based on the intensity.
#    - **Play Music:**
#      - Gets the `living_room_music_player` and plays music.
#    - **Simulate System Running:**
#      - Prints a message and sleeps for 5 seconds.
#    - **Clean Up:**
#      - Turns off all lights.
#    - Prints a shutdown message.

# 3. **`if __name__ == "__main__":` Block:**
#    - Calls the `main()` function when the script is run directly.

# **Key Features:**

# - **Sensor and Actuator Management:**
#   - Uses functions from `home_plan.py` to access and manipulate sensors and actuators in different rooms.
# - **Temperature Control:**
#   - Adjusts `heater` or `ac` based on temperature thresholds in `config.py`.
# - **Humidity Control:**
#   - Adjusts `humidifier` based on humidity thresholds in `config.py`.
# - **Light Intensity Control:**
#   - Adjusts lights based on light intensity thresholds in `config.py`.
# - **Music Playback:**
#   - Plays music in the living room.
# - **Example Smart Home Logic:**
#   - Provides a framework for implementing more complex smart home logic.

# **To Run the Script:**

# 1. Make sure you have all the necessary files (from `home` package) in the same directory.
# 2. Run the `function.py` file from your terminal: `python function.py`
