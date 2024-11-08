# Based on the functional description and the provided source code, the `function.py` file will implement the main function to maintain the indoor temperature, humidity, and light intensity according to your specifications. Below is the code for `function.py`:

# function.py
import time
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def maintain_environment(home):
    while True:
        for room in home:
            # Get sensors and actuators for the room
            temperature_sensors = get_all_sensors(home, "IndoorTemperature")
            humidity_sensors = get_all_sensors(home, "Humidity")
            light_sensors = get_all_sensors(home, "LightIntensive")
            lights = get_all_actuators(home, "Light")
            ac_units = get_all_actuators(home, "AC")
            heaters = get_all_actuators(home, "Heater")
            humidifiers = get_all_actuators(home, "Humidifier")

            # Check temperature
            current_temperature = sum(sensor.get_reading() for sensor in temperature_sensors if sensor.get_reading() is not None) / len(temperature_sensors)
            print(f"Current temperature in {room.name}: {current_temperature}°C")
            if current_temperature > TEMP_HIGH:
                # If too hot, turn on AC and turn off Heater
                for ac in ac_units:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temperature)
                for heater in heaters:
                    heater.turn_off()
            else:
                # If too cold, turn on Heater and turn off AC
                for heater in heaters:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(current_temperature)
                for ac in ac_units:
                    ac.turn_off()

            # Check humidity
            current_humidity = sum(sensor.get_reading() for sensor in humidity_sensors if sensor.get_reading() is not None) / len(humidity_sensors)
            print(f"Current humidity in {room.name}: {current_humidity}%")
            if current_humidity > HUMIDITY_LOW:
                for humidifier in humidifiers:
                    humidifier.decrease_humidity()

            # Check light intensity
            current_light_intensity = sum(sensor.get_reading() for sensor in light_sensors if sensor.get_reading() is not None) / len(light_sensors)
            print(f"Current light intensity in {room.name}: {current_light_intensity} lux")
            if current_light_intensity > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    light.turn_off()
            else:
                for light in lights:
                    light.turn_on()

        # Wait before the next reading
        time.sleep(5)  # Adjust the time as necessary

def main():
    home = home_plan()
    maintain_environment(home)

if __name__ == "__main__":
    main()