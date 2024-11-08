# To create the `function.py` file for your smart home project, we need to implement the main function that makes use of the sensor and actuator classes defined in your existing code. This function should simulate a scenario based on the functional description you provided. We'll use the sensors to get readings and decide on actions using the actuators.
# 
# Here is how you can implement the `function.py`:
# 
# ```python
# function.py

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Light, NotificationSender
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def main():
    home = home_plan()

    # Get all rooms
    for room in home:
        print(f"\nChecking {room.name}...")

        # Get sensors in the room
        for sensor in room.sensors:
            sensor.turn_on()
            reading = sensor.get_reading()

            if isinstance(sensor, IndoorTemperatureSensor):
                if reading > TEMP_HIGH:
                    print(f"Temperature ({reading}°C) is too high in {room.name}.")
                    acs = [a for a in room.actuators if isinstance(a, AC)]
                    for ac in acs:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.turn_on()

            elif isinstance(sensor, HumiditySensor):
                if reading < HUMIDITY_LOW:
                    print(f"Humidity ({reading}%) is too low in {room.name}.")
                    humidifiers = [a for a in room.actuators if isinstance(a, Humidifier)]
                    for humidifier in humidifiers:
                        humidifier.turn_on()
                        humidifier.increase_humidity()

            elif isinstance(sensor, LightIntensiveSensor):
                if reading < LIGHT_INTENSITY_LOW:
                    print(f"Light intensity ({reading} lux) is too low in {room.name}.")
                    lights = [a for a in room.actuators if isinstance(a, Light)]
                    for light in lights:
                        light.turn_on()
                        light.set_brightness_level("high")

            sensor.turn_off()

    # Send notifications
    notification_senders = [a for a in home[0].actuators if isinstance(a, NotificationSender)]
    for notifier in notification_senders:
        notifier.turn_on()
        notifier.notification_sender("Check completed for all rooms.")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Importing Necessary Modules**: We import the sensor and actuator classes and functions from `home_plan.py` to create the home environment.
# 
# 2. **Plan the Home**: We use the `home_plan()` function to create the home with predefined rooms, sensors, and actuators.
# 
# 3. **Iterate Through Rooms**: We loop through each room in the home.
# 
# 4. **Check Sensors**: For each sensor, we:
#    - Turn it on.
#    - Get its current reading.
#    - Based on the type of sensor and its reading, we decide whether to activate any corresponding actuators (e.g., AC when the temperature is too high).
# 
# 5. **Control Actuators**: For each sensor type, the corresponding actuators (like ACs, Humidifiers, Lights) are checked and activated if necessary.
# 
# 6. **Send Notifications**: After checking all rooms, notification messages are sent using `NotificationSender` actuators.
# 
# This code will handle the conditions mentioned in your functional description and interact with the sensors and actuators accordingly. Adjust the sensor readings and actuator actions based on actual requirements and thresholds defined in your `config.py`.