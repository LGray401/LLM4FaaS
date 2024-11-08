# Based on the functional description and the provided source code, I'll create a `function.py` file that includes a `main` function. The `main` function will use the provided code to set up the home plan, sensors, and actuators. It will also simulate interactions with the sensors and actuators to demonstrate their functionality.
# 
# Here is the `function.py` file:

# function.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Heater, AC, Humidifier
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create the home plan
    home = home_plan()

    # Set up sensors
    indoor_temp_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    light_intensity_sensor = LightIntensiveSensor("LivingRoom")

    # Get the sensors from the home plan
    sensors = [
        indoor_temp_sensor,
        humidity_sensor,
        light_intensity_sensor
    ]

    # Get the actuators from the home plan
    actuators = home[0].actuators  # Assuming LivingRoom has all the required actuators

    # Simulate sensor readings
    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            current_temp = sensor.get_reading()
            print(f"Current indoor temperature: {current_temp}°C")
            if current_temp < TEMP_LOW:
                print("Heater is on.")
                heater = next((act for act in actuators if isinstance(act, Heater)), None)
                if heater:
                    heater.turn_on()
            elif current_temp > TEMP_HIGH:
                print("AC is on.")
                ac = next((act for act in actuators if isinstance(act, AC)), None)
                if ac:
                    ac.turn_on()

        elif isinstance(sensor, HumiditySensor):
            current_humidity = sensor.get_reading()
            print(f"Current humidity: {current_humidity}%")
            if current_humidity < HUMIDITY_LOW:
                print("Humidifier is on.")
                humidifier = next((act for act in actuators if isinstance(act, Humidifier)), None)
                if humidifier:
                    humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                print("Humidifier is off.")
                humidifier = next((act for act in actuators if isinstance(act, Humidifier)), None)
                if humidifier:
                    humidifier.decrease_humidity()

        elif isinstance(sensor, LightIntensiveSensor):
            current_light_intensity = sensor.get_reading()
            print(f"Current light intensity: {current_light_intensity} lux")
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                print("Light is on.")
                light = next((act for act in actuators if isinstance(act, Light)), None)
                if light:
                    light.turn_on()
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                print("Light is off.")
                light = next((act for act in actuators if isinstance(act, Light)), None)
                if light:
                    light.turn_off()

    # Print the status of all sensors and actuators
    print("\nSensor and Actuator Status:")
    for sensor in sensors:
        print(f"{sensor.id} - Status: {sensor.get_status()}")
    for actuator in actuators:
        print(f"{actuator.id} - Status: {actuator.get_status()}")

if __name__ == "__main__":
    main()