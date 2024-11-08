# To create a smart home application based on your functional description and layout, we'll design a simple Python script that simulates the behavior of the smart devices in your home based on the given environmental conditions. The script will be run in a Linux terminal.
# 
# Here's a basic outline of the Python application:
# 
# 1. **Setup**: Define the layout and devices of the smart home.
# 2. **Simulate Sensors**: Based on the functional description, emulate the reading of sensors (temperature, humidity, light intensity).
# 3. **Control Logic**: Implement logic to control smart devices based on sensor readings.
# 4. **Execution**: Print out the state of each device based on the control logic.
# 
# ```python
class SmartHome:
    def __init__(self):
        self.rooms = {
            "Living Room": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": {
                    "Light": False,
                    "Window": "Closed",
                    "Socket": False,
                    "Door": "Closed",
                    "Heater": False,
                    "AC": False,
                    "Curtain": "Closed",
                    "Humidifier": False,
                    "Cleaning Robot": "Idle",
                    "Music Player": "Off",
                    "TV": "Off",
                    "Notification Sender": "Off"
                }
            },
            "Bedroom": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": {
                    "Light": False,
                    "Window": "Closed",
                    "Curtain": "Closed",
                    "AC": False,
                    "Heater": False,
                    "Music Player": "Off",
                    "Door": "Closed",
                    "Socket": False,
                    "Cleaning Robot": "Idle",
                    "Humidifier": False
                }
            },
            "Bathroom": {
                "sensors": ["Temperature", "Humidity"],
                "devices": {
                    "Light": False,
                    "Window": "Closed",
                    "Heater": False,
                    "Door": "Closed",
                    "Socket": False
                }
            },
            "Kitchen": {
                "sensors": ["Humidity", "Smoke"],
                "devices": {
                    "Light": False,
                    "Window": "Closed",
                    "Heater": False,
                    "Coffee Machine": "Off",
                    "Socket": False,
                    "Door": "Closed"
                }
            },
            "Balcony": {
                "sensors": ["Temperature", "Humidity"],
                "devices": {
                    "Door": "Closed"
                }
            }
        }
        self.sensor_data = {
            "Temperature": 25,
            "Humidity": "适中",
            "Light Intensity": "亮"
        }

    def control_devices(self):
        for room, details in self.rooms.items():
            # Example logic for controlling devices based on sensor data
            if "Light Intensity" in details["sensors"]:
                if self.sensor_data["Light Intensity"] == "亮":
                    details["devices"]["Light"] = False
                else:
                    details["devices"]["Light"] = True
            
            if "Temperature" in details["sensors"]:
                if self.sensor_data["Temperature"] < 20:
                    details["devices"]["Heater"] = True
                    details["devices"]["AC"] = False
                elif self.sensor_data["Temperature"] > 25:
                    details["devices"]["Heater"] = False
                    details["devices"]["AC"] = True
                else:
                    details["devices"]["Heater"] = False
                    details["devices"]["AC"] = False
            
            if "Humidity" in details["sensors"]:
                if self.sensor_data["Humidity"] != "适中":
                    details["devices"]["Humidifier"] = True
                else:
                    details["devices"]["Humidifier"] = False

    def display_status(self):
        for room, details in self.rooms.items():
            print(f"\n{room}:")
            for device, status in details["devices"].items():
                print(f"  {device}: {status}")

if __name__ == "__main__":
    home = SmartHome()
    home.control_devices()
    home.display_status()
# ```
# 
# ### How to Run
# 
# 1. Save the above script in a file, for example, `smart_home.py`.
# 2. Open a terminal and navigate to the directory containing `smart_home.py`.
# 3. Run the script with the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This basic script checks the sensor values and controls the devices accordingly. You can expand the control logic to include more sophisticated rules and interactions as needed.