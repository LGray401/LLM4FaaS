# Sure, here is the 'function.py' file based on your functional description:

from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Light, Curtain, SmartTV
from home.home_plan import get_room, get_all_sensors, get_all_actuators

def main():
    # Get the required sensors and actuators
    living_room = get_room(home, "LivingRoom")
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    light_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")
    curtains = get_all_actuators(home, "Curtain")
    smart_tvs = get_all_actuators(home, "SmartTV")

    # MORNING PLAN
    if any(sensor.get_reading() > 0 for sensor in light_sensors):
        for light in lights:
            light.turn_on()

    # LEAVE HOME PLAN
    if all(sensor.get_reading() > 0 for sensor in light_sensors):
        for curtain in curtains:
            curtain.open()

    # MOVIE PLAN
    for smart_tv in smart_tvs:
        smart_tv.turn_on()
        smart_tv.play_channel("Movie")

if __name__ == "__main__":
    main()