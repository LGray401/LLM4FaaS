# To create a smart home application based on your functional description and layout, we'll design a simple Python application that simulates the monitoring and control of smart devices in your home. The application will take inputs for temperature, humidity, and light intensity, and then adjust the smart devices accordingly. We will focus on creating a basic structure that you can expand upon.
# 
# Here's a simple version of this application:
# 
# ```python
import sys

class SmartHome:
    def __init__(self, temperature, humidity, light_intensity):
        self.temperature = temperature
        self.humidity = humidity
        self.light_intensity = light_intensity
        self.setup_devices()

    def setup_devices(self):
        # Initialize devices based on room layout
        self.living_room_devices = {
            "lights": 2,
            "windows": 2,
            "sockets": 2,
            "door": 1,
            "heater": 1,
            "AC": 1,
            "curtain": 1,
            "humidifier": 1,
            "cleaning_robot": 1,
            "music_player": 1,
            "TV": 1,
            "notification_sender": 1
        }
        
        self.bedroom_devices = {
            "lights": 2,
            "windows": 1,
            "curtain": 1,
            "AC": 1,
            "heater": 1,
            "music_player": 1,
            "door": 1,
            "sockets": 2,
            "cleaning_robot": 1,
            "humidifier": 1
        }
        
        self.bathroom_devices = {
            "lights": 1,
            "windows": 1,
            "heater": 1,
            "door": 1,
            "sockets": 2
        }
        
        self.kitchen_devices = {
            "lights": 1,
            "windows": 1,
            "heater": 1,
            "coffee_machine": 1,
            "sockets": 3,
            "door": 1
        }
        
        self.balcony_devices = {
            "door": 1
        }

    def control_devices(self):
        # Simulate controlling devices based on the current environmental conditions
        if self.temperature > 25:
            print("Turning on AC...")
        elif self.temperature < 18:
            print("Turning on heater...")
        
        if self.humidity < 30:
            print("Turning on humidifier...")
        
        if self.light_intensity < 50:
            print("Turning on lights...")
        else:
            print("Turning off lights...")

    def display_status(self):
        print(f"Temperature: {self.temperature}°C")
        print(f"Humidity: {self.humidity}%")
        print(f"Light Intensity: {self.light_intensity}/100")
        self.control_devices()

def main():
    if len(sys.argv) != 4:
        print("Usage: python smart_home.py <temperature> <humidity> <light_intensity>")
        return

    temperature = float(sys.argv[1])
    humidity = float(sys.argv[2])
    light_intensity = float(sys.argv[3])

    home = SmartHome(temperature, humidity, light_intensity)
    home.display_status()

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run
# 
# 1. Save the above code in a file named `smart_home.py`.
# 2. Open a terminal on your Linux system.
# 3. Navigate to the directory where you saved the `smart_home.py` file.
# 4. Run the following command:
# 
# ```bash
# python smart_home.py 27 80 80
# ```
# 
# This command will simulate the smart home environment with the given temperature, humidity, and light intensity, and will print actions taken by the smart devices based on these conditions.
# 
# You can modify the code to add more sophisticated logic for each device and room, or integrate with actual hardware or APIs if necessary.