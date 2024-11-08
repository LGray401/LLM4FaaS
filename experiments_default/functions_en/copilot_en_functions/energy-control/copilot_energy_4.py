# Based on the content of the markdown file, you are working on a smart home project and you need a `function.py` file. This file should be located in the 'functions' folder and should contain the main function. The main function should be based on the functional description provided, which is "Open windows to cool down".
#
# The `function.py` file should interact with the four existing Python files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) in your 'home' folder. These files contain various classes and functions related to sensors and actuators in a smart home environment.
#
# Here is a basic structure of the `function.py` file:
#
# ```python
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH

def main():
    # Get the home plan
    home = home_plan()

    # Get all indoor and outdoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")

    # Get all windows
    windows = get_all_actuators(home, "Window")

    # Iterate over each room's sensors
    for indoor_temp_sensor, outdoor_temp_sensor in zip(indoor_temp_sensors, outdoor_temp_sensors):
        # If the indoor temperature is higher than the threshold and outdoor temperature is lower than indoor temperature
        if indoor_temp_sensor.get_reading() > TEMP_HIGH and outdoor_temp_sensor.get_reading() < indoor_temp_sensor.get_reading():
            # Open all windows in the room
            for window in windows:
                if window.room_name == indoor_temp_sensor.room_name:
                    window.turn_on()

if __name__ == "__main__":
    main()
# ```
#
# This `main` function in `function.py` will check the readings from all indoor and outdoor temperature sensors in each room. If the indoor temperature is higher than the threshold (defined in `config.py`) and the outdoor temperature is lower than the indoor temperature, it will open all windows in that room.