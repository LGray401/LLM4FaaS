# Based on the functional description provided, we need to implement a `function.py` file that utilizes the existing classes and methods to automate responses for different environmental conditions. Let's assume the main function should check the sensors' readings for temperature, humidity, and light intensity and act accordingly.
# 
# Here's a possible implementation of `function.py` located in the `functions` folder:
# 
# ```python
# function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light, NotificationSender
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def main():
    # Initialize the home plan
    home = home_plan()

    # Get all relevant sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all relevant actuators
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    notification_senders = get_all_actuators(home, "NotificationSender")

    # Check temperature
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        
        # If it's too hot
        if temp_reading > TEMP_HIGH:
            # Turn on AC
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temp_reading)
            # Send notification
            for notifier in notification_senders:
                if notifier.room_name == sensor.room_name:
                    notifier.turn_on()
                    notifier.notification_sender("屋里太热了")
        sensor.turn_off()

    # Check humidity
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_reading = sensor.get_reading()
        
        # If it's too dry
        if humidity_reading < HUMIDITY_LOW:
            # Turn on Humidifier
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.turn_on()
                    humidifier.increase_humidity()
            # Send notification
            for notifier in notification_senders:
                if notifier.room_name == sensor.room_name:
                    notifier.turn_on()
                    notifier.notification_sender("屋里有点干")
        sensor.turn_off()

    # Check light intensity
    for sensor in light_sensors:
        sensor.turn_on()
        light_reading = sensor.get_reading()
        
        # If it's too dark
        if light_reading < LIGHT_INTENSITY_LOW:
            # Turn on Lights
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    light.set_brightness_level("high")
            # Send notification
            for notifier in notification_senders:
                if notifier.room_name == sensor.room_name:
                    notifier.turn_on()
                    notifier.notification_sender("屋里太暗了")
        sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# - **Temperature**: The code checks if the temperature is above a defined high threshold (`TEMP_HIGH`). If so, it turns on the AC and sets it to the target temperature, and sends a notification saying "屋里太热了" (It's too hot inside).
#   
# - **Humidity**: The code checks if the humidity is below a defined low threshold (`HUMIDITY_LOW`). If so, it turns on a humidifier and sends a notification saying "屋里有点干" (It's a bit dry inside).
# 
# - **Light Intensity**: The code checks if the light intensity is below a defined low threshold (`LIGHT_INTENSITY_LOW`). If so, it turns on the lights to a high brightness level and sends a notification saying "屋里太暗了" (It's too dark inside).
# 
# - **Notification**: For each condition, if the respective actuator is turned on, a notification is sent using the `NotificationSender`.
# 
# - The `main` function initializes the home plan, retrieves all necessary sensors and actuators, and then iterates through them to perform the necessary checks and actions.
# 
# This implementation assumes that all sensors and actuators are functioning as expected and are properly linked to their respective rooms. Adjust thresholds and logic as needed according to your specific requirements and setup.