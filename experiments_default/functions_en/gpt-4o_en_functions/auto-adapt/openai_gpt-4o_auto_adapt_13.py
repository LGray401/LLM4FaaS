# Based on your project structure and the provided functional description, here is the `function.py` file located in the `functions` folder. This file will contain the main function to adjust the smart home environment according to the described requirements (temperature of 26 degrees, suitable humidity, and better lighting).

# functions/function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Adjust temperature to 26 degrees
    target_temperature = 26
    indoor_temp_sensors = get_all_sensors(home, 'IndoorTemperature')
    heaters = get_all_actuators(home, 'Heater')
    acs = get_all_actuators(home, 'AC')
    
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        current_temp = sensor.get_reading()
        if current_temp is not None:
            for heater in heaters:
                if heater.room_name == sensor.room_name:
                    heater.set_target_temperature(target_temperature)
                    heater.adjust_temperature(current_temp)
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(target_temperature)
                    ac.adjust_temperature(current_temp)
        sensor.turn_off()

    # Adjust humidity to suitable range
    humidity_sensors = get_all_sensors(home, 'Humidity')
    humidifiers = get_all_actuators(home, 'Humidifier')
    
    for sensor in humidity_sensors:
        sensor.turn_on()
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    if current_humidity < HUMIDITY_LOW:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                    elif current_humidity > HUMIDITY_HIGH:
                        humidifier.turn_on()
                        humidifier.decrease_humidity()
                    else:
                        humidifier.turn_off()
        sensor.turn_off()

    # Adjust light intensity for better lighting
    light_sensors = get_all_sensors(home, 'LightIntensive')
    lights = get_all_actuators(home, 'Light')
    
    for sensor in light_sensors:
        sensor.turn_on()
        current_light = sensor.get_reading()
        if current_light is not None and current_light < LIGHT_INTENSITY_LOW:
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    light.set_brightness_level('high')
        sensor.turn_off()

if __name__ == "__main__":
    main()