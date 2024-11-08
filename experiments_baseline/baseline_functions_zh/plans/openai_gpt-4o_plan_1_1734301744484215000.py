# To create a smart home application based on your functional description and layout, we can write a Python script that simulates the automation of various smart devices in your home. Below is a simple example of how such a script could be structured. This script will handle the "Morning Plan," "Leave Home Plan," and "Movie Plan" by printing out what actions it would take for each plan.
# 
# ```python
class SmartHome:
    def __init__(self):
        self.devices = {
            "Living Room": ["Light", "Window", "TV", "Curtain", "Music Player", "Door"],
            "Bedroom": ["Light", "Curtain", "Music Player"],
            "Kitchen": ["Coffee Machine"],
        }

    def morning_plan(self):
        print("Executing Morning Plan...")
        # Living Room
        self.activate_device("Living Room", "Curtain")
        self.activate_device("Living Room", "Light")
        self.activate_device("Living Room", "Music Player")
        # Kitchen
        self.activate_device("Kitchen", "Coffee Machine")

    def leave_home_plan(self):
        print("Executing Leave Home Plan...")
        # Living Room
        self.deactivate_device("Living Room", "Light")
        self.deactivate_device("Living Room", "Door")

    def movie_plan(self):
        print("Executing Movie Plan...")
        # Living Room
        self.activate_device("Living Room", "TV")
        self.deactivate_device("Living Room", "Curtain")
        self.dim_device("Living Room", "Light")

    def activate_device(self, room, device):
        if device in self.devices[room]:
            print(f"Activating {device} in {room}...")
        else:
            print(f"Device {device} not found in {room}")

    def deactivate_device(self, room, device):
        if device in self.devices[room]:
            print(f"Deactivating {device} in {room}...")
        else:
            print(f"Device {device} not found in {room}")

    def dim_device(self, room, device):
        if device in self.devices[room]:
            print(f"Dimming {device} in {room}...")
        else:
            print(f"Device {device} not found in {room}")

if __name__ == "__main__":
    home = SmartHome()
    print("Welcome to the Smart Home System")
    plan = input("Enter plan (morning, leave, movie): ").strip().lower()

    if plan == "morning":
        home.morning_plan()
    elif plan == "leave":
        home.leave_home_plan()
    elif plan == "movie":
        home.movie_plan()
    else:
        print("Invalid plan entered.")
# ```
# 
# ### How to Run the Script
# 1. Save the script to a file, for example, `smart_home.py`.
# 2. Open a terminal on your Linux machine.
# 3. Navigate to the directory where the script is saved.
# 4. Run the script using Python:
# 
# ```sh
# python3 smart_home.py
# ```
# 
# This script will prompt you to enter a plan (`morning`, `leave`, or `movie`) and then execute the appropriate actions by simulating the activation or deactivation of smart devices in your home. Adjust the script as needed to match your actual smart home devices and their APIs if you plan to connect it to real hardware.