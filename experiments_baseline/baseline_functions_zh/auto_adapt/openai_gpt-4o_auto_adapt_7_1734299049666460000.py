# To create a smart home application based on your functional description and smart home layout, we'll need to implement a Python script that simulates the behavior of the smart home system. The application will monitor the sensors in each room and control the smart devices accordingly based on the conditions you specified.
# 
# Here's a simplified version of how this Python script might look:
# 
# ```python
import random

class SmartHome:
    def __init__(self):
        self.rooms = {
            "Living Room": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": ["Light", "Window", "Socket", "Door", "Heater", "AC", "Curtain", "Humidifier", "TV"]
            },
            "Bedroom": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": ["Light", "Window", "Curtain", "AC", "Heater", "Music Player", "Door", "Socket", "Humidifier"]
            },
            "Bathroom": {
                "sensors": ["Temperature", "Humidity"],
                "devices": ["Light", "Window", "Heater", "Door", "Socket"]
            },
            "Kitchen": {
                "sensors": ["Humidity", "Smoke"],
                "devices": ["Light", "Window", "Heater", "Coffee Machine", "Socket", "Door"]
            },
            "Balcony": {
                "sensors": ["Temperature", "Humidity"],
                "devices": ["Door"]
            }
        }

    def check_conditions_and_act(self):
        for room, info in self.rooms.items():
            print(f"\nChecking conditions in the {room}...")
            sensors = info["sensors"]
            devices = info["devices"]

            temperature = random.uniform(15, 35)  # Simulate temperature
            humidity = random.uniform(20, 80)     # Simulate humidity
            light_intensity = random.uniform(100, 800)  # Simulate light intensity

            # Check conditions based on your functional description
            if "Temperature" in sensors and temperature > 25:  # 屋里太热了
                if "AC" in devices:
                    print("Turning on the AC")
                if "Window" in devices:
                    print("Opening the window")

            if "Humidity" in sensors and humidity < 40:  # 屋里有点干
                if "Humidifier" in devices:
                    print("Turning on the humidifier")

            if "Light Intensity" in sensors and light_intensity < 300:  # 屋里太暗了
                if "Light" in devices:
                    print("Turning on the lights")

def main():
    home = SmartHome()
    home.check_conditions_and_act()

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Application
# 
# 1. Save the script above to a file named `smart_home.py`.
# 2. Open a terminal window in Linux.
# 3. Navigate to the directory where `smart_home.py` is located.
# 4. Run the script with the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - The script defines a `SmartHome` class that contains the layout of your home, including the sensors and smart devices in each room.
# - The `check_conditions_and_act` method simulates readings from the sensors and performs actions based on the conditions specified in your functional description.
# - The script uses random values to simulate sensor readings. You can replace these with actual sensor data if you have a real smart home setup.
# - The script is a simplified simulation and can be extended with real hardware integration for a functional smart home system.