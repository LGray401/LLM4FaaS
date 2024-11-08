# Based on the provided functional description and source code, I'll create a `function.py` file that will reside in the `functions` folder. This `function.py` file will include a main function which will implement the functionality to automatically turn on the air conditioner based on the specified conditions for temperature, humidity, and light intensity.
# 
# Here is the content of `function.py`:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH


def main():
    home = home_plan()
    
    # Get all relevant sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    # Get all air conditioners
    ac_units = get_all_actuators(home, "AC")
    
    # Turn on all sensors
    for sensor in temp_sensors + humidity_sensors + light_sensors:
        sensor.turn_on()
    
    # Function to check and control AC based on sensor readings
    def control_ac():
        for ac in ac_units:
            # Check temperature sensors
            for temp_sensor in temp_sensors:
                temp_reading = temp_sensor.get_reading()
                if temp_reading and temp_reading > TEMP_HIGH:
                    ac.turn_on()
                    print(f"AC in {ac.room_name} turned on due to temperature: {temp_reading}°C")
            
            # Check humidity sensors
            for humidity_sensor in humidity_sensors:
                humidity_reading = humidity_sensor.get_reading()
                if humidity_reading and humidity_reading > HUMIDITY_HIGH:
                    ac.turn_on()
                    print(f"AC in {ac.room_name} turned on due to humidity: {humidity_reading}%")
            
            # Check light intensity sensors
            for light_sensor in light_sensors:
                light_reading = light_sensor.get_reading()
                if light_reading and light_reading > LIGHT_INTENSITY_HIGH:
                    ac.turn_on()
                    print(f"AC in {ac.room_name} turned on due to light intensity: {light_reading} lux")
    
    # Control AC based on sensor readings
    control_ac()


if __name__ == "__main__":
    main()