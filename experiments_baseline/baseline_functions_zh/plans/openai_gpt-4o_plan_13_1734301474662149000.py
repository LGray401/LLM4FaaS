# To create a smart home application that can be run from a Linux terminal, we'll use Python to define the functionality based on your description. We'll define classes for each room and control the smart devices according to the plans you have provided. 
# 
# Here's a simple implementation:
# 
# ```python
import sys

class SmartHome:
    def __init__(self):
        self.living_room = {
            "lights": "off",
            "curtains": "closed",
            "sockets": "on",
            "door": "unlocked",
            "tv": "off",
            "music_player": "off"
        }
        self.bedroom = {
            "lights": "off",
            "curtains": "closed",
            "sockets": "on",
            "music_player": "off"
        }
        self.kitchen = {
            "lights": "off",
            "coffee_machine": "off"
        }

    def morning_plan(self):
        self.living_room["curtains"] = "open"
        self.living_room["lights"] = "dim"
        self.kitchen["coffee_machine"] = "on"
        self.living_room["music_player"] = "playing"
        print("Morning Plan Activated: Curtains opened, lights dim, coffee machine on, music playing.")

    def leave_home_plan(self):
        self.living_room["lights"] = "off"
        self.living_room["curtains"] = "open"
        self.living_room["sockets"] = "off"
        self.living_room["door"] = "locked"
        print("Leave Home Plan Activated: Lights off, curtains open, sockets off, door locked.")

    def movie_plan(self):
        self.living_room["curtains"] = "closed"
        self.living_room["lights"] = "dim"
        self.living_room["tv"] = "on"
        print("Movie Plan Activated: Curtains closed, lights dim, TV on.")

    def execute_plan(self, plan):
        if plan == "morning":
            self.morning_plan()
        elif plan == "leave":
            self.leave_home_plan()
        elif plan == "movie":
            self.movie_plan()
        else:
            print("Unknown plan. Please use 'morning', 'leave', or 'movie'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python smart_home.py [plan]")
        sys.exit(1)

    plan = sys.argv[1]
    home = SmartHome()
    home.execute_plan(plan)
# ```
# 
# ### How to Run
# 
# 1. Save the above code to a file named `smart_home.py`.
# 2. Open your terminal and navigate to the directory where `smart_home.py` is located.
# 3. Run the following command to execute a specific plan:
# 
# ```bash
# python smart_home.py morning
# ```
# 
# Replace `morning` with `leave` or `movie` to activate different plans.
# 
# This script provides a basic simulation of the smart home plans you described. Each plan adjusts the state of devices in the home according to the functional description. It can easily be expanded to include more detailed functionality or additional devices.