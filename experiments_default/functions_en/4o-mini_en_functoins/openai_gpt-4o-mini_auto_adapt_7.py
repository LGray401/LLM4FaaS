# Here is the `function.py` file based on the functional description you provided and the source code from your smart home project.

# function.py

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.actuator import Light, Heater, AC, Humidifier, NotificationSender
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def check_conditions_and_take_action(home):
    for room in home:
        sensors = room.sensors
        actuators = room.actuators
        
        # Check temperature conditions
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        if temperature_sensors:
            for sensor in temperature_sensors:
                sensor.turn_on()
                temperature = sensor.get_reading()
                if temperature is not None:
                    if temperature > TEMP_HIGH:
                        heater = next((actuator for actuator in actuators if isinstance(actuator, Heater)), None)
                        if heater:
                            heater.set_target_temperature(TEMP_HIGH)
                            heater.adjust_temperature(temperature)
                    elif temperature < TEMP_LOW:
                        ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
                        if ac:
                            ac.set_target_temperature(TEMP_LOW)
                            ac.adjust_temperature(temperature)

        # Check humidity conditions
        humidity_sensors = get_all_sensors(home, "Humidity")
        if humidity_sensors:
            for sensor in humidity_sensors:
                sensor.turn_on()
                humidity = sensor.get_reading()
                if humidity is not None:
                    humidifier = next((actuator for actuator in actuators if isinstance(actuator, Humidifier)), None)
                    if humidity < HUMIDITY_LOW and humidifier:
                        humidifier.turn_on()
                        humidifier.increase_humidity()
                    elif humidity > HUMIDITY_HIGH and humidifier:
                        humidifier.turn_off()
        
        # Check light intensity conditions
        light_sensors = get_all_sensors(home, "LightIntensive")
        if light_sensors:
            for sensor in light_sensors:
                sensor.turn_on()
                light_intensity = sensor.get_reading()
                if light_intensity is not None:
                    light = next((actuator for actuator in actuators if isinstance(actuator, Light)), None)
                    if light:
                        if light_intensity < LIGHT_INTENSITY_LOW:
                            light.turn_on()
                            light.set_brightness_level("high")
                        else:
                            light.turn_off()

def main():
    home = home_plan()
    check_conditions_and_take_action(home)

if __name__ == "__main__":
    main()