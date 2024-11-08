# Here is the 'function.py' file based on the given functional description and the provided source code files:

from home.home_plan import home_plan, print_home_plan, get_room_actuators, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Light

def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)

    # Get the living room actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    print("Living Room Actuators:")
    for actuator in living_room_actuators:
        print("-", actuator.id)

    # Get all the light actuators
    light_actuators = get_all_actuators(home, "Light")
    print("Light Actuators:")
    for actuator in light_actuators:
        print("-", actuator.id)

    # Create a temperature sensor in the living room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    temperature_sensor = IndoorTemperatureSensor("LivingRoom")
    living_room_sensors.append(temperature_sensor)

    # Create a humidity sensor in the living room
    humidity_sensor = HumiditySensor("LivingRoom")
    living_room_sensors.append(humidity_sensor)

    # Create a light intensity sensor in the living room
    light_intensity_sensor = LightIntensiveSensor("LivingRoom")
    living_room_sensors.append(light_intensity_sensor)

    # Adjust the temperature in the living room based on the target temperature and the current temperature
    target_temperature = 22
    current_temperature = temperature_sensor.get_reading()
    if current_temperature is not None:
        if current_temperature < target_temperature:
            heater = Heater("LivingRoom")
            heater.turn_on()
        else:
            ac = AC("LivingRoom")
            ac.turn_on()

    # Adjust the light intensity in the living room based on the current light intensity
    current_light_intensity = light_intensity_sensor.get_reading()
    if current_light_intensity is not None:
        if current_light_intensity < 500:
            for actuator in light_actuators:
                actuator.set_brightness_level("low")
        elif current_light_intensity < 800:
            for actuator in light_actuators:
                actuator.set_brightness_level("medium")
        else:
            for actuator in light_actuators:
                actuator.set_brightness_level("high")

    # Adjust the humidity in the living room based on the current humidity
    current_humidity = humidity_sensor.get_reading()
    if current_humidity is not None:
        if current_humidity < 40:
            humidifier = Humidifier("LivingRoom")
            humidifier.increase_humidity()
        elif current_humidity > 60:
            humidifier = Humidifier("LivingRoom")
            humidifier.decrease_humidity()

if __name__ == "__main__":
    main()