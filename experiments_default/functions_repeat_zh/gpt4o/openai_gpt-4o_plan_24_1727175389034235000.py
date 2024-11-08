# Here is the `function.py` file based on your functional description:
# 
# ## function.py

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, SmartSocket, Window

def morning_plan(home):
    print("Executing Morning Plan...")
    living_room = get_room(home, "LivingRoom")

    # Open curtains
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()

    # Check light intensity and turn on lights if it's cloudy
    light_sensor = None
    for sensor in get_all_sensors(home, "LightIntensive"):
        if sensor.room_name == "LivingRoom":
            light_sensor = sensor
            break

    if light_sensor:
        light_sensor.turn_on()
        light_intensity = light_sensor.get_reading()
        if light_intensity < 900:
            for actuator in get_all_actuators(home, "Light"):
                if actuator.room_name == "LivingRoom":
                    actuator.turn_on()

    # Make coffee
    kitchen = get_room(home, "Kitchen")
    for actuator in kitchen.actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")

    # Play music
    for actuator in living_room.actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")


def leave_home_plan(home):
    print("Executing Leave Home Plan...")
    living_room = get_room(home, "LivingRoom")

    # Open curtains if it's sunny
    outdoor_sensor = None
    for sensor in get_all_sensors(home, "OutdoorTemperature"):
        if sensor.room_name == "Balcony":
            outdoor_sensor = sensor
            break

    if outdoor_sensor:
        outdoor_sensor.turn_on()
        outdoor_temp = outdoor_sensor.get_reading()
        if outdoor_temp > 20:  # Assuming sunny if temperature is above 20 degrees
            for actuator in living_room.actuators:
                if isinstance(actuator, Curtain):
                    actuator.turn_on()

    # Turn off lights
    for actuator in get_all_actuators(home, "Light"):
        actuator.turn_off()

    # Turn off sockets
    for actuator in get_all_actuators(home, "SmartSocket"):
        actuator.turn_off()

    # Lock doors
    for actuator in get_all_actuators(home, "Door"):
        actuator.lock()


def movie_plan(home):
    print("Executing Movie Plan...")
    living_room = get_room(home, "LivingRoom")

    # Close curtains
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()

    # Turn off lights
    for actuator in get_all_actuators(home, "Light"):
        if actuator.room_name == "LivingRoom":
            actuator.turn_off()

def main():
    home = home_plan()
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()