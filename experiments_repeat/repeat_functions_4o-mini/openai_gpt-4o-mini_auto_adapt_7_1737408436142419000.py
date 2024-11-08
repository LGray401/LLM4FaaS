# Based on your functional description and the provided code files, I will create the `function.py` file for your smart home project. This file will contain a main function that integrates the functionalities of the sensors and actuators to respond to the specified conditions regarding temperature, humidity, and light intensity.
# 
# Here is the `function.py` file:
# 
# ```python
# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light, NotificationSender

def main():
    # Initialize the home plan
    home = home_plan()

    # Iterate through each room
    for room in home:
        # Get the sensors in the room
        temperature_sensors = [s for s in room.sensors if s.sensor_type == "IndoorTemperature"]
        humidity_sensors = [s for s in room.sensors if s.sensor_type == "Humidity"]
        light_sensors = [s for s in room.sensors if s.sensor_type == "LightIntensive"]

        # Get the actuators in the room
        heaters = [a for a in room.actuators if isinstance(a, Heater)]
        ac_units = [a for a in room.actuators if isinstance(a, AC)]
        humidifiers = [a for a in room.actuators if isinstance(a, Humidifier)]
        lights = [a for a in room.actuators if isinstance(a, Light)]
        notification_senders = [a for a in room.actuators if isinstance(a, NotificationSender)]

        # Check temperature
        for sensor in temperature_sensors:
            sensor.turn_on()
            current_temp = sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH and ac_units:
                    for ac in ac_units:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temp)
                        notification_sender = notification_senders[0] if notification_senders else None
                        if notification_sender:
                            notification_sender.notification_sender("屋里太热了，空调已开启。")
                elif current_temp < TEMP_LOW and heaters:
                    for heater in heaters:
                        heater.set_target_temperature(TEMP_LOW)
                        heater.adjust_temperature(current_temp)
                        notification_sender = notification_senders[0] if notification_senders else None
                        if notification_sender:
                            notification_sender.notification_sender("屋里太冷了，暖气已开启。")

        # Check humidity
        for sensor in humidity_sensors:
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW and humidifiers:
                    for humidifier in humidifiers:
                        humidifier.increase_humidity()
                        notification_sender = notification_senders[0] if notification_senders else None
                        if notification_sender:
                            notification_sender.notification_sender("屋里有点干，已开启加湿器。")

        # Check light intensity
        for sensor in light_sensors:
            sensor.turn_on()
            current_light = sensor.get_reading()
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_LOW and lights:
                    for light in lights:
                        light.turn_on()
                        light.set_brightness_level("high")
                        notification_sender = notification_senders[0] if notification_senders else None
                        if notification_sender:
                            notification_sender.notification_sender("屋里太暗了，灯光已开启。")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Initialization**: The `main` function initializes the home plan and retrieves sensors and actuators from each room.
#   
# 2. **Temperature Control**: It checks the readings from indoor temperature sensors and controls the heater or air conditioning unit based on the defined temperature thresholds. It also sends notifications when actions are taken.
# 
# 3. **Humidity Control**: It checks the humidity levels and activates the humidifier if the humidity is below the defined threshold, sending a notification as well.
# 
# 4. **Light Intensity Control**: It checks the light intensity and turns on the lights if the intensity is below the defined threshold, setting their brightness to high and notifying the user.
# 
# This file assumes that the home plan has already been set up correctly and that there are available sensors and actuators in each room to perform the necessary actions. Adjustments can be made based on the specific requirements of your project and available hardware.