# To create a smart home application based on your functional description and smart home layout, we'll need to simulate the behavior of the various devices and sensors in your home. The application will be able to execute three main plans: "Morning Plan", "Leave Home Plan", and "Movie Plan".
# 
# Below is a Python script that can be run in a Linux terminal. It simulates the smart home application and responds to the given plans.
# 
# ```python
import sys

class SmartHome:
    def __init__(self):
        self.devices = {
            "Living Room": {
                "lights": ["off", "off"],
                "curtain": "closed",
                "tv": "off",
                "door": "unlocked",
                "sockets": ["on", "on"],
            },
            "Bedroom": {
                "lights": ["off", "off"],
                "curtain": "closed",
                "door": "unlocked",
                "sockets": ["on", "on"],
            },
            "Bathroom": {
                "lights": "off",
                "door": "unlocked",
                "sockets": ["on", "on"],
            },
            "Kitchen": {
                "lights": "off",
                "coffee_machine": "off",
                "door": "unlocked",
                "sockets": ["on", "on", "on"],
            },
            "Balcony": {
                "door": "unlocked",
            }
        }

    def morning_plan(self):
        print("Executing MORNING PLAN...")
        self.devices["Bedroom"]["curtain"] = "open"
        self.devices["Kitchen"]["coffee_machine"] = "on"
        if self.is_dark():
            self.devices["Bedroom"]["lights"] = ["medium", "medium"]
            self.devices["Living Room"]["lights"] = ["medium", "medium"]
        print("Bedroom curtain opened, coffee machine started.")
        if self.is_dark():
            print("It's dark, lights set to medium.")
        self.print_status()

    def leave_home_plan(self):
        print("Executing LEAVE HOME PLAN...")
        for room in self.devices:
            if "lights" in self.devices[room]:
                if isinstance(self.devices[room]["lights"], list):
                    self.devices[room]["lights"] = ["off"] * len(self.devices[room]["lights"])
                else:
                    self.devices[room]["lights"] = "off"
            if "sockets" in self.devices[room]:
                self.devices[room]["sockets"] = ["off"] * len(self.devices[room]["sockets"])
            if "door" in self.devices[room]:
                self.devices[room]["door"] = "locked"
        print("Doors locked, lights and sockets turned off.")
        self.print_status()

    def movie_plan(self):
        print("Executing MOVIE PLAN...")
        self.devices["Living Room"]["curtain"] = "closed"
        self.devices["Living Room"]["lights"] = ["dim", "dim"]
        self.devices["Living Room"]["tv"] = "on"
        print("Curtains closed, lights dimmed, TV turned on.")
        self.print_status()

    def is_dark(self):
        # Simulate checking light intensity sensor
        return True  # Assume it's dark for simulation

    def print_status(self):
        for room, devices in self.devices.items():
            print(f"{room}:")
            for device, status in devices.items():
                print(f"  {device}: {status}")

def main(plan):
    home = SmartHome()
    if plan == "morning":
        home.morning_plan()
    elif plan == "leave_home":
        home.leave_home_plan()
    elif plan == "movie":
        home.movie_plan()
    else:
        print("Unknown plan. Please specify 'morning', 'leave_home', or 'movie'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python smart_home.py <plan>")
        print("Where <plan> is 'morning', 'leave_home', or 'movie'.")
    else:
        main(sys.argv[1])
# ```
# 
# ### How to Run the Application
# 
# 1. Save the script to a file named `smart_home.py`.
# 2. Open a terminal and navigate to the directory where the file is saved.
# 3. Run the script with one of the following commands, depending on the plan you want to execute:
# 
#    - For the Morning Plan:  
#      ```bash
#      python smart_home.py morning
#      ```
# 
#    - For the Leave Home Plan:  
#      ```bash
#      python smart_home.py leave_home
#      ```
# 
#    - For the Movie Plan:  
#      ```bash
#      python smart_home.py movie
#      ```
# 
# This script simulates the operation of your smart home based on the specified plans. It assumes the light intensity is always dark for simplicity in the simulation.