# Based on the functional description and the provided source code, you need to create a `function.py` file that contains the main function. This function should control the smart home system according to the following rules:
#
# 1. When the indoor temperature reaches 26℃, turn on the air conditioner to cool down.
# 2. When the indoor humidity is below 36 degrees, turn on the air conditioner to humidify.
# 3. Draw the curtains when the indoor light intensity is higher than 80.
#
# Here is a Python script that implements these functionalities:
#
# ```python
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    # Get the home plan
    home = home_plan()

    # Get the sensors and actuators for the room
    sensors = get_room_sensors(home, "LivingRoom")
    actuators = get_room_actuators(home, "LivingRoom")

    # Get the specific sensors and actuators we need
    temperature_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    humidity_sensor = next((sensor for sensor in sensors if isinstance(sensor, HumiditySensor)), None)
    light_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)
    ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
    curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)

    # Check the temperature and control the AC
    if temperature_sensor.get_reading() >= 26:
        ac.turn_on()
    else:
        ac.turn_off()

    # Check the humidity and control the AC
    if humidity_sensor.get_reading() < 36:
        ac.turn_on()
    else:
        ac.turn_off()

    # Check the light intensity and control the curtain
    if light_sensor.get_reading() > 80:
        curtain.turn_on()
    else:
        curtain.turn_off()

if __name__ == "__main__":
    main()
# ```
#
# This script should be saved as `function.py` in the `functions` folder. It first retrieves the home plan and the sensors and actuators for the "LivingRoom". It then checks the readings from the temperature, humidity, and light sensors and controls the air conditioner and curtains accordingly.