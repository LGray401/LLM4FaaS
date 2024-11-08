from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
from home.config import TEMP_HIGH, TEMP_LOW

def main():
    # Create a home plan
    home = home_plan()

    # Example usage of the functions:
    # Get a specific room
    living_room = get_room(home, "LivingRoom")

    # Get sensors in a room
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get actuators in a room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all sensors of a specific type
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all actuators of a specific type
    acs = get_all_actuators(home, "AC")
    windows = get_all_actuators(home, "Window")

    # Example function to control AC and window based on temperature
    for ac in acs:
        if ac.room_name == "LivingRoom" or ac.room_name == "Bedroom":
            # Get indoor temperature reading
            for sensor in indoor_temp_sensors:
                if sensor.room_name == ac.room_name:
                    indoor_temp = sensor.get_reading()
                    if indoor_temp:
                        if indoor_temp > TEMP_HIGH:
                            # Check outdoor temperature for potential ventilation
                            for outdoor_sensor in get_all_sensors(home, "OutdoorTemperature"):
                                outdoor_temp = outdoor_sensor.get_reading()
                                if outdoor_temp and outdoor_temp < TEMP_LOW:
                                    # Open windows
                                    for window in windows:
                                        if window.room_name == ac.room_name:
                                            window.turn_on()
                        else:
                            # Turn off AC
                            ac.turn_off()
                        break  # Stop searching for indoor temperature sensor
    
    # Example function to turn off windows when AC is on
    for ac in acs:
        if ac.status == "on":
            for window in windows:
                if window.room_name == ac.room_name:
                    window.turn_off()

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import Necessary Modules:**
#    - Imports relevant functions and classes from `home.home_plan`, `home.sensor`, `home.actuator`, and `home.config`.

# 2. **Define `main()` Function:**
#    - This function contains the main logic of your smart home system.
#    - It utilizes the imported functions to retrieve rooms, sensors, and actuators.

# 3. **Retrieve Home Plan:**
#    - `home = home_plan()` creates the home plan using the `home_plan()` function from `home.home_plan`.

# 4. **Example Usage:**
#    - **Get a Room:** `living_room = get_room(home, "LivingRoom")` retrieves the "LivingRoom" from the home plan.
#    - **Get Sensors and Actuators:** Uses the `get_room_sensors()` and `get_room_actuators()` functions to get components within the living room.
#    - **Get All Sensors/Actuators:** `get_all_sensors()` and `get_all_actuators()` are used to retrieve all sensors or actuators of a specific type from the entire home plan.

# 5. **Control Logic:**
#    - The example function demonstrates how to control the AC and windows based on temperature:
#      - It iterates through all ACs and checks if they are in the living room or bedroom.
#      - For each AC, it finds the corresponding indoor temperature sensor and gets the reading.
#      - If the temperature is higher than the threshold, it checks the outdoor temperature.
#      - If the outdoor temperature is lower than the threshold, it opens the windows in the room.
#      - Otherwise, it turns off the AC.
#      - The `break` statement after finding the indoor temperature sensor prevents unnecessary iteration.

#    - The second example function turns off windows when an AC in the same room is on.

# **How to Run:**

# 1. **Save the code:** Save the code as `function.py` in your `functions` folder.
# 2. **Run the script:** From the command line, navigate to the `functions` folder and run: `python function.py`

# **To integrate with your existing code:**

# - Modify the `main()` function to include the specific logic and functionality you need for your smart home project.
# - Replace the example temperature control logic with your desired logic for controlling actuators based on sensor readings.
# - You can add more functions and logic to the `function.py` file as needed.

# **Remember:** This code provides a starting point. You will need to customize it further to implement the full functionality and logic of your smart home project.
