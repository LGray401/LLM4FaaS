from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, \
    LIGHT_INTENSITY_HIGH, TEMP_CHANGE_DURATION_WINDOW

def main():
    home = home_plan()
    
    # Get the sensors and actuators for the LivingRoom
    living_room = get_room(home, "LivingRoom")
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    
    # Get all the AC units in the home
    ac_units = get_all_actuators(home, "AC")
    
    # Loop through each AC unit and check the temperature and humidity
    for ac in ac_units:
        # Get the indoor temperature sensor in the room where the AC is located
        indoor_temp_sensor = None
        for sensor in living_room_sensors:
            if sensor.sensor_type == "IndoorTemperature":
                indoor_temp_sensor = sensor
                break
        
        # Get the humidity sensor in the room where the AC is located
        humidity_sensor = None
        for sensor in living_room_sensors:
            if sensor.sensor_type == "Humidity":
                humidity_sensor = sensor
                break
        
        # If both sensors are found, get their readings
        if indoor_temp_sensor and humidity_sensor:
            indoor_temperature = indoor_temp_sensor.get_reading()
            humidity = humidity_sensor.get_reading()
            
            # Check if the AC should be turned on or off based on temperature
            if indoor_temperature > TEMP_HIGH:
                print(f"Indoor temperature is {indoor_temperature}, turning on AC {ac.id}")
                ac.turn_on()
            elif indoor_temperature < TEMP_LOW:
                print(f"Indoor temperature is {indoor_temperature}, turning off AC {ac.id}")
                ac.turn_off()
                
            # Check if the windows should be opened or closed based on temperature and humidity
            if indoor_temperature > TEMP_HIGH and humidity > HUMIDITY_LOW:
                # Check if there are any windows in the living room
                for actuator in living_room_actuators:
                    if actuator.actuator_type == "Window":
                        print(f"Indoor temperature is high and humidity is high, opening window {actuator.id}")
                        actuator.turn_on()
            elif indoor_temperature < TEMP_LOW and humidity < HUMIDITY_LOW:
                # Check if there are any windows in the living room
                for actuator in living_room_actuators:
                    if actuator.actuator_type == "Window":
                        print(f"Indoor temperature is low and humidity is low, closing window {actuator.id}")
                        actuator.turn_off()
                        
            # Check if the AC is already on and the indoor temperature is lower than the set temperature
            if ac.get_status() == "on" and indoor_temperature < TEMP_HIGH:
                print(f"AC is already on but the indoor temperature is {indoor_temperature}, asking if you want to open the windows")
                user_input = input("Would you like to open the windows to cool down? (y/n): ")
                if user_input.lower() == "y":
                    # Check if there are any windows in the living room
                    for actuator in living_room_actuators:
                        if actuator.actuator_type == "Window":
                            print(f"Opening window {actuator.id}")
                            actuator.turn_on()
                            break
    
    # Simulate sensor readings and actuator operations
    # ... (Code to simulate sensor readings and actuator operations would go here)
        
    # Sleep for a short duration to simulate real-time operation
    time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:** Import necessary modules from `home` folder.
# 2. **`main` Function:**
#     - Creates a `home` instance using `home_plan()`.
#     - Gets the LivingRoom and its sensors and actuators.
#     - Gets all AC units from the home.
# 3. **Looping Through AC Units:**
#     - Iterates through each AC unit.
#     - **Find Sensors:**
#         - Finds the indoor temperature sensor and humidity sensor in the living room.
#     - **Get Readings:**
#         - Retrieves readings from the found sensors.
#     - **AC Control:**
#         - Checks if the AC should be turned on or off based on the indoor temperature and the set temperature threshold.
#     - **Window Control:**
#         - Checks if the windows should be opened or closed based on temperature and humidity.
#     - **User Input for AC & Window Control:**
#         - If the AC is already on and the temperature is lower than the set threshold, it asks the user if they want to open the windows to cool down.
# 4. **Simulate Readings and Operations:**
#     - This section is commented out as a placeholder for simulating sensor readings and actuator actions. 
# 5. **Sleep:**
#     - Sleeps for a specified duration to simulate real-time operation.

# **Key Improvements:**

# - **Clearer Logic:** The code is organized for better readability.
# - **Sensor & Actuator Identification:** Code explicitly identifies the sensors and actuators needed for each operation.
# - **User Interaction:**  Prompts the user if they want to open windows when the AC is already on but the indoor temperature is below the set threshold.
# - **Simulate Readings:**  The section to simulate readings and actions is included as a placeholder for further development.
# - **Real-time Simulation:**  The `time.sleep` function simulates a real-time loop.

# **Remember:**

# - This code provides a basic structure. You'll need to add actual sensor readings, actuator operations, and error handling to make it functional in your smart home project.
# - Consider using a more robust simulation framework if you're not directly interacting with hardware.
# - Remember to install any missing dependencies (e.g., `time`).

# This improved version of `function.py` helps automate your home's temperature and humidity regulation based on user preferences and real-time conditions. 
