from home.actuator import AC
from home.config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, HUMIDITY_HIGH, HUMIDITY_LOW
from home.home_plan import home_plan, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor
# todo:
#   0. get current home plan
#   1. temperature control
#   2. humidity control
#   2. light intensive control
def light_intensity_control():
    #     todo:
    #      0. get all uv sensors at home (from different rooms)
    #      1. get uv readings
    #      2. control specific curtains according to their readings
    print("------Auto UV Control Function------")
    all_light_intensive_sensors = get_all_sensors(rooms_at_home, "LightIntensive")

    for light_intensive_sensor in all_light_intensive_sensors:
        print("----------------------------------------------------------------")
        if light_intensive_sensor.status == "off":
            light_intensive_sensor.turn_on()
            current_reading = light_intensive_sensor.get_reading()

        if current_reading < LIGHT_INTENSITY_LOW:
            #     todo: send msg to user
            notification_sender.notification_sender(
                f"It is too dark in {light_intensive_sensor.room_name} now, you can turn on the light")
        elif current_reading >= LIGHT_INTENSITY_HIGH:
            notification_sender.notification_sender(f"It is too bright in {light_intensive_sensor.room_name} now,")
            #            1. check if there is curtain in this room
            #            if true, and the curtain is open, then close the curtain
            # maybe we do not need to check if there is curtain in the room,
            # because we have already show the home play.
            # but the curtain might be not reachable for some reasons
            all_actuators_in_room = get_room_actuators(rooms_at_home, light_intensive_sensor.room_name)
            for actuator in all_actuators_in_room:
                if actuator.actuator_type == "Curtain":
                    notification_sender.notification_sender(
                        f"The curtain in {actuator.room_name} is closed automatically ")
                    actuator.turn_off()
                    # todo: if there is no curtain, we also need to notify user
            # notification_sender.notification_sender(f"There is not curtain in the {light_intensive_sensor.room_name}")
        else:
            notification_sender.notification_sender("light intensity in all room is fine now")


def humidity_control():
    #     todo:
    #      1. get outdoor humidity readings
    #      2. get indoor_readings(maybe in different rooms)
    #      3. auto_adapt_humidity by either open window or turn on humidifier
    print("------Auto Humidity Control Function------")
    all_humidity_sensors = get_all_sensors(rooms_at_home, "HumiditySensor")

    for humidity_sensor in all_humidity_sensors:
        if humidity_sensor.status == "off":
            humidity_sensor.turn_on()
            current_humidity_reading = humidity_sensor.get_reading()

        if current_humidity_reading >= HUMIDITY_HIGH:
            notification_sender.notification_sender(f"{humidity_sensor.room_name} humidity is too high")
        #     todo: open window or turn on dehumidifier
        elif current_humidity_reading < HUMIDITY_LOW:
            notification_sender.notification_sender(f"{humidity_sensor.room_name} is too dry")
        #     todo: turn on humidifier
        #       need to add new actuator
        else:
            notification_sender.notification_sender(f"{humidity_sensor.room_name} humidity is fine now")
def temperature_control():
    #     todo:
    #      1. get outdoor temperature readings
    #      2. get indoor_temperature_readings (from different rooms)
    #      3. auto_adapt_humidity by either open window or turn on humidifier
    print("------Auto Temperature Control Function------")
    all_indoor_temperature_sensors = get_all_sensors(rooms_at_home, "IndoorTemperature")
    all_outdoor_temperature_sensors = get_all_sensors(rooms_at_home, "OutdoorTemperature")
    print(all_outdoor_temperature_sensors.__len__())


#     which room has indoor temperature sensor
#     then this room need temperature control
#      so the real fun_logic should get the indoor_temp_reading,
#      perform different operations based on different room readings


def check_and_control_temperature():
    # current home plan
    # rooms_at_home = home_plan()  # return rooms

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


if __name__ == '__main__':
    rooms_at_home = home_plan()
    notification_sender = get_all_actuators(rooms_at_home, "NotificationSender")[0]
    # notification_sender.turn_on()
    # # print(notification_sender)
    # # notification_sender[0].turn_on()
    # light_intensity_control()
    temperature_control()
    # todo: the final funciton can check diffect facts one by one or in parallel
    #   temperature-> light intensive-> humidity
