# Sure, I can help you with that. Here is the 'function.py' file that you requested:

from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators, print_home_plan

def main():
    # Create the home plan
    home = home_plan()
    print_home_plan(home)
    
    # Example usage of functions to get sensors and actuators
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    all_temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    all_light_actuators = get_all_actuators(home, "Light")

    # Perform actions based on functional description
    # Open temperature sensor
    living_room_temperature_sensor = None
    for sensor in living_room_sensors:
        if sensor.sensor_type == "IndoorTemperature":
            living_room_temperature_sensor = sensor
            break
    if living_room_temperature_sensor is not None:
        living_room_temperature_sensor.turn_on()
    
    # Open window
    living_room_window = None
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Window":
            living_room_window = actuator
            break
    if living_room_window is not None:
        living_room_window.turn_on()
    
    # Open light
    living_room_light = None
    for actuator in living_room_actuators:
        if actuator.actuator_type == "Light":
            living_room_light = actuator
            break
    if living_room_light is not None:
        living_room_light.turn_on()


if __name__ == "__main__":
    main()