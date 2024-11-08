# Given your functional description and the provided source code, here's a `function.py` file that you can add to your project. This file will include a `main` function that will simulate the smart home system's operation based on the current temperature, humidity, and light intensity values provided.

# function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

# Main function
def main():
    # Create the home plan with all the rooms and their components
    home = home_plan()
    
    # Simulate the environment conditions
    current_temperature = 24  # Celsius
    current_humidity = 30  # Percentage
    current_light_intensity = 45  # Lux
    
    # Check the environment conditions and take actions
    for room in home:
        # Process all sensors in the room
        for sensor in room.sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                print(f"Indoor Temperature in {room.name}: {sensor.get_reading()}°C")
            elif isinstance(sensor, HumiditySensor):
                print(f"Humidity in {room.name}: {sensor.get_reading}%")
            elif isinstance(sensor, LightIntensiveSensor):
                print(f"Light Intensity in {room.name}: {sensor.get_reading()} Lux")
        
        # Process all actuators in the room
        for actuator in room.actuators:
            if isinstance(actuator, Heater) and current_temperature < TEMP_LOW:
                actuator.turn_on()
                print(f"Heater in {room.name} turned ON due to low temperature.")
            elif isinstance(actuator, AC) and current_temperature > TEMP_HIGH:
                actuator.turn_on()
                print(f"AC in {room.name} turned ON due to high temperature.")
            elif isinstance(actuator, Humidifier) and current_humidity < HUMIDITY_LOW:
                actuator.increase_humidity()
                print(f"Humidifier in {room.name} turned ON to increase humidity.")
            elif isinstance(actuator, Humidifier) and current_humidity > HUMIDITY_HIGH:
                actuator.decrease_humidity()
                print(f"Humidifier in {room.name} turned ON to decrease humidity.")
            elif isinstance(actuator, Light) and current_light_intensity < LIGHT_INTENSITY_LOW:
                actuator.turn_on()
                print(f"Light in {room.name} turned ON due to low light intensity.")
            elif isinstance(actuator, Light) and current_light_intensity > LIGHT_INTENSITY_HIGH:
                actuator.turn_off()
                print(f"Light in {room.name} turned OFF due to high light intensity.")
    
    print("Home system simulation complete.")

if __name__ == "__main__":
    main()