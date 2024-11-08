# Based on your functional description and the provided source code for your smart home project, I will create a `function.py` file that includes the main function to maintain the indoor temperature, humidity, and light intensity as per your requirements.
# 
# Here's the proposed `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def control_home_environment(home):
    for room in home:
        # Get sensors in the room
        temp_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
        humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
        light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
        
        # Get actuators in the room
        ac_units = [actuator for actuator in room.actuators if actuator.actuator_type == "AC"]
        heaters = [actuator for actuator in room.actuators if actuator.actuator_type == "Heater"]
        humidifiers = [actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"]
        lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]

        # Control Temperature
        for temp_sensor in temp_sensors:
            current_temperature = temp_sensor.get_reading()
            if current_temperature is not None:
                if current_temperature > TEMP_HIGH:
                    logger.info(f"{room.name}: Current temperature {current_temperature}°C exceeds {TEMP_HIGH}°C. Activating AC.")
                    for ac in ac_units:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temperature)
                else:
                    logger.info(f"{room.name}: Current temperature {current_temperature}°C is within acceptable range.")

                for heater in heaters:
                    heater.adjust_temperature(current_temperature)

        # Control Humidity
        for humidity_sensor in humidity_sensors:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity > HUMIDITY_LOW:
                    logger.info(f"{room.name}: Current humidity {current_humidity}% exceeds {HUMIDITY_LOW}%. Activating Humidifier.")
                    for humidifier in humidifiers:
                        humidifier.decrease_humidity()
                else:
                    logger.info(f"{room.name}: Current humidity {current_humidity}% is within acceptable range.")

        # Control Light Intensity
        for light_sensor in light_sensors:
            current_light = light_sensor.get_reading()
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_HIGH:
                    logger.info(f"{room.name}: Current light intensity {current_light} lux is below {LIGHT_INTENSITY_HIGH} lux. Activating lights.")
                    for light in lights:
                        light.turn_on()
                else:
                    logger.info(f"{room.name}: Current light intensity {current_light} lux is acceptable.")

def main():
    # Create home layout
    home = home_plan()
    control_home_environment(home)

if __name__ == "__main__":
    main()