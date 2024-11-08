# Sure, here is the 'function.py' file based on your provided source code:

from home.home_plan import home_plan, get_room_actuators, get_all_sensors
from home.sensor import Sensor

def main():
    # Initialize home plan
    home = home_plan()

    # Perform morning plan
    morning_plan(home)

    # Perform leave home plan
    leave_home_plan(home)

    # Perform movie plan
    movie_plan(home)


def morning_plan(home):
    print("\nPerforming Morning Plan:")

    # Check if it's time to wake up
    alarm_sensor = get_sensor(home, "Alarm")
    alarm_sensor.get_reading()
    # If alarm is on, wake up
    if alarm_sensor.get_status() == "on":
        wake_up(home)


def leave_home_plan(home):
    print("\nPerforming Leave Home Plan:")

    # Get all the actuators in the home
    all_actuators = get_all_actuators(home)

    # Turn off all actuators
    for actuator in all_actuators:
        actuator.turn_off()

    # Leave home
    print("Leaving home...")


def movie_plan(home):
    print("\nPerforming Movie Plan:")

    # Set the living room lights to low brightness
    living_room_lights = get_room_actuators(home, "LivingRoom", "Light")
    for light in living_room_lights:
        light.set_brightness_level("low")

    # Set the living room curtains to close
    living_room_curtains = get_room_actuators(home, "LivingRoom", "Curtain")
    for curtain in living_room_curtains:
        curtain.close()

    # Turn on the TV in the living room
    living_room_tv = get_room_actuators(home, "LivingRoom", "TV")
    for tv in living_room_tv:
        tv.turn_on()

    # Set the volume of the TV to 50%
    living_room_tv.set_volume(50)

    # Play a movie on the TV
    living_room_tv.play_movie("Movie")


def wake_up(home):
    print("\nWaking Up:")

    # Get the bedroom lights
    bedroom_lights = get_room_actuators(home, "Bedroom", "Light")

    # Turn on the lights in the bedroom
    for light in bedroom_lights:
        light.turn_on()


def get_sensor(home, sensor_type):
    # Get all sensors of the given type from all rooms
    all_sensors = get_all_sensors(home, sensor_type)

    # Select a random sensor
    sensor = random.choice(all_sensors)

    return sensor


def get_all_actuators(home):
    # Get all actuators from all rooms
    all_actuators = []

    for room in home:
        all_actuators += room.actuators

    return all_actuators


if __name__ == "__main__":
    main()