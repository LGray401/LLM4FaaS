# To create a smart home application in Python based on your provided functional description and layout, we need to implement the following functionalities:
# 
# 1. **Adjust Light Brightness**: Based on the light intensity sensor, control the lights in each room.
# 2. **Control Indoor Temperature**: Using temperature sensors, manage the heating and air conditioning in each room.
# 3. **Operate Curtains**: Open or close curtains based on user preferences or sensor data.
# 4. **Humidifier Control**: Adjust humidity using the humidifiers based on humidity sensor readings.
# 
# Let's outline a simple Python script to achieve this. We'll also create a command-line interface to run the script.
# 
# First, let's assume you have some classes that represent the devices and sensors. For simplicity, we'll mock these classes:
# 
# ```python
class Sensor:
    def __init__(self, sensor_type, initial_value=0):
        self.type = sensor_type
        self.value = initial_value

    def read_value(self):
        # Simulate reading sensor value
        return self.value

class SmartDevice:
    def __init__(self, device_type):
        self.type = device_type

    def set_state(self, state):
        print(f"{self.type} set to {state}")

class Room:
    def __init__(self, name, sensors, devices):
        self.name = name
        self.sensors = {sensor.type: sensor for sensor in sensors}
        self.devices = {device.type: device for device in devices}

    def adjust_lighting(self):
        light_intensity = self.sensors['Light Intensity'].read_value()
        for device in self.devices.values():
            if device.type == 'Light':
                if light_intensity < 300:  # Example threshold
                    device.set_state('ON')
                else:
                    device.set_state('OFF')

    def control_temperature(self):
        temperature = self.sensors['Temperature'].read_value()
        if temperature < 20:  # Example threshold for heating
            if 'Heater' in self.devices:
                self.devices['Heater'].set_state('ON')
            if 'AC' in self.devices:
                self.devices['AC'].set_state('OFF')
        elif temperature > 25:  # Example threshold for cooling
            if 'AC' in self.devices:
                self.devices['AC'].set_state('ON')
            if 'Heater' in self.devices:
                self.devices['Heater'].set_state('OFF')

    def operate_curtains(self):
        # A simple implementation for curtain control
        if 'Curtain' in self.devices:
            # Example logic to close curtains if too much light
            light_intensity = self.sensors['Light Intensity'].read_value()
            if light_intensity > 500:
                self.devices['Curtain'].set_state('CLOSED')
            else:
                self.devices['Curtain'].set_state('OPEN')

    def control_humidifier(self):
        humidity = self.sensors['Humidity'].read_value()
        if humidity < 30:
            if 'Humidifier' in self.devices:
                self.devices['Humidifier'].set_state('ON')
        else:
            if 'Humidifier' in self.devices:
                self.devices['Humidifier'].set_state('OFF')

def main():
    # Create rooms with sensors and devices
    living_room = Room("Living Room", [
            Sensor('Temperature', 22),
            Sensor('Humidity', 40),
            Sensor('Light Intensity', 250)
        ], [
            SmartDevice('Light'),
            SmartDevice('Heater'),
            SmartDevice('AC'),
            SmartDevice('Curtain'),
            SmartDevice('Humidifier')
        ])

    # Add more rooms similarly...

    # Example of adjusting devices based on sensor data
    living_room.adjust_lighting()
    living_room.control_temperature()
    living_room.operate_curtains()
    living_room.control_humidifier()

if __name__ == "__main__":
    main()
# ```
# 
# ### How to Run the Application
# 
# Save the script above to a file, for example, `smart_home.py`. Make sure you have Python installed on your Linux system. You can run this script from the terminal using the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This script offers a simplified example of how your smart home application might work. In a real-world application, you'd likely be interfacing with actual sensor and device APIs, handling more complex logic, and providing a user interface to configure preferences.