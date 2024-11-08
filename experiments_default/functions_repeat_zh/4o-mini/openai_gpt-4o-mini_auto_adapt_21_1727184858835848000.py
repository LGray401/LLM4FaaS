# Based on your functional description and the provided source code, I will create a `function.py` file that implements the required functionalities for your smart home project. 
# 
# This file will monitor temperature, humidity, and light intensity and will control actuators (like the AC and curtains) accordingly. Below is the `function.py` code:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain

def main():
    # Initialize home layout with rooms and their components
    home = home_plan()
    
    # Iterate through each room to monitor sensors and control actuators
    for room in home:
        # Get sensors and actuators in the room
        temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        humidity_sensors = [sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)]
        light_sensors = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]
        
        ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
        
        # Monitor temperature
        for sensor in temp_sensors:
            sensor.turn_on()  # Turn on the sensor to get readings
            temperature = sensor.get_reading()
            if temperature is not None:
                if temperature > TEMP_HIGH:  # If temperature is higher than 26°C
                    for ac in ac_units:
                        ac.set_target_temperature(26)  # Set AC target temperature
                        ac.adjust_temperature(temperature)  # Adjust AC based on current temperature

        # Monitor humidity
        for sensor in humidity_sensors:
            sensor.turn_on()  # Turn on the sensor to get readings
            humidity = sensor.get_reading()
            if humidity is not None:
                # Here you can implement humidity control logic if needed
                pass  # Currently, humidity regulation is normal as per description

        # Monitor light intensity
        for sensor in light_sensors:
            sensor.turn_on()  # Turn on the sensor to get readings
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                if light_intensity > LIGHT_INTENSITY_HIGH:  # If light intensity is high
                    for curtain in curtains:
                        curtain.turn_on()  # Open curtains

if __name__ == '__main__':
    main()