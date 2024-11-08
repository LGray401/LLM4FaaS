# Here is the 'function.py' file based on your description and the provided source code:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    home = home_plan()

    # Print all the temperature sensors in the home
    print("\nTemperature Sensors in the Home:")
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in temperature_sensors:
        sensor.get_reading()

    # Print the humidity sensors in the living room
    print("\nHumidity Sensors in the Living Room:")
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    for sensor in living_room_sensors:
        if sensor.sensor_type == "Humidity":
            sensor.get_reading()

    # Print the light intensity sensors in the kitchen
    print("\nLight Intensity Sensors in the Kitchen:")
    kitchen_sensors = get_room_sensors(home, "Kitchen")
    for sensor in kitchen_sensors:
        if sensor.sensor_type == "LightIntensive":
            sensor.get_reading()

    # Get all the lights in the home and set their brightness level to medium
    print("\nSetting Light Brightness Level to Medium:")
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.set_brightness_level("medium")

    # Check the temperature in the living room and adjust the heater and AC accordingly
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    for sensor in living_room_sensors:
        if sensor.sensor_type == "IndoorTemperature":
            current_temperature = sensor.get_reading()
            if current_temperature < TEMP_LOW:
                heaters = get_room_actuators(home, "LivingRoom")
                for heater in heaters:
                    if heater.actuator_type == "Heater":
                        heater.turn_on()
            elif current_temperature > TEMP_HIGH:
                acs = get_room_actuators(home, "LivingRoom")
                for ac in acs:
                    if ac.actuator_type == "AC":
                        ac.turn_on()

    # Check the humidity in the bathroom and adjust the humidifier accordingly
    bathroom_sensors = get_room_sensors(home, "Bathroom")
    for sensor in bathroom_sensors:
        if sensor.sensor_type == "Humidity":
            current_humidity = sensor.get_reading()
            if current_humidity < HUMIDITY_LOW:
                humidifiers = get_room_actuators(home, "Bathroom")
                for humidifier in humidifiers:
                    if humidifier.actuator_type == "Humidifier":
                        humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifiers = get_room_actuators(home, "Bathroom")
                for humidifier in humidifiers:
                    if humidifier.actuator_type == "Humidifier":
                        humidifier.decrease_humidity()

    # Check the light intensity in the kitchen and adjust the curtains accordingly
    kitchen_sensors = get_room_sensors(home, "Kitchen")
    for sensor in kitchen_sensors:
        if sensor.sensor_type == "LightIntensive":
            current_light_intensity = sensor.get_reading()
            if current_light_intensity < LIGHT_INTENSITY_LOW:
                curtains = get_room_actuators(home, "Kitchen")
                for curtain in curtains:
                    if curtain.actuator_type == "Curtain":
                        curtain.turn_on()
            elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                curtains = get_room_actuators(home, "Kitchen")
                for curtain in curtains:
                    if curtain.actuator_type == "Curtain":
                        curtain.turn_off()

if __name__ == "__main__":
    main()