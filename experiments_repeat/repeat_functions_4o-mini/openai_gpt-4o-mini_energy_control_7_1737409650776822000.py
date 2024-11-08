# Based on your functional description and existing code, here's the implementation for the `function.py` file. This file will include the main function to handle the following logic:
# 
# 1. When the AC is turned on, it will automatically close any doors and windows in the same room.
# 2. If the indoor temperature is higher than the target temperature set for the AC, and the outdoor temperature is lower than the indoor temperature, it will ask the user whether to open the windows to cool down the room.
# 
# Here’s the implementation of `function.py`:
# 
# ```python
# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH
from home.actuator import AC, Window, Door
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor

def main():
    # Initialize the home layout
    home = home_plan()

    # Example room name for demonstration
    room_name = "LivingRoom"

    # Get the sensors and actuators in the specified room
    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    # Find the AC, windows, and doors in the room
    ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
    windows = [actuator for actuator in actuators if isinstance(actuator, Window)]
    doors = [actuator for actuator in actuators if isinstance(actuator, Door)]

    # Turn on the AC
    if ac:
        ac.turn_on()
        # Close all windows and doors when AC is turned on
        for window in windows:
            window.turn_off()  # Assuming turning off means closing the window
            print(f"{window.id} is now closed.")

        for door in doors:
            door.lock()  # Assuming locking means securing the door
            print(f"{door.id} is now locked.")

        # Get the current indoor and outdoor temperatures
        indoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)

        if indoor_temp_sensor and outdoor_temp_sensor:
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()

            print(f"Indoor Temperature: {indoor_temp}°C, Outdoor Temperature: {outdoor_temp}°C")

            # Check if the indoor temperature is higher than the AC target temperature
            if indoor_temp > TEMP_HIGH and outdoor_temp < indoor_temp:
                user_input = input("The indoor temperature is high. Do you want to open the windows to cool down? (yes/no): ")
                if user_input.lower() == 'yes':
                    for window in windows:
                        window.turn_on()  # Assuming turning on means opening the window
                        print(f"{window.id} is now opened.")
                else:
                    print("Keeping the windows closed.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - The `main` function initializes the home layout and retrieves all sensors and actuators in the specified room.
# - It finds the AC, windows, and doors and turns on the AC.
# - When the AC is turned on, it closes all windows and locks the doors.
# - It retrieves the current indoor and outdoor temperatures and checks if the indoor temperature exceeds the defined threshold while the outdoor temperature is lower.
# - If the conditions are met, it prompts the user whether to open the windows to cool down.
# 
# ### Instructions:
# - Make sure to place this code in the `functions` folder as `function.py`.
# - Adjust the room name in the `main` function as needed for your specific use case.