# Based on your functional description and the provided source code, I will create the `function.py` file which will be responsible for controlling the smart home environment according to your requirements:
# 
# 1. **Temperature**:
#     - If indoor temperature exceeds 25°C, the air conditioner will turn on and the windows will close.
#     
# 2. **Humidity**:
#     - If indoor humidity is too low, the humidifier will turn on.
#     
# 3. **Light Intensity**:
#     - Adjust the lights based on the indoor sunlight intensity.
# 
# Here is the `function.py` file:
# 
# ## function.py

from home.home_plan import home_plan, get_all_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Window, Humidifier, Light
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

def main():
    # Get the home layout with rooms, sensors, and actuators
    home = home_plan()

    # Get all indoor temperature sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    # Get all light intensity sensors
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Check and control temperature
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        temp_reading = sensor.get_reading()
        if temp_reading is not None and temp_reading > TEMP_HIGH:
            room_actuators = get_room_actuators(home, sensor.room_name)
            for actuator in room_actuators:
                if isinstance(actuator, AC):
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(temp_reading)
                if isinstance(actuator, Window):
                    actuator.turn_off()

    # Check and control humidity
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity_reading = sensor.get_reading()
        if humidity_reading is not None and humidity_reading < HUMIDITY_LOW:
            room_actuators = get_room_actuators(home, sensor.room_name)
            for actuator in room_actuators:
                if isinstance(actuator, Humidifier):
                    actuator.turn_on()

    # Check and control light intensity
    for sensor in light_sensors:
        sensor.turn_on()
        light_reading = sensor.get_reading()
        room_actuators = get_room_actuators(home, sensor.room_name)
        for actuator in room_actuators:
            if isinstance(actuator, Light):
                if light_reading is not None and light_reading < LIGHT_INTENSITY_LOW:
                    actuator.turn_on()
                    actuator.set_brightness_level("high")
                elif light_reading is not None and light_reading > LIGHT_INTENSITY_HIGH:
                    actuator.turn_off()

if __name__ == "__main__":
    main()