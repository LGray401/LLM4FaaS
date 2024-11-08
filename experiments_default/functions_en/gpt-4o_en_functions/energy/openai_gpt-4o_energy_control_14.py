# Based on the given functional description and the provided source code, here is the `function.py` file that you can place in the 'functions' folder of your project. This file contains the main function to launch the Earth Environmental Protection Plan.

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor
from home.actuator import Light, AC, Heater, Humidifier

def main():
    print("Launching the Earth Environmental Protection Plan")

    # Create home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Turn on all Light sensors and actuators
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    
    for sensor in light_sensors:
        sensor.turn_on()
        
    for light in lights:
        light.turn_on()

    # Turn on all Indoor Temperature sensors and adjust ACs and Heaters
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")
    
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        
    for ac in acs:
        ac.turn_on()
        
    for heater in heaters:
        heater.turn_on()

    # Turn on all Humidity sensors and adjust Humidifiers
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        
    for humidifier in humidifiers:
        humidifier.turn_on()

    print("All sensors and actuators have been activated as part of the Earth Environmental Protection Plan.")

if __name__ == "__main__":
    main()