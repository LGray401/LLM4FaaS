# To create a smart home application that can be run in a Linux terminal and addresses your functional description, we'll need to implement a simple Python script. This script will encapsulate the functionality of turning off all lights and water sources in the smart home layout you provided.
# 
# Based on the layout, the devices we need to manage are primarily lights. Since your description does not mention specific water-controlling devices, we will assume that the water sources are controlled through a set of devices (e.g., faucets or smart valves) that we can turn off similarly to lights.
# 
# Here's a simple Python script that fulfills your functional requirements:
# 
# ```python
class SmartDevice:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.state = "on"

    def turn_off(self):
        self.state = "off"
        print(f"{self.name} in {self.location} is now {self.state}.")

class SmartHome:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def turn_off_all_lights(self):
        for device in self.devices:
            if "Light" in device.name:
                device.turn_off()

    def turn_off_all_water_sources(self):
        # Assuming there are devices named "Water Source" for this purpose
        for device in self.devices:
            if "Water Source" in device.name:
                device.turn_off()

    def shutdown(self):
        print("Shutting down all lights and water sources...")
        self.turn_off_all_lights()
        self.turn_off_all_water_sources()
        print("Shutdown complete.")

def setup_smart_home():
    home = SmartHome()
    
    # Adding lights to the home
    home.add_device(SmartDevice("Light", "Living Room"))
    home.add_device(SmartDevice("Light", "Living Room"))
    home.add_device(SmartDevice("Light", "Bedroom"))
    home.add_device(SmartDevice("Light", "Bedroom"))
    home.add_device(SmartDevice("Light", "Bathroom"))
    home.add_device(SmartDevice("Light", "Kitchen"))
    
    # Assuming we have water control devices named "Water Source"
    home.add_device(SmartDevice("Water Source", "Bathroom"))
    home.add_device(SmartDevice("Water Source", "Kitchen"))
    
    return home

if __name__ == "__main__":
    smart_home = setup_smart_home()
    smart_home.shutdown()
# ```
# 
# ### Explanation:
# - The `SmartDevice` class represents a generic smart device with basic functionalities, such as turning off.
# - The `SmartHome` class manages a collection of smart devices and provides methods to turn off all lights and water sources.
# - The `setup_smart_home` function initializes the smart home with the appropriate devices based on your layout.
# - When the script is run, it will print messages indicating that each light and water source device is turned off.
# 
# ### Command to run the application:
# To run this Python script from a Linux terminal, save it to a file, for example, `smart_home.py`, and then execute the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This command will execute the script using Python 3, shutting down all lights and water sources as per your functional requirements.