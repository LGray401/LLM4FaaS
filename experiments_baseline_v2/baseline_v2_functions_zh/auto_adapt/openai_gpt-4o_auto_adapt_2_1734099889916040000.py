# To create a smart home application based on the functional description you provided, we will make use of the existing sensor and actuator classes, as well as the home plan setup. The application will simulate a home environment where sensors read data and actuators respond based on the sensor readings. We'll create a main script to implement this logic.
# 
# ### Smart Home Application (`smart_home.py`)
# 
# ```python
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Window, Humidifier, Light
from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW

def control_temperature(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)
    temp_sensors = [s for s in sensors if isinstance(s, IndoorTemperatureSensor)]
    acs = [a for a in actuators if isinstance(a, AC)]
    windows = [a for a in actuators if isinstance(a, Window)]
    
    for sensor in temp_sensors:
        sensor.turn_on()
        temperature = sensor.get_reading()
        for ac in acs:
            ac.set_target_temperature(TEMP_HIGH)
            ac.adjust_temperature(temperature)
        for window in windows:
            if temperature > TEMP_HIGH:
                window.turn_off()  # Close the window if it's too hot
            else:
                window.turn_on()

def control_humidity(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)
    humidity_sensors = [s for s in sensors if isinstance(s, HumiditySensor)]
    humidifiers = [a for a in actuators if isinstance(a, Humidifier)]
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        humidity = sensor.get_reading()
        for humidifier in humidifiers:
            if humidity < HUMIDITY_LOW:
                humidifier.turn_on()
                humidifier.increase_humidity()
            else:
                humidifier.turn_off()

def control_light(room):
    sensors = get_room_sensors(home, room)
    actuators = get_room_actuators(home, room)
    light_sensors = [s for s in sensors if isinstance(s, LightIntensiveSensor)]
    lights = [a for a in actuators if isinstance(a, Light)]
    
    for sensor in light_sensors:
        sensor.turn_on()
        light_intensity = sensor.get_reading()
        for light in lights:
            if light_intensity < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("high")
            else:
                light.turn_off()

if __name__ == "__main__":
    home = home_plan()
    print_home_plan(home)
    
    # Simulate control in each room
    for room in ["LivingRoom", "Bedroom", "Kitchen", "Bathroom", "Balcony"]:
        print(f"\nControlling devices in {room}...")
        control_temperature(room)
        control_humidity(room)
        control_light(room)
        time.sleep(2)  # Wait for a while before next iteration
# ```
# 
# ### Running the Application
# 
# To run this application from a Linux terminal, save the above script as `smart_home.py` in the same directory level as the `home` module folder. You can execute it with:
# 
# ```bash
# python3 smart_home.py
# ```
# 
# ### Explanation:
# 
# - **Temperature Control**: If the indoor temperature exceeds 25°C, the air conditioner is turned on and windows are closed.
# - **Humidity Control**: If the humidity is below a certain threshold (30%), the humidifier is turned on.
# - **Light Control**: If the light intensity is below 300 lux, the lights are turned on with high brightness.
# 
# This script uses the sensors and actuators defined in the provided references to simulate a smart home's basic automation tasks based on temperature, humidity, and light intensity. Adjust the thresholds and logic as needed for your specific application.