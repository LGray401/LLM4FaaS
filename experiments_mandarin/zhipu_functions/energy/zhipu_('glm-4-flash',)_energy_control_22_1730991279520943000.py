# Based on the provided functional description and the source code from the sensor.py, actuator.py, home_plan.py, and config.py, I will create a function.py file with a main function to handle the smart home automation tasks as described.
# 
# Here's the `function.py` file located in the `functions` folder:

import time
from home_plan import home_plan
from sensor import SmokeSensor
from actuator import Actuator

# Load the home plan
home = home_plan()

def main():
    # Function to handle kitchen smoke sensor
    def handle_kitchen_smoke():
        kitchen_smoke_sensor = get_room_sensors(home, "Kitchen")[0]
        while True:
            smoke_level = kitchen_smoke_sensor.get_reading()
            if smoke_level is not None and smoke_level > 50:  # Assuming 50 is the threshold for smoke level
                print("Smoke detected in the kitchen!")
                # Assuming Actuator class has a method to turn on the smoke alarm
                smoke_alarm = get_room_actuators(home, "SmokeAlarm")[0]
                smoke_alarm.turn_on()
            time.sleep(1)  # Check every second

    # Function to handle AC based on temperature
    def handle_ac():
        ac = get_room_actuators(home, "AC")[0]
        while True:
            indoor_temp = get_room_sensors(home, "LivingRoom")[0].get_reading()
            if indoor_temp is not None:
                if indoor_temp < 20:
                    ac.turn_off()
                elif indoor_temp > 25:
                    ac.turn_on()
            time.sleep(1)  # Check every second

    # Start the kitchen smoke detection and AC handling
    kitchen_smoke_thread = threading.Thread(target=handle_kitchen_smoke)
    ac_thread = threading.Thread(target=handle_ac)
    kitchen_smoke_thread.start()
    ac_thread.start()

    kitchen_smoke_thread.join()
    ac_thread.join()

if __name__ == "__main__":
    main()