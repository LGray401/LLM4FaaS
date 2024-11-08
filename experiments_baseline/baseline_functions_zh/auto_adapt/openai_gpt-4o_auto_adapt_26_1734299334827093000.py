# To create a smart home application that manages temperature, humidity, and light intensity as per your specifications, we can develop a Python script that simulates these functionalities. The script will control smart devices based on sensor readings and user activity. Since the script should be executable with a single command, we'll encapsulate all logic within a Python file and provide a command to execute it.
# 
# Here's an outline of how such an application might be implemented:
# 
# 1. **Sensors and Devices Simulation**: We'll simulate sensors and devices, as actual hardware interaction would require specific libraries and hardware access.
# 
# 2. **Functional Logic**:
#    - Maintain indoor temperature at 26°C.
#    - Maintain indoor humidity at 60%.
#    - Adjust light intensity based on activity: bright for work, dim for relaxation, and off during rest.
# 
# 3. **User Activities**: Define activities (e.g., working, relaxing, resting) that determine light settings.
# 
# 4. **Python Script**: Below is a basic implementation of the smart home application.
# 
# ```python
import time
import random

class SmartHome:
    def __init__(self):
        # Initial state of the house
        self.temperature = 24.0
        self.humidity = 50.0
        self.light_intensity = "off"  # "bright", "dim", "off"
        self.activity = "resting"  # "working", "relaxing", "resting"

    def read_sensors(self):
        # Simulate reading from sensors
        # Adding random fluctuation to simulate real sensor reading
        self.temperature += random.uniform(-0.5, 0.5)
        self.humidity += random.uniform(-1, 1)
        print(f"Sensors -> Temperature: {self.temperature:.2f}°C, Humidity: {self.humidity:.2f}%")

    def control_temperature(self):
        if self.temperature < 26:
            print("Turning on heater to increase temperature.")
        elif self.temperature > 26:
            print("Turning on AC to decrease temperature.")
        else:
            print("Temperature is optimal.")

    def control_humidity(self):
        if self.humidity < 60:
            print("Turning on humidifier to increase humidity.")
        elif self.humidity > 60:
            print("Turning off humidifier to decrease humidity.")
        else:
            print("Humidity is optimal.")

    def control_lighting(self):
        if self.activity == "working":
            self.light_intensity = "bright"
        elif self.activity == "relaxing":
            self.light_intensity = "dim"
        elif self.activity == "resting":
            self.light_intensity = "off"
        print(f"Setting light intensity to: {self.light_intensity}")

    def update_activity(self, new_activity):
        self.activity = new_activity
        print(f"Activity updated to: {self.activity}")

    def run(self):
        while True:
            self.read_sensors()
            self.control_temperature()
            self.control_humidity()
            self.control_lighting()
            time.sleep(5)  # Wait for a while before repeating

if __name__ == "__main__":
    home = SmartHome()
    home.update_activity("working")  # Set initial activity
    try:
        home.run()
    except KeyboardInterrupt:
        print("Smart Home System Stopped.")
# ```
# 
# ### Running the Application
# 
# 1. **Save the script**: Save the above Python code to a file, e.g., `smart_home.py`.
# 
# 2. **Command to Run**: To run the application from a Linux terminal, use the following command:
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script provides a basic simulation of your smart home application. It continuously monitors and adjusts the temperature, humidity, and lighting based on simulated sensor readings and user activity. Adjustments can be made to refine the simulation or to integrate real hardware interfaces if needed.