# Based on your functional description and the provided source code files, I will create a `function.py` file that contains a `main` function. This function will simulate the operation of the smart home system by reading sensor values and controlling actuators based on the given conditions.
# 
# Here's how the `function.py` file will be structured:
# 
# 1. Create instances of sensors and actuators.
# 2. Retrieve the readings from the sensors.
# 3. Compare the readings to the specified thresholds (for temperature, humidity, and light intensity).
# 4. Control the actuators based on the readings.
# 5. Print the results.
# 
# Here's the content for `function.py`:

# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Create home plan
    home = home_plan()
    
    # Iterate through each room
    for room in home:
        print(f"\n--- {room.name} ---")
        
        # Get sensors and actuators in the room
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        
        actuators = room.actuators
        
        # Get readings from temperature sensors
        for sensor in temperature_sensors:
            sensor.turn_on()
            temperature_reading = sensor.get_reading()
            if temperature_reading is not None:
                # Control heater or AC based on the temperature
                for actuator in actuators:
                    if isinstance(actuator, Heater):
                        actuator.set_target_temperature(28)  # Example target temperature
                        actuator.adjust_temperature(temperature_reading)

                    if isinstance(actuator, AC):
                        actuator.set_target_temperature(24)  # Example target temperature
                        actuator.adjust_temperature(temperature_reading)

        # Get readings from humidity sensors
        for sensor in humidity_sensors:
            sensor.turn_on()
            humidity_reading = sensor.get_reading()
            if humidity_reading is not None:
                # Control humidifier or other humidity-related actuators
                for actuator in actuators:
                    if isinstance(actuator, Humidifier):
                        if humidity_reading < HUMIDITY_LOW:
                            actuator.turn_on()
                            actuator.increase_humidity()
                        elif humidity_reading > HUMIDITY_HIGH:
                            actuator.turn_on()
                            actuator.decrease_humidity()

        # Get readings from light sensors
        for sensor in light_sensors:
            sensor.turn_on()
            light_reading = sensor.get_reading()
            if light_reading is not None:
                # Control lights based on light intensity
                for actuator in actuators:
                    if isinstance(actuator, Light):
                        if light_reading < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()
                            actuator.set_brightness_level("high")  # Example action
                        elif light_reading > LIGHT_INTENSITY_HIGH:
                            actuator.turn_off()

if __name__ == "__main__":
    main()