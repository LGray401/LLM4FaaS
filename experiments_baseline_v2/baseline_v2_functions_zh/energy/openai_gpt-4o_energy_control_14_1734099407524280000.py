# To create a smart home application based on the given functional description "小g 启动地球环保计划" (which translates to "Xiao G starts the Earth Environmental Protection Plan"), we will build a Python script that utilizes the provided source code files. This script will simulate a smart home environment with sensors and actuators, focusing on energy efficiency and environmental protection by automating various controls.
# 
# We will create a `smart_home.py` script that utilizes the classes and functions from `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`. The script will simulate a smart home environment where devices are automatically managed based on sensor readings to optimize energy usage.
# 
# ### `smart_home.py`
# 
# ```python
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light, Curtain, Window, NotificationSender
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def start_environmental_plan():
    # Initialize the home environment
    home = home_plan()

    # Get all relevant sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    heaters = get_all_actuators(home, "Heater")
    air_conditioners = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")
    windows = get_all_actuators(home, "Window")
    notification_senders = get_all_actuators(home, "NotificationSender")

    # Turn on necessary sensors
    for sensor in indoor_temp_sensors + outdoor_temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    # Turn on notification senders
    for notifier in notification_senders:
        notifier.turn_on()

    # Main loop to monitor and control the home environment
    while True:
        for sensor in indoor_temp_sensors:
            room_name = sensor.room_name
            current_temp = sensor.get_reading()
            for heater in heaters:
                if heater.room_name == room_name:
                    heater.adjust_temperature(current_temp)
            for ac in air_conditioners:
                if ac.room_name == room_name:
                    ac.adjust_temperature(current_temp)

        for sensor in humidity_sensors:
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    for window in windows:
                        window.turn_on()
                elif current_humidity > HUMIDITY_HIGH:
                    for window in windows:
                        window.turn_off()

        for sensor in light_sensors:
            current_light = sensor.get_reading()
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_LOW:
                    for light in lights:
                        light.turn_on()
                        light.set_brightness_level('high')
                    for curtain in curtains:
                        curtain.turn_on()
                elif current_light > LIGHT_INTENSITY_HIGH:
                    for light in lights:
                        light.turn_off()
                    for curtain in curtains:
                        curtain.turn_off()

        # Send notifications
        for notifier in notification_senders:
            notifier.notification_sender("Environmental settings have been adjusted.")

        time.sleep(5)  # Wait for a while before the next loop iteration

if __name__ == "__main__":
    print("Starting the Earth Environmental Protection Plan...")
    start_environmental_plan()
# ```
# 
# ### Running the Application
# 
# To run this application in a Linux terminal, you would use the following command:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# Make sure all the referenced Python files (`sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`) are correctly placed in the `home` directory relative to where you run the command.
# 
# This script initializes a smart home simulation where various sensors and actuators are managed to maintain optimal environmental conditions, demonstrating energy efficiency and environmental protection principles.