# Based on your provided functional description and the source code, I will create a `function.py` file that contains the main function to control the smart home system according to the specified conditions. This script will be placed in the `functions` folder.
# 
# ### Functional Description
# - **Temperature**: When the indoor temperature reaches 26°C, turn on the AC to cool down.
# - **Humidity**: When the indoor humidity is below 36%, turn on the AC to increase humidity.
# - **Light Intensity**: When the indoor light intensity is above 80 lux, close the curtains.
# 
# ### `function.py`

import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    # Initialize the home plan
    home = home_plan()

    while True:
        for room in home:
            # Get the sensors and actuators for the current room
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Find the required sensors and actuators
            indoor_temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
            humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
            light_intensive_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)
            ac = next((a for a in actuators if isinstance(a, AC)), None)
            curtain = next((a for a in actuators if isinstance(a, Curtain)), None)

            # Check and control based on the temperature
            if indoor_temp_sensor and ac:
                indoor_temp_sensor.turn_on()
                temp_reading = indoor_temp_sensor.get_reading()
                if temp_reading and temp_reading > 26.0:
                    ac.set_target_temperature(25.0)  # Set target temperature to 25°C
                    ac.adjust_temperature(temp_reading)
                else:
                    ac.turn_off()

            # Check and control based on the humidity
            if humidity_sensor and ac:
                humidity_sensor.turn_on()
                humidity_reading = humidity_sensor.get_reading()
                if humidity_reading and humidity_reading < 36.0:
                    ac.turn_on()  # Turn on AC to increase humidity
                else:
                    ac.turn_off()

            # Check and control based on the light intensity
            if light_intensive_sensor and curtain:
                light_intensive_sensor.turn_on()
                light_reading = light_intensive_sensor.get_reading()
                if light_reading and light_reading > 80.0:
                    curtain.turn_on()  # Close the curtains
                else:
                    curtain.turn_off()  # Open the curtains

        # Wait for a short period before the next check
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()