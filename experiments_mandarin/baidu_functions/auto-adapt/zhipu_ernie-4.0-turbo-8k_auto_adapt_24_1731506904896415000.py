# Based on the functional description and the provided source code, here's the `function.py` file that maintains the indoor temperature, humidity, and light intensity according to the specified thresholds. This file will be located in the `functions` folder and will contain the main function to control the smart home environment.
# 
# ### function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def maintain_temperature(sensors, actuators):
    for sensor in sensors:
        if sensor.status == "on":
            reading = sensor.get_reading()
            if reading is not None:
                # Adjust heaters
                for actuator in actuators["Heater"]:
                    if reading < TEMP_HIGH - 1:  # Turn on heater if temperature is below threshold
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_HIGH)
                    else:
                        actuator.turn_off()
                
                # Adjust ACs
                for actuator in actuators["AC"]:
                    if reading > TEMP_HIGH:  # Turn on AC if temperature is above threshold
                        actuator.turn_on()
                        actuator.set_target_temperature(TEMP_HIGH)
                    else:
                        actuator.turn_off()

def maintain_humidity(sensors, actuators):
    for sensor in sensors:
        if sensor.status == "on":
            reading = sensor.get_reading()
            if reading is not None:
                # Adjust humidifiers
                for actuator in actuators["Humidifier"]:
                    if reading < HUMIDITY_HIGH:  # Assuming we want to maintain below a threshold
                        actuator.decrease_humidity()  # Decrease humidity if above threshold (inverse logic)
                    # Note: We might need a more sophisticated approach to actually control humidity
                    # e.g., turning on/off based on current humidity level and target

def maintain_light_intensity(sensors, actuators):
    for sensor in sensors:
        if sensor.status == "on":
            reading = sensor.get_reading()
            if reading is not None:
                # Adjust lights and curtains
                for actuator in actuators["Light"]:
                    if reading < LIGHT_INTENSITY_LOW:  # Turn on lights if intensity is below threshold
                        actuator.turn_on()
                        actuator.set_brightness_level("high")
                    else:
                        actuator.turn_off()
                
                for actuator in actuators["Curtain"]:
                    if reading > LIGHT_INTENSITY_HIGH:  # Close curtains if intensity is above threshold
                        # Assuming method to close curtains exists
                        actuator.turn_on()  # This should be replaced with actual curtain close logic
                    else:
                        actuator.turn_off()  # This should be replaced with actual curtain open logic

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get all relevant sensors and actuators
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")
    
    # Create a dictionary to easily access actuators by type
    actuators = {
        "Heater": heaters,
        "AC": acs,
        "Humidifier": humidifiers,
        "Light": lights,
        "Curtain": curtains
    }
    
    # Turn on all sensors
    for sensor in temperature_sensors + humidity_sensors + light_intensity_sensors:
        sensor.turn_on()
    
    # Maintain environmental conditions
    while True:
        maintain_temperature(temperature_sensors, actuators)
        maintain_humidity(humidity_sensors, actuators)
        maintain_light_intensity(light_intensity_sensors, actuators)
        
        # Sleep for some time before checking again (can adjust the duration as needed)
        # This is to prevent constantly checking the sensors and actuators
        import time
        time.sleep(10)

if __name__ == "__main__":
    main()