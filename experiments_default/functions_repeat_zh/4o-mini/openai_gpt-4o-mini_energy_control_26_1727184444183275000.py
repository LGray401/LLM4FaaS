# Based on the functional description provided, I will create a `function.py` file that incorporates the logic for controlling the window operations based on the state of the air conditioning and the temperature readings. This file will include the main function to bring everything together.
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH
from home.actuator import Window, AC
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from time import sleep

def control_windows(home):
    for room in home:
        # Check for AC in the room
        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
        indoor_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        outdoor_sensors = [sensor for sensor in room.sensors if isinstance(sensor, OutdoorTemperatureSensor)]

        if acs:
            ac = acs[0]  # Assuming one AC per room
            indoor_temp = indoor_sensors[0].get_reading() if indoor_sensors else None
            outdoor_temp = outdoor_sensors[0].get_reading() if outdoor_sensors else None

            # If AC is on, close the windows
            if ac.get_status() == "on":
                for window in windows:
                    window.turn_off()  # Close the windows
                print(f"Windows closed in {room.name} because AC is ON.")

            # If indoor temperature is high and outdoor temperature is low, open the windows
            elif indoor_temp is not None and outdoor_temp is not None:
                if indoor_temp > TEMP_HIGH and outdoor_temp < TEMP_HIGH:
                    for window in windows:
                        window.turn_on()  # Open the windows
                    print(f"Windows opened in {room.name} because indoor temperature is high and outdoor temperature is low.")

def main():
    # Create the home plan
    home = home_plan()

    # Main control loop
    while True:
        control_windows(home)
        sleep(5)  # Check every 5 seconds (adjust as necessary)

if __name__ == "__main__":
    main()