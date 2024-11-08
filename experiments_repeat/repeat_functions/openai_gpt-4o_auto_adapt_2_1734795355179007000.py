# Here is a `function.py` file that contains a main function to implement the described functionalities for your smart home project. This script will monitor temperature, humidity, and light intensity, and adjust the respective actuators accordingly.
# 
# ```python
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Window, Humidifier, Light
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def main():
    # Create the home plan
    home = home_plan()
    
    # Get sensors and actuators
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    acs = get_all_actuators(home, "AC")
    windows = get_all_actuators(home, "Window")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Turn on all sensors
    for sensor in temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()

    # Monitor and control loop
    while True:
        # Check temperature
        for sensor in temp_sensors:
            temp_reading = sensor.get_reading()
            if temp_reading and temp_reading > TEMP_HIGH:
                # Turn on AC
                for ac in acs:
                    if ac.room_name == sensor.room_name:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(temp_reading)
                # Close windows
                for window in windows:
                    if window.room_name == sensor.room_name:
                        window.turn_off()

        # Check humidity
        for sensor in humidity_sensors:
            humidity_reading = sensor.get_reading()
            if humidity_reading and humidity_reading < HUMIDITY_LOW:
                # Turn on Humidifier
                for humidifier in humidifiers:
                    if humidifier.room_name == sensor.room_name:
                        humidifier.turn_on()
                        humidifier.increase_humidity()

        # Check light intensity
        for sensor in light_sensors:
            light_reading = sensor.get_reading()
            if light_reading and light_reading < LIGHT_INTENSITY_LOW:
                # Turn on Lights and set brightness to high
                for light in lights:
                    if light.room_name == sensor.room_name:
                        light.turn_on()
                        light.set_brightness_level("high")
            else:
                # Turn off Lights
                for light in lights:
                    if light.room_name == sensor.room_name:
                        light.turn_off()

        # Wait before next check
        time.sleep(5)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Home Setup:**
#    - The script first sets up the home plan and retrieves all relevant sensors (temperature, humidity, light) and actuators (AC, windows, humidifiers, lights).
# 
# 2. **Sensor Activation:**
#    - It turns on all sensors so they can provide readings.
# 
# 3. **Monitoring Loop:**
#    - The script enters an infinite loop where it periodically checks sensor readings.
#    - **Temperature Control:** If the indoor temperature exceeds 25 degrees (as specified in `TEMP_HIGH`), it turns on the AC in the corresponding room and closes the windows.
#    - **Humidity Control:** If the humidity is below the `HUMIDITY_LOW` threshold, it turns on the humidifier in the respective room.
#    - **Light Control:** If the light intensity is below the `LIGHT_INTENSITY_LOW` threshold, it turns on the lights in the room and sets the brightness to high.
# 
# 4. **Loop Timing:**
#    - The loop waits for 5 seconds before checking the readings again to avoid excessive resource consumption.
# 
# This setup ensures that your smart home system continuously monitors and adjusts the environment according to the specified functional requirements. Adjust the thresholds in `config.py` as needed for different conditions.