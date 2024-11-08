# Sure, I can help you create a `function.py` file that will activate the energy-saving mode of your smart home system. 
# 
# Based on the provided code, it seems that energy-saving mode would likely involve turning off unnecessary devices and adjusting the settings of actuators like heaters and AC units to more energy-efficient levels.
# 
# Here is an implementation of `function.py` that will activate energy-saving mode:
# 
# ## function.py

from home.home_plan import home_plan, get_all_actuators, get_all_sensors
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW

def activate_energy_saving_mode():
    # Create the home plan
    home = home_plan()

    # Turn off all actuation devices except for heaters and AC units
    actuators_to_turn_off = ['Light', 'Window', 'Curtain', 'MusicPlayer', 'SmartSocket', 'CleaningRobot', 'SmartTV', 'NotificationSender', 'CoffeeMachine', 'Door', 'Humidifier']

    for actuator_type in actuators_to_turn_off:
        actuators = get_all_actuators(home, actuator_type)
        for actuator in actuators:
            actuator.turn_off()

    # Adjust heaters and AC units to energy-saving temperatures
    heaters = get_all_actuators(home, 'Heater')
    ac_units = get_all_actuators(home, 'AC')

    for heater in heaters:
        heater.turn_on()
        heater.set_target_temperature(TEMP_LOW)

    for ac in ac_units:
        ac.turn_on()
        ac.set_target_temperature(TEMP_HIGH)

    print("Energy saving mode activated.")

if __name__ == "__main__":
    activate_energy_saving_mode()