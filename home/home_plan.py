from home.sensor import IndoorTemperatureSensor, HumiditySensor, UVSensor, SmokeSensor, OutdoorTemperatureSensor
from home.actuator import Light, Window, Curtain, MusicPlayer, Heater, AC


class Room:
    def __init__(self, name):
        self.name = name
        self.sensors = []
        self.actuators = []

    def add_sensor(self, sensor):
        self.sensors.append(sensor)

    def add_actuator(self, actor):
        self.actuators.append(actor)

    def print_info(self):
        print(f"\n{self.name}:")
        print("Sensors:")
        for sensor in self.sensors:
            print("-", sensor.id)
        print("Actuators:")
        for actor in self.actuators:
            print("-", actor.id)


def create_room_with_components(name, sensor_types, actuator_types):
    room = Room(name)
    for sensor_type in sensor_types:
        room.add_sensor(sensor_type(name))
    for actuator_type in actuator_types:
        room.add_actuator(actuator_type(name))
    return room


def home_plan():
    # print("Starting Home Plan Now")
    # Define rooms and their components
    rooms = [
        create_room_with_components("LivingRoom", [UVSensor, UVSensor, IndoorTemperatureSensor, IndoorTemperatureSensor,
                                                   HumiditySensor],
                                    [Light, Window, Window, Curtain, MusicPlayer]),
        create_room_with_components("Bedroom", [IndoorTemperatureSensor, HumiditySensor],
                                    [Light, Light, Window, Curtain, AC, Heater]),
        create_room_with_components("Kitchen", [HumiditySensor, SmokeSensor],
                                    [Light, Window, Heater, Heater]),
        create_room_with_components("Bathroom", [IndoorTemperatureSensor, HumiditySensor],
                                    [Light, Window, Heater]),
        create_room_with_components("Outdoor", [OutdoorTemperatureSensor, HumiditySensor],
                                    [])
    ]

    # Print Home plan
    # for room in rooms:
    #     room.print_info()

    return rooms


# Example invocation
# home_plan()

def print_home_plan(home):
    for room in home:
        room.print_info()


def get_room_sensors(home, room_name):
    for room in home:
        if room.name == room_name:
            # room.print_info()
            return room.sensors

    print(f"there is no Sensor found in {room_name}")
    return None  # no room_name room


# todo: for outdoor, the 'room' exists, but no actuator there.
def get_room_actuators(home, room_name):
    for room in home:
        if room.name == room_name:
            # room.print_info()
            return room.actuators

    print(f"there is no Actuator found in {room_name}")
    return None


def get_room(home, room_name):
    for room in home:
        if room.name == room_name:
            print(f"We find {room_name}!")
            return room

    print(f"there is no room called {room_name} at home")
    return None


# get_room(home_plan(), "outdoor")
