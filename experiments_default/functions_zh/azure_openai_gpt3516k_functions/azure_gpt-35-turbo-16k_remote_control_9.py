# Sure, here is the 'function.py' file based on your functional description and the provided source code:

from home.home_plan import home_plan, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW

def set_temperature(room_name, temperature):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    sensors = get_all_sensors(home, "IndoorTemperature")

    if not actuators:
        print(f"No actuators found in {room_name}")
        return
    
    if not sensors:
        print(f"No temperature sensor found in {room_name}")
        return
    
    # Find the target actuator and set the temperature
    for actuator in actuators:
        if actuator.actuator_type == "AC":
            actuator.set_target_temperature(temperature)
    
    # Check the temperature readings of the sensors in the room
    current_temperatures = []
    for sensor in sensors:
        if sensor.room_name == room_name:
            current_temperatures.append(sensor.get_reading())
    
    # Adjust the temperature of the AC actuators based on the readings
    for temperature in current_temperatures:
        for actuator in actuators:
            if actuator.actuator_type == "AC":
                actuator.adjust_temperature(temperature)
    
    print(f"The temperature in {room_name} has been set to {temperature}°C.")


def increase_tv_volume(room_name, volume):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)

    if not actuators:
        print(f"No actuators found in {room_name}")
        return

    # Find the target actuator and increase the volume
    for actuator in actuators:
        if actuator.actuator_type == "SmartTV":
            actuator.play_channel("increase volume")  # Assuming the play_channel method increases the volume

    print(f"The volume of the TV in {room_name} has been increased by {volume}.")

    
def boil_kettle(room_name, temperature):
    home = home_plan()
    actuators = get_room_actuators(home, room_name)
    sensors = get_all_sensors(home, "IndoorTemperature")

    if not actuators:
        print(f"No actuators found in {room_name}")
        return
    
    if not sensors:
        print("No temperature sensor found in the room")
        return
    
    # Find the target actuator and set the temperature
    for actuator in actuators:
        if actuator.actuator_type == "CoffeeMachine":
            actuator.set_target_temperature(temperature)

    # Check the temperature readings of the sensors in the room
    current_temperatures = []
    for sensor in sensors:
        if sensor.room_name == room_name:
            current_temperatures.append(sensor.get_reading())
    
    # Adjust the temperature of the kettle actuators based on the readings
    for temperature in current_temperatures:
        for actuator in actuators:
            if actuator.actuator_type == "CoffeeMachine":
                actuator.adjust_temperature(temperature)
    
    print(f"The kettle in {room_name} has been set to boil at {temperature}°C.")