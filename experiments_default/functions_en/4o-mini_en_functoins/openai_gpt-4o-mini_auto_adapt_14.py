# Based on the provided functional description and source code, I will create the `function.py` file that implements the main function for your smart home project. The function will check the readings from the sensors and take appropriate actions through the actuators when specific conditions are met. 
# 
# Here is the `function.py` file:

# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Create the home setup
    home = home_plan()
    
    for room in home:
        # Get sensors in the room
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]

        # Get actuators in the room
        heaters = [actuator for actuator in room.actuators if actuator.actuator_type == "Heater"]
        humidifiers = [actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"]
        lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]
        notification_senders = [actuator for actuator in room.actuators if actuator.actuator_type == "NotificationSender"]

        # Check temperature
        for sensor in temperature_sensors:
            current_temp = sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH:
                    for notifier in notification_senders:
                        notifier.turn_on()
                        notifier.notification_sender(f"{room.name}: Xiaog is too hot!")
                    for heater in heaters:
                        heater.turn_off()  # Turn off heater if it's on
                elif current_temp < TEMP_LOW:
                    for notifier in notification_senders:
                        notifier.turn_on()
                        notifier.notification_sender(f"{room.name}: Xiaog is too cold!")
                    for heater in heaters:
                        heater.turn_on()  # Turn on heater

        # Check humidity
        for sensor in humidity_sensors:
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    for notifier in notification_senders:
                        notifier.turn_on()
                        notifier.notification_sender(f"{room.name}: Little G is too dry!")
                    for humidifier in humidifiers:
                        humidifier.turn_on()  # Turn on humidifier
                elif current_humidity > HUMIDITY_HIGH:
                    for notifier in notification_senders:
                        notifier.turn_on()
                        notifier.notification_sender(f"{room.name}: Little G is too humid!")
                    for humidifier in humidifiers:
                        humidifier.turn_off()  # Turn off humidifier

        # Check light intensity
        for sensor in light_sensors:
            current_light = sensor.get_reading()
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_LOW:
                    for notifier in notification_senders:
                        notifier.turn_on()
                        notifier.notification_sender(f"{room.name}: Little G is too dark!")
                    for light in lights:
                        light.turn_on()  # Turn on light
                elif current_light > LIGHT_INTENSITY_HIGH:
                    for notifier in notification_senders:
                        notifier.turn_on()
                        notifier.notification_sender(f"{room.name}: Little G is too bright!")
                    for light in lights:
                        light.turn_off()  # Turn off light

if __name__ == "__main__":
    main()