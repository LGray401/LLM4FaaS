# Based on the provided functional description and the existing code in your smart home project, I will create the `function.py` file. This file will contain a main function that uses the sensors and actuators to monitor and respond to the specified conditions for temperature, humidity, and light intensity.
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import NotificationSender, Heater, AC, Light
from home.logger_config import logger

def main():
    # Initialize the home plan
    home = home_plan()

    # Define thresholds based on functional description
    target_temperature = 22  # Target temperature in Celsius
    humidity_status = "Moderate"  # Moderate humidity condition
    light_intensity_status = "Weak"  # Weak light intensity condition

    # Get the sensors and actuators
    living_room = next(room for room in home if room.name == "LivingRoom")
    temperature_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor))
    humidity_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, HumiditySensor))
    light_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor))

    notification_sender = next(actuator for actuator in living_room.actuators if isinstance(actuator, NotificationSender))
    heater = next(actuator for actuator in living_room.actuators if isinstance(actuator, Heater))
    ac = next(actuator for actuator in living_room.actuators if isinstance(actuator, AC))
    light_actuator = next(actuator for actuator in living_room.actuators if isinstance(actuator, Light))

    # Turn on sensors to get readings
    temperature_sensor.turn_on()
    humidity_sensor.turn_on()
    light_sensor.turn_on()

    # Get current readings
    current_temperature = temperature_sensor.get_reading()
    current_humidity = humidity_sensor.get_reading()
    current_light_intensity = light_sensor.get_reading()

    # Decision making based on readings
    if current_temperature is not None:
        if current_temperature < target_temperature:
            heater.set_target_temperature(target_temperature)
            heater.adjust_temperature(current_temperature)
        elif current_temperature > target_temperature:
            ac.set_target_temperature(target_temperature)
            ac.adjust_temperature(current_temperature)

    # Notify user based on humidity status
    if current_humidity is not None:
        if current_humidity < 30:  # Assuming 30% is low humidity
            notification_sender.notification_sender("Humidity is too low! Consider using a humidifier.")
        elif current_humidity > 50:  # Assuming 50% is high humidity
            notification_sender.notification_sender("Humidity is too high! Consider using a dehumidifier.")

    # Check light intensity and adjust lighting
    if current_light_intensity is not None:
        if current_light_intensity < 300:  # Assuming 300 lux is low light
            light_actuator.turn_on()
            light_actuator.set_brightness_level("high")
        else:
            light_actuator.turn_off()

    # Turn off sensors
    temperature_sensor.turn_off()
    humidity_sensor.turn_off()
    light_sensor.turn_off()

if __name__ == "__main__":
    main()