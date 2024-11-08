# Certainly! Here is the `function.py` file based on the given functional description and the provided source code:

from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_sensors

def turn_off_air_conditioning():
    home = home_plan()
    room = get_room(home, "LivingRoom")
    actuators = get_room_actuators(home, "LivingRoom")
    sensors = get_room_sensors(home, "LivingRoom")
    indoor_temperature_sensor = next((sensor for sensor in sensors if sensor.sensor_type == "IndoorTemperature"), None)
    air_conditioner = next((actuator for actuator in actuators if actuator.actuator_type == "AC"), None)

    if indoor_temperature_sensor and air_conditioner:
        indoor_temperature = indoor_temperature_sensor.get_reading()

        if indoor_temperature and indoor_temperature > 25:
            air_conditioner.turn_off()
        else:
            print("No need to turn off air conditioning.")
    else:
        print("Cannot find indoor temperature sensor or air conditioner.")

turn_off_air_conditioning()