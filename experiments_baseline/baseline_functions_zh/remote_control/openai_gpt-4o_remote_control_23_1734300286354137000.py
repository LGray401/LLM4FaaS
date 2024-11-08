# To create a smart home application based on your functional description and smart home layout, we can design a Python application that simulates the network control system. Each room will be a subsystem, and each subsystem will contain both sensor and smart device branches. Below is a simplified version of the application that can be run from a Linux terminal.
# 
# First, I'll outline the structure of the application, and then provide you with the Python code for it.
# 
# ### Structure
# 
# 1. **Main System**: Manages all subsystems.
# 2. **Subsystems**: One for each room (Living Room, Bedroom, Bathroom, Kitchen, Balcony).
# 3. **Sensor System**: Handles temperature, humidity, light intensity, and smoke sensors.
# 4. **Smart Device System**: Manages smart devices like lights, windows, sockets, doors, etc.
# 
# ### Python Code
# 
# Here's a Python script to simulate this application:
# 
# ```python
class SensorSystem:
    def __init__(self, temperature=False, humidity=False, light_intensity=False, smoke=False):
        self.temperature = temperature
        self.humidity = humidity
        self.light_intensity = light_intensity
        self.smoke = smoke

    def status(self):
        return {
            "Temperature": self.temperature,
            "Humidity": self.humidity,
            "Light Intensity": self.light_intensity,
            "Smoke": self.smoke
        }


class SmartDeviceSystem:
    def __init__(self, devices):
        self.devices = devices

    def status(self):
        return {device: "Off" for device in self.devices}


class Subsystem:
    def __init__(self, name, sensors, devices):
        self.name = name
        self.sensor_system = SensorSystem(**sensors)
        self.smart_device_system = SmartDeviceSystem(devices)

    def status(self):
        return {
            "Sensors": self.sensor_system.status(),
            "Devices": self.smart_device_system.status()
        }


class SmartHome:
    def __init__(self):
        self.subsystems = {
            "Living Room": Subsystem("Living Room",
                                     {"temperature": True, "humidity": True, "light_intensity": True},
                                     ["Light", "Light", "Window", "Window", "Socket", "Socket", "Door", "Heater", "AC", "Curtain", "Humidifier", "Cleaning Robot", "Music Player", "TV", "Notification Sender"]),
            "Bedroom": Subsystem("Bedroom",
                                 {"temperature": True, "humidity": True, "light_intensity": True},
                                 ["Light", "Light", "Window", "Curtain", "AC", "Heater", "Music Player", "Door", "Socket", "Socket", "Cleaning Robot", "Humidifier"]),
            "Bathroom": Subsystem("Bathroom",
                                  {"temperature": True, "humidity": True},
                                  ["Light", "Window", "Heater", "Door", "Socket", "Socket"]),
            "Kitchen": Subsystem("Kitchen",
                                 {"humidity": True, "smoke": True},
                                 ["Light", "Window", "Heater", "Coffee Machine", "Socket", "Socket", "Socket", "Door"]),
            "Balcony": Subsystem("Balcony",
                                 {"temperature": True, "humidity": True},
                                 ["Door"])
        }

    def status(self):
        status_report = {}
        for name, subsystem in self.subsystems.items():
            status_report[name] = subsystem.status()
        return status_report


def main():
    smart_home = SmartHome()
    status = smart_home.status()
    
    for room, details in status.items():
        print(f"Room: {room}")
        print("  Sensors:")
        for sensor, state in details["Sensors"].items():
            print(f"    {sensor}: {'Active' if state else 'Inactive'}")
        print("  Devices:")
        for device, state in details["Devices"].items():
            print(f"    {device}: {state}")
        print("\n")


if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run
# 
# 1. Save the code to a file, for example, `smart_home.py`.
# 2. Open a terminal in Linux.
# 3. Make sure you have Python installed. You can check by running `python3 --version`.
# 4. Run the application with the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This script provides a basic simulation of the smart home system, showing the status of sensors and smart devices in each room as specified in your layout. You can expand this script further to add more functionalities, such as turning devices on/off, reading sensor values, etc.