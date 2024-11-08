# Based on the provided functional description and source code, we can create a `function.py` file that contains the main function to control and monitor the smart home environment. The main function will utilize the sensors and actuators defined in the other modules to maintain the desired temperature, humidity, and light intensity levels.
# 
# Here is a possible implementation of the `function.py` file:

from home.sensor import get_all_sensors
from home.actuator import get_all_actuators
from home.home_plan import home_plan, get_room
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def maintain_environment(home):
    while True:
        for room in home:
            # Get sensors for the current room
            temp_sensors = get_all_sensors(home, "IndoorTemperature") + get_all_sensors(home, "OutdoorTemperature")
            humidity_sensors = get_all_sensors(home, "Humidity")
            light_sensors = get_all_sensors(home, "LightIntensive")

            # Initialize variables to store readings
            temp_readings = []
            humidity_readings = []
            light_readings = []

            # Collect sensor readings
            for sensor in temp_sensors:
                if sensor.room_name == room.name:
                    sensor.turn_on()
                    temp_readings.append(sensor.get_reading())
                    sensor.turn_off()

            for sensor in humidity_sensors:
                if sensor.room_name == room.name:
                    sensor.turn_on()
                    humidity_readings.append(sensor.get_reading())
                    sensor.turn_off()

            for sensor in light_sensors:
                if sensor.room_name == room.name:
                    sensor.turn_on()
                    light_readings.append(sensor.get_reading())
                    sensor.turn_off()

            # Calculate average readings
            avg_temp = sum(temp_readings) / len(temp_readings) if temp_readings else 0
            avg_humidity = sum(humidity_readings) / len(humidity_readings) if humidity_readings else 0
            avg_light = sum(light_readings) / len(light_readings) if light_readings else 0

            # Get actuators for the current room
            heaters = get_all_actuators(home, "Heater")
            acs = get_all_actuators(home, "AC")
            humidifiers = get_all_actuators(home, "Humidifier")
            lights = get_all_actuators(home, "Light")

            # Control temperature
            for heater in heaters:
                if heater.room_name == room.name and avg_temp < TEMP_LOW:
                    heater.turn_on()
                    heater.set_target_temperature(TEMP_LOW + 1)  # Set slightly higher than threshold for comfort
                else:
                    heater.turn_off()

            for ac in acs:
                if ac.room_name == room.name and avg_temp > TEMP_HIGH:
                    ac.turn_on()
                    ac.set_target_temperature(TEMP_HIGH - 1)  # Set slightly lower than threshold for comfort
                else:
                    ac.turn_off()

            # Control humidity
            for humidifier in humidifiers:
                if humidifier.room_name == room.name:
                    if avg_humidity < HUMIDITY_LOW:
                        humidifier.increase_humidity()
                    elif avg_humidity > HUMIDITY_HIGH:
                        humidifier.decrease_humidity()

            # Control light intensity
            for light in lights:
                if light.room_name == room.name:
                    if avg_light < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level("high")
                    elif avg_light > LIGHT_INTENSITY_HIGH:
                        light.turn_off()
                    else:
                        light.set_brightness_level("medium")

        # Sleep for a while before checking again
        time.sleep(10)

def main():
    # Initialize the home plan
    home = home_plan()

    # Start maintaining the environment
    maintain_environment(home)

if __name__ == "__main__":
    main()