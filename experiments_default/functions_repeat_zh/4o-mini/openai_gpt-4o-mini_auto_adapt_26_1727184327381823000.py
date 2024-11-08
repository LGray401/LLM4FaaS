# Here is the `function.py` file based on your functional description and the provided source code. This file includes a `main` function that manages the temperature, humidity, and light intensity according to the requirements specified:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def maintain_conditions(home):
    for room in home:
        # Get sensors and actuators in the room
        temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        humidity_sensors = [sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)]
        light_sensors = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]
        
        heaters = [actuator for actuator in room.actuators if isinstance(actuator, Heater)]
        acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
        humidifiers = [actuator for actuator in room.actuators if isinstance(actuator, Humidifier)]
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        
        # Maintain temperature
        if temp_sensors and heaters and acs:
            current_temp = temp_sensors[0].get_reading()
            if current_temp is not None:
                for heater in heaters:
                    heater.set_target_temperature(26)  # Target temperature
                    heater.adjust_temperature(current_temp)
                for ac in acs:
                    ac.set_target_temperature(26)  # Target temperature
                    ac.adjust_temperature(current_temp)

        # Maintain humidity
        if humidity_sensors and humidifiers:
            current_humidity = humidity_sensors[0].get_reading()
            if current_humidity is not None:
                if current_humidity < 60:
                    for humidifier in humidifiers:
                        humidifier.increase_humidity()
                elif current_humidity > 60:
                    for humidifier in humidifiers:
                        humidifier.decrease_humidity()

        # Maintain light intensity based on work, relax, and rest
        if light_sensors and lights:
            current_light = light_sensors[0].get_reading()
            if current_light is not None:
                # Example logic for light adjustment based on time of day or activity
                # Here you would implement your own logic to check if someone is working, relaxing, or resting
                # For simplicity, let's assume the following:
                activity = "work"  # This should be dynamically determined by your application logic

                if activity == "work":
                    for light in lights:
                        light.set_brightness_level("high")
                elif activity == "relax":
                    for light in lights:
                        light.set_brightness_level("low")
                elif activity == "rest":
                    for light in lights:
                        light.turn_off()

def main():
    home = home_plan()
    maintain_conditions(home)

if __name__ == "__main__":
    main()