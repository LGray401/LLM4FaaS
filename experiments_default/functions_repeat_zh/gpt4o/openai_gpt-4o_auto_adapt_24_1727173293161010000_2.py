# Sure, I can help you create the `function.py` file based on the provided functional description and source code files. The goal is to maintain the temperature, humidity, and light intensity within specified ranges using the available sensors and actuators.
# 
# Here’s a possible implementation of `function.py`:
# 
# ### function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Curtain, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        manage_temperature(room.name, sensors, actuators)
        manage_humidity(room.name, sensors, actuators)
        manage_light_intensity(room.name, sensors, actuators)

def manage_temperature(room_name, sensors, actuators):
    temp_sensors = [sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)]
    ac_units = [actuator for actuator in actuators if isinstance(actuator, AC)]
    heaters = [actuator for actuator in actuators if isinstance(actuator, Heater)]
    
    for sensor in temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp is not None:
            for ac in ac_units:
                ac.set_target_temperature(TEMP_HIGH)
                ac.adjust_temperature(current_temp)

            for heater in heaters:
                heater.set_target_temperature(TEMP_HIGH)
                heater.adjust_temperature(current_temp)
        
        sensor.turn_off()

def manage_humidity(room_name, sensors, actuators):
    humidity_sensors = [sensor for sensor in sensors if isinstance(sensor, HumiditySensor)]
    humidifiers = [actuator for actuator in actuators if isinstance(actuator, Humidifier)]
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            for humidifier in humidifiers:
                if current_humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()
                else:
                    humidifier.turn_off()
        
        sensor.turn_off()

def manage_light_intensity(room_name, sensors, actuators):
    light_sensors = [sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)]
    lights = [actuator for actuator in actuators if isinstance(actuator, Light)]
    curtains = [actuator for actuator in actuators if isinstance(actuator, Curtain)]
    
    for sensor in light_sensors:
        sensor.turn_on()
        current_light_intensity = sensor.get_reading()
        if current_light_intensity is not None:
            for light in lights:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.turn_on()
                    light.set_brightness_level("high")
                else:
                    light.turn_off()
            
            for curtain in curtains:
                if current_light_intensity > LIGHT_INTENSITY_HIGH:
                    curtain.turn_on()
                else:
                    curtain.turn_off()
        
        sensor.turn_off()

if __name__ == "__main__":
    main()