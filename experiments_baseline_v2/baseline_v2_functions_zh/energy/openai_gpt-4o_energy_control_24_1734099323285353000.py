# To create a smart home application based on your functional description and the provided code, we need to implement the "energy-saving mode" logic. This involves:
# 
# 1. **Cooling Strategy 1**: If the outdoor temperature is lower than the indoor temperature, open the window.
# 2. **Cooling Strategy 2**: If the indoor temperature is lower than the outdoor temperature and the sunlight is strong, close the curtains.
# 
# We'll create a Python script named `smart_home.py` that uses the components from the `home` folder to implement these strategies.
# 
# Here's the code for `smart_home.py`:
# 
# ```python
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Window, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import LIGHT_INTENSITY_HIGH

def energy_saving_mode(home):
    for room in home:
        # Get the sensors and actuators for this room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Find the relevant sensors and actuators
        indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        outdoor_temp_sensor = next((s for s in sensors if isinstance(s, OutdoorTemperatureSensor)), None)
        light_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)

        windows = [a for a in actuators if isinstance(a, Window)]
        curtains = [a for a in actuators if isinstance(a, Curtain)]

        # Turn on the sensors to get readings
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_on()
            indoor_temp = indoor_temp_sensor.get_reading()

        if outdoor_temp_sensor:
            outdoor_temp_sensor.turn_on()
            outdoor_temp = outdoor_temp_sensor.get_reading()

        if light_sensor:
            light_sensor.turn_on()
            light_intensity = light_sensor.get_reading()

        # Strategy 1: If outdoor temperature is lower, open windows
        if outdoor_temp_sensor and indoor_temp_sensor:
            if outdoor_temp < indoor_temp:
                for window in windows:
                    window.turn_on()

        # Strategy 2: If indoor temperature is lower but sunlight is strong, close curtains
        if indoor_temp_sensor and outdoor_temp_sensor and light_sensor:
            if indoor_temp < outdoor_temp and light_intensity > LIGHT_INTENSITY_HIGH:
                for curtain in curtains:
                    curtain.turn_off()

if __name__ == "__main__":
    home = home_plan()
    energy_saving_mode(home)
# ```
# 
# ### Explanation
# 
# - We import necessary classes from the `home` module.
# - We define a function `energy_saving_mode` that iterates over each room in the home.
# - For each room, we get all the sensors and actuators.
# - We turn on the sensors to get the current readings for temperature and light intensity.
# - We implement the two strategies:
#   - **Strategy 1**: If the outdoor temperature is lower than the indoor temperature, open the windows.
#   - **Strategy 2**: If the indoor temperature is lower than the outdoor temperature and the light intensity is high, close the curtains.
# - Finally, the script is set to run the `energy_saving_mode` function when executed directly.
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, you'll use the following command:
# 
# ```bash
# python smart_home.py
# ```
# 
# This assumes that the `smart_home.py` script is in the same directory as the `home` folder containing the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files. Make sure all these files are in the same directory to ensure proper module imports.