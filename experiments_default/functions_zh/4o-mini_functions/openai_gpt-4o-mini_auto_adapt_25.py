# Based on your functional description and the provided code files, we will create a `function.py` file that implements the desired logic for controlling the AC (air conditioner) for temperature and humidity, and the curtain for light intensity.
# 
# The main function in `function.py` will check the readings from the sensors and take actions using the actuators when certain conditions are met. Here's how the `function.py` file will look:

# function.py
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Curtain
from home.logger_config import logger

def control_smart_home(home):
    for room in home:
        # Get the sensors and actuators in the room
        temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        
        ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
        
        # Check temperature
        for temp_sensor in temperature_sensors:
            temp_reading = temp_sensor.get_reading()
            if temp_reading is not None:
                if temp_reading >= TEMP_HIGH:
                    for ac in ac_units:
                        ac.turn_on()
                else:
                    for ac in ac_units:
                        ac.turn_off()

        # Check humidity
        for humidity_sensor in humidity_sensors:
            humidity_reading = humidity_sensor.get_reading()
            if humidity_reading is not None:
                if humidity_reading < HUMIDITY_LOW:
                    for ac in ac_units:
                        ac.turn_on()  # Turn on AC for humidification (if applicable)
                else:
                    for ac in ac_units:
                        ac.turn_off()

        # Check light intensity
        for light_sensor in light_sensors:
            light_reading = light_sensor.get_reading()
            if light_reading is not None:
                if light_reading > LIGHT_INTENSITY_HIGH:
                    for curtain in curtains:
                        curtain.turn_on()  # Assuming curtain has a method to close it
                else:
                    for curtain in curtains:
                        curtain.turn_off()  # Assuming curtain has a method to open it

def main():
    logger.info("Starting Smart Home Control...")
    home = home_plan()
    control_smart_home(home)
    logger.info("Smart Home Control finished.")

if __name__ == "__main__":
    main()