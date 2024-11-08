# Sure, I have created the 'function.py' file for you. You can find it in the 'functions' folder. Here is the content of the file:

from home.sensor import LightIntensiveSensor
from home.actuator import Light
from home.home_plan import home_plan, get_room, get_room_actuators, get_all_sensors, get_all_actuators

def control_living_room_light():
    home = home_plan()
    living_room = get_room(home, "LivingRoom")
    if living_room is not None:
        light_sensors = get_all_sensors(home, "LightIntensive")
        light_actuators = get_all_actuators(home, "Light")
        if light_sensors and light_actuators:
            for sensor in light_sensors:
                if sensor.room_name == "LivingRoom":
                    sensor.turn_on()
                    break
            for actuator in light_actuators:
                if actuator.room_name == "LivingRoom":
                    actuator.turn_off()
                    break
            for actuator in light_actuators:
                if actuator.room_name == "LivingRoom":
                    actuator.set_brightness_level("low")
                    break

if __name__ == "__main__":
    control_living_room_light()