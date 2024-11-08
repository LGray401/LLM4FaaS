# Based on your functional description and the provided source code, here's the `function.py` file that implements the required functionality for your smart home project.
# 
# ### `function.py`

from home.home_plan import home_plan
from home.actuator import AC, Window, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def check_temperature(home):
    indoor_temp_sensors = []
    for room in home:
        indoor_temp_sensors.extend([sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)])
    
    if not indoor_temp_sensors:
        print("No indoor temperature sensors found.")
        return
    
    all_above_threshold = all(sensor.get_reading() > 26 for sensor in indoor_temp_sensors if sensor.get_status() == "on")
    
    if all_above_threshold:
        print("Temperature is above 26 degrees, turning on AC and closing windows.")
        for room in home:
            acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
            windows = [actuator for actuator in room.actuators if isinstance(actuator, Window)]
            for ac in acs:
                ac.turn_on()
            for window in windows:
                window.turn_off()  # Assuming closing a window means turning it off

def check_humidity(home):
    for room in home:
        humidity_sensors = [sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)]
        humidifier = [actuator for actuator in room.actuators if isinstance(actuator, Humidifier)]
        
        if humidity_sensors:
            current_humidity = humidity_sensors[0].get_reading()
            if current_humidity is not None and current_humidity < 30:
                print("Humidity is below 30%, turning on humidifier.")
                for hum in humidifier:
                    hum.turn_on()
                    hum.increase_humidity()

def check_light_intensity(home):
    for room in home:
        light_sensors = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
        
        if light_sensors:
            current_light = light_sensors[0].get_reading()
            if current_light is not None:
                if current_light < 150:
                    print("Light intensity is below 150 lux, turning up the lights.")
                    for light in lights:
                        light.turn_on()
                elif current_light > 1080:
                    print("Light intensity is above 1080 lux, drawing curtains and turning on indoor lights.")
                    for curtain in room.actuators:
                        if isinstance(curtain, Curtain):
                            curtain.turn_on()
                    for light in lights:
                        light.turn_on()

def main():
    home = home_plan()
    check_temperature(home)
    check_humidity(home)
    check_light_intensity(home)

if __name__ == "__main__":
    main()