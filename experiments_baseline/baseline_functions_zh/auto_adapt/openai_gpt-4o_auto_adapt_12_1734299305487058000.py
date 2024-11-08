# Based on your functional description and smart home layout, I will create a simple Python application that simulates a smart home system. The application will use the sensor readings to make decisions about controlling the smart devices.
# 
# Here is a basic implementation in Python:
# 
# ```python
import sys

# Sensor readings as per the functional description
temperature = 22  # Temperature in Celsius
humidity = "适中"  # Moderate
light_intensity = "微弱"  # Weak

# Function to control the devices based on sensor readings
def control_smart_home():
    # Living Room
    print("Living Room:")
    if temperature < 22:
        print("  - Turning on the Heater")
    elif temperature > 22:
        print("  - Turning on the AC")
    else:
        print("  - Temperature is optimal")
    
    if humidity == "适中":
        print("  - Humidity is optimal")
    else:
        print("  - Adjusting Humidity")
    
    if light_intensity == "微弱":
        print("  - Turning on the Lights")
    else:
        print("  - Light intensity is sufficient")

    # Bedroom
    print("\nBedroom:")
    if temperature < 22:
        print("  - Turning on the Heater")
    elif temperature > 22:
        print("  - Turning on the AC")
    else:
        print("  - Temperature is optimal")
    
    if humidity == "适中":
        print("  - Humidity is optimal")
    else:
        print("  - Adjusting Humidity")

    if light_intensity == "微弱":
        print("  - Turning on the Lights")
    else:
        print("  - Light intensity is sufficient")

    # Bathroom
    print("\nBathroom:")
    if temperature < 22:
        print("  - Turning on the Heater")
    else:
        print("  - Temperature is optimal")
    
    if humidity == "适中":
        print("  - Humidity is optimal")
    else:
        print("  - Adjusting Humidity")

    # Kitchen
    print("\nKitchen:")
    if humidity == "适中":
        print("  - Humidity is optimal")
    else:
        print("  - Adjusting Humidity")

    # Note: The kitchen has a smoke sensor, which isn't covered by the provided functional description.

    # Balcony
    print("\nBalcony:")
    if temperature < 22:
        print("  - Door is closed to keep warmth inside")
    else:
        print("  - Door is open for fresh air")

# Main function to run the application
def main():
    control_smart_home()

if __name__ == "__main__":
    main()
# ```
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, follow these steps:
# 
# 1. Save the code in a file, for example, `smart_home.py`.
# 2. Open your terminal.
# 3. Navigate to the directory where `smart_home.py` is saved.
# 4. Run the script using the command:
#    
#    ```bash
#    python3 smart_home.py
#    ```
# 
# This command assumes you have Python 3 installed on your Linux system. If you don't have Python 3 installed, you can usually install it using your distribution's package manager. For example, on Ubuntu, you can install it with `sudo apt install python3`.