# Based on your provided functional description and the source code for `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py`, I will create a `function.py` file that contains the main function to control the smart home system according to the specified requirements.
# 
# ### Functional Requirements:
# 1. **Temperature Control:**
#    - When the indoor temperature is above 26°C, automatically turn on the AC to regulate the temperature.
#    
# 2. **Humidity Control:**
#    - Ensure the humidity is within the normal range (no specific action required in this case, but we can add logging or notifications if needed).
# 
# 3. **Light Intensity Control:**
#    - When the light intensity is high (e.g., during midday), automatically open the curtains.
# 
# ### `function.py` Implementation:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, Curtain
from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
import time

def main():
    # Initialize the home plan
    home = home_plan()

    # Main loop to continuously monitor and control the home
    while True:
        # Check and control temperature
        for room in home:
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Get all indoor temperature sensors
            temp_sensors = [s for s in sensors if isinstance(s, IndoorTemperatureSensor)]
            acs = [a for a in actuators if isinstance(a, AC)]

            for sensor in temp_sensors:
                if sensor.get_status() == "on":
                    current_temp = sensor.get_reading()
                    if current_temp is not None and current_temp > TEMP_HIGH:
                        for ac in acs:
                            ac.set_target_temperature(TEMP_HIGH)
                            ac.adjust_temperature(current_temp)
                            print(f"AC in {room.name} turned on to cool down the room.")
                    else:
                        for ac in acs:
                            ac.turn_off()
                            print(f"AC in {room.name} turned off as the temperature is within the normal range.")

        # Check and control light intensity
        for room in home:
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Get all light intensity sensors
            light_sensors = [s for s in sensors if isinstance(s, LightIntensiveSensor)]
            curtains = [a for a in actuators if isinstance(a, Curtain)]

            for sensor in light_sensors:
                if sensor.get_status() == "on":
                    current_light_intensity = sensor.get_reading()
                    if current_light_intensity is not None and current_light_intensity > LIGHT_INTENSITY_HIGH:
                        for curtain in curtains:
                            curtain.turn_on()
                            print(f"Curtain in {room.name} opened due to high light intensity.")
                    else:
                        for curtain in curtains:
                            curtain.turn_off()
                            print(f"Curtain in {room.name} closed as the light intensity is within the normal range.")

        # Sleep for a short duration before the next check
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()