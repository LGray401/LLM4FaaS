# Sure! Here is the 'function.py' file based on the given functional description and the source code provided:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators

def energy_saving_system():
    # Get the home plan
    home = home_plan()

    # Print the home plan
    # print_home_plan(home)

    # Get the Living Room
    living_room = get_room(home, "LivingRoom")

    # Get the Living Room Sensors
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get the Living Room Actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get the Indoor Temperature Sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get the Humidity Sensors
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Get the Light Actuators
    light_actuators = get_all_actuators(home, "Light")

    # Get the AC Actuators
    ac_actuators = get_all_actuators(home, "AC")

    # Check the indoor temperature and adjust the AC accordingly
    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        for actuator in ac_actuators:
            actuator.set_target_temperature(current_temp)
            actuator.adjust_temperature(current_temp)

    # Check the humidity and adjust the AC and Humidifier accordingly
    for sensor in humidity_sensors:
        current_humidity = sensor.get_reading()
        for actuator in ac_actuators:
            actuator.set_target_humidity(current_humidity)
            actuator.adjust_humidity(current_humidity)
        for actuator in humidifier_actuators:
            actuator.set_target_humidity(current_humidity)
            actuator.adjust_humidity(current_humidity)

    # Check the light intensity and adjust the lights accordingly
    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()
            for actuator in light_actuators:
                actuator.set_brightness_level(light_intensity)

    # Turn off unnecessary lights and appliances
    for actuator in living_room_actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()
        elif isinstance(actuator, MusicPlayer):
            actuator.stop_music()
        elif isinstance(actuator, CoffeeMachine):
            actuator.turn_off()
        elif isinstance(actuator, SmartSocket):
            actuator.disconnect()

energy_saving_system()