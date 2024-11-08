# Based on your functional description and provided source code, I will create a `function.py` file in the `functions` folder that contains the main function to control the smart home system according to the given conditions.
# 
# Here is the `function.py` file:

# function.py
import logging
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

# Configure logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

def main():
    # Create rooms and sensors/actuators
    home = home_plan()

    # Define sensors and actuators
    living_room_temp_sensor = get_room_sensors(home, "LivingRoom")[0]
    living_room_humidity_sensor = get_room_sensors(home, "LivingRoom")[1]
    living_room_light_sensor = get_room_sensors(home, "LivingRoom")[2]
    living_room_heater = get_room_actuators(home, "LivingRoom")[1]
    living_room_ac = get_room_actuators(home, "LivingRoom")[2]
    living_room_humidifier = get_room_actuators(home, "LivingRoom")[3]

    # Monitor and control the living room
    while True:
        # Get current readings
        temp = living_room_temp_sensor.get_reading()
        humidity = living_room_humidity_sensor.get_reading()
        light_intensity = living_room_light_sensor.get_reading()

        # Control temperature
        if temp is not None and (temp < TEMP_LOW or temp > TEMP_HIGH):
            if temp < TEMP_LOW:
                living_room_heater.turn_on()
                living_room_ac.turn_off()
            elif temp > TEMP_HIGH:
                living_room_ac.turn_on()
                living_room_heater.turn_off()

        # Control humidity
        if humidity is not None and (humidity < HUMIDITY_LOW or humidity > HUMIDITY_HIGH):
            if humidity < HUMIDITY_LOW:
                living_room_humidifier.increase_humidity()
            elif humidity > HUMIDITY_HIGH:
                living_room_humidifier.decrease_humidity()

        # Control light intensity (if needed)
        # This part is not implemented as the description only mentions temperature and humidity.
        
        # Sleep for a while before checking again
        time.sleep(10)

if __name__ == "__main__":
    main()