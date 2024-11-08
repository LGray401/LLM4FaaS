# To create a smart home application based on your functional description and layout, we'll simulate the behavior of the smart devices using a Python script. The script will monitor sensor data and control devices accordingly. Here's a basic implementation that you can run in a Linux terminal.
# 
# ```python
import sys
import time
import random

# Simulate sensor readings
def get_sensor_data():
    return {
        "living_room": {
            "temperature": random.uniform(20, 30),
            "humidity": random.uniform(30, 70),
            "light_intensity": random.uniform(100, 1000)
        },
        "bedroom": {
            "temperature": random.uniform(20, 30),
            "humidity": random.uniform(30, 70),
            "light_intensity": random.uniform(100, 1000)
        },
        "bathroom": {
            "temperature": random.uniform(20, 30),
            "humidity": random.uniform(30, 70)
        },
        "kitchen": {
            "humidity": random.uniform(30, 70),
            "smoke": random.choice([True, False])
        },
        "balcony": {
            "temperature": random.uniform(15, 35),
            "humidity": random.uniform(30, 70)
        }
    }

# Function to control devices based on sensor data
def control_devices(sensor_data):
    # Temperature control
    for room, sensors in sensor_data.items():
        if "temperature" in sensors and sensors["temperature"] > 25:
            print(f"{room.capitalize()} AC: ON")
            if "Window" in room:
                print(f"{room.capitalize()} Window: CLOSED")

    # Humidity control
    for room, sensors in sensor_data.items():
        if "humidity" in sensors and sensors["humidity"] < 40:
            print(f"{room.capitalize()} Humidifier: ON")

    # Light intensity control
    for room, sensors in sensor_data.items():
        if "light_intensity" in sensors:
            if sensors["light_intensity"] < 300:
                print(f"{room.capitalize()} Lights: ON")
            else:
                print(f"{room.capitalize()} Lights: OFF")

def main():
    print("Starting Smart Home Management System...")
    while True:
        sensor_data = get_sensor_data()
        control_devices(sensor_data)
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Script
# 
# 1. Save this script to a file, for example, `smart_home.py`.
# 
# 2. Open a terminal on your Linux machine.
# 
# 3. Navigate to the directory where the `smart_home.py` file is saved.
# 
# 4. Run the script using Python:
# 
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script simulates a smart home system that manages temperature, humidity, and light levels based on the functional description you provided. It uses random values to simulate sensor readings and prints out the actions taken by the system. You can modify the logic and details to fit your specific needs or actual sensor data inputs.