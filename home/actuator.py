import random
import time

from home.config import DAILY_ROUTINE_DURATION


class Actuator:
    actuator_count = {}  # Dictionary to keep track of sensor count for each room and sensor type

    def __init__(self, actuator_type, room_name):
        if room_name not in Actuator.actuator_count:
            Actuator.actuator_count[room_name] = {}  # Initialize sensor count for the room if not already present
        if actuator_type not in Actuator.actuator_count[room_name]:
            Actuator.actuator_count[room_name][actuator_type] = 0  # Initialize sensor count for the sensor type if not already present

        Actuator.actuator_count[room_name][actuator_type] += 1  # Increment sensor count for the sensor type in the room

        self.id = f"/Actuator/{actuator_type}/{room_name}/{Actuator.actuator_count[room_name][actuator_type]}"
        self.actuator_type = actuator_type
        self.room_name = room_name
        self.status = "off"

    def turn_on(self):
        self.status = "on"
        print(f"{self.actuator_type} actuator '{self.id}' in {self.room_name} is now ON.")

    def turn_off(self):
        self.status = "off"
        print(f"{self.actuator_type} actuator '{self.id}' in {self.room_name} is now OFF.")

    def get_status(self):
        print(f"{self.actuator_type} actuator in {self.room_name} current status is {self.status}")
        return self.status


# todo: set different heating level: maybe from1-5, with a higher heating level, the temperature increases faster
class Heater(Actuator):
    def __init__(self, room_name):
        super().__init__("Heater", room_name)
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


class AC(Actuator):
    def __init__(self, room_name):
        super().__init__("AC", room_name)


class CoffeeMachine(Actuator):
    def __init__(self, room_name):
        super().__init__("CoffeeMachine", room_name)


# todo: the window can be [on, off, inclined]
class Window(Actuator):
    def __init__(self, room_name):
        super().__init__("Window", room_name)

class Door(Actuator):
    def __init__(self, room_name):
        super().__init__("Door", room_name)


class Curtain(Actuator):
    def __init__(self, room_name):
        super().__init__("Curtain", room_name)


class CleaningRobot(Actuator):
    def __init__(self, room_name):
        super().__init__("CleaningRobot", room_name)

    def daily_routine(self):
        self.turn_on()
        print(f"Robot in {self.room_name} Starts Daily Cleaning Routine")
        time.sleep(DAILY_ROUTINE_DURATION)
        self.turn_off()


class NotificationSender(Actuator):
    def __init__(self, room_name):
        super().__init__("NotificationSender", room_name)

    def notification_sender(self, message):
        if self.status == "on":
            print(f"Notification Sender in {self.room_name} send message: {message}")
        elif self.status == "off":
            print(f"Notification Sender in the {self.room_name} is OFF, please turn it on then send the message again.")
        else:
            print("There is some error with the Notification Sender")


class MusicPlayer(Actuator):
    def __init__(self, room_name):
        super().__init__("MusicPlayer", room_name)

    def play_music(self, playlist):
        if self.status == "on":
            print(f"Start playing {playlist} list on the {self.room_name} Player")
        elif self.status == "off":
            print(f"Music Player in {self.room_name} is OFF now")
            self.turn_on()
            print(f"Turn it on and Start playing {playlist} list")
        else:
            print("There is some error with the music player.")


# todo: some modification needed when status is off,
#  i.e., if it is off and we choose 'low' brightness,
#  we definitely need to turn it on and set brightness to low
class Light(Actuator):
    def __init__(self, room_name):
        super().__init__("Light", room_name)
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
                print(f"Set the {self.room_name} light brightness level to {level_name.upper()}")
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


# # todo: maybe need some further modification
# class SmartDoorLock(Actuator):
#     def __init__(self, room_name):
#         super().__init__("SmartLock", room_name)


class SmartTV(Actuator):
    def __init__(self, room_name):
        super().__init__("SmartTV", room_name)


class SmartSocket(Actuator):
    def __init__(self, room_name):
        super().__init__("SmartSocket", room_name)


# generated by proving the no-window auto-adapt function description
class Humidifier(Actuator):
    def __init__(self, room_name):
        super().__init__("Humidifier", room_name)

    def increase_humidity(self):
        print(f"Increasing humidity in {self.room_name}")

    def decrease_humidity(self):
        print(f"Decreasing humidity in {self.room_name}")


# if __name__ == '__main__':
#   ns = NotificationSender("LivingRoom")
#   ns.turn_on()
#   ns.notification_sender("test test test")