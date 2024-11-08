# Based on the functional description and the provided source code, I will create a `function.py` file that includes a main function to manage the smart home features. The main function will use the sensors and actuators to monitor and respond to the conditions specified in your functional description.
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def main():
    # Create the home environment with rooms, sensors, and actuators
    home = home_plan()

    # Example room names (you may modify these as per your home setup)
    living_room = home[0]
    bedroom = home[1]
    
    # Initialize required sensors and actuators
    temperature_sensor = living_room.sensors[0]  # Assuming the first sensor is the temperature sensor
    humidity_sensor = living_room.sensors[1]     # Assuming the second sensor is the humidity sensor
    light_sensor = living_room.sensors[2]        # Assuming the third sensor is the light intensity sensor
    heater = living_room.actuators[5]            # Assuming the heater is the sixth actuator
    humidifier = living_room.actuators[6]        # Assuming the humidifier is the seventh actuator
    light = living_room.actuators[1]             # Assuming the light is the second actuator

    # Turn on sensors to start monitoring
    temperature_sensor.turn_on()
    humidity_sensor.turn_on()
    light_sensor.turn_on()

    # Main loop to monitor and manage the home environment
    try:
        while True:
            # Get readings from sensors
            current_temperature = temperature_sensor.get_reading()
            current_humidity = humidity_sensor.get_reading()
            current_light_intensity = light_sensor.get_reading()

            # Control Heater based on temperature
            if current_temperature is not None:
                if current_temperature < TEMP_LOW:
                    heater.set_target_temperature(26)
                    heater.adjust_temperature(current_temperature)
                elif current_temperature > TEMP_HIGH:
                    heater.turn_off()

            # Control Humidifier based on humidity
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

            # Control Light based on light intensity
            if current_light_intensity is not None:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    light.turn_off()

            # Wait before the next reading to avoid too frequent checks
            time.sleep(5)

    except KeyboardInterrupt:
        print("Terminating smart home monitoring...")

    finally:
        # Turn off all sensors when exiting
        temperature_sensor.turn_off()
        humidity_sensor.turn_off()
        light_sensor.turn_off()

if __name__ == "__main__":
    main()