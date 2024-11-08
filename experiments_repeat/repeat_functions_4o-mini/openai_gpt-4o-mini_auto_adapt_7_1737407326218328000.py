# Based on the functional description and the provided code files, here's the implementation for the `function.py` file that coordinates the smart home functionalities. The code will check the readings from the sensors and control the actuators accordingly.
# 
# ### `function.py`
# ```python
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light, NotificationSender

def main():
    # Step 1: Create the home environment
    home = home_plan()

    # Step 2: Define thresholds based on functional requirements
    temperature_threshold = TEMP_HIGH  # If the temperature is above this, turn on AC or heater
    humidity_threshold = HUMIDITY_LOW   # If humidity is low, turn on humidifier
    light_threshold = LIGHT_INTENSITY_HIGH  # If light is below this, turn on lights

    # Step 3: Iterate through rooms and check sensor readings
    for room in home:
        sensors = get_all_sensors(home, room.name)
        actuators = get_all_actuators(home, room.name)

        # Check temperature sensors
        temperature_sensors = [s for s in sensors if s.sensor_type == "IndoorTemperature"]
        for sensor in temperature_sensors:
            sensor.turn_on()
            current_temp = sensor.get_reading()
            if current_temp is not None:
                if current_temp > temperature_threshold:
                    ac = next((a for a in actuators if isinstance(a, AC)), None)
                    if ac:
                        ac.set_target_temperature(temperature_threshold)
                        ac.adjust_temperature(current_temp)
                else:
                    heater = next((a for a in actuators if isinstance(a, Heater)), None)
                    if heater:
                        heater.set_target_temperature(temperature_threshold)
                        heater.adjust_temperature(current_temp)

        # Check humidity sensors
        humidity_sensors = [s for s in sensors if s.sensor_type == "Humidity"]
        for sensor in humidity_sensors:
            sensor.turn_on()
            current_humidity = sensor.get_reading()
            if current_humidity is not None and current_humidity < humidity_threshold:
                humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
                if humidifier:
                    humidifier.increase_humidity()

        # Check light intensity sensors
        light_sensors = [s for s in sensors if s.sensor_type == "LightIntensive"]
        for sensor in light_sensors:
            sensor.turn_on()
            current_light = sensor.get_reading()
            if current_light is not None and current_light < light_threshold:
                light = next((a for a in actuators if isinstance(a, Light)), None)
                if light:
                    light.turn_on()
                    light.set_brightness_level("high")  # Set to high brightness

        # Send notifications if necessary
        notification_sender = next((a for a in actuators if isinstance(a, NotificationSender)), None)
        if notification_sender:
            notification_sender.turn_on()
            if temperature_sensors:
                notification_sender.notification_sender("屋里太热了" if current_temp > temperature_threshold else "屋里温度正常")
            if humidity_sensors:
                notification_sender.notification_sender("屋里有点干" if current_humidity < humidity_threshold else "屋里湿度正常")
            if light_sensors:
                notification_sender.notification_sender("屋里太暗了" if current_light < light_threshold else "屋里光线正常")


if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation of `function.py`:
# 1. **Import Necessary Components**: The script imports functions and classes required to interact with the home setup.
# 
# 2. **Main Function**: The `main()` function creates the home environment and initializes the sensor and actuator checks.
# 
# 3. **Thresholds**: The thresholds for temperature, humidity, and light intensity are defined based on the requirements.
# 
# 4. **Sensor Readings**: The script iterates through the rooms, retrieves sensor readings, and takes action based on the readings:
#    - If the temperature is above the threshold, it activates the AC to cool down.
#    - If the humidity is below the threshold, it activates the humidifier.
#    - If light intensity is below the threshold, it turns on the light and sets it to high brightness.
# 
# 5. **Notifications**: The script sends notifications based on the conditions to inform the user about the current status.
# 
# Make sure to place this `function.py` file in the `functions` folder of your project structure.