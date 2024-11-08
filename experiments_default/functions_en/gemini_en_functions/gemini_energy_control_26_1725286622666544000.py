from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import AC, Window
from home.config import TEMP_HIGH
from home.logger_config import logger

def main():
    home = home_plan()
    
    while True:
        # Get the living room and bedroom
        living_room = get_room(home, "LivingRoom")
        bedroom = get_room(home, "Bedroom")

        # Check if the rooms exist
        if living_room and bedroom:
            # Get the temperature sensors in the living room and bedroom
            living_room_sensors = get_room_sensors(home, "LivingRoom")
            bedroom_sensors = get_room_sensors(home, "Bedroom")

            # Check if the sensors exist
            if living_room_sensors and bedroom_sensors:
                # Find the indoor temperature sensors in each room
                living_room_temp_sensor = None
                bedroom_temp_sensor = None
                for sensor in living_room_sensors:
                    if isinstance(sensor, IndoorTemperatureSensor):
                        living_room_temp_sensor = sensor
                        break

                for sensor in bedroom_sensors:
                    if isinstance(sensor, IndoorTemperatureSensor):
                        bedroom_temp_sensor = sensor
                        break

                # Check if the temperature sensors were found
                if living_room_temp_sensor and bedroom_temp_sensor:
                    # Get the indoor temperature readings
                    living_room_temp = living_room_temp_sensor.get_reading()
                    bedroom_temp = bedroom_temp_sensor.get_reading()

                    # Get the AC and window actuators in each room
                    living_room_actuators = get_room_actuators(home, "LivingRoom")
                    bedroom_actuators = get_room_actuators(home, "Bedroom")

                    # Check if the actuators exist
                    if living_room_actuators and bedroom_actuators:
                        living_room_ac = None
                        living_room_window = None
                        bedroom_ac = None
                        bedroom_window = None
                        for actuator in living_room_actuators:
                            if isinstance(actuator, AC):
                                living_room_ac = actuator
                            elif isinstance(actuator, Window):
                                living_room_window = actuator

                        for actuator in bedroom_actuators:
                            if isinstance(actuator, AC):
                                bedroom_ac = actuator
                            elif isinstance(actuator, Window):
                                bedroom_window = actuator

                        # Check if the AC and window actuators were found
                        if living_room_ac and living_room_window and bedroom_ac and bedroom_window:
                            # Logic for controlling the AC and windows
                            if living_room_ac.get_status() == "on" or bedroom_ac.get_status() == "on":
                                # Close the windows in both rooms
                                living_room_window.turn_off()
                                bedroom_window.turn_off()
                                logger.info(f"Closing the windows in the living room and bedroom")
                            elif living_room_temp > TEMP_HIGH or bedroom_temp > TEMP_HIGH:
                                # Open the windows in both rooms
                                living_room_window.turn_on()
                                bedroom_window.turn_on()
                                logger.info(f"Opening the windows in the living room and bedroom")
        # Wait for a short duration before checking again
        time.sleep(1)

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Import functions to manage the home plan and retrieve rooms, sensors, and actuators.
#    - `home.sensor`: Import the `IndoorTemperatureSensor` class to get temperature readings.
#    - `home.actuator`: Import the `AC` and `Window` classes to control air conditioning and windows.
#    - `home.config`: Import the `TEMP_HIGH` constant for temperature comparison.
#    - `home.logger_config`: Import the `logger` for logging messages.

# 2. **Define `main` function:**
#    - This function contains the main logic for controlling the smart home system.
#    - Create the home plan using `home_plan()`.
#    - Enter an infinite loop to continuously monitor and control the system.

# 3. **Retrieve rooms and sensors:**
#    - Use `get_room()` to obtain the living room and bedroom.
#    - Use `get_room_sensors()` to get the sensors in each room.

# 4. **Find temperature sensors:**
#    - Iterate through the sensors in each room to find the `IndoorTemperatureSensor` using `isinstance()`.

# 5. **Get temperature readings:**
#    - If temperature sensors are found, call `get_reading()` to obtain the temperature values.

# 6. **Retrieve actuators:**
#    - Use `get_room_actuators()` to get the actuators in each room.

# 7. **Find AC and window actuators:**
#    - Iterate through the actuators in each room to find the `AC` and `Window` actuators using `isinstance()`.

# 8. **Control AC and windows:**
#    - If the AC in either room is turned on, close the windows in both rooms.
#    - If the temperature in either room exceeds `TEMP_HIGH`, open the windows in both rooms.

# 9. **Wait and repeat:**
#    - Use `time.sleep(1)` to pause for one second before checking the conditions again.

# **Key improvements:**

# - **Room and sensor retrieval:**
#    - The code now explicitly retrieves the living room and bedroom using `get_room()`.
#    - It then uses `get_room_sensors()` to get the sensors in each room.
# - **Temperature sensor handling:**
#    - The code iterates through the sensors in each room to find the specific `IndoorTemperatureSensor`.
# - **Actuator retrieval:**
#    - The code retrieves the actuators in each room using `get_room_actuators()`.
# - **AC and window handling:**
#    - The code iterates through the actuators to find the specific `AC` and `Window` actuators.
# - **Temperature threshold:**
#    - The code uses the `TEMP_HIGH` constant from `home.config` to compare the temperature readings.
# - **Logging:**
#    - The code uses the `logger` object to log messages for debugging and monitoring purposes.

# This updated code provides a more structured and robust approach to managing the smart home system. It correctly retrieves and identifies the necessary sensors and actuators, enabling the logic to control the AC and windows based on temperature readings and AC status.
