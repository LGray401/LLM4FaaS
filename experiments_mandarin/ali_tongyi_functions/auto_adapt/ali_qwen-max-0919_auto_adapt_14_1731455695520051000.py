# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to handle the smart home functionalities. The main function will check the temperature, humidity, and light intensity, and take appropriate actions based on the given thresholds.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light

def main():
    # Initialize the home plan
    home = home_plan()

    # Define the rooms to monitor
    rooms_to_monitor = ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]

    for room_name in rooms_to_monitor:
        # Get sensors and actuators for the current room
        sensors = get_room_sensors(home, room_name)
        actuators = get_room_actuators(home, room_name)

        if not sensors or not actuators:
            print(f"Skipping {room_name} as it has no sensors or actuators.")
            continue

        # Check and handle temperature
        indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        ac = next((a for a in actuators if isinstance(a, AC)), None)
        heater = next((a for a in actuators if isinstance(a, Heater)), None)

        if indoor_temp_sensor:
            indoor_temp_sensor.turn_on()
            temp_reading = indoor_temp_sensor.get_reading()
            if temp_reading is not None:
                if temp_reading > TEMP_HIGH and ac:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(temp_reading)
                elif temp_reading < TEMP_LOW and heater:
                    heater.set_target_temperature(TEMP_LOW)
                    heater.adjust_temperature(temp_reading)
            indoor_temp_sensor.turn_off()

        # Check and handle humidity
        humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
        humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)

        if humidity_sensor:
            humidity_sensor.turn_on()
            humidity_reading = humidity_sensor.get_reading()
            if humidity_reading is not None:
                if humidity_reading < HUMIDITY_LOW and humidifier:
                    humidifier.increase_humidity()
                elif humidity_reading > HUMIDITY_HIGH and humidifier:
                    humidifier.decrease_humidity()
            humidity_sensor.turn_off()

        # Check and handle light intensity
        light_intensity_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)
        lights = [a for a in actuators if isinstance(a, Light)]

        if light_intensity_sensor:
            light_intensity_sensor.turn_on()
            light_reading = light_intensity_sensor.get_reading()
            if light_reading is not None:
                if light_reading < LIGHT_INTENSITY_LOW:
                    for light in lights:
                        light.turn_on()
                        light.set_brightness_level("high")
                elif light_reading > LIGHT_INTENSITY_HIGH:
                    for light in lights:
                        light.turn_off()
            light_intensity_sensor.turn_off()

if __name__ == "__main__":
    main()