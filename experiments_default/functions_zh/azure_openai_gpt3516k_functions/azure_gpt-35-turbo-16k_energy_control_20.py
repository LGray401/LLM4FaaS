# Sure, I will provide you with the 'function.py' file based on your functional description and the provided code files:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_actuators, get_room_sensors, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Heater, AC


def adjust_room_environment(room_name):
    home = home_plan()
    room = get_room(home, room_name)

    if room is None:
        return

    sensors = get_room_sensors(home, room_name)
    actuators = get_room_actuators(home, room_name)

    if len(sensors) == 0 or len(actuators) == 0:
        print(f"No sensors or actuators found in {room_name}.")
        return

    # Get sensor readings
    temperature = None
    humidity = None
    light_intensity = None
    for sensor in sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature = sensor.get_reading()
        elif isinstance(sensor, HumiditySensor):
            humidity = sensor.get_reading()
        elif isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()

    # Adjust environment based on sensor readings
    for actuator in actuators:
        if isinstance(actuator, Light):
            if light_intensity is not None:
                if light_intensity < actuator.brightness_levels["low"]:
                    actuator.set_brightness_level("low")
                elif light_intensity > actuator.brightness_levels["high"]:
                    actuator.set_brightness_level("high")
                else:
                    actuator.set_brightness_level("medium")

        elif isinstance(actuator, Heater):
            if temperature is not None:
                if temperature < actuator.target_temperature:
                    actuator.turn_on()
                else:
                    actuator.turn_off()

        elif isinstance(actuator, AC):
            if temperature is not None:
                if temperature > actuator.target_temperature:
                    actuator.turn_on()
                else:
                    actuator.turn_off()

    print(f"The environment in {room_name} has been adjusted.")
    return


def adjust_home_environment():
    home = home_plan()

    for room in home:
        adjust_room_environment(room.name)

    print("The environment in the entire home has been adjusted.")
    return


if __name__ == "__main__":
    # Example invocation
    print_home_plan(home_plan())
    adjust_home_environment()