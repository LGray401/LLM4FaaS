# Based on your functional description and the provided source code, I will create a `function.py` file that implements the main function for your smart home project. This function will be responsible for monitoring the temperature, humidity, and light intensity, and will activate or deactivate the relevant actuators based on the readings from the sensors.
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Curtain, Humidifier
from time import sleep

def main():
    # Set up the home environment
    home = home_plan()
    
    # Infinite loop to continuously monitor the sensors
    while True:
        for room in home:
            # Get the sensors in the room
            temperature_sensors = [s for s in room.sensors if s.sensor_type == "IndoorTemperature"]
            humidity_sensors = [s for s in room.sensors if s.sensor_type == "Humidity"]
            light_sensors = [s for s in room.sensors if s.sensor_type == "LightIntensive"]
            
            # Check temperature
            for sensor in temperature_sensors:
                sensor.turn_on()
                temperature = sensor.get_reading()
                if temperature is not None:
                    if temperature > TEMP_HIGH:
                        # Activate AC if temperature is above threshold
                        ac = next((a for a in room.actuators if isinstance(a, AC)), None)
                        if ac:
                            ac.set_target_temperature(25)  # Set target temperature to 25°C
                            ac.adjust_temperature(temperature)

            # Check humidity
            for sensor in humidity_sensors:
                sensor.turn_on()
                humidity = sensor.get_reading()
                if humidity is not None:
                    humidifier = next((a for a in room.actuators if isinstance(a, Humidifier)), None)
                    if humidifier:
                        if humidity < HUMIDITY_LOW:
                            humidifier.increase_humidity()
                        elif humidity > HUMIDITY_HIGH:
                            humidifier.decrease_humidity()

            # Check light intensity
            for sensor in light_sensors:
                sensor.turn_on()
                light_intensity = sensor.get_reading()
                if light_intensity is not None:
                    curtain = next((a for a in room.actuators if isinstance(a, Curtain)), None)
                    if curtain and light_intensity > LIGHT_INTENSITY_HIGH:
                        curtain.turn_on()

        # Wait before the next reading
        sleep(5)  # Adjust the sleep duration as needed

if __name__ == "__main__":
    main()