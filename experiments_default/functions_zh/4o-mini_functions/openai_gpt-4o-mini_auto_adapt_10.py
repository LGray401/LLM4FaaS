# Sure! Based on the functional description and the provided source code, here is the `function.py` that will contain the `main` function to simulate the behavior of your smart home system. This function will check the current temperature, humidity, and light intensity, and then take appropriate actions based on the readings.

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW
from home.logger_config import logger

def main():
    # Get the home plan
    home = home_plan()

    # Assuming we are checking the first room (LivingRoom) for this example
    living_room = home[0]

    # Read sensors
    temperature_sensor = living_room.sensors[0]  # IndoorTemperatureSensor
    humidity_sensor = living_room.sensors[1]     # HumiditySensor
    light_sensor = living_room.sensors[2]        # LightIntensiveSensor

    # Turn on sensors to get readings
    temperature_sensor.turn_on()
    humidity_sensor.turn_on()
    light_sensor.turn_on()

    current_temperature = temperature_sensor.get_reading()
    current_humidity = humidity_sensor.get_reading()
    current_light_intensity = light_sensor.get_reading()

    # Check temperature
    if current_temperature is not None:
        if current_temperature < TEMP_LOW:
            heater = living_room.actuators[0]  # Assuming first actuator is Heater
            heater.set_target_temperature(TEMP_LOW)
            heater.adjust_temperature(current_temperature)
        elif current_temperature > TEMP_HIGH:
            ac = living_room.actuators[1]  # Assuming second actuator is AC
            ac.set_target_temperature(TEMP_HIGH)
            ac.adjust_temperature(current_temperature)

    # Check humidity
    if current_humidity is not None:
        if current_humidity < HUMIDITY_LOW:
            humidifier = living_room.get_actuators("Humidifier")[0]  # Get the humidifier
            humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH:
            humidifier = living_room.get_actuators("Humidifier")[0]  # Get the humidifier
            humidifier.decrease_humidity()

    # Check light intensity
    if current_light_intensity is not None:
        light = living_room.get_actuators("Light")[0]  # Get the first light actuator
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            light.turn_off()

    # Logging the results
    logger.info(f"Current temperature: {current_temperature}°C")
    logger.info(f"Current humidity: {current_humidity}%")
    logger.info(f"Current light intensity: {current_light_intensity} lux")

if __name__ == "__main__":
    main()