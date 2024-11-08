# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control the windows and air conditioners (ACs) in the living room and bedroom. The logic will be as follows:
# 
# 1. If the AC in the bedroom or living room is turned on, close the windows in that room.
# 2. If the indoor temperature is above 26 degrees Celsius and the outdoor temperature is below 26 degrees Celsius, open the windows in that room.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
from home.home_plan import home_plan, get_room_actuators, get_room_sensors
from home.config import TEMP_HIGH

def control_windows_and_ac():
    # Initialize the home plan
    home = home_plan()

    # Define the rooms to check
    rooms_to_check = ["LivingRoom", "Bedroom"]

    for room_name in rooms_to_check:
        # Get the sensors and actuators for the current room
        sensors = get_room_sensors(home, room_name)
        actuators = get_room_actuators(home, room_name)

        # Find the indoor and outdoor temperature sensors
        indoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)

        # Find the AC and window actuators
        ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
        windows = [actuator for actuator in actuators if isinstance(actuator, Window)]

        # Check if the AC is on
        if ac and ac.get_status() == "on":
            # Close all windows in the room
            for window in windows:
                window.turn_off()
            print(f"AC is on in {room_name}. Closing all windows.")
        else:
            # Check the indoor and outdoor temperatures
            if indoor_temp_sensor and outdoor_temp_sensor:
                indoor_temp = indoor_temp_sensor.get_reading()
                outdoor_temp = outdoor_temp_sensor.get_reading()

                if indoor_temp and outdoor_temp:
                    if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_HIGH:
                        # Open all windows in the room
                        for window in windows:
                            window.turn_on()
                        print(f"Indoor temperature in {room_name} is {indoor_temp}°C and outdoor temperature is {outdoor_temp}°C. Opening all windows.")
                    else:
                        # Close all windows in the room
                        for window in windows:
                            window.turn_off()
                        print(f"Indoor temperature in {room_name} is {indoor_temp}°C and outdoor temperature is {outdoor_temp}°C. Closing all windows.")
                else:
                    print(f"Could not get temperature readings for {room_name}.")
            else:
                print(f"Could not find temperature sensors for {room_name}.")

if __name__ == "__main__":
    control_windows_and_ac()