# To create a smart home application based on your layout and requirements, we'll design a simple command-line application in Python. This application will manage the smart devices and sensors in each room. Since the functional description is provided as "控制" (which means "control" in Chinese), we'll focus on basic control functionalities for the devices.
# 
# Here's a basic outline of the Python application:
# 
# 1. **Sensors and Devices**: We'll define classes to represent sensors and smart devices.
# 2. **Rooms**: We'll group sensors and devices into rooms.
# 3. **Commands**: The application will accept commands to perform actions like turning devices on/off or checking sensor status.
# 
# ### Step-by-Step Implementation
# 
# 1. **Define Classes for Sensors and Devices**
# 
# ```python
class Sensor:
    def __init__(self, type):
        self.type = type

    def read(self):
        # Placeholder for sensor reading
        return f"Reading {self.type} sensor"

class Device:
    def __init__(self, name):
        self.name = name
        self.state = False  # False for off, True for on

    def turn_on(self):
        self.state = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.state = False
        print(f"{self.name} is now OFF.")

    def status(self):
        return f"{self.name} is {'ON' if self.state else 'OFF'}"
# ```
# 
# 2. **Define a Room Class**
# 
# ```python
class Room:
    def __init__(self, name, sensors, devices):
        self.name = name
        self.sensors = {sensor.type: sensor for sensor in sensors}
        self.devices = {device.name: device for device in devices}

    def read_sensors(self):
        for sensor in self.sensors.values():
            print(sensor.read())

    def control_device(self, device_name, action):
        if device_name in self.devices:
            device = self.devices[device_name]
            if action == 'on':
                device.turn_on()
            elif action == 'off':
                device.turn_off()
            else:
                print("Invalid action. Use 'on' or 'off'.")
        else:
            print(f"Device {device_name} not found in {self.name}.")
# ```
# 
# 3. **Setup the Smart Home**
# 
# ```python
def setup_smart_home():
    living_room = Room(
        "Living Room",
        sensors=[Sensor("Temperature"), Sensor("Humidity"), Sensor("Light Intensity")],
        devices=[
            Device("Light 1"), Device("Light 2"), Device("Window 1"), Device("Window 2"),
            Device("Socket 1"), Device("Socket 2"), Device("Door"), Device("Heater"),
            Device("AC"), Device("Curtain"), Device("Humidifier"), Device("Cleaning Robot"),
            Device("Music Player"), Device("TV"), Device("Notification Sender")
        ]
    )

    bedroom = Room(
        "Bedroom",
        sensors=[Sensor("Temperature"), Sensor("Humidity"), Sensor("Light Intensity")],
        devices=[
            Device("Light 1"), Device("Light 2"), Device("Window"), Device("Curtain"),
            Device("AC"), Device("Heater"), Device("Music Player"), Device("Door"),
            Device("Socket 1"), Device("Socket 2"), Device("Cleaning Robot"), Device("Humidifier")
        ]
    )

    bathroom = Room(
        "Bathroom",
        sensors=[Sensor("Temperature"), Sensor("Humidity")],
        devices=[
            Device("Light"), Device("Window"), Device("Heater"),
            Device("Door"), Device("Socket 1"), Device("Socket 2")
        ]
    )

    kitchen = Room(
        "Kitchen",
        sensors=[Sensor("Humidity"), Sensor("Smoke")],
        devices=[
            Device("Light"), Device("Window"), Device("Heater"),
            Device("Coffee Machine"), Device("Socket 1"),
            Device("Socket 2"), Device("Socket 3"), Device("Door")
        ]
    )

    balcony = Room(
        "Balcony",
        sensors=[Sensor("Temperature"), Sensor("Humidity")],
        devices=[Device("Door")]
    )

    return {
        "Living Room": living_room,
        "Bedroom": bedroom,
        "Bathroom": bathroom,
        "Kitchen": kitchen,
        "Balcony": balcony
    }
# ```
# 
# 4. **Main Application Loop**
# 
# ```python
def main():
    smart_home = setup_smart_home()

    print("Welcome to the Smart Home Controller")
    while True:
        command = input("Enter command (e.g., 'Living Room Light 1 on'): ").strip()
        if command.lower() == 'exit':
            break
        try:
            room_name, device_name, action = command.split()
            room = smart_home.get(room_name)
            if room:
                room.control_device(device_name, action)
            else:
                print(f"Room {room_name} not found.")
        except ValueError:
            print("Invalid command format. Use 'Room Device Action'.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Execution
# 
# Save this code to a file named `smart_home.py`. To run the application, use the following command in your Linux terminal:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This application will allow you to enter commands in the format `Room Device Action`, such as `Living Room Light 1 on` or `Bedroom Heater off`. It will provide feedback on the actions taken and the status of devices. Adjust the code to add any additional functionality or customizations as needed.