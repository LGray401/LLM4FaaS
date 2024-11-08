# Sure, I can help you with the function.py file. Based on your description and the provided source codes, I will create a main function that integrates the sensor and actuator functionalities for a smart home system. 
# 
# Here's what the `functions/function.py` file could look like:

# functions/function.py
import time
from home.home_plan import home_plan, print_home_plan, get_room, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create home plan
    home = home_plan()
    print_home_plan(home)

    # Example of controlling actuators based on sensor readings
    while True:
        for room in home:
            for sensor in room.sensors:
                sensor.turn_on()
                reading = sensor.get_reading()
                
                if sensor.sensor_type == "IndoorTemperature":
                    handle_temperature(room, reading)
                
                elif sensor.sensor_type == "Humidity":
                    handle_humidity(room, reading)

                elif sensor.sensor_type == "LightIntensive":
                    handle_light_intensity(room, reading)
                
                sensor.turn_off()

        time.sleep(10)  # Adjust the sleep time as necessary

def handle_temperature(room, reading):
    heaters = get_all_actuators([room], "Heater")
    acs = get_all_actuators([room], "AC")
    
    for heater in heaters:
        if reading < TEMP_LOW:
            heater.turn_on()
            heater.set_target_temperature(TEMP_HIGH)
        else:
            heater.turn_off()

    for ac in acs:
        if reading > TEMP_HIGH:
            ac.turn_on()
            ac.set_target_temperature(TEMP_LOW)
        else:
            ac.turn_off()

def handle_humidity(room, reading):
    humidifiers = get_all_actuators([room], "Humidifier")
    
    for humidifier in humidifiers:
        if reading < HUMIDITY_LOW:
            humidifier.turn_on()
            humidifier.increase_humidity()
        elif reading > HUMIDITY_HIGH:
            humidifier.turn_on()
            humidifier.decrease_humidity()
        else:
            humidifier.turn_off()

def handle_light_intensity(room, reading):
    lights = get_all_actuators([room], "Light")
    
    for light in lights:
        if reading < LIGHT_INTENSITY_LOW:
            light.turn_on()
            light.set_brightness_level("high")
        elif reading > LIGHT_INTENSITY_HIGH:
            light.turn_off()
        else:
            light.set_brightness_level("medium")

if __name__ == "__main__":
    main()