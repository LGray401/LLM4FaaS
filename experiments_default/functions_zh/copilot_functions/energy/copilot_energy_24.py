# Based on the functional description and the provided source code, you want to create a `function.py` file that implements an energy-saving mode for a smart home system. The energy-saving mode has two conditions:
#
# 1. If the outdoor temperature is lower than the indoor temperature, open the window.
# 2. If the indoor temperature is lower than the outdoor temperature and the sunlight is strong, close the curtain.
#
# Here is the Python code that implements these functionalities:
#
# ```python
from home.home_plan import get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.config import LIGHT_INTENSITY_HIGH

def energy_saving_mode(home):
    # Get all necessary sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    light_sensors = get_all_sensors(home, "LightIntensive")
    windows = get_all_actuators(home, "Window")
    curtains = get_all_actuators(home, "Curtain")

    # Check each room
    for room in home:
        # Get the room's sensors and actuators
        indoor_temp_sensor = next((s for s in indoor_temp_sensors if s.room_name == room.name), None)
        outdoor_temp_sensor = next((s for s in outdoor_temp_sensors if s.room_name == room.name), None)
        light_sensor = next((s for s in light_sensors if s.room_name == room.name), None)
        window = next((a for a in windows if a.room_name == room.name), None)
        curtain = next((a for a in curtains if a.room_name == room.name), None)

        # If the room has all necessary sensors and actuators
        if indoor_temp_sensor and outdoor_temp_sensor and light_sensor and window and curtain:
            # Get the current readings
            indoor_temp = indoor_temp_sensor.get_reading()
            outdoor_temp = outdoor_temp_sensor.get_reading()
            light_intensity = light_sensor.get_reading()

            # Implement the energy-saving mode
            if indoor_temp and outdoor_temp and light_intensity:
                if outdoor_temp < indoor_temp:
                    window.turn_on()  # Open the window
                elif indoor_temp < outdoor_temp and light_intensity > LIGHT_INTENSITY_HIGH:
                    curtain.turn_on()  # Close the curtain
# ```
#
# This function should be placed in the `function.py` file in the `functions` folder. It goes through each room in the home, checks the current readings from the necessary sensors, and controls the window and curtain actuators based on the energy-saving mode conditions. The function uses the `get_all_sensors` and `get_all_actuators` functions from `home_plan.py` to get all sensors and actuators of a certain type in the home.