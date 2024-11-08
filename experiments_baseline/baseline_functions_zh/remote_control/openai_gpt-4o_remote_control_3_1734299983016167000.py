# To implement the functional requirement "关闭客厅的灯" (which translates to "Turn off the lights in the living room"), we can create a simple Python script that simulates this action. Since this is a smart home application, I'll assume you have some kind of smart home system API or a way to control the devices programmatically. For this example, I'll create a mock-up script that represents the functionality.
# 
# ```python
# smart_home.py

class SmartHome:
    def __init__(self):
        # Assume we have two lights in the living room
        self.living_room_lights = [True, True]  # True means the light is on

    def turn_off_living_room_lights(self):
        for i in range(len(self.living_room_lights)):
            self.living_room_lights[i] = False
        print("All living room lights are now off.")

def main():
    home = SmartHome()
    home.turn_off_living_room_lights()

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run the Script
# 
# 1. **Save the Script**: Save the above Python code into a file named `smart_home.py`.
# 
# 2. **Run the Script in a Linux Terminal**:
#    - Open your terminal.
#    - Navigate to the directory where `smart_home.py` is saved.
#    - Run the following command:
#      ```bash
#      python3 smart_home.py
#      ```
# 
# This script initializes a smart home scenario with two lights in the living room turned on. The method `turn_off_living_room_lights` turns off these lights and prints a confirmation message. This is a basic simulation and can be expanded to integrate with actual smart home devices or an API if available.