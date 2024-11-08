# To create a simple smart home application based on your functional description and smart home layout, we need to implement a Python script that simulates the control of various smart devices in your home. The script will have predefined plans (Morning Plan, Leave Home Plan, Movie Plan) that control the devices in different rooms according to your description.
# 
# Since your functional description only mentions "灯" for each plan, which translates to "light" in English, we will assume that each plan primarily controls the lights in various rooms. Let's create a Python script for this purpose.
# 
# ### Smart Home Application (smart_home.py)
# 
# ```python
class SmartHome:
    def __init__(self):
        self.rooms = {
            "Living Room": {"Light": 2},
            "Bedroom": {"Light": 2},
            "Bathroom": {"Light": 1},
            "Kitchen": {"Light": 1},
            "Balcony": {"Light": 0}  # No lights mentioned for Balcony
        }
        self.device_states = {room: {"Light": [False] * count} for room, devices in self.rooms.items() for device, count in devices.items()}

    def morning_plan(self):
        print("Executing Morning Plan...")
        self.device_states["Living Room"]["Light"] = [True, True]
        self.device_states["Bedroom"]["Light"] = [True, True]
        self.device_states["Bathroom"]["Light"] = [True]
        self.device_states["Kitchen"]["Light"] = [True]

    def leave_home_plan(self):
        print("Executing Leave Home Plan...")
        for room in self.device_states:
            for device in self.device_states[room]:
                self.device_states[room][device] = [False] * len(self.device_states[room][device])

    def movie_plan(self):
        print("Executing Movie Plan...")
        self.device_states["Living Room"]["Light"] = [False, False]
        self.device_states["Bedroom"]["Light"] = [False, False]
        # Assume the movie plan involves dimming or turning off lights for ambience

    def display_state(self):
        print("Current Device States:")
        for room, devices in self.device_states.items():
            print(f"{room}:")
            for device, states in devices.items():
                print(f"  {device}: {states}")

def main(plan):
    home = SmartHome()
    if plan == "morning":
        home.morning_plan()
    elif plan == "leave":
        home.leave_home_plan()
    elif plan == "movie":
        home.movie_plan()
    else:
        print("Unknown plan. Available plans: morning, leave, movie")
        return
    home.display_state()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python smart_home.py <plan>")
    else:
        main(sys.argv[1])
# ```
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, save the above script as `smart_home.py`. You can then execute it with the following command, replacing `<plan>` with `morning`, `leave`, or `movie` depending on which plan you want to simulate:
# 
# ```bash
# python smart_home.py <plan>
# ```
# 
# For example, to execute the "Morning Plan", you would run:
# 
# ```bash
# python smart_home.py morning
# ```
# 
# This script initializes a smart home with the given layout and controls the lights based on the selected plan. Each function simulates turning lights on or off according to the plan you're executing.