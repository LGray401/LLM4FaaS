# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control the smart home system. The main function will read the sensor values, compare them with the desired conditions (temperature 26°C, humidity 50%, light intensity moderate), and adjust the actuators accordingly.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Define the desired conditions
    desired_temperature = 26.0
    desired_humidity = 50.0
    desired_light_intensity = (LIGHT_INTENSITY_LOW + LIGHT_INTENSITY_HIGH) / 2  # Moderate light intensity
    
    # Iterate through each room in the home
    for room in home:
        # Get the sensors and actuators for the current room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)
        
        # Find the relevant sensors and actuators
        indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
        light_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)
        
        heater = next((a for a in actuators if isinstance(a, Heater)), None)
        ac = next((a for a in actuators if isinstance(a, AC)), None)
        humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
        light = next((a for a in actuators if isinstance(a, Light)), None)
        
        # Turn on the sensors
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_on()
        if humidity_sensor:
            humidity_sensor.turn_on()
        if light_sensor:
            light_sensor.turn_on()
        
        # Read the sensor values
        current_temperature = indoor_temp_sensor.get_reading() if indoor_temp_sensor else None
        current_humidity = humidity_sensor.get_reading() if humidity_sensor else None
        current_light_intensity = light_sensor.get_reading() if light_sensor else None
        
        # Adjust the temperature
        if current_temperature is not None:
            if current_temperature < desired_temperature:
                if heater:
                    heater.set_target_temperature(desired_temperature)
                    heater.adjust_temperature(current_temperature)
            elif current_temperature > desired_temperature:
                if ac:
                    ac.set_target_temperature(desired_temperature)
                    ac.adjust_temperature(current_temperature)
        
        # Adjust the humidity
        if current_humidity is not None:
            if current_humidity < desired_humidity:
                if humidifier:
                    humidifier.increase_humidity()
            elif current_humidity > desired_humidity:
                if humidifier:
                    humidifier.decrease_humidity()
        
        # Adjust the light intensity
        if current_light_intensity is not None:
            if current_light_intensity < desired_light_intensity:
                if light:
                    light.set_brightness_level("high")
            elif current_light_intensity > desired_light_intensity:
                if light:
                    light.set_brightness_level("low")
        
        # Turn off the sensors
        if indoor_temp_sensor:
            indoor_temp_sensor.turn_off()
        if humidity_sensor:
            humidity_sensor.turn_off()
        if light_sensor:
            light_sensor.turn_off()

if __name__ == "__main__":
    main()