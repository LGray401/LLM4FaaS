# Based on your functional description and the provided source code, I will create a `function.py` file that implements a main function to control the smart home system. This function will utilize the sensors and actuators to maintain the desired temperature, humidity, and light intensity in a room.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Create the home with rooms and their components
    home = home_plan()

    # Example room to monitor; you can change this to any room you wish to manage
    target_room_name = "LivingRoom"
    target_room = next((room for room in home if room.name == target_room_name), None)

    if not target_room:
        print(f"Room {target_room_name} not found!")
        logger.error(f"Room {target_room_name} not found!")
        return

    # Turn on all sensors in the room
    for sensor in target_room.sensors:
        sensor.turn_on()

    # Get readings from sensors
    temperature_sensor = next((s for s in target_room.sensors if s.sensor_type == "IndoorTemperature"), None)
    humidity_sensor = next((s for s in target_room.sensors if s.sensor_type == "Humidity"), None)
    light_sensor = next((s for s in target_room.sensors if s.sensor_type == "LightIntensive"), None)

    # Turn on all actuators in the room
    for actuator in target_room.actuators:
        actuator.turn_on()

    # Control logic based on sensor readings
    current_temperature = temperature_sensor.get_reading() if temperature_sensor else None
    current_humidity = humidity_sensor.get_reading() if humidity_sensor else None
    current_light_intensity = light_sensor.get_reading() if light_sensor else None

    # Control heating/cooling based on temperature
    heater = next((a for a in target_room.actuators if a.actuator_type == "Heater"), None)
    ac = next((a for a in target_room.actuators if a.actuator_type == "AC"), None)

    if current_temperature is not None:
        if current_temperature < TEMP_LOW:
            if heater:
                heater.set_target_temperature(TEMP_HIGH)  # Set to a comfortable temperature
                heater.adjust_temperature(current_temperature)
        elif current_temperature > TEMP_HIGH:
            if ac:
                ac.set_target_temperature(TEMP_LOW)  # Set to a comfortable temperature
                ac.adjust_temperature(current_temperature)

    # Control humidity
    humidifier = next((a for a in target_room.actuators if a.actuator_type == "Humidifier"), None)
    
    if current_humidity is not None:
        if current_humidity < HUMIDITY_LOW:
            if humidifier:
                humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH:
            if humidifier:
                humidifier.decrease_humidity()

    # Control light intensity
    light = next((a for a in target_room.actuators if a.actuator_type == "Light"), None)
    
    if current_light_intensity is not None:
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            if light:
                light.turn_on()  # Turn on the light if intensity is too low
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            if light:
                light.turn_off()  # Turn off the light if intensity is too high

    # Print final statuses
    print(f"\n--- Status of {target_room_name} ---")
    for sensor in target_room.sensors:
        sensor.get_status()
    for actuator in target_room.actuators:
        actuator.get_status()

if __name__ == "__main__":
    main()