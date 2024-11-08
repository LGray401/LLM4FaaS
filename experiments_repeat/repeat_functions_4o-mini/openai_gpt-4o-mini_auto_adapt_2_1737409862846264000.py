# Based on the provided functional description and the existing code files, here is the `function.py` file that implements the main function for your smart home project. This function will monitor the sensors and control the actuators based on the specified conditions for temperature, humidity, and light intensity.
# 
# ```python
# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW
from home.actuator import AC, Humidifier, Light
from time import sleep

def main():
    # Initialize the home
    home = home_plan()

    while True:
        # Check the status of each room
        for room in home:
            # Get relevant sensors and actuators
            temp_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
            humidity_sensor = next((s for s in room.sensors if isinstance(s, HumiditySensor)), None)
            light_sensor = next((s for s in room.sensors if isinstance(s, LightIntensiveSensor)), None)

            ac = next((a for a in room.actuators if isinstance(a, AC)), None)
            humidifier = next((a for a in room.actuators if isinstance(a, Humidifier)), None)
            light = next((a for a in room.actuators if isinstance(a, Light)), None)

            # Temperature control
            if temp_sensor and ac:
                current_temp = temp_sensor.get_reading()
                if current_temp is not None:
                    if current_temp > TEMP_HIGH:
                        ac.turn_on()
                    else:
                        ac.turn_off()

            # Humidity control
            if humidity_sensor and humidifier:
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.turn_on()
                        humidifier.increase_humidity()  # Increase humidity
                    else:
                        humidifier.turn_off()

            # Light control
            if light_sensor and light:
                current_light = light_sensor.get_reading()
                if current_light is not None:
                    if current_light < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                    else:
                        light.turn_off()

        # Wait before the next check to avoid rapid polling
        sleep(5)

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 1. **Initialization**: The main function initializes the home plan and enters an infinite loop to continuously monitor the sensors.
# 
# 2. **Sensor Readings**: For each room, it retrieves the relevant sensors (temperature, humidity, and light intensity) and actuators (AC, humidifier, and light).
# 
# 3. **Control Logic**:
#    - **Temperature**: If the indoor temperature exceeds the defined high threshold, the AC is turned on; otherwise, it is turned off.
#    - **Humidity**: If the indoor humidity is below the defined low threshold, the humidifier is turned on and humidity is increased; otherwise, it is turned off.
#    - **Light Intensity**: If the light intensity is below the defined low threshold, the light is turned on; otherwise, it is turned off.
# 
# 4. **Polling Interval**: The system waits for 5 seconds before polling the sensors again to avoid rapid checks.
# 
# ### Notes:
# - Ensure that the `functions` folder is properly configured in your project structure.
# - You can adjust the sleep duration as per your requirements.
# - This code assumes that the actuators and sensors are correctly initialized and available in the rooms as per your home plan.