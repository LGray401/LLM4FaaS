# Sure! Based on your functional description and the provided source code, here is the `function.py` file. This file will contain the main function that handles the three plans: MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN.

# function.py
from home.home_plan import home_plan, get_room, get_all_actuators
from home.sensor import LightIntensiveSensor
from home.actuator import Curtain, Light, CoffeeMachine, MusicPlayer, Door, SmartSocket, Window

def main():
    home = home_plan()

    def morning_plan():
        print("Executing Morning Plan...")
        living_room = get_room(home, "LivingRoom")
        kitchen = get_room(home, "Kitchen")
        if living_room and kitchen:
            # Open curtains in the living room
            for actuator in living_room.actuators:
                if isinstance(actuator, Curtain):
                    actuator.turn_on()

            # Check if it's cloudy outside using LightIntensiveSensor and turn on the light if necessary
            for sensor in living_room.sensors:
                if isinstance(sensor, LightIntensiveSensor):
                    sensor.turn_on()
                    reading = sensor.get_reading()
                    if reading and reading < 900:  # Assuming 900 is the threshold for a sunny day
                        for actuator in living_room.actuators:
                            if isinstance(actuator, Light):
                                actuator.turn_on()

            # Make coffee in the kitchen
            for actuator in kitchen.actuators:
                if isinstance(actuator, CoffeeMachine):
                    actuator.turn_on()
                    actuator.make_coffee("Espresso")

            # Play music once the coffee is made
            for actuator in living_room.actuators:
                if isinstance(actuator, MusicPlayer):
                    actuator.turn_on()
                    actuator.play_music("Morning Playlist")

    def leave_home_plan():
        print("Executing Leave Home Plan...")
        living_room = get_room(home, "LivingRoom")
        if living_room:
            # Open curtains if it's sunny outside
            for sensor in living_room.sensors:
                if isinstance(sensor, LightIntensiveSensor):
                    sensor.turn_on()
                    reading = sensor.get_reading()
                    if reading and reading >= 900:  # Assuming 900 is the threshold for a sunny day
                        for actuator in living_room.actuators:
                            if isinstance(actuator, Curtain):
                                actuator.turn_on()

            # Turn off lights and smart sockets, and lock the door
            for actuator in living_room.actuators:
                if isinstance(actuator, Light) or isinstance(actuator, SmartSocket):
                    actuator.turn_off()
                if isinstance(actuator, Door):
                    actuator.lock()

    def movie_plan():
        print("Executing Movie Plan...")
        living_room = get_room(home, "LivingRoom")
        if living_room:
            # Close curtains and turn off lights
            for actuator in living_room.actuators:
                if isinstance(actuator, Curtain) or isinstance(actuator, Light):
                    actuator.turn_off()

    # Execute plans
    morning_plan()
    leave_home_plan()
    movie_plan()

if __name__ == "__main__":
    main()