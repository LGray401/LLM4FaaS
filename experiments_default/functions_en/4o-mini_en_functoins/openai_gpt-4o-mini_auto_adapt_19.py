# Based on the functional description and the provided source code, we will create a `function.py` file that implements a main function to monitor the sensors and control the actuators based on the specified conditions regarding temperature, humidity, and light intensity.
# 
# Here’s the implementation for `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import NotificationSender, AC, Heater, Humidifier, Light

def monitor_home():
    home = home_plan()

    for room in home:
        # Get the sensors and actuators in the room
        temperature_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        humidity_sensors = [sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)]
        light_sensors = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]
        
        # Get corresponding actuators
        ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        heaters = [actuator for actuator in room.actuators if isinstance(actuator, Heater)]
        humidifiers = [actuator for actuator in room.actuators if isinstance(actuator, Humidifier)]
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        notification_senders = [actuator for actuator in room.actuators if isinstance(actuator, NotificationSender)]

        # Monitor temperature
        for sensor in temperature_sensors:
            sensor.turn_on()
            temperature_reading = sensor.get_reading()
            if temperature_reading is not None:
                if temperature_reading > TEMP_HIGH and ac_units:
                    ac_units[0].set_target_temperature(TEMP_HIGH)
                    ac_units[0].adjust_temperature(temperature_reading)
                    for notifier in notification_senders:
                        notifier.notification_sender(f"Temperature too high in {room.name}: {temperature_reading}°C")

                elif temperature_reading < TEMP_HIGH and heaters:
                    heaters[0].set_target_temperature(TEMP_HIGH)
                    heaters[0].adjust_temperature(temperature_reading)
                    for notifier in notification_senders:
                        notifier.notification_sender(f"Temperature too low in {room.name}: {temperature_reading}°C")

        # Monitor humidity
        for sensor in humidity_sensors:
            sensor.turn_on()
            humidity_reading = sensor.get_reading()
            if humidity_reading is not None:
                if humidity_reading < HUMIDITY_LOW and humidifiers:
                    humidifiers[0].increase_humidity()
                    for notifier in notification_senders:
                        notifier.notification_sender(f"Humidity too low in {room.name}: {humidity_reading}%")

        # Monitor light intensity
        for sensor in light_sensors:
            sensor.turn_on()
            light_reading = sensor.get_reading()
            if light_reading is not None:
                if light_reading > LIGHT_INTENSITY_HIGH and lights:
                    lights[0].turn_off()
                    for notifier in notification_senders:
                        notifier.notification_sender(f"Light intensity too high in {room.name}: {light_reading} lux")

if __name__ == "__main__":
    monitor_home()