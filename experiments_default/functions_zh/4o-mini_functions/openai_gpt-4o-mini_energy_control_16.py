# Based on your functional description focusing on energy saving, I will create a `function.py` file that utilizes the existing sensor and actuator classes to monitor environmental conditions and adjust actuators accordingly. This will include turning on/off lights, heaters, and AC units based on temperature and humidity readings, promoting energy efficiency.
# 
# Here is the content of the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def energy_saving_mode(home):
    for room in home:
        print(f"\nChecking room: {room.name}")
        
        # Retrieve sensors and actuators in the room
        sensors = room.sensors
        actuators = room.actuators
        
        # Initialize variables to hold readings
        temperature = None
        humidity = None
        
        # Get readings from sensors
        for sensor in sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                temperature = sensor.get_reading()
            elif isinstance(sensor, HumiditySensor):
                humidity = sensor.get_reading()
        
        # Make decisions based on readings
        if temperature is not None:
            if temperature < TEMP_LOW:
                # Turn on the heater
                for actuator in actuators:
                    if isinstance(actuator, Heater):
                        actuator.set_target_temperature(TEMP_HIGH)
                        actuator.adjust_temperature(temperature)
            elif temperature > TEMP_HIGH:
                # Turn on the AC
                for actuator in actuators:
                    if isinstance(actuator, AC):
                        actuator.set_target_temperature(TEMP_LOW)
                        actuator.adjust_temperature(temperature)
            else:
                # Temperature is within range, turn off any heating or cooling
                for actuator in actuators:
                    if isinstance(actuator, Heater) or isinstance(actuator, AC):
                        actuator.turn_off()
        
        if humidity is not None:
            if humidity < HUMIDITY_LOW:
                # Turn on the humidifier
                for actuator in actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.increase_humidity()
            elif humidity > HUMIDITY_HIGH:
                # Turn off the humidifier
                for actuator in actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.decrease_humidity()

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Activate energy saving mode
    energy_saving_mode(home)

if __name__ == "__main__":
    main()