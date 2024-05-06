from home.actuator import AC
from home.home_plan import home_plan, get_room_sensors,get_room_actuators
from home.sensor import IndoorTemperatureSensor


# todo:
#   1. get the whole room plan
#   2. keyword is related to (one) specific rooms.
#   2. use the sensor readings in that room to trigger actuators in that room.

def check_and_control_temperature():
    # current home plan
    rooms_at_home = home_plan() # return rooms

    bedroom_sensors = get_room_sensors(rooms_at_home, "Bedroom")
    bedroom_actuators = get_room_actuators(rooms_at_home, "Bedroom")

    # if there is AC & temp_sensor
    has_temperature_sensor = False
    has_ac = False
    for sensor in bedroom_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            has_temperature_sensor = True
            break
    for actor in bedroom_actuators:
        if isinstance(actor, AC):
            has_ac = True
            break

    # if there is temp_sensor & AC
    # get temperature reading and trigger AC when necessary
    if has_temperature_sensor and has_ac:
        for sensor in bedroom_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                if sensor.status == "off":
                    print(f"Indoor Temperature Sensor is off, Turn it on now")
                    sensor.turn_on()
                temperature = sensor.get_reading()
                if temperature and temperature > 25:
                    for actor in bedroom_actuators:
                        if isinstance(actor, AC):
                            print("AC turned on in the Bedroom due to high temperature.")
                            actor.turn_on()
                            break
    else:
        print("Bedroom does not have both Indoor Temperature Sensor and AC.")



# main
# if __name__ == "__main__":
#     check_and_control_temperature()



# todo: auto_temp_control code backup

#     # if there is AC & temp_sensor
#     has_temperature_sensor = False
#     has_ac = False
#     # for sensor in bedroom.sensors:
#     for sensor in bedroom_sensors:
#         if isinstance(sensor, IndoorTemperatureSensor):
#             has_temperature_sensor = True
#             break
#     # for actor in bedroom.actuators:
#     for actor in bedroom_actuators:
#         if isinstance(actor, AC):
#             has_ac = True
#             break
#
#     # if there is temp_sensor & AC
#     # get temperature reading and trigger AC when necessary
#     if has_temperature_sensor and has_ac:
#         for sensor in bedroom_sensors:
#             if isinstance(sensor, IndoorTemperatureSensor):
#                 if sensor.status == "off":
#                     print(f"Indoor Temperature Sensor is off, Turn it on now")
#                     sensor.turn_on()
#                 temperature = sensor.get_reading()
#                 if temperature and temperature > 25:
#                     for actor in bedroom_actuators:
#                         if isinstance(actor, AC):
#                             print("AC turned on in the Bedroom due to high temperature.")
#                             actor.turn_on()
#                             break
#     else:
#         print("Bedroom does not have both Indoor Temperature Sensor and AC.")