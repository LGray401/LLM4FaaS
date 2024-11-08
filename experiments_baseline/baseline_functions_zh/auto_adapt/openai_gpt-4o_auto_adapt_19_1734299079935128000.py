# To create a smart home application based on your functional description and layout, we need to implement a Python script that simulates the behavior of the smart home system. The application should respond to sensor inputs and control smart devices accordingly. Here's a basic implementation outline to get you started:
# 
# ```python
import random

class Sensor:
    def __init__(self, name):
        self.name = name
        self.value = 0

    def read_value(self):
        # Simulate reading a sensor value
        self.value = random.uniform(0, 100)
        return self.value

class Device:
    def __init__(self, name):
        self.name = name
        self.state = "off"

    def turn_on(self):
        self.state = "on"
        print(f"{self.name} is turned on.")

    def turn_off(self):
        self.state = "off"
        print(f"{self.name} is turned off.")

class SmartHome:
    def __init__(self):
        # Initialize sensors
        self.temperature_sensor = Sensor("Temperature Sensor")
        self.humidity_sensor = Sensor("Humidity Sensor")
        self.light_sensor = Sensor("Light Sensor")

        # Initialize devices
        self.ac = Device("AC")
        self.heater = Device("Heater")
        self.light = Device("Light")
        self.humidifier = Device("Humidifier")
        self.notification_sender = Device("Notification Sender")

    def check_environment(self):
        temperature = self.temperature_sensor.read_value()
        humidity = self.humidity_sensor.read_value()
        light_intensity = self.light_sensor.read_value()

        print(f"Temperature: {temperature:.2f}")
        print(f"Humidity: {humidity:.2f}")
        print(f"Light Intensity: {light_intensity:.2f}")

        # Control logic
        if temperature > 30:  # 太热了
            self.ac.turn_on()
            self.heater.turn_off()
        elif temperature < 20:
            self.heater.turn_on()
            self.ac.turn_off()
        else:
            self.ac.turn_off()
            self.heater.turn_off()

        if humidity < 30:  # 太干了
            self.humidifier.turn_on()
        else:
            self.humidifier.turn_off()

        if light_intensity > 70:  # 太亮了
            self.light.turn_off()
        else:
            self.light.turn_on()

    def run(self):
        # Simulate continuous monitoring
        while True:
            self.check_environment()
            user_input = input("Press Enter to recheck or type 'exit' to quit: ")
            if user_input.lower() == 'exit':
                break

if __name__ == "__main__":
    home = SmartHome()
    home.run()
# ```
# 
# ### Explanation:
# 
# 1. **Sensors**: Simulated with random values to mimic real sensor readings.
# 2. **Devices**: Can be turned on or off based on conditions.
# 3. **SmartHome Class**: Manages sensors and devices, checking conditions like too hot, too dry, and too bright.
# 4. **Control Logic**: Adjusts devices based on readings.
# 
# ### Running the Script:
# 
# 1. Save the code to a file, e.g., `smart_home.py`.
# 2. Run the script in a Linux terminal with the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Note:
# - The script uses random values for sensor readings for demonstration purposes.
# - Adjust thresholds and add more complex logic as needed to fit your specific requirements.