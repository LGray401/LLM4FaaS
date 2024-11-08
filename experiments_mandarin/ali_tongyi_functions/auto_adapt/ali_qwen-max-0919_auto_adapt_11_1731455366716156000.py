# Based on your functional description and the provided source code, I will create a `function.py` file that contains the main function to control the smart home system. This function will check the sensor readings for temperature, humidity, and light intensity, and automatically turn on the air conditioner (AC) if any of the conditions are met.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    # Initialize the home plan
    home = home_plan()
    
    while True:
        # Iterate over each room in the home
        for room in home:
            # Get the sensors and actuators for the current room
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)
            
            # Find the AC actuator in the current room
            ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
            if not ac:
                print(f"No AC found in {room.name}.")
                continue
            
            # Check the sensor readings and control the AC
            for sensor in sensors:
                if isinstance(sensor, IndoorTemperatureSensor):
                    reading = sensor.get_reading()
                    if reading and reading > TEMP_HIGH:
                        print(f"Temperature in {room.name} is {reading}°C, which is above {TEMP_HIGH}°C. Turning on AC.")
                        ac.turn_on()
                
                elif isinstance(sensor, HumiditySensor):
                    reading = sensor.get_reading()
                    if reading and reading > HUMIDITY_LOW:
                        print(f"Humidity in {room.name} is {reading}%, which is above {HUMIDITY_LOW}%. Turning on AC.")
                        ac.turn_on()
                
                elif isinstance(sensor, LightIntensiveSensor):
                    reading = sensor.get_reading()
                    if reading and reading > LIGHT_INTENSITY_HIGH:
                        print(f"Light intensity in {room.name} is {reading} lux, which is above {LIGHT_INTENSITY_HIGH} lux. Turning on AC.")
                        ac.turn_on()
        
        # Wait for a short period before checking again
        time.sleep(5)

if __name__ == "__main__":
    main()