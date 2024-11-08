# Based on your functional description "关闭客厅灯" (which translates to "Turn off the living room lights") and the smart home layout you've provided, I’ll create a simple Python script that simulates turning off the lights in the living room. This script will be designed to run in a Linux terminal.
# 
# Here's a basic implementation:
# 
# ```python
# smart_home.py

class SmartHome:
    def __init__(self):
        # Initialize the state of devices in each room
        self.rooms = {
            "Living Room": {
                "Lights": [True, True],  # Assuming two lights, both initially on
                # Other devices...
            },
            # Other rooms...
        }

    def turn_off_living_room_lights(self):
        # Turn off all lights in the living room
        for i in range(len(self.rooms["Living Room"]["Lights"])):
            self.rooms["Living Room"]["Lights"][i] = False
        print("Living room lights have been turned off.")

    def show_status(self):
        # Display the status of lights in the living room
        lights_status = self.rooms["Living Room"]["Lights"]
        status = ["off" if not light else "on" for light in lights_status]
        print(f"Living room lights status: {status}")

def main():
    home = SmartHome()
    print("Initial status of living room lights:")
    home.show_status()
    
    home.turn_off_living_room_lights()
    
    print("Updated status of living room lights:")
    home.show_status()

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run:
# 
# 1. Save the above code into a file named `smart_home.py`.
# 
# 2. Open a terminal and navigate to the directory where `smart_home.py` is saved.
# 
# 3. Run the script with the following command:
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script initializes a smart home system with the living room lights turned on. It then turns off the living room lights and displays the status before and after the action. The output will show the change in the state of the lights in the living room.