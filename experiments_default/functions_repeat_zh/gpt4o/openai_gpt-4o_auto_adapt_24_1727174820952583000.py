# Given the provided functional description and source code files, we can create a `function.py` file to manage the main functionalities and ensure the home automation system adheres to the given requirements. The main function will be responsible for maintaining the indoor temperature no higher than 26 degrees Celsius, the humidity below 30%, and the light intensity within the specified range.
# 
# Here's the `function.py` file:

# function.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Humidifier, Light, Curtain
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def control_temperature(temperature_sensors, acs):
    for sensor in temperature_sensors:
        reading = sensor.get_reading()
        if reading is not None and reading > TEMP_HIGH:
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.turn_on()


def control_humidity(humidity_sensors, humidifiers):
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading is not None and reading > HUMIDITY_HIGH:
            for humidifier in humidifiers:
                if humidifier.room_name == sensor.room_name:
                    humidifier.turn_on()
                    humidifier.decrease_humidity()


def control_light_intensity(light_sensors, lights, curtains):
    for sensor in light_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            for light in lights:
                if light.room_name == sensor.room_name:
                    if reading < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                        light.set_brightness_level('high')
                    else:
                        light.turn_off()

            for curtain in curtains:
                if curtain.room_name == sensor.room_name:
                    if reading > LIGHT_INTENSITY_HIGH:
                        curtain.turn_on()
                    else:
                        curtain.turn_off()


def main():
    home = home_plan()

    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    acs = get_all_actuators(home, "AC")
    humidifiers = get_all_actuators(home, "Humidifier")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")

    control_temperature(temperature_sensors, acs)
    control_humidity(humidity_sensors, humidifiers)
    control_light_intensity(light_sensors, lights, curtains)


if __name__ == "__main__":
    main()