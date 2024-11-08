# Here is the updated 'function.py' file based on the provided functional description:
from home.home_plan import Room


class Functions:
    def __init__(self, room):
        self.room = room

    def morning_plan(self):
        light_actuators = self.room.get_actuators("Light")
        for light in light_actuators:
            light.set_brightness_level("medium")

    def leave_home_plan(self):
        light_actuators = self.room.get_actuators("Light")
        for light in light_actuators:
            light.turn_off()

    def movie_plan(self):
        light_actuators = self.room.get_actuators("Light")
        for light in light_actuators:
            light.set_brightness_level("low")