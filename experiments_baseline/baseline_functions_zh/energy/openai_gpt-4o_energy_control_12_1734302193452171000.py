# To create a smart home application that can run in a Linux terminal and activate energy-saving mode based on outdoor temperature and humidity, we'll write a Python script. This script will interact with sensors and smart devices in your smart home layout. I'll provide the logic for the energy-saving mode and the command to run it.
# 
# ### Python Script
# 
# ```python
import random

class SmartHome:
    def __init__(self):
        self.outdoor_temperature = None
        self.outdoor_humidity = None
        self.living_room_ac = False
        self.bedroom_ac = False
        self.heater_status = {
            "living_room": False,
            "bedroom": False,
            "bathroom": False,
            "kitchen": False
        }

    def get_outdoor_conditions(self):
        """Simulate getting conditions from outdoor sensors."""
        # In a real scenario, this would interface with actual sensors
        self.outdoor_temperature = random.uniform(-10, 40)  # Simulating -10 to 40 degrees Celsius
        self.outdoor_humidity = random.uniform(0, 100)  # Simulating 0 to 100% humidity
        print(f"Outdoor conditions - Temperature: {self.outdoor_temperature:.2f}°C, Humidity: {self.outdoor_humidity:.2f}%")

    def decide_ac_usage(self):
        """Decide whether to turn on or off AC based on outdoor conditions."""
        # Example logic: Turn on AC if temperature is greater than 25°C and humidity is above 60%
        if self.outdoor_temperature > 25 and self.outdoor_humidity > 60:
            self.living_room_ac = True
            self.bedroom_ac = True
        else:
            self.living_room_ac = False
            self.bedroom_ac = False

        self.update_ac_status()

    def update_ac_status(self):
        """Update AC status."""
        print(f"Living Room AC {'ON' if self.living_room_ac else 'OFF'}")
        print(f"Bedroom AC {'ON' if self.bedroom_ac else 'OFF'}")

    def run_energy_saving_mode(self):
        """Run the energy-saving mode."""
        self.get_outdoor_conditions()
        self.decide_ac_usage()

if __name__ == "__main__":
    smart_home = SmartHome()
    smart_home.run_energy_saving_mode()
# ```
# 
# ### Running the Script
# 
# To run this script in a Linux terminal, follow these steps:
# 
# 1. **Save the Script**: Save the above code in a file named `smart_home.py`.
# 
# 2. **Make the Script Executable**: Open a terminal and navigate to the directory where you saved `smart_home.py`. Run the following command to make the script executable:
#    ```bash
#    chmod +x smart_home.py
#    ```
# 
# 3. **Run the Script**: Execute the script with the following command:
#    ```bash
#    ./smart_home.py
#    ```
# 
# This script simulates outdoor conditions and decides whether to activate the air conditioning in the living room and bedroom based on the specified conditions. Adjust the logic as needed to match your specific requirements for energy-saving mode.