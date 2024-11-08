# To create a smart home application that implements an "Energy Saving Mode" (节能模式), we can use the provided files as references and build a main control script to adjust the behavior of the actuators and sensors accordingly. Here is how we can implement this:
# 
# ### New Python File: `smart_home.py`
# 
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Curtain
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def energy_saving_mode(home):
    # Turn off all unnecessary lights
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

    # Adjust temperature settings for energy saving
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        heaters = get_all_actuators(home, "Heater")
        ac_units = get_all_actuators(home, "AC")
        
        for heater in heaters:
            heater.set_target_temperature(TEMP_LOW)
            heater.adjust_temperature(current_temp)
        
        for ac in ac_units:
            ac.set_target_temperature(TEMP_HIGH)
            ac.adjust_temperature(current_temp)

    # Adjust curtain settings for natural light
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()  # Let's assume turning on the curtain means opening it

    # Print status for confirmation
    print("Energy Saving Mode is now active.")

if __name__ == "__main__":
    home = home_plan()
    energy_saving_mode(home)
# ```
# 
# ### Explanation
# 
# - **Lights**: All lights are turned off to conserve energy.
# - **Temperature Control**: Heaters and AC units are adjusted to maintain a temperature range that is energy-efficient (e.g., using lower heating and higher cooling settings).
# - **Curtains**: Open curtains to use natural light and reduce the need for artificial lighting.
# 
# ### Command to Run the Application
# 
# To execute this script in a Linux terminal, navigate to the directory containing the `smart_home.py` file and run:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# This command will activate the energy-saving mode by adjusting the actuators and sensors as described in the script. Make sure the Python environment is correctly set up and the `home` directory containing the reference files is in the same directory or the Python path is properly configured.