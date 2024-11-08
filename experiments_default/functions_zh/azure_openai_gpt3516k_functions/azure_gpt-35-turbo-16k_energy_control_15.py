# Sure! I have created the 'function.py' file for you. Here it is:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_all_sensors, get_room_actuators, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Heater, AC, MusicPlayer


def main():
    # Create home plan
    home = home_plan()

    # Print home plan
    print_home_plan(home)

    # Get sensors in a specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get all sensors of a specific type
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get actuators in a specific room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all actuators of a specific type
    light_actuators = get_all_actuators(home, "Light")

    # Perform actions
    # Turn on living room lights
    for light in living_room_actuators:
        if isinstance(light, Light):
            light.turn_on()

    # Set target temperature for all heater actuators
    for heater in get_all_actuators(home, "Heater"):
        heater.set_target_temperature(20)

    # Set target temperature for specific heater actuator
    bedroom_heater = None
    for heater in get_room_actuators(home, "Bedroom"):
        if isinstance(heater, Heater):
            bedroom_heater = heater
            break

    if bedroom_heater is not None:
        bedroom_heater.set_target_temperature(22)

    # Increase brightness level of all light actuators
    for light in light_actuators:
        light.set_brightness_level("high")

    # Play music in living room
    for music_player in get_room_actuators(home, "LivingRoom"):
        if isinstance(music_player, MusicPlayer):
            music_player.play_music("jazz")

    # Get readings from all temperature sensors
    for sensor in temperature_sensors:
        reading = sensor.get_reading()
        print(reading)


if __name__ == "__main__":
    main()