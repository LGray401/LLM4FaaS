# Based on your functional description and the provided source code, the `function.py` file will implement the main functionality for your smart home system. This will involve creating instances of your sensors and actuators, checking their readings, and controlling the actuators based on the sensor readings. 
# 
# Here's the `function.py` file that meets your requirements:

# function.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Light, Window
from home.home_plan import home_plan
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Create home setup
    home = home_plan()
    
    for room in home:
        # Check sensors and control actuators based on readings
        temperature_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "IndoorTemperature"), None)
        humidity_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "Humidity"), None)
        light_sensor = next((sensor for sensor in room.sensors if sensor.sensor_type == "LightIntensive"), None)

        ac_unit = next((actuator for actuator in room.actuators if actuator.actuator_type == "AC"), None)
        humidifier = next((actuator for actuator in room.actuators if actuator.actuator_type == "Humidifier"), None)
        window = next((actuator for actuator in room.actuators if actuator.actuator_type == "Window"), None)
        light = next((actuator for actuator in room.actuators if actuator.actuator_type == "Light"), None)

        # Temperature control
        if temperature_sensor:
            current_temp = temperature_sensor.get_reading()
            if current_temp is not None:
                if current_temp > TEMP_HIGH:
                    if ac_unit:
                        ac_unit.turn_on()
                        if window:
                            window.turn_off()  # Close the window if AC is on

        # Humidity control
        if humidity_sensor:
            current_humidity = humidity_sensor.get_reading()
            if current_humidity is not None:
                if current_humidity < HUMIDITY_LOW:
                    if humidifier:
                        humidifier.turn_on()
                        humidifier.increase_humidity()

        # Light control based on light intensity
        if light_sensor:
            current_light = light_sensor.get_reading()
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_HIGH:
                    if light:
                        light.turn_on()
                        light.set_brightness_level("high")  # Adjust brightness as needed

if __name__ == "__main__":
    main()