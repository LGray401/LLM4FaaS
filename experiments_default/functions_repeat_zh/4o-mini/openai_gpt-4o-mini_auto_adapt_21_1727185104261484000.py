# Based on your functional description and the provided source code, I will create a `function.py` file that implements the required functionalities of automatically controlling the air conditioning when the temperature exceeds 26°C, managing humidity levels, and controlling the curtains based on light intensity.
# 
# Here is the `function.py` file that meets your requirements:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Curtain

def main():
    # Initialize home plan
    home = home_plan()

    # Example: Assume we are focusing on the Living Room
    living_room = next(room for room in home if room.name == "LivingRoom")
    
    # Sensors in the Living Room
    temperature_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor))
    humidity_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, HumiditySensor))
    light_sensor = next(sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor))

    # Actuators in the Living Room
    ac = next(actuator for actuator in living_room.actuators if isinstance(actuator, AC))
    humidifier = next(actuator for actuator in living_room.actuators if isinstance(actuator, Humidifier))
    curtain = next(actuator for actuator in living_room.actuators if isinstance(actuator, Curtain))

    # Main logic for controlling temperature, humidity, and curtains
    # Check temperature and control AC
    current_temperature = temperature_sensor.get_reading()
    if current_temperature is not None:
        if current_temperature > 26:
            ac.set_target_temperature(25)  # Set desired temperature for AC
            ac.adjust_temperature(current_temperature)

    # Check humidity and control humidifier
    current_humidity = humidity_sensor.get_reading()
    if current_humidity is not None:
        if current_humidity < 30:
            humidifier.increase_humidity()
        elif current_humidity > 50:
            humidifier.decrease_humidity()

    # Check light intensity and control curtains
    light_intensity = light_sensor.get_reading()
    if light_intensity is not None:
        if light_intensity > LIGHT_INTENSITY_HIGH:
            curtain.turn_on()  # Open curtains when light is too intense
        else:
            curtain.turn_off()  # Close curtains when light is normal

if __name__ == "__main__":
    main()