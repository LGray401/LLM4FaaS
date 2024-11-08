# Sure, I can help you create the `function.py` file based on your description and the provided source code.
# 
# The main function will control the actuators based on the sensor readings to maintain the desired environment in the smart home. We'll need to use the sensors to get the current readings and then adjust the actuators accordingly.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light, Curtain
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH

def main():
    # Initialize home plan
    home = home_plan()

    for room in home:
        print(f"Checking {room.name}")

        # Get sensors and actuators in the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Initialize variables to store sensor readings
        indoor_temp = None
        humidity = None
        light_intensity = None

        # Get readings from sensors
        for sensor in sensors:
            sensor.turn_on()  # Ensure the sensor is turned on
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp = sensor.get_reading()
            elif isinstance(sensor, HumiditySensor):
                humidity = sensor.get_reading()
            elif isinstance(sensor, LightIntensiveSensor):
                light_intensity = sensor.get_reading()
            sensor.turn_off()  # Turn off the sensor after getting the reading

        # Control actuators based on sensor readings
        for actuator in actuators:
            if isinstance(actuator, AC):
                if indoor_temp is not None and indoor_temp > TEMP_HIGH:
                    actuator.turn_on()
                    actuator.set_target_temperature(TEMP_HIGH)
                else:
                    actuator.turn_off()
            elif isinstance(actuator, Heater):
                if indoor_temp is not None and indoor_temp < TEMP_HIGH:
                    actuator.turn_on()
                    actuator.set_target_temperature(TEMP_HIGH)
                else:
                    actuator.turn_off()
            elif isinstance(actuator, Humidifier):
                if humidity is not None:
                    if humidity > HUMIDITY_HIGH:
                        actuator.decrease_humidity()
                    else:
                        actuator.increase_humidity()
            elif isinstance(actuator, Light):
                if light_intensity is not None:
                    if light_intensity < LIGHT_INTENSITY_HIGH:
                        actuator.turn_on()
                        actuator.set_brightness_level("high")
                    else:
                        actuator.turn_off()
            elif isinstance(actuator, Curtain):
                if light_intensity is not None and light_intensity > LIGHT_INTENSITY_HIGH:
                    actuator.turn_on()  # Assume turning on the curtain means opening it
                else:
                    actuator.turn_off()  # Assume turning off the curtain means closing it

if __name__ == "__main__":
    main()