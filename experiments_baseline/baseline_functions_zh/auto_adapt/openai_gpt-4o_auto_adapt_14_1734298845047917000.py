# To create a smart home application based on your functional description and layout, we'll need to simulate the functionality of the sensors and devices in each room. The application will respond to specific conditions as described in your functional description. 
# 
# Here's a simplified version of the application in Python:
# 
# ```python
import random
import time

class SmartHome:
    def __init__(self):
        # Initial states for sensors
        self.rooms = {
            "Living Room": {"Temperature": 25, "Humidity": 50, "Light Intensity": 300},
            "Bedroom": {"Temperature": 22, "Humidity": 45, "Light Intensity": 250},
            "Bathroom": {"Temperature": 24, "Humidity": 60},
            "Kitchen": {"Humidity": 55, "Smoke": False},
            "Balcony": {"Temperature": 27, "Humidity": 40}
        }

    def simulate_sensors(self):
        # Randomly change sensor values to simulate real-world changes
        for room, sensors in self.rooms.items():
            for sensor in sensors:
                if sensor == "Smoke":
                    sensors[sensor] = random.choice([True, False])
                else:
                    sensors[sensor] += random.choice([-1, 0, 1])

    def check_conditions(self):
        for room, sensors in self.rooms.items():
            if "Temperature" in sensors and sensors["Temperature"] > 30:
                print(f"{room}: 小g 太热了")
            if "Humidity" in sensors and sensors["Humidity"] < 30:
                print(f"{room}: 小g 太干了")
            if "Light Intensity" in sensors and sensors["Light Intensity"] < 200:
                print(f"{room}: 小g 太暗了")

    def run(self):
        while True:
            self.simulate_sensors()
            self.check_conditions()
            time.sleep(5)  # Wait for 5 seconds before the next check

if __name__ == "__main__":
    home = SmartHome()
    home.run()
# ```
# 
# This application initializes a `SmartHome` class with sensor states for each room. It simulates changes in these states and checks for the conditions specified in your functional description. When a condition is met, it prints a message that corresponds to the issue.
# 
# To run this application in a Linux terminal, save the code to a file, for example, `smart_home.py`, and use the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This command assumes you have Python 3 installed on your system. The application will continuously simulate sensor data and print messages when specific conditions are met, as described in your functional requirements.