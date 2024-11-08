# Based on your functional description and the provided source code files, I'll create a `function.py` file that will serve as the main entry point for your smart home project. This file will interact with the sensors and actuators to manage and monitor the environment based on the specified temperature, humidity, and light intensity.
# 
# Here's the `function.py` file content:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.logger_config import logger
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create the home plan
    home = home_plan()

    # Define target conditions
    desired_temperature = 24
    desired_humidity = 30
    desired_light_intensity = 45

    # Loop through each room to check conditions and take action
    for room in home:
        print(f"Checking conditions in {room.name}...")

        # Get sensors and actuators in the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Read sensor values and determine actions
        temperature_sensor = next((s for s in sensors if s.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((s for s in sensors if s.sensor_type == "Humidity"), None)
        light_sensor = next((s for s in sensors if s.sensor_type == "LightIntensive"), None)

        current_temperature = temperature_sensor.get_reading() if temperature_sensor else None
        current_humidity = humidity_sensor.get_reading() if humidity_sensor else None
        current_light_intensity = light_sensor.get_reading() if light_sensor else None

        # Adjust temperature using heaters or AC
        if current_temperature is not None:
            for actuator in actuators:
                if isinstance(actuator, Heater):
                    actuator.set_target_temperature(desired_temperature)
                    actuator.adjust_temperature(current_temperature)
                elif isinstance(actuator, AC):
                    actuator.set_target_temperature(desired_temperature)
                    actuator.adjust_temperature(current_temperature)

        # Adjust humidity using humidifiers
        if current_humidity is not None:
            humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
            if humidifier:
                if current_humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

        # Adjust light conditions
        if current_light_intensity is not None:
            light = next((a for a in actuators if isinstance(a, Light)), None)
            if light:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    light.turn_off()

    print("Smart home management completed.")

if __name__ == "__main__":
    main()