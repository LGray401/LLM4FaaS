# To create a simple smart home application that can be run in a Linux terminal, we'll use Python. The application will interpret a command to turn off the lights in the bedroom, based on your functional description.
# 
# Here's a basic implementation:
# 
# ```python
# smart_home.py

class SmartDevice:
    def __init__(self, name, device_type, status='off'):
        self.name = name
        self.device_type = device_type
        self.status = status

    def turn_on(self):
        self.status = 'on'
        print(f"{self.name} is now {self.status}.")

    def turn_off(self):
        self.status = 'off'
        print(f"{self.name} is now {self.status}.")


class Room:
    def __init__(self, name, devices):
        self.name = name
        self.devices = devices

    def find_devices(self, device_type):
        return [device for device in self.devices if device.device_type == device_type]


class SmartHome:
    def __init__(self, rooms):
        self.rooms = rooms

    def execute_command(self, command):
        if command == "请把卧室的灯关了":
            bedroom = next(room for room in self.rooms if room.name == "Bedroom")
            lights = bedroom.find_devices("Light")
            for light in lights:
                light.turn_off()


def main():
    # Initialize devices
    bedroom_devices = [
        SmartDevice("Bedroom Light 1", "Light"),
        SmartDevice("Bedroom Light 2", "Light"),
        SmartDevice("Bedroom Window", "Window"),
        SmartDevice("Bedroom Curtain", "Curtain"),
        SmartDevice("Bedroom AC", "AC"),
        SmartDevice("Bedroom Heater", "Heater"),
        SmartDevice("Bedroom Music Player", "Music Player"),
        SmartDevice("Bedroom Door", "Door"),
        SmartDevice("Bedroom Socket 1", "Socket"),
        SmartDevice("Bedroom Socket 2", "Socket"),
        SmartDevice("Bedroom Cleaning Robot", "Cleaning Robot"),
        SmartDevice("Bedroom Humidifier", "Humidifier")
    ]

    bedroom = Room("Bedroom", bedroom_devices)

    # Initialize smart home
    home = SmartHome([bedroom])

    # Example command execution
    command = "请把卧室的灯关了"
    home.execute_command(command)


if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# 1. Save the above code into a file named `smart_home.py`.
# 2. Open a terminal.
# 3. Navigate to the directory where `smart_home.py` is located.
# 4. Run the command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This will simulate turning off the lights in the bedroom based on the given command "请把卧室的灯关了". The program is designed to be extendable for more commands and functionality as needed.