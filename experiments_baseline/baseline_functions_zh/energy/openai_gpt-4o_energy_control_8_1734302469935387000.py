# To implement the smart home application according to your functional description and layout, we can create a Python script that interacts with the smart devices. The script will focus on the functionality: turning on an air conditioner (AC) at 17 degrees and closing all windows.
# 
# Here's the Python script for the functionality:
# 
# ```python
class SmartDevice:
    def __init__(self, name, is_on=False):
        self.name = name
        self.is_on = is_on

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF.")

class AC(SmartDevice):
    def __init__(self, name, temperature=24):
        super().__init__(name)
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f"Temperature of {self.name} set to {self.temperature}°C.")

class Window(SmartDevice):
    def close(self):
        self.turn_off()
        print(f"{self.name} is now closed.")

class Room:
    def __init__(self, name, devices):
        self.name = name
        self.devices = {device.name: device for device in devices}

    def get_device(self, device_name):
        return self.devices.get(device_name, None)

def main():
    # Define devices
    living_room_ac = AC("Living Room AC")
    living_room_window1 = Window("Living Room Window 1")
    living_room_window2 = Window("Living Room Window 2")
    
    bedroom_ac = AC("Bedroom AC")
    bedroom_window = Window("Bedroom Window")
    
    bathroom_window = Window("Bathroom Window")
    
    kitchen_window = Window("Kitchen Window")
    
    # Define rooms
    living_room = Room("Living Room", [living_room_ac, living_room_window1, living_room_window2])
    bedroom = Room("Bedroom", [bedroom_ac, bedroom_window])
    bathroom = Room("Bathroom", [bathroom_window])
    kitchen = Room("Kitchen", [kitchen_window])

    # Action: Turn on AC to 17°C and close all windows
    for room in [living_room, bedroom, bathroom, kitchen]:
        for device_name, device in room.devices.items():
            if isinstance(device, AC):
                device.turn_on()
                device.set_temperature(17)
            elif isinstance(device, Window):
                device.close()

if __name__ == "__main__":
    main()
# ```
# 
# To run this script in a Linux terminal, you can save it to a file, say `smart_home.py`, and then execute it with the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This script initializes the rooms and devices based on your layout, then performs the actions specified in the functional description: turning on the air conditioners to 17°C and closing all windows across all rooms.