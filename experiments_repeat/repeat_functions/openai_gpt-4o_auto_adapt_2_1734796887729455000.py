# Based on the given functional description and the code you have provided, I'll create a `function.py` file located in the `functions` folder. This file will define a main function that utilizes the classes and methods from your other modules to achieve the desired functionality.
# 
# Here's the `function.py` file:
# 
# ```python
# function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create the home plan
    home = home_plan()

    # Monitor temperature
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    ac_actuators = get_all_actuators(home, "AC")
    window_actuators = get_all_actuators(home, "Window")

    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        if temp_reading is not None and temp_reading > TEMP_HIGH:
            # Turn on AC
            for ac in ac_actuators:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temp_reading)
            # Close windows
            for window in window_actuators:
                if window.room_name == sensor.room_name:
                    window.turn_off()

    # Monitor humidity
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_reading = sensor.get_reading()
        if humidity_reading is not None and humidity_reading < HUMIDITY_LOW:
            # Turn on humidifier
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.turn_on()
                    humidifier.increase_humidity()

    # Adjust light intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    if light_intensity > LIGHT_INTENSITY_HIGH:
                        light.set_brightness_level("low")
                    elif light_intensity < LIGHT_INTENSITY_HIGH / 2:
                        light.set_brightness_level("high")
                    else:
                        light.set_brightness_level("medium")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Temperature Control:**
#    - If the indoor temperature exceeds 25°C, the air conditioner is turned on and set to cool the room to 25°C. Simultaneously, windows in that room are closed.
# 
# 2. **Humidity Control:**
#    - If the indoor humidity is below the threshold (too dry), the humidifier in that room is turned on to increase humidity.
# 
# 3. **Light Intensity Adjustment:**
#    - Adjusts the light brightness based on the light intensity reading. If the light intensity is high, the brightness is set to low. If it's very low, the brightness is increased to high.
# 
# This code assumes that the logger and print functions are used for debugging and not for controlling actual devices. Make sure your `home_plan`, `sensor`, and `actuator` modules are imported correctly and the logger is configured if you want to log the information. Adjust the `config.py` thresholds if needed to fit your specific requirements.