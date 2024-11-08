# Based on your functional description and provided source code, I will create the `function.py` file for your smart home project. This file will incorporate a main function that simulates the interaction between sensors and actuators in your smart home system.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import LIGHT_INTENSITY_HIGH, HUMIDITY_HIGH, TEMP_HIGH
from home.logger_config import logger

def main():
    # Create the home with rooms and components
    home = home_plan()

    # Simulate readings from sensors
    for room in home:
        print(f"\n--- {room.name} ---")
        
        # Get sensor readings
        temperature_sensor = next((s for s in room.sensors if s.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((s for s in room.sensors if s.sensor_type == "Humidity"), None)
        light_sensor = next((s for s in room.sensors if s.sensor_type == "LightIntensive"), None)

        if temperature_sensor:
            temperature_sensor.turn_on()
            current_temp = temperature_sensor.get_reading()
            temperature_sensor.turn_off()
            logger.info(f"{room.name} - Current Temperature: {current_temp}°C")

        if humidity_sensor:
            humidity_sensor.turn_on()
            current_humidity = humidity_sensor.get_reading()
            humidity_sensor.turn_off()
            logger.info(f"{room.name} - Current Humidity: {current_humidity}%")

        if light_sensor:
            light_sensor.turn_on()
            current_light = light_sensor.get_reading()
            light_sensor.turn_off()
            logger.info(f"{room.name} - Current Light Intensity: {current_light} lux")

        # Control actuators based on sensor readings
        if current_temp is not None:
            if current_temp > TEMP_HIGH:
                ac = next((a for a in room.actuators if a.actuator_type == "AC"), None)
                if ac:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temp)

            elif current_temp < TEMP_LOW:
                heater = next((a for a in room.actuators if a.actuator_type == "Heater"), None)
                if heater:
                    heater.set_target_temperature(TEMP_LOW)
                    heater.adjust_temperature(current_temp)

        if current_humidity is not None:
            humidifier = next((a for a in room.actuators if a.actuator_type == "Humidifier"), None)
            if humidifier:
                if current_humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

        if current_light is not None:
            light = next((a for a in room.actuators if a.actuator_type == "Light"), None)
            if light:
                if current_light < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                elif current_light > LIGHT_INTENSITY_HIGH:
                    light.turn_off()

if __name__ == "__main__":
    main()