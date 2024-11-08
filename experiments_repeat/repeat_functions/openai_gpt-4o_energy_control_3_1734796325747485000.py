# To implement the functionality described as "开窗关空调" (which translates to "open the window and turn off the air conditioner"), we can create a `function.py` file in the `functions` folder. This script will interact with the components in your smart home system based on the given source files.
# 
# Here's how you can implement this in `function.py`:
# 
# ```python
# function.py
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, AC
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.config import TEMP_HIGH

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Iterate through each room
    for room in home:
        print(f"\nChecking room: {room.name}")
        
        # Get all IndoorTemperatureSensors in the room
        indoor_temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        
        # Get all Windows and ACs in the room
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        
        # Turn on sensors to get readings
        for sensor in indoor_temp_sensors:
            sensor.turn_on()
            current_temp = sensor.get_reading()
            
            # If the temperature is above the high threshold, open the windows and turn off the AC
            if current_temp is not None and current_temp > TEMP_HIGH:
                print(f"Indoor temperature in {room.name} is {current_temp}°C, which is above {TEMP_HIGH}°C.")
                for window in windows:
                    window.turn_on()  # Open the window
                    print(f"Opened {window.id}.")
                
                for ac in ac_units:
                    ac.turn_off()  # Turn off the AC
                    print(f"Turned off {ac.id}.")
            else:
                print(f"Indoor temperature in {room.name} is {current_temp}°C, which is not above {TEMP_HIGH}°C.")
        
        # Turn off the sensors after checking
        for sensor in indoor_temp_sensors:
            sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Home Initialization**: The `home_plan()` function is used to initialize the entire home setup, obtaining all rooms, sensors, and actuators.
# - **Room Iteration**: The script iterates through each room in the home.
# - **Sensor and Actuator Management**: It identifies all indoor temperature sensors, windows, and air conditioners in each room.
# - **Temperature Check and Actuation**: For each indoor temperature sensor, if the current temperature reading is above a specified threshold (`TEMP_HIGH`), it opens all windows and turns off all air conditioners in that room.
# - **Sensor Management**: Sensors are turned on before reading and turned off afterwards to ensure they provide readings.
# 
# Ensure that this script is saved as `function.py` in your `functions` folder. This script assumes you have a logger set up as indicated in the provided code. Adjust logging as necessary for your needs.