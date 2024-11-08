# To develop a smart home application based on the provided functional description and layout, we need to simulate the control of various smart devices and sensors. Let's create a Python script that handles the specified conditions:
# 
# 1. Activate the smoke alarm when smoke levels in the kitchen are too high.
# 2. In summer, turn off the AC when the indoor temperature is below 20°C and turn it on when above 25°C.
# 3. Implement motion-activated lights that turn on when someone is present and off when no one is detected.
# 
# Here's a simple implementation in Python:
# 
# ```python
import time

class SmartHome:
    def __init__(self):
        self.kitchen_smoke_level = 0
        self.indoor_temperature = 22  # Example temperature
        self.motion_detected = False
    
    def check_smoke(self):
        if self.kitchen_smoke_level > 5:  # Assuming 5 is the threshold for smoke
            self.activate_smoke_alarm()

    def activate_smoke_alarm(self):
        print("Smoke alarm activated in the kitchen!")

    def control_ac(self, season='summer'):
        if season == 'summer':
            if self.indoor_temperature < 20:
                self.turn_off_ac()
            elif self.indoor_temperature > 25:
                self.turn_on_ac()

    def turn_on_ac(self):
        print("AC turned on.")

    def turn_off_ac(self):
        print("AC turned off.")

    def control_lights(self):
        if self.motion_detected:
            self.turn_on_lights()
        else:
            self.turn_off_lights()

    def turn_on_lights(self):
        print("Lights turned on.")

    def turn_off_lights(self):
        print("Lights turned off.")

    def run(self):
        while True:
            self.check_smoke()
            self.control_ac()
            self.control_lights()
            time.sleep(5)  # Pause for 5 seconds before next check

if __name__ == "__main__":
    home = SmartHome()
    home.run()
# ```
# 
# ### Running the Application
# 
# 1. Save the script to a file, `smart_home.py`.
# 2. Run the script in a Linux terminal using the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - **Smoke Detection**: The `check_smoke` function simulates checking the smoke level in the kitchen. If the level exceeds a certain threshold, it activates the smoke alarm.
# - **AC Control**: The `control_ac` function simulates turning the AC on or off based on the indoor temperature. The conditions are checked only during the summer as specified.
# - **Motion-Activated Lights**: The `control_lights` function checks for motion and turns the lights on or off accordingly.
# 
# **Note**: This script is a basic simulation. In a real-world application, you'd replace sensor readings and device control with actual API calls to smart home devices.