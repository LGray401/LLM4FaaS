# To create a smart home application based on your functional description and layout, I'll write a Python script that controls the appropriate devices based on the sensors' readings. The application will be designed to run in a Linux terminal with a single command.
# 
# Here's a proposed outline of the Python application:
# 
# ```python
class SmartHome:
    def __init__(self):
        self.rooms = {
            "Living Room": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": ["Light", "Window", "Socket", "Door", "Heater", "AC", "Curtain", "Humidifier", "Cleaning Robot", "Music Player", "TV", "Notification Sender"]
            },
            "Bedroom": {
                "sensors": ["Temperature", "Humidity", "Light Intensity"],
                "devices": ["Light", "Window", "Curtain", "AC", "Heater", "Music Player", "Door", "Socket", "Cleaning Robot", "Humidifier"]
            },
            "Bathroom": {
                "sensors": ["Temperature", "Humidity"],
                "devices": ["Light", "Window", "Heater", "Door", "Socket"]
            },
            "Kitchen": {
                "sensors": ["Humidity", "Smoke"],
                "devices": ["Light", "Window", "Heater", "Coffee Machine", "Socket", "Door"]
            },
            "Balcony": {
                "sensors": ["Temperature", "Humidity"],
                "devices": ["Door"]
            }
        }

    def adjust_temperature(self, target_temp=17):
        print(f"Setting temperature to {target_temp}°C.")
        # Code to set the temperature using AC/Heater

    def adjust_humidity(self):
        print("Adjusting humidity to normal levels.")
        # Code to control humidifiers

    def control_lights(self, action="off"):
        if action == "off":
            print("Turning off all lights.")
        else:
            print(f"Setting lights to {action} mode.")
        # Code to control lights

    def run(self):
        # Example logic to execute the functional requirements
        self.adjust_temperature(17)
        self.adjust_humidity()
        self.control_lights("off")

if __name__ == "__main__":
    home = SmartHome()
    home.run()
# ```
# 
# ### Explanation:
# 
# 1. **Temperature**: The `adjust_temperature` function sets the temperature to 17°C using available devices like AC or Heater in each room.
# 2. **Humidity**: The `adjust_humidity` function makes sure humidity is at normal levels using humidifiers.
# 3. **Light Intensity**: The `control_lights` function turns off all lights.
# 
# ### Running the Application:
# 
# To run this application from a Linux terminal, save the Python script to a file named `smart_home.py`. Then, use the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This command assumes you have Python 3 installed on your system. If you have specific hardware or interfaces to interact with the actual smart devices, you'll need to integrate those into the application where indicated by comments.