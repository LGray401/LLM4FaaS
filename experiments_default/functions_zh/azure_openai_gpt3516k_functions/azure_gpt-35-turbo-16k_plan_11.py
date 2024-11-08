# Here is the 'function.py' file for your smart home project:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, \
    get_all_sensors, get_all_actuators
from home.actuator import Light, Window, Curtain, SmartTV
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor


def main():
    home = home_plan()
    print_home_plan(home)

    # Get the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        # Get the sensors and actuators in the LivingRoom
        living_room_sensors = get_room_sensors(home, "LivingRoom")
        living_room_actuators = get_room_actuators(home, "LivingRoom")

        # Get the Light sensor and turn it on
        light_sensor = next((sensor for sensor in living_room_sensors if isinstance(sensor, LightIntensiveSensor)), None)
        if light_sensor:
            light_sensor.turn_on()

        # Get the Light and Window actuators and turn them on
        light = next((actuator for actuator in living_room_actuators if isinstance(actuator, Light)), None)
        window = next((actuator for actuator in living_room_actuators if isinstance(actuator, Window)), None)
        if light:
            light.turn_on()
        if window:
            window.turn_on()

        # Get the SmartTV actuator and play a channel
        smart_tv = next((actuator for actuator in living_room_actuators if isinstance(actuator, SmartTV)), None)
        if smart_tv:
            smart_tv.play_channel("CNN")


if __name__ == "__main__":
    main()