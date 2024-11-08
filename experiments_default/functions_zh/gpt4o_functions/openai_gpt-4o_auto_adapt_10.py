# Given the functional description and the provided source code files, we can create the `function.py` file which will be placed in the `functions` folder. This file will contain the main function to interact with the smart home system.
# 
# ### function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Initialize the home plan
    home = home_plan()

    # Get sensors for LivingRoom
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    
    # Get actuators for LivingRoom
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn on all sensors in the LivingRoom
    for sensor in living_room_sensors:
        sensor.turn_on()

    # Get readings from sensors
    temperature_reading = None
    humidity_reading = None
    light_intensity_reading = None

    for sensor in living_room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature_reading = sensor.get_reading()
        elif isinstance(sensor, HumiditySensor):
            humidity_reading = sensor.get_reading()
        elif isinstance(sensor, LightIntensiveSensor):
            light_intensity_reading = sensor.get_reading()

    # Print the readings
    print(f"Temperature: {temperature_reading}°")
    print(f"Humidity: {humidity_reading}")
    print(f"Light Intensity: {light_intensity_reading}")

    # Control actuators based on sensor readings
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Heater" and temperature_reading is not None:
            if temperature_reading < TEMP_LOW:
                actuator.turn_on()
            else:
                actuator.turn_off()
        elif actuator.actuator_type == "AC" and temperature_reading is not None:
            if temperature_reading > TEMP_HIGH:
                actuator.turn_on()
            else:
                actuator.turn_off()
        elif actuator.actuator_type == "Humidifier" and humidity_reading is not None:
            if humidity_reading < HUMIDITY_LOW:
                actuator.increase_humidity()
            elif humidity_reading > HUMIDITY_HIGH:
                actuator.decrease_humidity()
        elif actuator.actuator_type == "Light" and light_intensity_reading is not None:
            if light_intensity_reading < LIGHT_INTENSITY_LOW:
                actuator.turn_on()
            else:
                actuator.turn_off()

if __name__ == "__main__":
    main()