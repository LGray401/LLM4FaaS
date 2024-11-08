from home.home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, Door, SmartTV
from home.logger_config import logger
import time


def morning_plan(home):
    """Executes the morning plan:
    - Checks if the light intensity is above a certain threshold.
    - If so, it opens the curtains, turns off the bedroom lights, turns on the music player, and starts the coffee machine.
    """
    print("\nStarting MORNING PLAN...")
    logger.info("Starting MORNING PLAN")
    living_room = get_room_sensors(home, "LivingRoom")
    if living_room:
        for sensor in living_room:
            if isinstance(sensor, LightIntensiveSensor):
                light_intensity = sensor.get_reading()
                if light_intensity >= 300:
                    print(f"Light intensity is {light_intensity}, above threshold. Executing morning plan...")
                    logger.info(f"Light intensity is {light_intensity}, above threshold. Executing morning plan...")

                    # Open the curtains
                    curtains = get_all_actuators(home, "Curtain")
                    for curtain in curtains:
                        if curtain.room_name == "LivingRoom":
                            curtain.turn_on()

                    # Turn off bedroom lights
                    bedroom_lights = get_room_actuators(home, "Bedroom")
                    if bedroom_lights:
                        for light in bedroom_lights:
                            if isinstance(light, Light):
                                light.turn_off()

                    # Turn on music player
                    music_player = get_all_actuators(home, "MusicPlayer")
                    for player in music_player:
                        if player.room_name == "LivingRoom":
                            player.play_music("Morning Playlist")

                    # Start coffee machine
                    coffee_machine = get_all_actuators(home, "CoffeeMachine")
                    for machine in coffee_machine:
                        if machine.room_name == "Kitchen":
                            machine.make_coffee("Espresso")

                    print("Morning Plan Completed")
                    logger.info("Morning Plan Completed")
                    return

    print("Light intensity is below threshold. Morning plan not executed.")
    logger.info("Light intensity is below threshold. Morning plan not executed.")


def leave_home_plan(home):
    """Executes the leave home plan:
    - Closes the curtains, turns off the lights, and disconnects the sockets when the front door is locked.
    """
    print("\nStarting LEAVE HOME PLAN...")
    logger.info("Starting LEAVE HOME PLAN")
    # Check if the front door is locked
    door = get_all_actuators(home, "Door")
    for d in door:
        if d.status == "on":
            print(f"Door {d.id} is locked. Executing leave home plan...")
            logger.info(f"Door {d.id} is locked. Executing leave home plan...")

            # Close the curtains
            curtains = get_all_actuators(home, "Curtain")
            for curtain in curtains:
                if curtain.room_name != "Balcony":
                    curtain.turn_off()

            # Turn off the lights
            lights = get_all_actuators(home, "Light")
            for light in lights:
                light.turn_off()

            # Disconnect the sockets
            sockets = get_all_actuators(home, "SmartSocket")
            for socket in sockets:
                socket.turn_off()

            print("Leave Home Plan Completed")
            logger.info("Leave Home Plan Completed")
            return

    print("Front door is not locked. Leave home plan not executed.")
    logger.info("Front door is not locked. Leave home plan not executed.")


def movie_plan(home):
    """Executes the movie plan:
    - Closes the curtains and dims the lights when the TV is turned on.
    """
    print("\nStarting MOVIE PLAN...")
    logger.info("Starting MOVIE PLAN")
    # Check if the TV is turned on
    tv = get_all_actuators(home, "SmartTV")
    for t in tv:
        if t.status == "on":
            print(f"TV {t.id} is turned on. Executing movie plan...")
            logger.info(f"TV {t.id} is turned on. Executing movie plan...")

            # Close the curtains
            curtains = get_all_actuators(home, "Curtain")
            for curtain in curtains:
                curtain.turn_off()

            # Dim the lights
            lights = get_all_actuators(home, "Light")
            for light in lights:
                light.set_brightness_level("low")

            print("Movie Plan Completed")
            logger.info("Movie Plan Completed")
            return

    print("TV is not turned on. Movie plan not executed.")
    logger.info("TV is not turned on. Movie plan not executed.")


if __name__ == '__main__':
    home = home_plan()
    morning_plan(home)
    time.sleep(5)
    leave_home_plan(home)
    time.sleep(5)
    movie_plan(home)