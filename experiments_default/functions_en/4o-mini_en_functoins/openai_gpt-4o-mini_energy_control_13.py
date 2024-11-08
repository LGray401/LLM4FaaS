# Based on the functional description you've provided, we need to implement logic in `function.py` that manages the various smart home components (sensors and actuators) to automate the actions of turning off lights, sockets, heating, air conditioning, and more based on the current conditions.
# 
# Here's the code for `function.py` that incorporates these functionalities:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, LIGHT_INTENSITY_HIGH, HUMIDITY_HIGH
import time

def manage_home(home):
    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        # Check sensors and take actions accordingly
        indoor_temp_sensor = next((s for s in sensors if s.sensor_type == "IndoorTemperature"), None)
        light_sensor = next((s for s in sensors if s.sensor_type == "LightIntensive"), None)
        humidity_sensor = next((s for s in sensors if s.sensor_type == "Humidity"), None)
        
        # Get current readings
        indoor_temp = indoor_temp_sensor.get_reading() if indoor_temp_sensor else None
        light_reading = light_sensor.get_reading() if light_sensor else None
        humidity_reading = humidity_sensor.get_reading() if humidity_sensor else None
        
        # Manage lights
        if light_reading is not None and light_reading < LIGHT_INTENSITY_HIGH:
            for actuator in actuators:
                if actuator.actuator_type == "Light":
                    actuator.turn_off()

        # Manage heater
        if indoor_temp is not None:
            if indoor_temp < TEMP_LOW:
                for actuator in actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.turn_on()
            else:
                for actuator in actuators:
                    if actuator.actuator_type == "Heater":
                        actuator.turn_off()

        # Manage AC
        if indoor_temp is not None:
            for actuator in actuators:
                if actuator.actuator_type == "AC":
                    # Assuming we have some condition to check if windows are closed
                    windows_closed = True  # This should be determined by a window sensor or status
                    if indoor_temp > TEMP_LOW and windows_closed:
                        actuator.turn_on()
                    else:
                        actuator.turn_off()

        # Manage sockets (Assuming SmartSockets are used)
        for actuator in actuators:
            if actuator.actuator_type == "SmartSocket":
                # Assuming we determine if there's load (e.g., via a sensor)
                load_in_use = False  # This should be determined by a load sensor
                if not load_in_use:
                    actuator.turn_off()

def main():
    home = home_plan()
    while True:
        manage_home(home)
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()