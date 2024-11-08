# To implement a smart home application based on your functional description and layout, we can create a Python script that reads sensor data and controls smart devices accordingly. Below is a simple implementation:
# 
# ```python
import random
import time

class SmartHome:
    def __init__(self):
        self.rooms = {
            "Living Room": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": ["AC", "Curtain", "Humidifier"]
            },
            "Bedroom": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": ["AC", "Curtain", "Humidifier"]
            },
            "Bathroom": {
                "sensors": ["Temperature", "Humidity"],
                "devices": []
            },
            "Kitchen": {
                "sensors": ["Humidity", "Smoke"],
                "devices": []
            },
            "Balcony": {
                "sensors": ["Temperature", "Humidity"],
                "devices": []
            }
        }

    def read_sensor(self, room, sensor):
        # Simulate reading a sensor value
        if sensor == "Temperature":
            return random.uniform(20, 30)  # Temperature in Celsius
        elif sensor == "Humidity":
            return random.uniform(30, 40)  # Humidity percentage
        elif sensor == "Light Intensity":
            return random.uniform(50, 100)  # Light intensity value

    def control_device(self, room, device, action):
        print(f"{device} in {room} is now {action}.")

    def monitor_and_control(self):
        while True:
            for room, components in self.rooms.items():
                for sensor in components["sensors"]:
                    value = self.read_sensor(room, sensor)
                    if sensor == "Temperature" and value >= 26:
                        if "AC" in components["devices"]:
                            self.control_device(room, "AC", "ON")
                    elif sensor == "Humidity" and value < 36:
                        if "Humidifier" in components["devices"]:
                            self.control_device(room, "Humidifier", "ON")
                    elif sensor == "Light Intensity" and value > 80:
                        if "Curtain" in components["devices"]:
                            self.control_device(room, "Curtain", "CLOSED")
            time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    home = SmartHome()
    home.monitor_and_control()
# ```
# 
# ### How to Run
# 
# 1. Save the above code to a file, e.g., `smart_home.py`.
# 2. Open a terminal in Linux.
# 3. Run the script with the following command:
# 
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script simulates the smart home environment by checking sensor values and controlling devices in the rooms according to the specified conditions. The `read_sensor` function generates random values to simulate sensor readings. The `monitor_and_control` method continuously checks these values and takes appropriate actions. Adjust the random value ranges and conditions as necessary to better fit real-world scenarios.