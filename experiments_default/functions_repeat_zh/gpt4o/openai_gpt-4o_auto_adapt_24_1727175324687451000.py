# Sure, I'll provide you with a `function.py` that integrates the functionalities described in the functional description and interacts with the components defined in your provided source code.
# 
# Here's the `function.py`:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light, Curtain
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Fetch all necessary sensors and actuators
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    acs = get_all_actuators(home, "AC")
    heaters = get_all_actuators(home, "Heater")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")

    for sensor in temp_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading > TEMP_HIGH:
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(reading)

    for sensor in humidity_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading > HUMIDITY_LOW:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.decrease_humidity()

    for sensor in light_sensors:
        sensor.turn_on()
        reading = sensor.get_reading()
        if reading and reading < LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    curtain.turn_off()
            for light in lights:
                if light.room_name == sensor.room_name:
                    light.turn_on()
                    light.set_brightness_level("high")

if __name__ == "__main__":
    main()