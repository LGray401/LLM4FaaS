# To create a Python application that can run in a Linux terminal and perform the task of turning off the lights in the living room, we can create a simple script that simulates this functionality. 
# 
# Here's a Python script that represents this functionality:
# 
# ```python
# smart_home.py

class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} is now OFF.")

class LivingRoom:
    def __init__(self):
        self.lights = [SmartDevice("Living Room Light 1"), SmartDevice("Living Room Light 2")]

    def turn_off_lights(self):
        for light in self.lights:
            light.turn_off()

def main():
    living_room = LivingRoom()
    living_room.turn_off_lights()

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run the Script
# 
# 1. Save the script above to a file named `smart_home.py`.
# 
# 2. Open your terminal and navigate to the directory where the `smart_home.py` file is located.
# 
# 3. Run the script using the following command:
#    ```bash
#    python3 smart_home.py
#    ```
#    
# This script defines a `SmartDevice` class and a `LivingRoom` class. The `LivingRoom` class contains two light devices, and the `turn_off_lights` method turns off all the lights in the living room. The `main` function initializes the `LivingRoom` and calls the method to turn off the lights, simulating the action described in the functional description.