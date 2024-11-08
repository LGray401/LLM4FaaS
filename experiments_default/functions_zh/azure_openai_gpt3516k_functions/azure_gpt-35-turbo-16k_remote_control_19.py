# Sure! Here is the 'function.py' file you requested:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, OutdoorTemperatureSensor


def set_temperature(room_name, temperature):
    home = home_plan()
    room = get_room(home, room_name)
    temp_sensors = get_room_sensors(home, room_name)
    ac = None
    heater = None

    for actuator in room.actuators:
        if actuator.actuator_type == 'AC':
            ac = actuator
        elif actuator.actuator_type == 'Heater':
            heater = actuator

    if ac is not None:
        ac.set_target_temperature(temperature)
    if heater is not None:
        heater.set_target_temperature(temperature)


def set_humidity(room_name, humidity):
    home = home_plan()
    room = get_room(home, room_name)
    humidity_sensors = get_room_sensors(home, room_name)
    humidifiers = get_all_actuators(home, 'Humidifier')

    for humidifier in humidifiers:
        if humidifier.room_name == room_name:
            if humidity > humidifier.get_status():
                humidifier.increase_humidity()
            elif humidity < humidifier.get_status():
                humidifier.decrease_humidity()


def set_light_intensity(room_name, intensity):
    home = home_plan()
    room = get_room(home, room_name)
    light_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    for actuator in room_actuators:
        if actuator.actuator_type == 'Light':
            light = actuator
            light.set_brightness_level(intensity)


def main():
    functional_description = "打开客厅空调设置26度"

    command_list = functional_description.split(" ")
    if command_list[0] == "打开" and command_list[1] == "客厅空调设置":
        room_name = "LivingRoom"
        temperature = float(command_list[2].replace("度", ""))
        set_temperature(room_name, temperature)


if __name__ == "__main__":
    # main()
    set_temperature("LivingRoom", 26.0)