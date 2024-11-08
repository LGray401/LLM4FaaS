# Based on your functional description and the provided source code for your smart home project, here's the implementation of the `function.py` file. This file will contain the main function that checks the temperature and opens the window if the temperature is above 26 degrees Celsius.

# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_HIGH
from home.actuator import Window
from home.sensor import IndoorTemperatureSensor

def main():
    # Create the home plan
    home = home_plan()
    
    # Get all indoor temperature sensors
    temperature_sensors = []
    for room in home:
        temperature_sensors.extend(room.sensors)

    # Assuming we want to check the first indoor temperature sensor found
    for sensor in temperature_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            sensor.turn_on()  # Make sure the sensor is on
            current_temperature = sensor.get_reading()  # Get the current temperature reading
            if current_temperature is not None:
                print(f"Current temperature in {sensor.room_name} is: {current_temperature}°C")
                if current_temperature > 26:
                    # Open the window if the temperature is above 26 degrees
                    window = next((actuator for actuator in room.actuators if isinstance(actuator, Window)), None)
                    if window:
                        window.turn_on()  # Open the window
                        print(f"Opened the window in {room.name} due to high temperature.")
                    else:
                        print(f"No window actuator found in {room.name}.")
            else:
                print("Failed to read temperature.")
            break  # Exit after checking the first sensor

if __name__ == "__main__":
    main()