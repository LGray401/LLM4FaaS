# Based on the functional description and the provided source code, we will create a `function.py` file that initializes the smart home system, reads sensor values, and controls the actuators based on the specified temperature, humidity, and light intensity thresholds.
# 
# Here's the `function.py` code:

# functions/function.py

from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light

def main():
    # Create the home structure
    home = home_plan()
    
    # Initialize sensors and actuators
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    # Assuming there's only one sensor of each type for simplicity
    if indoor_temp_sensors:
        indoor_temp_sensor = indoor_temp_sensors[0]
        indoor_temp_sensor.turn_on()
        current_temp = indoor_temp_sensor.get_reading()  # Simulate getting the reading
        
        # Control the Heater and AC based on temperature
        heater = Heater("LivingRoom")
        ac = AC("LivingRoom")
        heater.set_target_temperature(26)  # Target temperature for heater
        ac.set_target_temperature(26)  # Target temperature for AC
        
        heater.adjust_temperature(current_temp)
        ac.adjust_temperature(current_temp)

    if humidity_sensors:
        humidity_sensor = humidity_sensors[0]
        humidity_sensor.turn_on()
        current_humidity = humidity_sensor.get_reading()  # Simulate getting the reading
        
        # Control the Humidifier based on humidity
        humidifier = Humidifier("LivingRoom")
        if current_humidity < HUMIDITY_LOW:
            humidifier.turn_on()
            humidifier.increase_humidity()
        elif current_humidity > HUMIDITY_HIGH:
            humidifier.turn_off()
            humidifier.decrease_humidity()

    if light_sensors:
        light_sensor = light_sensors[0]
        light_sensor.turn_on()
        current_light_intensity = light_sensor.get_reading()  # Simulate getting the reading
        
        # Control the Light based on light intensity
        light = Light("LivingRoom")
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            light.turn_on()  # Turn on light if it's too dark
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            light.turn_off()  # Turn off light if too bright

if __name__ == "__main__":
    main()