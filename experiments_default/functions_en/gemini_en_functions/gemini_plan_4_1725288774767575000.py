from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Light, Heater, AC, CoffeeMachine, Curtain, MusicPlayer, SmartTV, Window, CleaningRobot, Door
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW

home = home_plan()


def morning_plan():
    """
    The Morning Plan:
    - Open the curtain in the living room
    """

    # Get the Living Room
    living_room = get_room(home, "LivingRoom")
    if living_room is None:
        return

    # Get the curtain in the Living Room
    curtain = get_room_actuators(home, "LivingRoom")[0]

    # Turn on the curtain
    curtain.turn_on()


def leave_home_plan():
    """
    The Leave Home Plan:
    - Turn off the lamp in the living room
    """

    # Get the Living Room
    living_room = get_room(home, "LivingRoom")
    if living_room is None:
        return

    # Get the lamp in the Living Room
    lamp = get_room_actuators(home, "LivingRoom")[0]

    # Turn off the lamp
    lamp.turn_off()


def movie_plan():
    """
    The Movie Plan:
    - Adjust the light brightness in the living room to low
    """

    # Get the Living Room
    living_room = get_room(home, "LivingRoom")
    if living_room is None:
        return

    # Get the light in the Living Room
    light = get_room_actuators(home, "LivingRoom")[0]

    # Set the light brightness to low
    light.set_brightness_level("low")


def main():
    """
    The main function.
    """
    print("Welcome to Smart Home System!")
    while True:
        print("\nChoose a plan:")
        print("1. Morning Plan")
        print("2. Leave Home Plan")
        print("3. Movie Plan")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            morning_plan()
        elif choice == "2":
            leave_home_plan()
        elif choice == "3":
            movie_plan()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()