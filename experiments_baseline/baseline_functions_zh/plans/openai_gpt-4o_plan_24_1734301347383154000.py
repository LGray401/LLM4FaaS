# Certainly! Based on your functional description and smart home layout, I'll provide a Python application that you can run from a Linux terminal. This application will simulate the different plans you outlined: Morning Plan, Leave Home Plan, and Movie Plan. We'll assume that the sensors provide data and that the smart devices can be controlled via simple commands.
# 
# Below is a simple Python script to achieve this:
# 
# ```python
import random

# Simulated sensor readings
def get_light_intensity():
    # Simulate light intensity (0 to 1000 lux)
    return random.randint(0, 1000)

def get_weather():
    # Simulate weather condition
    return random.choice(['Sunny', 'Cloudy', 'Rainy'])

# Smart Device control functions
def control_device(device, action):
    print(f"{action.capitalize()} {device}")

def morning_plan():
    print("Executing Morning Plan...")
    control_device('Curtain', 'open')
    if get_weather() == 'Cloudy':
        control_device('Light', 'turn on')
    control_device('Coffee Machine', 'start brewing')
    print("Coffee is ready!")
    control_device('Music Player', 'play music')

def leave_home_plan():
    print("Executing Leave Home Plan...")
    if get_weather() == 'Sunny':
        control_device('Curtain', 'open')
    control_device('Light', 'turn off')
    control_device('Socket', 'turn off')
    control_device('Door', 'lock')

def movie_plan():
    print("Executing Movie Plan...")
    control_device('Curtain', 'close')
    control_device('Light', 'turn off')

def main():
    print("Welcome to the Smart Home Application")
    print("Choose a plan to execute:")
    print("1. Morning Plan")
    print("2. Leave Home Plan")
    print("3. Movie Plan")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        morning_plan()
    elif choice == '2':
        leave_home_plan()
    elif choice == '3':
        movie_plan()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Instructions to Run the Script
# 
# 1. Save the above script to a file named `smart_home.py`.
# 
# 2. Open your Linux terminal.
# 
# 3. Navigate to the directory where `smart_home.py` is saved.
# 
# 4. Run the script using the following command:
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This script simulates your smart home environment by controlling devices based on the predefined plans. It uses mock functions to simulate sensor data and weather conditions. You can further enhance this by integrating actual hardware or APIs for real-time data and control.