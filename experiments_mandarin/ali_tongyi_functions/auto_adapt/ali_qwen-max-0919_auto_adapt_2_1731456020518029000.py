# Based on your provided functional description and the source code, I will create a `function.py` file that contains the main function to control the smart home system. This function will handle the logic for temperature, humidity, and light intensity as per your requirements.
# 
# Here is the `function.py` file:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Window, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()

    # Loop through each room in the home
    for room in home:
        # Get sensors and actuators for the current room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Find the relevant sensors and actuators
        indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
        light_intensity_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)
        
        ac = next((a for a in actuators if isinstance(a, AC)), None)
        window = next((a for a in actuators if isinstance(a, Window)), None)
        humidifier = next((a for a in actuators if isinstance(a, Humidifier)), None)
        light = next((a for a in actuators if isinstance(a, Light)), None)

        # Check and control temperature
        if indoor_temp_sensor and ac:
            temp_reading = indoor_temp_sensor.get_reading()
            if temp_reading and temp_reading > TEMP_HIGH:
                ac.turn_on()
                if window and window.status == "on":
                    window.turn_off()
            else:
                ac.turn_off()

        # Check and control humidity
        if humidity_sensor and humidifier:
            humidity_reading = humidity_sensor.get_reading()
            if humidity_reading and humidity_reading < HUMIDITY_LOW:
                humidifier.turn_on()
            else:
                humidifier.turn_off()

        # Check and control light intensity
        if light_intensity_sensor and light:
            light_reading = light_intensity_sensor.get_reading()
            if light_reading:
                if light_reading < LIGHT_INTENSITY_LOW:
                    light.set_brightness_level("high")
                elif light_reading < LIGHT_INTENSITY_HIGH:
                    light.set_brightness_level("medium")
                else:
                    light.set_brightness_level("low")

if __name__ == "__main__":
    main()