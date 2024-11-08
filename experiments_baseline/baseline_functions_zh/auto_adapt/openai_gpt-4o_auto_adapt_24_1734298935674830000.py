# To create a smart home application in Python that fulfills your functional description and runs in a Linux terminal with a single command, we will follow these steps:
# 
# 1. **Design the Application Structure**: We'll create a simple script that reads sensor data and controls smart devices based on the given rules for temperature, humidity, and light intensity.
# 
# 2. **Implement Sensor Reading and Device Control**: We'll simulate sensor readings and device controls in the code.
# 
# 3. **Define the Logic**: Based on your functional description, the application will:
#    - Keep the indoor temperature not higher than 26 degrees Celsius.
#    - Maintain humidity below 30%.
#    - Adjust light intensity by managing curtains and lights.
# 
# 4. **Create the Command to Run the Application**: We'll package everything into a single Python script that can be executed with one command.
# 
# Let's write the Python script:
# 
# ```python
import random
import time

# Sample functions to simulate sensor readings
def read_temperature(room):
    return random.uniform(20.0, 30.0)

def read_humidity(room):
    return random.uniform(20.0, 40.0)

def read_light_intensity(room):
    return random.uniform(200.0, 800.0)

# Sample functions to simulate device controls
def control_ac(room, state):
    print(f"{'Turning on' if state else 'Turning off'} AC in the {room}")

def control_heater(room, state):
    print(f"{'Turning on' if state else 'Turning off'} heater in the {room}")

def control_curtain(room, state):
    print(f"{'Opening' if state else 'Closing'} curtain in the {room}")

def control_light(room, state):
    print(f"{'Turning on' if state else 'Turning off'} light in the {room}")

def control_humidifier(room, state):
    print(f"{'Turning on' if state else 'Turning off'} humidifier in the {room}")

# Main control logic
def control_environment(room):
    temperature = read_temperature(room)
    humidity = read_humidity(room)
    light_intensity = read_light_intensity(room)

    print(f"{room} - Temperature: {temperature:.2f}°C, Humidity: {humidity:.2f}%, Light Intensity: {light_intensity:.2f} lux")

    # Control temperature
    if temperature > 26.0:
        control_ac(room, True)
        control_heater(room, False)
    else:
        control_ac(room, False)

    # Control humidity
    if humidity >= 30.0:
        control_humidifier(room, False)
    else:
        control_humidifier(room, True)

    # Control light intensity (simulated threshold values)
    if light_intensity < 300.0:
        control_light(room, True)
        control_curtain(room, False)
    elif light_intensity > 600.0:
        control_light(room, False)
        control_curtain(room, True)
    else:
        control_light(room, False)
        control_curtain(room, False)

def main():
    rooms = ["Living Room", "Bedroom", "Bathroom", "Kitchen"]
    while True:
        for room in rooms:
            if room != "Balcony":  # Balcony doesn't require indoor control
                control_environment(room)
        time.sleep(5)  # Simulate delay between sensor readings

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run the Application:
# 
# 1. **Save the Script**: Save the above script in a file named `smart_home.py`.
# 
# 2. **Command to Run**: Open your Linux terminal and navigate to the directory containing `smart_home.py`. Run the script using the following command:
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script simulates the reading of sensors and controlling of devices in your smart home based on the functional description and layout you provided. It prints actions to the console, simulating what a real system might do. Adjust the sensor reading functions and control logic as needed to integrate with actual sensors and devices in a real smart home setup.