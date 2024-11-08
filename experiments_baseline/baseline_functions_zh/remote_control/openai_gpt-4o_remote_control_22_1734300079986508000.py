# Based on your functional description, the smart home application will need to perform the following operations:
# 
# 1. Turn on the lights in the living room, bedroom, and bathroom.
# 2. Turn on the AC in the living room and bedroom.
# 3. Turn on the heater in the bathroom.
# 4. Turn on the TV in the living room.
# 
# I'll write a Python script to simulate these actions. This script will use a simple command-line interface to execute the required actions.
# 
# Here's the Python script:
# 
# ```python
class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.state = "off"

    def turn_on(self):
        self.state = "on"
        print(f"{self.name} is now {self.state}.")

    def turn_off(self):
        self.state = "off"
        print(f"{self.name} is now {self.state}.")


class SmartHome:
    def __init__(self):
        # Living room devices
        self.living_room_light = SmartDevice("Living Room Light")
        self.living_room_ac = SmartDevice("Living Room AC")
        self.living_room_tv = SmartDevice("Living Room TV")

        # Bedroom devices
        self.bedroom_light = SmartDevice("Bedroom Light")
        self.bedroom_ac = SmartDevice("Bedroom AC")

        # Bathroom devices
        self.bathroom_light = SmartDevice("Bathroom Light")
        self.bathroom_heater = SmartDevice("Bathroom Heater")

    def execute_scenario(self):
        # Turn on lights
        self.living_room_light.turn_on()
        self.bedroom_light.turn_on()
        self.bathroom_light.turn_on()

        # Turn on ACs
        self.living_room_ac.turn_on()
        self.bedroom_ac.turn_on()

        # Turn on bathroom heater
        self.bathroom_heater.turn_on()

        # Turn on living room TV
        self.living_room_tv.turn_on()


if __name__ == "__main__":
    home = SmartHome()
    home.execute_scenario()
# ```
# 
# ### Running the Script
# 
# To run this script in a Linux terminal, save it to a file, for example, `smart_home.py`, and then execute the following command:
# 
# ```bash
# python smart_home.py
# ```
# 
# This command assumes you have Python installed on your system. If Python 3 is installed, you might need to use `python3` instead of `python`.