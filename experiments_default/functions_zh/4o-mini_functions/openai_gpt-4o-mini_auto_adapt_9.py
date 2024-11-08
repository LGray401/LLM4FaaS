# Based on the functional description and the provided source code files, here is the `function.py` that you can place in the `functions` folder. This file includes a main function that simulates reading the temperature, humidity, and light intensity, and then prints these values. It also interacts with the sensors and actuators in your smart home system.

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def main():
    # Create the home layout
    home = home_plan()

    # Iterate through the rooms and get readings from sensors
    for room in home:
        print(f"\n--- {room.name} ---")
        
        # Reading temperature
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        for sensor in temperature_sensors:
            sensor.turn_on()  # Turn on the sensor to get readings
            temperature = sensor.get_reading()
            if temperature is not None:
                print(f"Temperature: {temperature}°C")
                if temperature < TEMP_LOW:
                    print("Warning: Temperature is too low!")
                elif temperature > TEMP_HIGH:
                    print("Warning: Temperature is too high!")

        # Reading humidity
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        for sensor in humidity_sensors:
            sensor.turn_on()
            humidity = sensor.get_reading()
            if humidity is not None:
                print(f"Humidity: {humidity}%")
                if humidity < HUMIDITY_LOW:
                    print("Warning: Humidity is too low!")
                elif humidity > HUMIDITY_HIGH:
                    print("Warning: Humidity is too high!")

        # Reading light intensity
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        for sensor in light_sensors:
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                print(f"Light Intensity: {light_intensity} lux")
                if light_intensity < LIGHT_INTENSITY_LOW:
                    print("Warning: Light intensity is too low!")
                elif light_intensity > LIGHT_INTENSITY_HIGH:
                    print("Warning: Light intensity is too high!")

        # Here you could also control actuators based on sensor readings, e.g.:
        for actuator in room.actuators:
            if actuator.actuator_type in ["Heater", "AC"]:
                if actuator.actuator_type == "Heater" and temperature < TEMP_LOW:
                    actuator.turn_on()
                    actuator.set_target_temperature(22)  # Example target temperature
                elif actuator.actuator_type == "AC" and temperature > TEMP_HIGH:
                    actuator.turn_on()
                    actuator.set_target_temperature(20)  # Example target temperature
                else:
                    actuator.turn_off()

if __name__ == "__main__":
    main()