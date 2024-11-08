from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Curtain
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

# functions.py
def main():
    # Get the home plan
    home = home_plan()

    # Temperature control
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")

    for sensor in indoor_temp_sensors:
        temperature = sensor.get_reading()
        if temperature is not None and temperature >= TEMP_HIGH:
            for ac in acs:
                ac.turn_on()
        elif temperature is not None and temperature < TEMP_HIGH:
            for ac in acs:
                ac.turn_off()

    # Humidity control
    humidity_sensors = get_all_sensors(home, "Humidity")
    acs = get_all_actuators(home, "AC")  # Using AC for both cooling and humidifying

    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity is not None and humidity <= HUMIDITY_LOW:
            for ac in acs:
                ac.turn_on()
        elif humidity is not None and humidity > HUMIDITY_LOW:
            for ac in acs:
                ac.turn_off()

    # Light intensity control
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    curtains = get_all_actuators(home, "Curtain")

    for sensor in light_intensity_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is not None and light_intensity >= LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                curtain.turn_on()
        elif light_intensity is not None and light_intensity < LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                curtain.turn_off()


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan`: Contains functions to manage the home plan, retrieve rooms, sensors, and actuators.
#    - `home.sensor`: Contains classes for various sensor types (IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor).
#    - `home.actuator`: Contains classes for various actuator types (AC, Heater, Curtain).
#    - `home.config`: Contains configuration values like temperature thresholds.

# 2. **`main()` function:**
#    - **Get the home plan:** `home = home_plan()`
#    - **Temperature control:**
#      - Retrieve all indoor temperature sensors using `get_all_sensors(home, "IndoorTemperature")`.
#      - Retrieve all ACs and heaters using `get_all_actuators(home, "AC")` and `get_all_actuators(home, "Heater")`.
#      - Iterate through the sensors and check the temperature reading.
#      - If the temperature is above `TEMP_HIGH`, turn on all ACs.
#      - If the temperature is below `TEMP_HIGH`, turn off all ACs.
#    - **Humidity control:**
#      - Retrieve all humidity sensors using `get_all_sensors(home, "Humidity")`.
#      - Iterate through the sensors and check the humidity reading.
#      - If the humidity is below `HUMIDITY_LOW`, turn on all ACs (assuming you use AC for humidifying).
#      - If the humidity is above `HUMIDITY_LOW`, turn off all ACs.
#    - **Light intensity control:**
#      - Retrieve all light intensity sensors using `get_all_sensors(home, "LightIntensive")`.
#      - Retrieve all curtains using `get_all_actuators(home, "Curtain")`.
#      - Iterate through the sensors and check the light intensity reading.
#      - If the light intensity is above `LIGHT_INTENSITY_HIGH`, turn on all curtains.
#      - If the light intensity is below `LIGHT_INTENSITY_HIGH`, turn off all curtains.

# **How to Use:**

# 1. **Save the code:** Save the code as `function.py` in the `functions` folder within your project.
# 2. **Run the script:** Run the `function.py` script. It will read sensor data, apply the logic, and control the actuators based on your functional description.

# **Remember:** This code provides a basic example. You can extend it further by:

# - Adding more sensors and actuators.
# - Implementing different control logic based on your specific needs.
# - Incorporating time-based actions or schedules.
# - Integrating with a real smart home system.
