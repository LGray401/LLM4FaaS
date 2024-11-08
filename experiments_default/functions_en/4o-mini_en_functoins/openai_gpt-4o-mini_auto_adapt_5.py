# Based on your functional description and the provided code files, I'll create a `function.py` file that includes a main function to demonstrate the behavior of your smart home system. The script will utilize the sensors and actuators to manage the temperature, humidity, and light intensity based on predefined values.
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Define the target values
    target_temperature = 24
    target_humidity = 30
    target_light_intensity = 45

    # Initialize the home plan
    home = home_plan()

    # Iterate through rooms and control actuators based on sensor readings
    for room in home:
        print(f"\nChecking room: {room.name}")

        # Get sensors and actuators for the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Process temperature
        temperature_sensor = next((s for s in sensors if s.sensor_type == "IndoorTemperature"), None)
        if temperature_sensor:
            temperature_sensor.turn_on()
            current_temp = temperature_sensor.get_reading()
            if current_temp is not None:
                heater = next((a for a in actuators if a.actuator_type == "Heater"), None)
                ac = next((a for a in actuators if a.actuator_type == "AC"), None)
                
                if current_temp < target_temperature:
                    if heater:
                        heater.set_target_temperature(target_temperature)
                        heater.adjust_temperature(current_temp)
                elif current_temp > target_temperature:
                    if ac:
                        ac.set_target_temperature(target_temperature)
                        ac.adjust_temperature(current_temp)

        # Process humidity
        humidity_sensor = next((s for s in sensors if s.sensor_type == "Humidity"), None)
        if humidity_sensor:
            humidity_sensor.turn_on()
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                humidifier = next((a for a in actuators if a.actuator_type == "Humidifier"), None)
                if current_humidity < target_humidity and humidifier:
                    humidifier.increase_humidity()
                elif current_humidity > target_humidity and humidifier:
                    humidifier.decrease_humidity()

        # Process light intensity
        light_sensor = next((s for s in sensors if s.sensor_type == "LightIntensive"), None)
        if light_sensor:
            light_sensor.turn_on()
            current_light_intensity = light_sensor.get_reading()
            if current_light_intensity is not None:
                light = next((a for a in actuators if a.actuator_type == "Light"), None)
                if current_light_intensity < target_light_intensity and light:
                    light.turn_on()
                    light.set_brightness_level("high")
                elif current_light_intensity > target_light_intensity and light:
                    light.turn_off()

if __name__ == "__main__":
    main()