# Based on the functional description and the provided source code, I will create a `function.py` file that includes a main function to manage the smart home system by maintaining the indoor temperature, humidity, and light intensity as specified. 
# 
# The main function will:
# 1. Create the home setup using the components defined in `home_plan.py`.
# 2. Continuously monitor the readings from the sensors.
# 3. Activate or deactivate actuators (Heater, AC, Humidifier, and Light) based on the conditions for temperature, humidity, and light intensity.
# 
# Here’s how the `function.py` file will look:

# function.py
import time
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Setup the home
    home = home_plan()

    while True:
        for room in home:
            # Get the readings from the sensors
            temperature_sensor = next((s for s in room.sensors if s.sensor_type == "IndoorTemperature"), None)
            humidity_sensor = next((s for s in room.sensors if s.sensor_type == "Humidity"), None)
            light_sensor = next((s for s in room.sensors if s.sensor_type == "LightIntensive"), None)
            
            current_temperature = temperature_sensor.get_reading() if temperature_sensor else None
            current_humidity = humidity_sensor.get_reading() if humidity_sensor else None
            current_light_intensity = light_sensor.get_reading() if light_sensor else None
            
            # Control the heater and AC
            heater = next((a for a in room.actuators if a.actuator_type == "Heater"), None)
            ac = next((a for a in room.actuators if a.actuator_type == "AC"), None)
            
            if current_temperature is not None:
                if current_temperature > TEMP_HIGH:
                    if ac:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temperature)
                elif current_temperature < TEMP_HIGH:
                    if heater:
                        heater.set_target_temperature(TEMP_HIGH)
                        heater.adjust_temperature(current_temperature)

            # Control the humidifier
            humidifier = next((a for a in room.actuators if a.actuator_type == "Humidifier"), None)
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    if humidifier:
                        humidifier.increase_humidity()
                else:
                    if humidifier:
                        humidifier.decrease_humidity()

            # Control the light
            light = next((a for a in room.actuators if a.actuator_type == "Light"), None)
            if current_light_intensity is not None:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    if light:
                        light.turn_on()
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    if light:
                        light.turn_off()

        time.sleep(5)  # Sleep for a while before the next loop

if __name__ == "__main__":
    main()