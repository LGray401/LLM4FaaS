# Based on the provided functional description and source code, I will create a `function.py` file that contains a `main` function to demonstrate how the smart home system could be used. This `main` function will simulate the interaction between sensors and actuators based on the sensor readings and predefined rules.
# 
# Here is the content of `function.py`:

# function.py
import logging
from home.sensor import Sensor, IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Actuator, Heater, AC, CoffeeMachine, Window, Curtain, MusicPlayer, Door, \
    CleaningRobot, SmartTV, NotificationSender, Light, Humidifier
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators

# Configure logging
logging.basicConfig(level=logging.INFO)

# Main function to simulate smart home system operation
def main():
    # Create home plan
    home = home_plan()

    # Example interaction with sensors and actuators
    # Get sensors and actuators for a specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all sensors of a specific type
    all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # Simulate sensor readings and actuator responses
    for sensor in living_room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature = sensor.get_reading()
            # Check if the temperature is too high and turn on the AC
            if temperature > TEMP_HIGH:
                for actuator in living_room_actuators:
                    if isinstance(actuator, AC):
                        actuator.turn_on()
                        break
            # Check if the temperature is too low and turn on the heater
            elif temperature < TEMP_LOW:
                for actuator in living_room_actuators:
                    if isinstance(actuator, Heater):
                        actuator.turn_on()
                        break
        elif isinstance(sensor, HumiditySensor):
            humidity = sensor.get_reading()
            # Check if the humidity is too low and turn on the humidifier
            if humidity < HUMIDITY_LOW:
                for actuator in living_room_actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.increase_humidity()
                        break
            # Check if the humidity is too high and turn off the humidifier
            elif humidity > HUMIDITY_HIGH:
                for actuator in living_room_actuators:
                    if isinstance(actuator, Humidifier):
                        actuator.decrease_humidity()
                        break

    # Print information about the home plan
    for room in home:
        print(f"Room: {room.name}")
        print(f"Sensors: {[sensor.id for sensor in room.sensors]}")
        print(f"Actuators: {[actuator.id for actuator in room.actuators]}")
        print("")

if __name__ == "__main__":
    main()