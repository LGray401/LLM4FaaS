# Based on the functional description and the provided source code, I will create a `function.py` file that contains the main function to handle the automation of your smart home project. This function will monitor the readings from the sensors and accordingly control the actuators based on the specified conditions for temperature, humidity, and light intensity.
# 
# Here is the implementation of `function.py`:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Humidifier, Light

def main():
    # Create home layout with rooms, sensors, and actuators
    home = home_plan()

    # Check conditions in each room
    for room in home:
        print(f"Checking conditions in {room.name}...")
        
        # Get sensors and actuators in the room
        temperature_sensors = [s for s in room.sensors if s.sensor_type == 'IndoorTemperature']
        humidity_sensors = [s for s in room.sensors if s.sensor_type == 'Humidity']
        light_sensors = [s for s in room.sensors if s.sensor_type == 'LightIntensive']
        
        ac_units = [a for a in room.actuators if isinstance(a, AC)]
        humidifiers = [a for a in room.actuators if isinstance(a, Humidifier)]
        lights = [a for a in room.actuators if isinstance(a, Light)]

        # Check temperature
        for sensor in temperature_sensors:
            current_temp = sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH and ac_units:
                    for ac in ac_units:
                        ac.set_target_temperature(TEMP_HIGH)
                        ac.adjust_temperature(current_temp)

        # Check humidity
        for sensor in humidity_sensors:
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW and humidifiers:
                    for humidifier in humidifiers:
                        humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH and humidifiers:
                    for humidifier in humidifiers:
                        humidifier.decrease_humidity()

        # Check light intensity
        for sensor in light_sensors:
            current_light = sensor.get_reading()
            if current_light is not None:
                if current_light > LIGHT_INTENSITY_HIGH and lights:
                    for light in lights:
                        light.set_brightness_level("low")
                elif current_light <= LIGHT_INTENSITY_HIGH and lights:
                    for light in lights:
                        light.set_brightness_level("high")

if __name__ == "__main__":
    main()