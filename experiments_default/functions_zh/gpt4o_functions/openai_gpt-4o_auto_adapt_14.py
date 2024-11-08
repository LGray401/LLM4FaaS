# Based on the provided functional description and the source code files, I will create a `function.py` file that will reside in the `functions` folder. This file will contain the main function to handle the temperature, humidity, and light intensity alerts as specified.
# 
# Here is the `function.py` file:

# functions/function.py

import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def main():
    home = home_plan()

    # Get all sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    # Get notification sender actuators
    notification_senders = get_all_actuators(home, "NotificationSender")

    # Turn on all notification senders
    for sender in notification_senders:
        sender.turn_on()

    while True:
        # Check indoor temperature sensors
        for sensor in indoor_temp_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None and reading > TEMP_HIGH:
                message = "小g 太热了"
                for sender in notification_senders:
                    sender.notification_sender(message)

        # Check humidity sensors
        for sensor in humidity_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None and reading < HUMIDITY_LOW:
                message = "小g 太干了"
                for sender in notification_senders:
                    sender.notification_sender(message)

        # Check light intensity sensors
        for sensor in light_intensity_sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            if reading is not None and reading < LIGHT_INTENSITY_LOW:
                message = "小g 太暗了"
                for sender in notification_senders:
                    sender.notification_sender(message)

        time.sleep(60)  # Check sensors every minute

if __name__ == "__main__":
    main()