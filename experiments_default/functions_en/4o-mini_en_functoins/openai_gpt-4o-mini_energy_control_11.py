# Here is the `function.py` file that implements the required functionality of opening windows when the temperature is above 26 degrees. This file will utilize the classes from your existing source code files.

# functions/function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH
from home.actuator import Window

def open_windows_if_temperature_high():
    home = home_plan()
    
    # Get all indoor temperature sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    
    # Iterate through each sensor and check the readings
    for sensor in temperature_sensors:
        sensor.turn_on()  # Ensure the sensor is on
        temperature = sensor.get_reading()
        
        if temperature is not None and temperature > 26:
            print(f"Temperature in {sensor.room_name} is {temperature}°C. Opening windows.")
            # Get all windows in the same room as the sensor
            windows = get_all_actuators(home, "Window")
            for window in windows:
                if window.room_name == sensor.room_name:
                    window.turn_on()  # Open the window

def main():
    open_windows_if_temperature_high()

if __name__ == "__main__":
    main()