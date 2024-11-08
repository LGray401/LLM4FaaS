from home.home_plan import get_room, get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Light, Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, NotificationSender, \
    MusicPlayer, SmartTV, SmartSocket, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

class Function:

    def __init__(self, home):
        self.home = home

    def adjust_room_temperature(self, room_name, target_temperature):
        """
        Adjusts the temperature of a room using heaters and ACs based on the target temperature.

        Args:
            room_name (str): The name of the room to adjust.
            target_temperature (float): The desired temperature for the room.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            sensors = get_room_sensors(self.home, room_name)
            if sensors is not None:
                for sensor in sensors:
                    if isinstance(sensor, IndoorTemperatureSensor):
                        current_temperature = sensor.get_reading()
                        if current_temperature is not None:
                            actuators = get_room_actuators(self.home, room_name)
                            if actuators is not None:
                                for actuator in actuators:
                                    if isinstance(actuator, Heater):
                                        actuator.set_target_temperature(target_temperature)
                                        actuator.adjust_temperature(current_temperature)
                                    elif isinstance(actuator, AC):
                                        actuator.set_target_temperature(target_temperature)
                                        actuator.adjust_temperature(current_temperature)
                                        
    def adjust_room_humidity(self, room_name, target_humidity):
        """
        Adjusts the humidity of a room using humidifiers based on the target humidity.

        Args:
            room_name (str): The name of the room to adjust.
            target_humidity (float): The desired humidity level for the room.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            sensors = get_room_sensors(self.home, room_name)
            if sensors is not None:
                for sensor in sensors:
                    if isinstance(sensor, HumiditySensor):
                        current_humidity = sensor.get_reading()
                        if current_humidity is not None:
                            actuators = get_room_actuators(self.home, room_name)
                            if actuators is not None:
                                for actuator in actuators:
                                    if isinstance(actuator, Humidifier):
                                        if current_humidity < target_humidity:
                                            actuator.increase_humidity()
                                        elif current_humidity > target_humidity:
                                            actuator.decrease_humidity()
                                        else:
                                            print(f"Humidity in {room_name} is already at the target level.")

    def adjust_room_light(self, room_name, target_intensity):
        """
        Adjusts the light intensity in a room based on the target intensity.

        Args:
            room_name (str): The name of the room to adjust.
            target_intensity (float): The desired light intensity level for the room.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            sensors = get_room_sensors(self.home, room_name)
            if sensors is not None:
                for sensor in sensors:
                    if isinstance(sensor, LightIntensiveSensor):
                        current_intensity = sensor.get_reading()
                        if current_intensity is not None:
                            actuators = get_room_actuators(self.home, room_name)
                            if actuators is not None:
                                for actuator in actuators:
                                    if isinstance(actuator, Light):
                                        if current_intensity < target_intensity:
                                            actuator.turn_on()
                                            if target_intensity <= LIGHT_INTENSITY_LOW:
                                                actuator.set_brightness_level("low")
                                            elif target_intensity <= LIGHT_INTENSITY_HIGH:
                                                actuator.set_brightness_level("medium")
                                            else:
                                                actuator.set_brightness_level("high")
                                        elif current_intensity > target_intensity:
                                            actuator.turn_off()
                                        else:
                                            print(f"Light intensity in {room_name} is already at the target level.")

    def turn_on_coffee_machine(self, room_name, coffee_type="Espresso"):
        """
        Turns on the coffee machine in a room and starts brewing coffee.

        Args:
            room_name (str): The name of the room where the coffee machine is located.
            coffee_type (str, optional): The type of coffee to brew. Defaults to "Espresso".
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, CoffeeMachine):
                        actuator.turn_on()
                        actuator.make_coffee(coffee_type)
                        print(f"Coffee machine in {room_name} is now brewing {coffee_type}.")

    def play_music(self, room_name, playlist_name="Pop"):
        """
        Plays music in a room using the music player.

        Args:
            room_name (str): The name of the room where the music player is located.
            playlist_name (str, optional): The name of the playlist to play. Defaults to "Pop".
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, MusicPlayer):
                        actuator.turn_on()
                        actuator.play_music(playlist_name)
                        print(f"Music player in {room_name} is now playing {playlist_name} playlist.")

    def start_daily_cleaning_routine(self, room_name):
        """
        Starts the daily cleaning routine for the cleaning robot in a room.

        Args:
            room_name (str): The name of the room where the cleaning robot is located.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, CleaningRobot):
                        actuator.turn_on()
                        actuator.daily_routine()
                        print(f"Cleaning robot in {room_name} started daily cleaning routine.")

    def send_notification(self, room_name, message):
        """
        Sends a notification using the notification sender in a room.

        Args:
            room_name (str): The name of the room where the notification sender is located.
            message (str): The message to be sent in the notification.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, NotificationSender):
                        actuator.turn_on()
                        actuator.notification_sender(message)
                        print(f"Notification sent from {room_name}: {message}")

    def open_window(self, room_name):
        """
        Opens a window in a room.

        Args:
            room_name (str): The name of the room where the window is located.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, Window):
                        actuator.turn_on()
                        print(f"Window in {room_name} is now open.")

    def close_window(self, room_name):
        """
        Closes a window in a room.

        Args:
            room_name (str): The name of the room where the window is located.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, Window):
                        actuator.turn_off()
                        print(f"Window in {room_name} is now closed.")

    def open_curtain(self, room_name):
        """
        Opens the curtain in a room.

        Args:
            room_name (str): The name of the room where the curtain is located.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, Curtain):
                        actuator.turn_on()
                        print(f"Curtain in {room_name} is now open.")

    def close_curtain(self, room_name):
        """
        Closes the curtain in a room.

        Args:
            room_name (str): The name of the room where the curtain is located.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, Curtain):
                        actuator.turn_off()
                        print(f"Curtain in {room_name} is now closed.")

    def lock_door(self, room_name):
        """
        Locks the door in a room.

        Args:
            room_name (str): The name of the room where the door is located.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, Door):
                        actuator.lock()
                        print(f"Door in {room_name} is now locked.")

    def unlock_door(self, room_name):
        """
        Unlocks the door in a room.

        Args:
            room_name (str): The name of the room where the door is located.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, Door):
                        actuator.unlock()
                        print(f"Door in {room_name} is now unlocked.")

    def play_channel(self, room_name, channel_name):
        """
        Plays a channel on the Smart TV in a room.

        Args:
            room_name (str): The name of the room where the Smart TV is located.
            channel_name (str): The name of the channel to play.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, SmartTV):
                        actuator.turn_on()
                        actuator.play_channel(channel_name)
                        print(f"Smart TV in {room_name} is now playing channel {channel_name}.")

    def turn_on_smart_socket(self, room_name):
        """
        Turns on a Smart Socket in a room.

        Args:
            room_name (str): The name of the room where the Smart Socket is located.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, SmartSocket):
                        actuator.turn_on()
                        print(f"Smart Socket in {room_name} is now turned on.")

    def turn_off_smart_socket(self, room_name):
        """
        Turns off a Smart Socket in a room.

        Args:
            room_name (str): The name of the room where the Smart Socket is located.
        """
        room = get_room(self.home, room_name)
        if room is not None:
            actuators = get_room_actuators(self.home, room_name)
            if actuators is not None:
                for actuator in actuators:
                    if isinstance(actuator, SmartSocket):
                        actuator.turn_off()
                        print(f"Smart Socket in {room_name} is now turned off.")

    def get_all_temperature_sensors(self):
        """
        Returns a list of all temperature sensors in the home.

        Returns:
            list: A list of TemperatureSensor objects.
        """
        return get_all_sensors(self.home, "IndoorTemperature") + get_all_sensors(self.home, "OutdoorTemperature")

    def get_all_humidity_sensors(self):
        """
        Returns a list of all humidity sensors in the home.

        Returns:
            list: A list of HumiditySensor objects.
        """
        return get_all_sensors(self.home, "Humidity")

    def get_all_light_intensity_sensors(self):
        """
        Returns a list of all light intensity sensors in the home.

        Returns:
            list: A list of LightIntensiveSensor objects.
        """
        return get_all_sensors(self.home, "LightIntensive")

    def get_all_smoke_sensors(self):
        """
        Returns a list of all smoke sensors in the home.

        Returns:
            list: A list of SmokeSensor objects.
        """
        return get_all_sensors(self.home, "Smoke")

    def get_all_heaters(self):
        """
        Returns a list of all heaters in the home.

        Returns:
            list: A list of Heater objects.
        """
        return get_all_actuators(self.home, "Heater")

    def get_all_acs(self):
        """
        Returns a list of all AC units in the home.

        Returns:
            list: A list of AC objects.
        """
        return get_all_actuators(self.home, "AC")

    def get_all_coffee_machines(self):
        """
        Returns a list of all coffee machines in the home.

        Returns:
            list: A list of CoffeeMachine objects.
        """
        return get_all_actuators(self.home, "CoffeeMachine")

    def get_all_windows(self):
        """
        Returns a list of all windows in the home.

        Returns:
            list: A list of Window objects.
        """
        return get_all_actuators(self.home, "Window")

    def get_all_doors(self):
        """
        Returns a list of all doors in the home.

        Returns:
            list: A list of Door objects.
        """
        return get_all_actuators(self.home, "Door")

    def get_all_curtains(self):
        """
        Returns a list of all curtains in the home.

        Returns:
            list: A list of Curtain objects.
        """
        return get_all_actuators(self.home, "Curtain")

    def get_all_cleaning_robots(self):
        """
        Returns a list of all cleaning robots in the home.

        Returns:
            list: A list of CleaningRobot objects.
        """
        return get_all_actuators(self.home, "CleaningRobot")

    def get_all_notification_senders(self):
        """
        Returns a list of all notification senders in the home.

        Returns:
            list: A list of NotificationSender objects.
        """
        return get_all_actuators(self.home, "NotificationSender")

    def get_all_music_players(self):
        """
        Returns a list of all music players in the home.

        Returns:
            list: A list of MusicPlayer objects.
        """
        return get_all_actuators(self.home, "MusicPlayer")

    def get_all_smart_tvs(self):
        """
        Returns a list of all Smart TVs in the home.

        Returns:
            list: A list of SmartTV objects.
        """
        return get_all_actuators(self.home, "SmartTV")

    def get_all_smart_sockets(self):
        """
        Returns a list of all Smart Sockets in the home.

        Returns:
            list: A list of SmartSocket objects.
        """
        return get_all_actuators(self.home, "SmartSocket")

    def get_all_humidifiers(self):
        """
        Returns a list of all humidifiers in the home.

        Returns:
            list: A list of Humidifier objects.
        """
        return get_all_actuators(self.home, "Humidifier")


if __name__ == "__main__":
    home = home_plan()
    func = Function(home)

    func.adjust_room_temperature("LivingRoom", 22)
    func.adjust_room_humidity("Kitchen", 40)
    func.adjust_room_light("Bedroom", 600)
    func.turn_on_coffee_machine("Kitchen")
    func.play_music("LivingRoom", "Jazz")
    func.start_daily_cleaning_routine("LivingRoom")
    func.send_notification("LivingRoom", "Remember to take out the trash!")
    func.open_window("Bedroom")
    func.close_window("LivingRoom")
    func.open_curtain("Bedroom")
    func.close_curtain("LivingRoom")
    func.lock_door("LivingRoom")
    func.unlock_door("Bedroom")
    func.play_channel("LivingRoom", "News")
    func.turn_on_smart_socket("LivingRoom")
    func.turn_off_smart_socket("Kitchen")

    print(func.get_all_temperature_sensors())
    print(func.get_all_humidity_sensors())
    print(func.get_all_light_intensity_sensors())
    print(func.get_all_smoke_sensors())
    print(func.get_all_heaters())
    print(func.get_all_acs())
    print(func.get_all_coffee_machines())
    print(func.get_all_windows())
    print(func.get_all_doors())
    print(func.get_all_curtains())
    print(func.get_all_cleaning_robots())
    print(func.get_all_notification_senders())
    print(func.get_all_music_players())
    print(func.get_all_smart_tvs())
    print(func.get_all_smart_sockets())
    print(func.get_all_humidifiers())

# **Explanation:**

# 1. **Import Necessary Modules:**
#    - Imports `get_room`, `get_room_actuators`, `get_room_sensors`, `get_all_actuators`, and `get_all_sensors` from `home.home_plan`.
#    - Imports `IndoorTemperatureSensor`, `OutdoorTemperatureSensor`, `HumiditySensor`, `LightIntensiveSensor`, and `SmokeSensor` from `home.sensor`.
#    - Imports `Light`, `Heater`, `AC`, `CoffeeMachine`, `Window`, `Door`, `Curtain`, `CleaningRobot`, `NotificationSender`, `MusicPlayer`, `SmartTV`, `SmartSocket`, and `Humidifier` from `home.actuator`.
#    - Imports `TEMP_LOW`, `TEMP_HIGH`, `HUMIDITY_LOW`, `HUMIDITY_HIGH`, `LIGHT_INTENSITY_LOW`, and `LIGHT_INTENSITY_HIGH` from `home.config`.

# 2. **`Function` Class:**
#    - **`__init__(self, home)`:** Initializes the `Function` object with the `home` object (which represents the home plan).
#    - **Methods:**
#      - **`adjust_room_temperature(self, room_name, target_temperature)`:** Adjusts the temperature of a room using heaters and ACs.
#      - **`adjust_room_humidity(self, room_name, target_humidity)`:** Adjusts the humidity of a room using humidifiers.
#      - **`adjust_room_light(self, room_name, target_intensity)`:** Adjusts the light intensity in a room using lights.
#      - **`turn_on_coffee_machine(self, room_name, coffee_type="Espresso")`:** Turns on the coffee machine and starts brewing coffee.
#      - **`play_music(self, room_name, playlist_name="Pop")`:** Plays music in a room.
#      - **`start_daily_cleaning_routine(self, room_name)`:** Starts the cleaning robot's daily routine.
#      - **`send_notification(self, room_name, message)`:** Sends a notification using the notification sender.
#      - **`open_window(self, room_name)`:** Opens a window in a room.
#      - **`close_window(self, room_name)`:** Closes a window in a room.
#      - **`open_curtain(self, room_name)`:** Opens the curtain in a room.
#      - **`close_curtain(self, room_name)`:** Closes the curtain in a room.
#      - **`lock_door(self, room_name)`:** Locks the door in a room.
#      - **`unlock_door(self, room_name)`:** Unlocks the door in a room.
#      - **`play_channel(self, room_name, channel_name)`:** Plays a channel on the Smart TV.
#      - **`turn_on_smart_socket(self, room_name)`:** Turns on a Smart Socket.
#      - **`turn_off_smart_socket(self, room_name)`:** Turns off a Smart Socket.
#      - **`get_all_temperature_sensors(self)`:** Returns a list of all temperature sensors.
#      - **`get_all_humidity_sensors(self)`:** Returns a list of all humidity sensors.
#      - **`get_all_light_intensity_sensors(self)`:** Returns a list of all light intensity sensors.
#      - **`get_all_smoke_sensors(self)`:** Returns a list of all smoke sensors.
#      - **`get_all_heaters(self)`:** Returns a list of all heaters.
#      - **`get_all_acs(self)`:** Returns a list of all AC units.
#      - **`get_all_coffee_machines(self)`:** Returns a list of all coffee machines.
#      - **`get_all_windows(self)`:** Returns a list of all windows.
#      - **`get_all_doors(self)`:** Returns a list of all doors.
#      - **`get_all_curtains(self)`:** Returns a list of all curtains.
#      - **`get_all_cleaning_robots(self)`:** Returns a list of all cleaning robots.
#      - **`get_all_notification_senders(self)`:** Returns a list of all notification senders.
#      - **`get_all_music_players(self)`:** Returns a list of all music players.
#      - **`get_all_smart_tvs(self)`:** Returns a list of all Smart TVs.
#      - **`get_all_smart_sockets(self)`:** Returns a list of all Smart Sockets.
#      - **`get_all_humidifiers(self)`:** Returns a list of all humidifiers.

# 3. **Example Usage:**
#    - Creates a `home` object using `home_plan()`.
#    - Creates a `func` object of the `Function` class, passing the `home` object.
#    - Demonstrates how to use various methods of the `Function` class to control smart home devices.

# This provides a comprehensive set of functions for interacting with and controlling various smart home devices based on your provided code structure.
