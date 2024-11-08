# To create a smart home application based on your functional description and layout, we can develop a Python script that simulates reading sensor data and controlling smart devices in each room of your smart home. This script will provide a basic simulation of how such an application might operate.
# 
# Here's a simple implementation:
# 
# ```python
class SmartHome:
    def __init__(self):
        self.rooms = {
            "Living Room": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": {
                    "Light": 2,
                    "Window": 2,
                    "Socket": 2,
                    "Door": 1,
                    "Heater": 1,
                    "AC": 1,
                    "Curtain": 1,
                    "Humidifier": 1,
                    "Cleaning Robot": 1,
                    "Music Player": 1,
                    "TV": 1,
                    "Notification Sender": 1
                }
            },
            "Bedroom": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": {
                    "Light": 2,
                    "Window": 1,
                    "Curtain": 1,
                    "AC": 1,
                    "Heater": 1,
                    "Music Player": 1,
                    "Door": 1,
                    "Socket": 2,
                    "Cleaning Robot": 1,
                    "Humidifier": 1
                }
            },
            "Bathroom": {
                "sensors": ["Temperature", "Humidity"],
                "devices": {
                    "Light": 1,
                    "Window": 1,
                    "Heater": 1,
                    "Door": 1,
                    "Socket": 2
                }
            },
            "Kitchen": {
                "sensors": ["Humidity", "Smoke"],
                "devices": {
                    "Light": 1,
                    "Window": 1,
                    "Heater": 1,
                    "Coffee Machine": 1,
                    "Socket": 3,
                    "Door": 1
                }
            },
            "Balcony": {
                "sensors": ["Temperature", "Humidity"],
                "devices": {
                    "Door": 1
                }
            }
        }

    def show_status(self):
        for room, details in self.rooms.items():
            print(f"--- {room} ---")
            sensors = ", ".join(details["sensors"])
            print(f"Sensors: {sensors}")
            print("Devices:")
            for device, count in details["devices"].items():
                print(f"  {device}: {count}")
            print()

def main():
    home = SmartHome()
    home.show_status()

if __name__ == "__main__":
    main()
# ```
# 
# ### Command to run the application:
# 
# 1. Save the above code to a file called `smart_home.py`.
# 2. Open your terminal and navigate to the directory where `smart_home.py` is located.
# 3. Run the application using the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This script is a simple representation of a smart home system. It displays the sensors and devices in each room according to the layout you provided. You can expand this further by adding functionalities such as reading real sensor data, controlling the devices, or simulating user interactions.