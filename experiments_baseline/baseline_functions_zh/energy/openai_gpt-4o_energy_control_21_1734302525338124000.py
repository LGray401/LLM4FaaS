# To create a smart home application that can be run from a Linux terminal, we can write a Python script that performs the required actions based on your functional description. Here's a basic implementation:
# 
# ```python
# smart_home.py

class SmartDevice:
    def __init__(self, name):
        self.name = name

    def turn_off(self):
        print(f"{self.name}: turned off")

    def set_energy_saving_mode(self):
        print(f"{self.name}: energy saving mode activated")

    def set_dim(self):
        print(f"{self.name}: set to dim")

class Room:
    def __init__(self, name, devices):
        self.name = name
        self.devices = devices

    def activate_energy_saving_mode(self):
        for device in self.devices:
            if isinstance(device, Light):
                device.set_dim()
            elif isinstance(device, Curtain):
                device.turn_off()
            elif isinstance(device, Humidifier):
                device.turn_off()
            elif isinstance(device, CleaningRobot):
                device.return_to_base()
            elif isinstance(device, MusicPlayer):
                device.turn_off()
            elif isinstance(device, TV):
                device.set_energy_saving_mode()
            elif isinstance(device, Socket):
                device.turn_off()

class Light(SmartDevice):
    pass

class Curtain(SmartDevice):
    pass

class Humidifier(SmartDevice):
    pass

class CleaningRobot(SmartDevice):
    def return_to_base(self):
        print(f"{self.name}: returning to base")

class MusicPlayer(SmartDevice):
    pass

class TV(SmartDevice):
    pass

class Socket(SmartDevice):
    pass

# Define smart home layout
living_room = Room("Living Room", [
    Light("Living Room Light 1"),
    Light("Living Room Light 2"),
    Curtain("Living Room Curtain"),
    Humidifier("Living Room Humidifier"),
    CleaningRobot("Living Room Cleaning Robot"),
    MusicPlayer("Living Room Music Player"),
    TV("Living Room TV"),
    Socket("Living Room Socket 1"),
    Socket("Living Room Socket 2"),
])

bedroom = Room("Bedroom", [
    Light("Bedroom Light 1"),
    Light("Bedroom Light 2"),
    Curtain("Bedroom Curtain"),
    Humidifier("Bedroom Humidifier"),
    CleaningRobot("Bedroom Cleaning Robot"),
    MusicPlayer("Bedroom Music Player"),
    Socket("Bedroom Socket 1"),
    Socket("Bedroom Socket 2"),
])

bathroom = Room("Bathroom", [
    Light("Bathroom Light"),
    Socket("Bathroom Socket 1"),
    Socket("Bathroom Socket 2"),
])

kitchen = Room("Kitchen", [
    Light("Kitchen Light"),
    Socket("Kitchen Socket 1"),
    Socket("Kitchen Socket 2"),
    Socket("Kitchen Socket 3"),
])

# Activate energy saving mode for all rooms
rooms = [living_room, bedroom, bathroom, kitchen]
for room in rooms:
    room.activate_energy_saving_mode()
# ```
# 
# Save this script as `smart_home.py`. Then, you can run it from a Linux terminal with the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This script defines a `SmartDevice` class and specific subclasses for each type of device. It then creates instances of these devices for each room and defines a `Room` class that can perform actions on all devices in that room to switch them to energy-saving mode according to your description.