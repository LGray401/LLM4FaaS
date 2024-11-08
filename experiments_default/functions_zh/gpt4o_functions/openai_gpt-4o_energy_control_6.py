# Based on your functional description and the provided source code, here's the 'function.py' file located in the 'functions' folder. This script will initiate the energy-saving mode by turning off unnecessary devices and adjusting other devices to lower energy consumption.

# functions/function.py

from home.home_plan import home_plan, get_all_actuators, get_all_sensors
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def initiate_energy_saving_mode(home):
    # Turn off unnecessary devices
    actuators_to_turn_off = ["SmartTV", "MusicPlayer", "CoffeeMachine", "CleaningRobot"]
    for actuator_type in actuators_to_turn_off:
        actuators = get_all_actuators(home, actuator_type)
        for actuator in actuators:
            actuator.turn_off()

    # Adjust AC and Heater to energy-saving temperatures
    acs = get_all_actuators(home, "AC")
    for ac in acs:
        ac.set_target_temperature(TEMP_HIGH)  # Setting AC to the higher threshold to save energy
        ac.adjust_temperature(ac.target_temperature)

    heaters = get_all_actuators(home, "Heater")
    for heater in heaters:
        heater.set_target_temperature(TEMP_LOW)  # Setting Heater to the lower threshold to save energy
        heater.adjust_temperature(heater.target_temperature)

    # Turn off Lights if the light intensity is high
    lights = get_all_actuators(home, "Light")
    light_sensors = get_all_sensors(home, "LightIntensive")
    for light_sensor in light_sensors:
        light_sensor.turn_on()
        light_intensity = light_sensor.get_reading()
        if light_intensity and light_intensity > LIGHT_INTENSITY_HIGH:
            for light in lights:
                light.turn_off()

    # Adjust Humidifiers
    humidifiers = get_all_actuators(home, "Humidifier")
    humidity_sensors = get_all_sensors(home, "Humidity")
    for humidity_sensor in humidity_sensors:
        humidity_sensor.turn_on()
        humidity = humidity_sensor.get_reading()
        if humidity and (humidity < HUMIDITY_LOW or humidity > HUMIDITY_HIGH):
            for humidifier in humidifiers:
                if humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

    print("Energy-saving mode initiated.")


if __name__ == "__main__":
    home = home_plan()
    initiate_energy_saving_mode(home)