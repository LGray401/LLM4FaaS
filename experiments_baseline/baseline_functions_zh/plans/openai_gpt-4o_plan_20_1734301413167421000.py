# To create a smart home application in Python that performs actions based on your functional description ("Morning Plan," "Leave Home Plan," and "Movie Plan"), we will simulate the interactions with the smart devices in your home layout. Below, I'll provide a simple command-line application that can be run in a Linux terminal.
# 
# ### Python Script: `smart_home.py`
# 
# ```python
class SmartHome:
    def __init__(self):
        self.rooms = {
            "Living Room": {
                "Curtain": "closed",
                "Light1": "off",
                "Light2": "off"
            },
            "Bedroom": {
                "Curtain": "closed",
                "Light1": "off",
                "Light2": "off"
            },
            "Bathroom": {
                "Light": "off"
            },
            "Kitchen": {
                "Light": "off"
            }
        }

    def execute_plan(self, plan_name):
        if plan_name == "morning":
            self.morning_plan()
        elif plan_name == "leave_home":
            self.leave_home_plan()
        elif plan_name == "movie":
            self.movie_plan()
        else:
            print("Invalid plan name.")

    def morning_plan(self):
        print("Executing Morning Plan: 打开窗帘 (Open Curtains)")
        for room in self.rooms:
            if "Curtain" in self.rooms[room]:
                self.rooms[room]["Curtain"] = "open"
        self.print_status()

    def leave_home_plan(self):
        print("Executing Leave Home Plan: 关灯 (Turn off Lights)")
        for room in self.rooms:
            for device in self.rooms[room]:
                if "Light" in device:
                    self.rooms[room][device] = "off"
        self.print_status()

    def movie_plan(self):
        print("Executing Movie Plan: 调节灯光亮度 (Adjust Light Intensity)")
        for room in self.rooms:
            for device in self.rooms[room]:
                if "Light" in device:
                    self.rooms[room][device] = "dimmed"
        self.print_status()

    def print_status(self):
        for room, devices in self.rooms.items():
            print(f"{room}:")
            for device, state in devices.items():
                print(f"  {device}: {state}")
        print("\n")

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python smart_home.py [plan_name]")
        print("plan_name options: morning, leave_home, movie")
        sys.exit(1)

    plan_name = sys.argv[1].lower()
    smart_home = SmartHome()
    smart_home.execute_plan(plan_name)
# ```
# 
# ### Instructions to Run the Application
# 
# 1. **Save the Script**: Save the above Python script in a file named `smart_home.py`.
# 
# 2. **Run the Command**: Open your Linux terminal and navigate to the directory containing `smart_home.py`.
# 
# 3. **Execute the Application**: Run the application with one of the following commands based on the desired plan:
# 
#    ```bash
#    python smart_home.py morning
#    ```
# 
#    ```bash
#    python smart_home.py leave_home
#    ```
# 
#    ```bash
#    python smart_home.py movie
#    ```
# 
# ### Explanation
# 
# - **Initialization**: The script initializes a `SmartHome` object that contains a dictionary representing the rooms and their smart devices.
# - **Plan Execution**: The `execute_plan` method determines which plan to execute based on the command-line argument.
# - **Plan Methods**: Each method (`morning_plan`, `leave_home_plan`, `movie_plan`) modifies the state of the relevant devices as per the functional description.
# - **Status Output**: After executing a plan, the current status of all devices is printed to the terminal.
# 
# This script simulates the actions of a smart home system based on your functional requirements and can be customized further for more complex interactions.