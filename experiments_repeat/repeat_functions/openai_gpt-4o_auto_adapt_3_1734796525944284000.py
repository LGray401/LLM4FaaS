# Based on the functional description you've provided, we need to create a `function.py` file that contains the main function for your smart home project. The description mentions specific conditions for temperature, humidity, and light intensity. Here's how we can create a main function that will utilize the classes and methods from the other files you've shared:
# 
# ```python
# function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan

def main():
    # Initialize the home with its rooms and components
    home = home_plan()

    # Set desired conditions
    desired_temperature = 26  # Celsius
    desired_humidity = 50  # Percentage
    desired_light_intensity = "medium"  # Light level

    # Iterate through each room in the home
    for room in home:
        # Iterate through sensors in each room
        for sensor in room.sensors:
            sensor.turn_on()  # Make sure the sensor is on
            
            if isinstance(sensor, IndoorTemperatureSensor):
                current_temp = sensor.get_reading()
                # Adjust AC or Heater based on the current temperature
                for actuator in room.actuators:
                    if isinstance(actuator, AC):
                        actuator.set_target_temperature(desired_temperature)
                        actuator.adjust_temperature(current_temp)
                    elif isinstance(actuator, Heater):
                        actuator.set_target_temperature(desired_temperature)
                        actuator.adjust_temperature(current_temp)

            elif isinstance(sensor, HumiditySensor):
                current_humidity = sensor.get_reading()
                # Adjust Humidifier based on the current humidity
                for actuator in room.actuators:
                    if isinstance(actuator, Humidifier):
                        if current_humidity < desired_humidity:
                            actuator.increase_humidity()
                        else:
                            actuator.decrease_humidity()

            elif isinstance(sensor, LightIntensiveSensor):
                current_light = sensor.get_reading()
                # Adjust Light based on the current light intensity
                for actuator in room.actuators:
                    if isinstance(actuator, Light):
                        if current_light < 900:
                            actuator.turn_on()
                            actuator.set_brightness_level(desired_light_intensity)
                        else:
                            actuator.turn_off()

        # Turn off the sensors after use
        for sensor in room.sensors:
            sensor.turn_off()

if __name__ == "__main__":
    main()
# ```
# 
# ### Explanation:
# 
# 1. **Sensor Initialization**: The script turns on each sensor to get its reading. It uses `IndoorTemperatureSensor`, `HumiditySensor`, and `LightIntensiveSensor` to monitor the environment.
# 
# 2. **Actuator Control**: Based on the sensor readings:
#    - **Temperature Control**: Uses `AC` and `Heater` to maintain the desired temperature of 26°C.
#    - **Humidity Control**: Uses `Humidifier` to maintain the desired humidity at 50%.
#    - **Light Control**: Uses `Light` to set the brightness level if the light intensity is below the threshold.
# 
# 3. **Structure**: The `main()` function initializes the home setup and checks each room's conditions, adjusting actuators accordingly.
# 
# Please ensure that the `functions` folder exists and place this `function.py` file inside it. This script assumes all required imports and classes are available and functioning as expected based on your provided code. Adjust any paths if necessary to fit your project structure.