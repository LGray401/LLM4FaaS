# To create the `function.py` file according to your functional description, we'll need to develop a main function that monitors the readings from the sensors and controls the actuators accordingly. Based on your description:
# 
# - "屋里太热了" (It's too hot inside) suggests that the AC should be turned on if the indoor temperature is too high.
# - "屋里有点干" (It's a bit dry inside) suggests that the humidifier should be turned on if the humidity is too low.
# - "屋里太暗了" (It's too dark inside) suggests that the lights should be turned on if the light intensity is too low.
# 
# Here's a `function.py` file that incorporates logic based on the above requirements:
# 
# ```python
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def main():
    home = home_plan()

    # Get all necessary sensors
    indoor_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all necessary actuators
    ac_units = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")

    # Check Indoor Temperature and control AC
    for sensor in indoor_temperature_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        if temp_reading is not None and temp_reading > TEMP_HIGH:
            print(f"Temperature is too high: {temp_reading}°C. Turning on AC.")
            for ac in ac_units:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temp_reading)

    # Check Humidity and control Humidifier
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_reading = sensor.get_reading()
        if humidity_reading is not None and humidity_reading < HUMIDITY_LOW:
            print(f"Humidity is too low: {humidity_reading}%. Turning on Humidifier.")
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.turn_on()
                    humidifier.increase_humidity()

    # Check Light Intensity and control Lights
    for sensor in light_sensors:
        sensor.turn_on()
        light_reading = sensor.get_reading()
        if light_reading is not None and light_reading < LIGHT_INTENSITY_LOW:
            print(f"Light intensity is too low: {light_reading} lux. Turning on Lights.")
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    light.set_brightness_level("high")

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# - The `main()` function initializes the home setup using `home_plan()`.
# - It retrieves all the relevant sensors and actuators for temperature, humidity, and light control.
# - For each sensor type, it reads the current value and performs the necessary checks against the thresholds defined in `config.py`.
# - If conditions are met (e.g., temperature is too high), it activates the corresponding actuators (e.g., turning on the AC).
# - The script is designed to be run as the main program, and it will execute the control logic for the smart home environment.
# 
# Make sure your directory structure is correctly set up with the `home` and `functions` folders, and place this `function.py` file inside the `functions` folder.