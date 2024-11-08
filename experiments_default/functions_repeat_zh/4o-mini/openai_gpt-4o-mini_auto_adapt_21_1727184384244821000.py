# Based on your functional description and the provided source code, I'll create a `function.py` file that implements the main function. This function will monitor the sensors and actuators in the smart home, responding to temperature, humidity, and light intensity as specified.
# 
# Here's the `function.py` file:

# function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Humidifier, Curtain
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Initialize the home plan
    home = home_plan()

    # Create a dictionary to keep track of the actuators for easy access
    actuators = {}
    for room in home:
        for actuator in room.actuators:
            actuators[actuator.actuator_type] = actuator

    # Monitor and control the actuators based on sensor readings
    while True:
        for room in home:
            # Get temperature sensor reading
            temp_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
            if temp_sensor:
                current_temp = temp_sensor.get_reading()
                if current_temp is not None and current_temp > TEMP_HIGH:
                    ac = actuators.get("AC")
                    if ac:
                        ac.set_target_temperature(26)  # Set AC target temperature
                        ac.adjust_temperature(current_temp)  # Adjust AC based on current temperature

            # Get humidity sensor reading
            humidity_sensor = next((s for s in room.sensors if isinstance(s, HumiditySensor)), None)
            if humidity_sensor:
                current_humidity = humidity_sensor.get_reading()
                humidifier = actuators.get("Humidifier")
                if humidifier:
                    if current_humidity < 30:
                        humidifier.increase_humidity()
                    elif current_humidity > 50:
                        humidifier.decrease_humidity()

            # Get light intensity sensor reading
            light_sensor = next((s for s in room.sensors if isinstance(s, LightIntensiveSensor)), None)
            if light_sensor:
                light_intensity = light_sensor.get_reading()
                curtain = actuators.get("Curtain")
                if curtain and light_intensity is not None and light_intensity > LIGHT_INTENSITY_HIGH:
                    curtain.turn_on()  # Open curtains if light intensity is high
                elif curtain:
                    curtain.turn_off()  # Close curtains if light intensity is acceptable

        # Sleep for a bit before checking again (to avoid busy waiting)
        import time
        time.sleep(10)  # Check every 10 seconds

if __name__ == "__main__":
    main()