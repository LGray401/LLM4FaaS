# Sure, here is the `function.py` file based on the functional description and the provided source code:

# Import required modules
from home.home_plan import home_plan, get_all_actuators, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

# Define the main function
def main():
    # Get the home plan
    home = home_plan()
    
    # Get all the sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    # Perform actions based on sensor readings
    for sensor in temperature_sensors:
        temperature = sensor.get_reading()
        if temperature is not None:
            if temperature < TEMP_LOW:
                print(f"Temperature is below {TEMP_LOW}°C. Turning on lights.")
                for light in lights:
                    light.turn_on()
            elif temperature > TEMP_HIGH:
                print(f"Temperature is above {TEMP_HIGH}°C. Turning off lights.")
                for light in lights:
                    light.turn_off()

    for sensor in humidity_sensors:
        humidity = sensor.get_reading()
        if humidity is not None:
            if humidity < HUMIDITY_LOW:
                print(f"Humidity is below {HUMIDITY_LOW}%. Turning on lights.")
                for light in lights:
                    light.turn_on()
            elif humidity > HUMIDITY_HIGH:
                print(f"Humidity is above {HUMIDITY_HIGH}%. Turning off lights.")
                for light in lights:
                    light.turn_off()

    for sensor in light_intensity_sensors:
        light_intensity = sensor.get_reading()
        if light_intensity is not None:
            if light_intensity < LIGHT_INTENSITY_LOW:
                print(f"Light intensity is below {LIGHT_INTENSITY_LOW} lux. Turning on lights.")
                for light in lights:
                    light.turn_on()
            elif light_intensity > LIGHT_INTENSITY_HIGH:
                print(f"Light intensity is above {LIGHT_INTENSITY_HIGH} lux. Turning off lights.")
                for light in lights:
                    light.turn_off()

# Call the main function
if __name__ == "__main__":
    main()