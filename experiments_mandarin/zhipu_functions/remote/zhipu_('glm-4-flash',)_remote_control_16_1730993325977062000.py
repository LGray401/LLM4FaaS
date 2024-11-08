# Based on your functional description and provided source code, here's a `function.py` file for your smart home project:

# function.py

import importlib
from home_plan import home_plan

def main():
    # Load home plan
    home = home_plan()
    
    # Get all sensors of a specific type
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    print(f"Found {len(indoor_temp_sensors)} indoor temperature sensors:")
    for sensor in indoor_temp_sensors:
        print(sensor.id)
    
    # Get all actuators of a specific type
    lights = get_all_actuators(home, "Light")
    print(f"Found {len(lights)} lights:")
    for light in lights:
        print(light.id)
    
    # Perform actions on sensors and actuators
    for sensor in indoor_temp_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            print(f"Indoor temperature in {sensor.room_name}: {reading}°C")
    
    for light in lights:
        if light.get_status() == "off":
            light.turn_on()
            print(f"Light {light.id} turned ON")
        else:
            light.turn_off()
            print(f"Light {light.id} turned OFF")

if __name__ == "__main__":
    main()