# Based on the functional description and the provided source code, I will create the `function.py` file that will implement the main function to monitor temperature, humidity, and light intensity, and control the actuators accordingly.
# 
# Here's how the `function.py` file will be structured:
# 
# 1. It will initialize the home environment using the `home_plan` function.
# 2. It will retrieve the necessary sensors and actuators for each room.
# 3. It will continuously monitor the readings from the sensors.
# 4. It will control the actuators to maintain the specified conditions for temperature, humidity, and light intensity.
# 
# Here is the content of `function.py`:

import time
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def monitor_home_conditions():
    home = home_plan()

    while True:
        for room in home:
            # Get sensors and actuators for the room
            temperature_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"]
            humidity_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"]
            light_sensors = [sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"]
            heaters = [actuator for actuator in room.actuators if actuator.actuator_type == "Heater"]
            acs = [actuator for actuator in room.actuators if actuator.actuator_type == "AC"]
            humidifiers = [actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"]
            lights = [actuator for actuator in room.actuators if actuator.actuator_type == "Light"]

            # Monitor temperature
            for sensor in temperature_sensors:
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    for heater in heaters:
                        heater.adjust_temperature(current_temp)
                    for ac in acs:
                        ac.adjust_temperature(current_temp)

            # Monitor humidity
            for sensor in humidity_sensors:
                current_humidity = sensor.get_reading()
                if current_humidity is not None:
                    for humidifier in humidifiers:
                        if current_humidity < HUMIDITY_LOW:
                            humidifier.increase_humidity()
                        else:
                            humidifier.decrease_humidity()

            # Monitor light intensity
            for sensor in light_sensors:
                current_light = sensor.get_reading()
                if current_light is not None:
                    for light in lights:
                        if current_light < LIGHT_INTENSITY_LOW:
                            light.turn_on()
                        else:
                            light.turn_off()

        # Sleep for a short duration before the next reading
        time.sleep(5)

def main():
    print("Starting home monitoring system...")
    monitor_home_conditions()

if __name__ == "__main__":
    main()