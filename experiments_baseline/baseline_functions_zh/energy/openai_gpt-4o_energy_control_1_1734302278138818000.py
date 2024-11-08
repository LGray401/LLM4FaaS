# To create a smart home application in Python that can be executed in a Linux terminal with a single command, we'll need to define a simple script that can manage the devices based on the functional description, which in this case is "请关闭不必要的开关" (Please turn off unnecessary switches).
# 
# Below is a sample Python script that simulates this functionality:
# 
# ```python
#!/usr/bin/env python3

class SmartHome:
    def __init__(self):
        self.rooms = {
            "Living Room": [
                "Light", "Light", "Socket", "Socket", "Heater", "AC", "Humidifier", "Music Player", "TV"
            ],
            "Bedroom": [
                "Light", "Light", "AC", "Heater", "Music Player", "Socket", "Socket", "Humidifier"
            ],
            "Bathroom": [
                "Light", "Heater", "Socket", "Socket"
            ],
            "Kitchen": [
                "Light", "Heater", "Coffee Machine", "Socket", "Socket", "Socket"
            ],
            "Balcony": []
        }
        self.active_devices = {
            "Living Room": [],
            "Bedroom": [],
            "Bathroom": [],
            "Kitchen": [],
            "Balcony": []
        }

    def turn_off_unnecessary_devices(self):
        for room, devices in self.rooms.items():
            for device in devices:
                if device not in self.active_devices[room]:
                    print(f"Turning off {device} in {room}")

    def run(self):
        print("Smart home system initializing...")
        self.turn_off_unnecessary_devices()
        print("All unnecessary devices turned off.")

if __name__ == "__main__":
    home = SmartHome()
    home.run()
# ```
# 
# This script initializes a `SmartHome` object, with a list of devices in each room. It assumes that initially, all devices are considered necessary and thus "active." The `turn_off_unnecessary_devices` method simulates turning off devices that are not in use by iterating over the list of devices and printing a message for each one that is turned off.
# 
# To run this script in a Linux terminal, follow these steps:
# 
# 1. Save the script to a file, for example, `smart_home.py`.
# 2. Make the script executable by running the command: `chmod +x smart_home.py`.
# 3. Execute the script with: `./smart_home.py`.
# 
# This command sequence will run the Python script and simulate turning off unnecessary devices in your smart home.