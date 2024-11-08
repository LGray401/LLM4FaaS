# Sure! Here is the 'function.py' file that you requested:

import sys
sys.path.append('home')

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators

def main():
    functional_description = '''
    Temperature:
    今日26度

    Humidity:
    今日湿度，45

    Light Intensity:
    今日光照75'''

    print(functional_description)

    # Specify the path to the 'home' folder
    home_folder_path = 'home'

    # Specify the path to the 'functions' folder
    functions_folder_path = 'functions'

    # Add the 'home' folder to the system path
    sys.path.append(home_folder_path)

    # Import the required modules from the 'home' folder
    from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
    from home.actuator import Light

    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get the room named 'LivingRoom'
    living_room = get_room(home, 'LivingRoom')

    # Get the sensors in the 'LivingRoom'
    living_room_sensors = get_room_sensors(home, 'LivingRoom')

    # Get the actuators in the 'LivingRoom'
    living_room_actuators = get_room_actuators(home, 'LivingRoom')

    # Get all the sensors of type 'IndoorTemperature'
    temperature_sensors = get_all_sensors(home, 'IndoorTemperature')

    # Get all the actuators of type 'Light'
    lights = get_all_actuators(home, 'Light')

    # Use the sensors and actuators as needed
    for sensor in living_room_sensors:
        sensor.get_reading()

    for actuator in living_room_actuators:
        actuator.turn_on()

    for temperature_sensor in temperature_sensors:
        temperature = temperature_sensor.get_reading()
        print(f"Temperature: {temperature}°C")

    for light in lights:
        light.set_brightness_level('medium')
        light.get_status()

if __name__ == '__main__':
    main()