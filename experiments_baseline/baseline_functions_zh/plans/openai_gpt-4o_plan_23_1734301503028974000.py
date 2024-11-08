# Based on your functional description and smart home layout, we'll create a Python script to simulate the smart home application. This script will focus on the three plans you provided: Morning Plan, Leave Home Plan, and Movie Plan. I'll provide a simple implementation using Python classes and a command-line interface to activate each plan. 
# 
# Here's a high-level overview of how the script will work:
# 
# 1. Define classes for the Smart Home, Rooms, Sensors, and Devices.
# 2. Implement methods to handle each of the three plans.
# 3. Provide a command-line interface to execute the plans.
# 
# Below is a Python script that accomplishes this:
# 
# ```python
import sys

class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.state = "off"

    def turn_on(self):
        self.state = "on"
        print(f"{self.name} turned on.")

    def turn_off(self):
        self.state = "off"
        print(f"{self.name} turned off.")

    def dim_light(self):
        if self.name == "Light":
            self.state = "dimmed"
            print(f"{self.name} dimmed.")

class SmartHome:
    def __init__(self):
        # Living Room Devices
        self.living_room_devices = {
            "curtain": SmartDevice("Curtain"),
            "music_player": SmartDevice("Music Player"),
            "light": SmartDevice("Light")
        }

        # Bedroom Devices
        self.bedroom_devices = {
            "curtain": SmartDevice("Curtain"),
            "music_player": SmartDevice("Music Player"),
            "light": SmartDevice("Light")
        }

    def morning_plan(self):
        print("Executing Morning Plan...")
        self.living_room_devices["curtain"].turn_on()
        self.living_room_devices["music_player"].turn_on()

    def leave_home_plan(self):
        print("Executing Leave Home Plan...")
        self.living_room_devices["curtain"].turn_on()
        self.living_room_devices["light"].turn_off()

    def movie_plan(self):
        print("Executing Movie Plan...")
        self.living_room_devices["curtain"].turn_off()
        self.living_room_devices["light"].dim_light()

def main(plan):
    home = SmartHome()
    if plan == "morning":
        home.morning_plan()
    elif plan == "leave_home":
        home.leave_home_plan()
    elif plan == "movie":
        home.movie_plan()
    else:
        print("Unknown plan!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 smart_home.py [morning|leave_home|movie]")
    else:
        main(sys.argv[1])
# ```
# 
# ### Instructions to Run the Script
# 
# 1. Save the script to a file named `smart_home.py`.
# 2. Open your terminal and navigate to the directory containing `smart_home.py`.
# 3. Run the script using the command:
# 
#    ```bash
#    python3 smart_home.py [plan]
#    ```
# 
#    Replace `[plan]` with one of the following options: `morning`, `leave_home`, or `movie`.
# 
# For example, to execute the Morning Plan, you would run:
# 
# ```bash
# python3 smart_home.py morning
# ```
# 
# This script provides a basic simulation of your smart home plans and can be expanded with more detailed logic and additional devices as needed.