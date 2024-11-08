# Sure, here is the 'function.py' file based on your given functional description:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors
from home.logger_config import logger
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor, OutdoorTemperatureSensor
from home.actuator import Light, Window, Curtain, MusicPlayer


def morning_plan():
    logger.info("Executing MORNING PLAN")

    # Get the required components
    home = home_plan()
    living_room = get_room_actuators(home, "LivingRoom")
    living_room_lights = get_all_actuators(home, "Light")
    living_room_window = get_room_actuators(home, "LivingRoom")[1]
    living_room_curtain = get_room_actuators(home, "LivingRoom")[2]
    living_room_music_player = get_room_actuators(home, "LivingRoom")[6]

    # Open the curtains
    living_room_curtain.turn_on()

    # Check if it's a cloudy day
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    cloudiness = outdoor_temp_sensors[0].get_reading()
    if cloudiness < 100:
        # Turn on the lights
        for light in living_room_lights:
            light.turn_on()

    # Make coffee
    coffee_machine = get_room_actuators(home, "Kitchen")[3]
    coffee_machine.make_coffee("coffee")
    
    # Play music
    living_room_music_player.play_music("morning playlist")

    # Get indoor temperature and light intensity readings
    living_room_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    living_room_light_intensity_sensor = get_all_sensors(home, "LightIntensive")
    current_temp = living_room_temp_sensors[0].get_reading()
    light_intensity = living_room_light_intensity_sensor[0].get_reading()

    logger.info("MORNING PLAN executed successfully")


def leave_home_plan():
    logger.info("Executing LEAVE HOME PLAN")

    # Get the required components
    home = home_plan()
    living_room = get_room_actuators(home, "LivingRoom")
    living_room_lights = get_all_actuators(home, "Light")
    living_room_window = get_room_actuators(home, "LivingRoom")[1]
    living_room_curtain = get_room_actuators(home, "LivingRoom")[2]
    living_room_door = get_room_actuators(home, "LivingRoom")[10]
    
    # Check if it's a sunny day
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    sunlight_intensity = outdoor_temp_sensors[0].get_reading()
    if sunlight_intensity > 500:
        # Open the curtains and turn off the lights
        living_room_curtain.turn_on()
        for light in living_room_lights:
            light.turn_off()
    
    # Close the window and lock the door
    living_room_window.turn_off()
    living_room_door.lock()

    logger.info("LEAVE HOME PLAN executed successfully")


def movie_plan():
    logger.info("Executing MOVIE PLAN")

    # Get the required components
    home = home_plan()
    living_room_lights = get_all_actuators(home, "Light")
    living_room_curtain = get_room_actuators(home, "LivingRoom")[2]

    # Close the curtains and turn off the lights
    living_room_curtain.turn_off()
    for light in living_room_lights:
        light.turn_off()

    logger.info("MOVIE PLAN executed successfully")


if __name__ == "__main__":
    morning_plan()

    leave_home_plan()

    movie_plan()