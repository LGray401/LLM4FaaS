from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, MusicPlayer, CoffeeMachine, Door
from home.config import LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def morning_plan(home):
    """
    Morning Plan:
    When the sensor senses that the light intensity reaches a certain value, open the curtains, turn off the bedroom lights,
    turn on the music player to listen to music, start the coffee machine, and make a cup of coffee
    """

    bedroom = get_room(home, "Bedroom")
    living_room = get_room(home, "LivingRoom")

    if bedroom and living_room:
        # Get light intensity sensor in living room
        light_intensity_sensor = get_room_sensors(home, "LivingRoom")[0]
        print(light_intensity_sensor.id)

        # Check if light intensity is high enough
        light_intensity_sensor.turn_on()
        reading = light_intensity_sensor.get_reading()
        if reading is not None and reading > LIGHT_INTENSITY_HIGH:
            print(f"Light intensity is high enough. Proceeding with morning plan.")
            logger.info(f"Light intensity is high enough. Proceeding with morning plan.")

            # Open the curtains in the living room
            curtains = get_room_actuators(home, "LivingRoom")
            for curtain in curtains:
                if curtain.actuator_type == "Curtain":
                    curtain.turn_on()

            # Turn off the lights in the bedroom
            lights = get_room_actuators(home, "Bedroom")
            for light in lights:
                if light.actuator_type == "Light":
                    light.turn_off()

            # Turn on the music player in the living room
            music_players = get_room_actuators(home, "LivingRoom")
            for music_player in music_players:
                if music_player.actuator_type == "MusicPlayer":
                    music_player.turn_on()
                    music_player.play_music("Morning Playlist")

            # Start the coffee machine in the kitchen
            coffee_machines = get_all_actuators(home, "CoffeeMachine")
            for coffee_machine in coffee_machines:
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Cappuccino")

        else:
            print(f"Light intensity is not high enough. Morning plan not activated.")
            logger.warning(f"Light intensity is not high enough. Morning plan not activated.")
    else:
        print(f"Cannot find LivingRoom or Bedroom. Morning plan cannot be executed.")
        logger.error(f"Cannot find LivingRoom or Bedroom. Morning plan cannot be executed.")


def leave_home_plan(home):
    """
    Leave Home Plan:
    After the door is locked, the curtains are closed, the lights are turned off, and the sockets are disconnected.
    """

    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")
    bathroom = get_room(home, "Bathroom")

    if living_room and bedroom and kitchen and bathroom:
        # Lock the door in the living room
        doors = get_room_actuators(home, "LivingRoom")
        for door in doors:
            if door.actuator_type == "Door":
                door.lock()

        # Close the curtains in the living room and bedroom
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_off()

        # Turn off the lights in the living room, bedroom, kitchen, and bathroom
        lights = get_all_actuators(home, "Light")
        for light in lights:
            light.turn_off()

        # Disconnect the sockets in the living room, bedroom, kitchen, and bathroom
        smart_sockets = get_all_actuators(home, "SmartSocket")
        for smart_socket in smart_sockets:
            smart_socket.turn_off()

        print(f"Leave home plan completed successfully.")
        logger.info(f"Leave home plan completed successfully.")
    else:
        print(f"Cannot find LivingRoom, Bedroom, Kitchen or Bathroom. Leave home plan cannot be executed.")
        logger.error(f"Cannot find LivingRoom, Bedroom, Kitchen or Bathroom. Leave home plan cannot be executed.")


def movie_plan(home):
    """
    Movie Plan:
    After giving the command to turn on the TV, draw the curtains and dim the lights in the room.
    """

    living_room = get_room(home, "LivingRoom")

    if living_room:
        # Turn on the TV in the living room
        smart_tvs = get_room_actuators(home, "LivingRoom")
        for smart_tv in smart_tvs:
            if smart_tv.actuator_type == "SmartTV":
                smart_tv.turn_on()
                smart_tv.play_channel("Netflix")

        # Draw the curtains in the living room
        curtains = get_room_actuators(home, "LivingRoom")
        for curtain in curtains:
            if curtain.actuator_type == "Curtain":
                curtain.turn_off()

        # Dim the lights in the living room
        lights = get_room_actuators(home, "LivingRoom")
        for light in lights:
            if light.actuator_type == "Light":
                light.set_brightness_level("low")

        print(f"Movie plan completed successfully.")
        logger.info(f"Movie plan completed successfully.")
    else:
        print(f"Cannot find LivingRoom. Movie plan cannot be executed.")
        logger.error(f"Cannot find LivingRoom. Movie plan cannot be executed.")


def main():
    """Main function to execute smart home plans."""
    home = home_plan()

    # Example usage
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)


if __name__ == "__main__":
    main()