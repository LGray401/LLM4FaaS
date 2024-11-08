# To create a smart home application based on your functional description and layout, we'll focus on implementing the energy-saving modes you described: "降温1" and "降温2". These modes involve controlling windows and curtains based on temperature and light conditions. Below is a Python script that simulates this functionality. We'll use a simple command-line interface to trigger the energy-saving modes.
# 
# ### Python Script: `smart_home.py`
# 
# ```python
import random

class SmartHome:
    def __init__(self):
        # Simulate sensor data
        self.indoor_temp = random.uniform(20, 30)  # Indoor temperature in Celsius
        self.outdoor_temp = random.uniform(15, 35)  # Outdoor temperature in Celsius
        self.light_intensity = random.uniform(300, 1000)  # Light intensity in Lux
        
        # Simulate device states
        self.window_open = False
        self.curtain_closed = False

    def energy_saving_mode_1(self):
        # "降温1": 室外温度低于室内温度，开窗。
        if self.outdoor_temp < self.indoor_temp:
            self.window_open = True
            print("Energy Saving Mode 1: Opening windows because outdoor temperature is lower than indoor.")
        else:
            self.window_open = False
            print("Energy Saving Mode 1: Closing windows because outdoor temperature is not lower than indoor.")

    def energy_saving_mode_2(self):
        # "降温2": 室内温度低于室外温度，日照强烈，拉帘。
        if self.indoor_temp < self.outdoor_temp and self.light_intensity > 500:
            self.curtain_closed = True
            print("Energy Saving Mode 2: Closing curtains because indoor temperature is lower and sunlight is strong.")
        else:
            self.curtain_closed = False
            print("Energy Saving Mode 2: Opening curtains because conditions are not met.")

    def get_status(self):
        print(f"Indoor Temperature: {self.indoor_temp:.2f}°C")
        print(f"Outdoor Temperature: {self.outdoor_temp:.2f}°C")
        print(f"Light Intensity: {self.light_intensity:.2f} Lux")
        print(f"Window is {'open' if self.window_open else 'closed'}.")
        print(f"Curtain is {'closed' if self.curtain_closed else 'open'}.")

def main():
    home = SmartHome()
    home.get_status()
    
    print("\nActivating Energy Saving Mode 1...")
    home.energy_saving_mode_1()
    print("\nActivating Energy Saving Mode 2...")
    home.energy_saving_mode_2()

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# 1. Save the above code to a file named `smart_home.py`.
# 2. Open a terminal in the directory where you saved the file.
# 3. Run the following command to execute the application:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation
# 
# - The script simulates sensor data for indoor and outdoor temperatures and light intensity using random values.
# - Two methods, `energy_saving_mode_1` and `energy_saving_mode_2`, implement the logic for opening windows and closing curtains based on the conditions described.
# - The `get_status` method prints the current state of the sensors and devices.
# - The `main` function creates an instance of the `SmartHome` class, displays the current sensor readings, and activates both energy-saving modes.