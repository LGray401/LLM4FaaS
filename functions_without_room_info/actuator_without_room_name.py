import random


class Actor:
    def __init__(self, actor_type):
        self.actor_type = actor_type
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        print(f"{self.actor_type} is now ON.")

    def turn_off(self):
        self.status = "off"
        print(f"{self.actor_type} is now OFF.")

    def get_status(self):
        print(f"{self.actor_type} current status is " f"{self.status}")
        return self.status


# todo: set different heating level: maybe from1-5, with a higher heating level, the temperature increases faster
class Heater(Actor):
    def __init__(self):
        super().__init__("Heater")
        self.heating_levels = {
            # match level to very 10 minutes temperature increment # the interval can be changed.
            0: 0,
            1: 0.5,
            2: 1,
            3: 1.5,
            4: 2,
            5: 2.5
        }
        self.heating_increment = 0

    # different heating level has different temperature increment
    def temp_increment(self, init_temp, curr_level):
        if curr_level in self.heating_levels:
            self.heating_increment = self.heating_levels[curr_level]
            curr_temp = init_temp + self.heating_increment
            print(curr_temp)


class AC(Actor):
    def __init__(self):
        super().__init__("AC")


# todo: the window can be [on, off, inclined]
class Window(Actor):
    def __init__(self):
        super().__init__("Window")


class Curtain(Actor):
    def __init__(self):
        super().__init__("Curtain")


class NotificationSender(Actor):
    def __init__(self):
        super().__init__("NotificationSender")

    def notification_sender(self, message):
        if self.status == "on":
            print(f"{message} message")
        if self.status == "off":
            print("Notification Sender is OFF, please turn it on then send the message again.")
        else:
            print("There is some error with the Notification Sender")


class MusicPlayer(Actor):
    def __init__(self):
        super().__init__("MusicPlayer")

    def music_player(self, playlist):
        if self.status == "on":
            print(f"Start playing {playlist} list")
        if self.status == "off":
            print("Music Player is OFF, please turn it on and try again.")
        else:
            print("There is some error.")


# todo: some modification needed when status is off,
#  i.e., if it is off and we choose 'low' brightness,
#  we definitely need to turn it on and set brightness to low
class Light(Actor):
    def __init__(self):
        super().__init__("Light")
        self.brightness_levels = {
            "low": 30,
            "medium": 60,
            "high": 90
        }
        self.brightness_level = 0

    def set_brightness_level(self, level_name):
        if level_name in self.brightness_levels:
            if self.status == "on":
                self.brightness_level = self.brightness_levels[level_name]
                print(f"Set brightness level to {level_name}")
            elif self.status == "off":
                print("Light is OFF. Please turn it on before setting the brightness level.")
            else:
                print("There is an error with the Light.")
        else:
            print(
                f"Invalid brightness level: {level_name}. Available levels are {list(self.brightness_levels.keys())}.")


def simulate_temperature_change(initial_temperature, action):
    # Simulate temperature changes based on the action
    if action == "hot_open_window":
        temperature_change = random.uniform(-2, -1)  # Decrease temperature when window is open
    elif action == "cold_open_window":
        temperature_change = random.uniform(1, 2)  # Decrease temperature when window is open
    elif action == "turn_on_heater":
        temperature_change = random.uniform(1, 2)  # Increase temperature when heater is on
    elif action == "turn_on_ac":
        temperature_change = random.uniform(-2, -1)  # Decrease temperature when AC is on
    else:
        temperature_change = random.uniform(-0.5, 0.5)  # Random small temperature change

    new_temperature = initial_temperature + temperature_change
    return max(0, min(40, new_temperature))  # Ensure temperature stays within valid range


# todo: maybe need some further modification
class SmartDoorLock(Actor):
    def __init__(self):
        super().__init__("SmartLock")

    def lock_all(self):
        print("Locking all doors and windows")
        # Add code to lock all doors and windows


class SmartTV(Actor):
    def __init__(self):
        super().__init__("SmartLock")

    def lock_all(self):
        print("Locking all doors and windows")
        # Add code to lock all doors and windows


class SmartSocket(Actor):
    def __init__(self):
        super().__init__("SmartSocket")

    def turn_off_except(self, exceptions=None):
        if exceptions is None:
            exceptions = []
        print(f"Turning off all sockets except {exceptions}")
        # Add code to turn off sockets except for specified exceptions


# Testing the Actor classes
if __name__ == "__main__":
    # actors = [AC(), Heater(), Curtain()]
    #
    # # Get default status from all actors
    # for actor in actors:
    #     actor.get_status()
    #
    # # turn on actors
    # for actor in actors:
    #     actor.turn_on()
    #
    # # Get current status from actors
    # for actor in actors:
    #     actor.get_status()
    #
    # # Turn off actors
    # for actor in actors:
    #     actor.turn_off()
    #
    # # Try to get status when sensors are off
    # for actor in actors:
    #     actor.get_status()

    # notificationSender = NotificationSender()
    # notificationSender.notification_sender("This is a test message")
    light = Light()
    light.turn_on()
    light.get_status()
    light.set_brightness_level("low")
    light.turn_off()
    light.set_brightness_level("medium")
