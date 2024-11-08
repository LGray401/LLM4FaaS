# Based on your functional description and the provided source code, I will create a `function.py` file that maintains the indoor temperature, humidity, and light intensity according to your specified requirements. 
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def maintain_environment(home):
    for room in home:
        # Get relevant sensors and actuators for controlling the environment
        temp_sensors = [s for s in room.sensors if s.sensor_type == "IndoorTemperature"]
        humidity_sensors = [s for s in room.sensors if s.sensor_type == "Humidity"]
        light_sensors = [s for s in room.sensors if s.sensor_type == "LightIntensive"]
        heaters = [a for a in room.actuators if a.actuator_type == "Heater"]
        acs = [a for a in room.actuators if a.actuator_type == "AC"]
        lights = [a for a in room.actuators if a.actuator_type == "Light"]

        # Maintain temperature
        for temp_sensor in temp_sensors:
            current_temp = temp_sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH:
                    logger.info(f"Temperature is above {TEMP_HIGH}°C. Turning on AC.")
                    for ac in acs:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temp)
                else:
                    for heater in heaters:
                        heater.turn_off()

        # Maintain humidity
        for humidity_sensor in humidity_sensors:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity > HUMIDITY_LOW:
                    logger.info("Humidity is above 30%. Turning on Humidifier.")
                    # Assuming you have a Humidifier actuator in the room
                    humidifier = next((a for a in room.actuators if a.actuator_type == "Humidifier"), None)
                    if humidifier:
                        humidifier.decrease_humidity()

        # Maintain light intensity
        for light_sensor in light_sensors:
            current_light = light_sensor.get_reading()
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_LOW:
                    logger.info("Light intensity is below threshold. Turning on lights.")
                    for light in lights:
                        light.turn_on()
                elif current_light > LIGHT_INTENSITY_HIGH:
                    logger.info("Light intensity is above threshold. Turning off lights.")
                    for light in lights:
                        light.turn_off()

def main():
    logger.info("Starting smart home environment maintenance...")
    home = home_plan()
    maintain_environment(home)
    logger.info("Smart home environment maintenance completed.")

if __name__ == "__main__":
    main()