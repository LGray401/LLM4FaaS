# To create a smart home application that operates based on your functional description and smart home layout, we'll write a Python script that monitors sensor data and controls smart devices accordingly. Since you mentioned the application should be runnable with one command in a Linux terminal, we'll make it a standalone script.
# 
# ### Python Script
# 
# Below is a Python script that simulates the functionality you described:
# 
# ```python
#!/usr/bin/env python3

import random
import time

# Simulating sensor data for demonstration purposes
def get_sensor_data(room, sensor_type):
    # Randomly generate sensor data
    if sensor_type == "Temperature":
        return random.uniform(15.0, 30.0)
    elif sensor_type == "Humidity":
        return random.uniform(0, 50)
    elif sensor_type == "Light Intensity":
        return random.uniform(0, 50)
    elif sensor_type == "Smoke":
        return random.choice([True, False])

# Smart home device control functions
def control_ac(room, action):
    print(f"[{room}] AC is now {'ON' if action else 'OFF'}.")

def monitor_and_control():
    rooms = {
        "Living Room": ["Temperature", "Humidity", "Light Intensity"],
        "Bedroom": ["Temperature", "Humidity", "Light Intensity"],
        "Bathroom": ["Temperature", "Humidity"],
        "Kitchen": ["Humidity", "Smoke"],
        "Balcony": ["Temperature", "Humidity"]
    }
    
    while True:
        for room, sensors in rooms.items():
            sensor_data = {sensor: get_sensor_data(room, sensor) for sensor in sensors}

            # Check conditions for AC
            if ("Temperature" in sensor_data and sensor_data["Temperature"] > 26) or \
               ("Humidity" in sensor_data and sensor_data["Humidity"] > 10) or \
               ("Light Intensity" in sensor_data and sensor_data["Light Intensity"] > 20):
                control_ac(room, True)
            else:
                control_ac(room, False)

        # Sleep for a while before next check
        time.sleep(5)

if __name__ == "__main__":
    monitor_and_control()
# ```
# 
# ### Running the Script
# 
# 1. Save the script to a file, for example, `smart_home.py`.
# 2. Make the script executable by running the following command in the terminal:
#    ```bash
#    chmod +x smart_home.py
#    ```
# 3. Execute the script with the following command:
#    ```bash
#    ./smart_home.py
#    ```
# 
# ### Explanation
# 
# - **Sensor Simulation**: The `get_sensor_data` function randomly generates data to simulate sensor readings. In a real application, this would interface with actual sensors.
#   
# - **Control Logic**: The script checks the conditions specified in your functional description. If any of the conditions are met, it turns on the AC for that room.
# 
# - **Loop**: The `monitor_and_control` function continuously checks the sensor data every 5 seconds.
# 
# This script is a basic simulation to demonstrate functionality. In a real-world application, you would replace random data generation with actual sensor readings and control signals.