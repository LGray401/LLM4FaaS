# Based on the provided functional description and the existing code in your smart home project, I will create the `function.py` file to implement a main function that integrates the functionalities of the sensors and actuators.
# 
# Here’s the code for `function.py`:

# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Create the home plan
    home = home_plan()

    # Get sensors and actuators from the Living Room
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    
    if living_room:
        temperature_sensor = next((sensor for sensor in living_room.sensors if sensor.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((sensor for sensor in living_room.sensors if sensor.sensor_type == "Humidity"), None)
        light_sensor = next((sensor for sensor in living_room.sensors if sensor.sensor_type == "LightIntensive"), None)

        heater = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "Heater"), None)
        ac = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "AC"), None)
        humidifier = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "Humidifier"), None)
        light = next((actuator for actuator in living_room.actuators if actuator.actuator_type == "Light"), None)

        # Turn on sensors
        if temperature_sensor:
            temperature_sensor.turn_on()
            current_temp = temperature_sensor.get_reading()
        
        if humidity_sensor:
            humidity_sensor.turn_on()
            current_humidity = humidity_sensor.get_reading()

        if light_sensor:
            light_sensor.turn_on()
            current_light = light_sensor.get_reading()

        # Control the heater and AC based on temperature
        if current_temp is not None:
            if current_temp < TEMP_LOW:
                if heater:
                    heater.set_target_temperature(22)  # Set to a comfortable temperature
                    heater.adjust_temperature(current_temp)
            elif current_temp > TEMP_HIGH:
                if ac:
                    ac.set_target_temperature(22)  # Set to a comfortable temperature
                    ac.adjust_temperature(current_temp)

        # Control the humidifier based on humidity
        if current_humidity is not None:
            if current_humidity < HUMIDITY_LOW:
                if humidifier:
                    humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                if humidifier:
                    humidifier.decrease_humidity()

        # Control the light based on light intensity
        if current_light is not None:
            if current_light < LIGHT_INTENSITY_LOW:
                if light:
                    light.turn_on()
            elif current_light > LIGHT_INTENSITY_HIGH:
                if light:
                    light.turn_off()
        
        # Log the current status
        logger.info(f"Current Temperature: {current_temp}°C, Humidity: {current_humidity}%, Light Intensity: {current_light} lux")
    
    else:
        logger.warning("Living Room not found in home plan.")


if __name__ == "__main__":
    main()