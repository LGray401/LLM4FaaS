# Here is the 'function.py' file based on the given functional description and the provided source code:

import time
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import Heater, AC, Humidifier, Light

def start_energy_saving_mode():
    # Get the home plan
    home = home_plan()

    # Get the required sensors and actuators
    temperature_sensors = get_room_sensors(home, "LivingRoom")
    heater_actuators = get_room_actuators(home, "LivingRoom")
    ac_actuators = get_room_actuators(home, "LivingRoom")
    humidifier_actuators = get_room_actuators(home, "LivingRoom")
    light_actuators = get_room_actuators(home, "LivingRoom")

    # Turn off the lights
    for light in light_actuators:
        light.turn_off()

    # Check the temperature and adjust the heater or AC accordingly
    while True:
        current_temperature = temperature_sensors[0].get_reading()

        if current_temperature < 18:
            # Turn on the heater
            for heater in heater_actuators:
                heater.turn_on()
            for ac in ac_actuators:
                ac.turn_off()
        elif current_temperature > 22:
            # Turn on the AC
            for ac in ac_actuators:
                ac.turn_on()
            for heater in heater_actuators:
                heater.turn_off()
        else:
            # Turn off both the heater and AC
            for heater in heater_actuators:
                heater.turn_off()
            for ac in ac_actuators:
                ac.turn_off()

        # Check the humidity and adjust the humidifiers accordingly
        for humidifier in humidifier_actuators:
            current_humidity = humidifier.get_reading()
            if current_humidity < 40:
                humidifier.increase_humidity()
            elif current_humidity > 60:
                humidifier.decrease_humidity()

        time.sleep(60)

if __name__ == "__main__":
    start_energy_saving_mode()