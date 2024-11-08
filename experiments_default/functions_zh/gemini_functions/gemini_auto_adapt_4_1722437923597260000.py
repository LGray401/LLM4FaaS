from home.home_plan import get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Light, Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, NotificationSender, \
    MusicPlayer, SmartTV, SmartSocket, Humidifier
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger
import time


def main():
    home = home_plan()
    #
    # # Example usage:
    # # Get all sensors of type 'IndoorTemperature'
    # indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    # print(indoor_temp_sensors)
    #
    # # Get all actuators of type 'Light'
    # lights = get_all_actuators(home, "Light")
    # print(lights)
    #
    # # Get the 'LivingRoom' room
    # living_room = get_room(home, "LivingRoom")
    # print(living_room)
    #
    # # Get the sensors in the 'LivingRoom'
    # living_room_sensors = get_room_sensors(home, "LivingRoom")
    # print(living_room_sensors)
    #
    # # Get the actuators in the 'LivingRoom'
    # living_room_actuators = get_room_actuators(home, "LivingRoom")
    # print(living_room_actuators)

    # Get the 'LivingRoom' room
    living_room = get_room(home, "LivingRoom")

    # Get the sensors in the 'LivingRoom'
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get the actuators in the 'LivingRoom'
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Turn on the lights in the 'LivingRoom'
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()

    # Set the target temperature for the AC in the 'LivingRoom'
    ac = get_all_actuators(home, "AC")[0]  # Assuming there's only one AC in the living room
    ac.set_target_temperature(22)

    # Get the 'Kitchen' room
    kitchen = get_room(home, "Kitchen")

    # Get the sensors in the 'Kitchen'
    kitchen_sensors = get_room_sensors(home, "Kitchen")

    # Get the actuators in the 'Kitchen'
    kitchen_actuators = get_room_actuators(home, "Kitchen")

    # Turn on the coffee machine in the 'Kitchen'
    coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]  # Assuming there's only one coffee machine in the kitchen
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")

    # Adjust the temperature of the heater in the 'LivingRoom' based on the current temperature reading
    heater = get_all_actuators(home, "Heater")[0]  # Assuming there's only one heater in the living room
    for temp_sensor in living_room_sensors:
        if isinstance(temp_sensor, IndoorTemperatureSensor):
            current_temp = temp_sensor.get_reading()
            if current_temp < TEMP_LOW:
                heater.turn_on()
            else:
                heater.turn_off()

    # Adjust the temperature of the AC in the 'LivingRoom' based on the current temperature reading
    for temp_sensor in living_room_sensors:
        if isinstance(temp_sensor, IndoorTemperatureSensor):
            current_temp = temp_sensor.get_reading()
            if current_temp > TEMP_HIGH:
                ac.turn_on()
            else:
                ac.turn_off()

    # Adjust the humidity of the humidifier in the 'LivingRoom' based on the current humidity reading
    humidifier = get_all_actuators(home, "Humidifier")[0]
    for humidity_sensor in living_room_sensors:
        if isinstance(humidity_sensor, HumiditySensor):
            current_humidity = humidity_sensor.get_reading()
            if current_humidity < HUMIDITY_LOW:
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()

    # Simulate the cleaning robot's daily routine
    cleaning_robot = get_all_actuators(home, "CleaningRobot")[0]
    cleaning_robot.turn_on()
    cleaning_robot.daily_routine()

    # Simulate the notification sender sending a message
    notification_sender = get_all_actuators(home, "NotificationSender")[0]
    notification_sender.turn_on()
    notification_sender.notification_sender("It's time to go to bed!")

    # Simulate the music player playing music
    music_player = get_all_actuators(home, "MusicPlayer")[0]
    music_player.turn_on()
    music_player.play_music("Jazz")

    # Simulate the smart TV playing a channel
    smart_tv = get_all_actuators(home, "SmartTV")[0]
    smart_tv.turn_on()
    smart_tv.play_channel("CNN")

    # Simulate the smart socket turning on and off a device
    smart_socket = get_all_actuators(home, "SmartSocket")[0]
    smart_socket.turn_on()
    time.sleep(5)
    smart_socket.turn_off()

    # Simulate the door being locked and unlocked
    door = get_all_actuators(home, "Door")[0]
    door.lock()
    time.sleep(3)
    door.unlock()

    # Simulate the window being opened and closed
    window = get_all_actuators(home, "Window")[0]
    window.turn_on()
    time.sleep(2)
    window.turn_off()

    # Simulate the curtain being opened and closed
    curtain = get_all_actuators(home, "Curtain")[0]
    curtain.turn_on()
    time.sleep(2)
    curtain.turn_off()

    logger.info("Home automation system is running.")


def home_plan():
    # Define rooms and their components
    rooms = [
        create_room_with_components("LivingRoom",
                                    [LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor],
                                    [Door, Light, Window, Window, Curtain, MusicPlayer, SmartSocket, SmartSocket,
                                     CleaningRobot, SmartTV, NotificationSender, AC, Heater, Humidifier]),
        create_room_with_components("Bedroom",
                                    [IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor],
                                    [Light, Light, Window, Curtain, AC, Heater, MusicPlayer, Door, SmartSocket,
                                     SmartSocket, CleaningRobot]),
        create_room_with_components("Kitchen",
                                    [HumiditySensor, SmokeSensor],
                                    [Light, Window, Heater, CoffeeMachine, SmartSocket, SmartSocket, SmartSocket,
                                     Door]),
        create_room_with_components("Bathroom",
                                    [IndoorTemperatureSensor, HumiditySensor],
                                    [Light, Window, Heater, Door, SmartSocket, SmartSocket]),
        create_room_with_components("Balcony",
                                    [OutdoorTemperatureSensor, HumiditySensor],
                                    [Door])
    ]

    return rooms


def create_room_with_components(name, sensor_types, actuator_types):
    room = Room(name)
    for sensor_type in sensor_types:
        room.add_sensor(sensor_type(name))
    for actuator_type in actuator_types:
        room.add_actuator(actuator_type(name))
    return room


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


if __name__ == "__main__":
    main()