# Based on your functional description and the provided source code, I'll create a `function.py` file that contains the main functions to handle the MORNING PLAN, LEAVE HOME PLAN, and MOVIE PLAN. These functions will interact with the sensors and actuators defined in the other modules.
# 
# Here is the `function.py` file:
# 
# ```python
# from home.home_plan import home_plan, get_room, get_all_actuators, get_all_sensors
# from home.actuator import Heater, AC, Light, CoffeeMachine, SmartTV, MusicPlayer, NotificationSender, Door
# from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
# from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
# from home.logger_config import logger
#
# def morning_plan():
#     home = home_plan()
#
#     # Assuming the morning plan is executed in the LivingRoom and Bedroom
#     rooms = ["LivingRoom", "Bedroom"]
#
#     for room_name in rooms:
#         room = get_room(home, room_name)
#         if room:
#             # Turn on lights to medium brightness
#             lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
#             for light in lights:
#                 light.turn_on()
#                 light.set_brightness_level("medium")
#
#             # Open curtains
#             curtains = [actuator for actuator in room.actuators if isinstance(actuator, Curtain)]
#             for curtain in curtains:
#                 curtain.turn_on()  # Assuming turn_on() opens the curtain
#
#             # Turn on heater if temperature is low
#             temperature_sensors = get_all_sensors(home, "IndoorTemperature")
#             for sensor in temperature_sensors:
#                 if sensor.room_name == room_name and sensor.get_reading() < TEMP_LOW:
#                     heaters = [actuator for actuator in room.actuators if isinstance(actuator, Heater)]
#                     for heater in heaters:
#                         heater.turn_on()
#                         heater.set_target_temperature(TEMP_HIGH)
#
#             # Turn on coffee machine in the Kitchen (only once)
#             if room_name == "LivingRoom":  # or any specific room where you want to trigger the coffee machine
#                 kitchen = get_room(home, "Kitchen")
#                 if kitchen:
#                     coffee_machines = [actuator for actuator in kitchen.actuators if isinstance(actuator, CoffeeMachine)]
#                     for coffee_machine in coffee_machines:
#                         coffee_machine.turn_on()
#                         coffee_machine.make_coffee("Espresso")  # or any preferred coffee type
#
#             # Send a notification
#             notification_senders = [actuator for actuator in room.actuators if isinstance(actuator, NotificationSender)]
#             for sender in notification_senders:
#                 sender.turn_on()
#                 sender.notification_sender("Good morning! Have a great day!")
#
# def leave_home_plan():
#     home = home_plan()
#
#     # Assuming the leave home plan is executed for the whole house
#     for room in home:
#         # Turn off all lights
#         lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
#         for light in lights:
#             light.turn_off()
#
#         # Turn off all appliances (except for essential ones like security systems)
#         appliances = [actuator for actuator in room.actuators if isinstance(actuator, (Heater, AC, MusicPlayer, SmartTV))]
#         for appliance in appliances:
#             appliance.turn_off()
#
#         # Lock all doors
#         doors = [actuator for actuator in room.actuators if isinstance(actuator, Door)]
#         for door in doors:
#             door.lock()
#
#         # Send a notification
#         notification_senders = [actuator for actuator in room.actuators if isinstance(actuator, NotificationSender)]
#         for sender in notification_senders:
#             sender.turn_on()
#             sender.notification_sender("You have left the house. Have a safe day!")
#
# def movie_plan():
#     home = home_plan()
#
#     # Assuming the movie plan is executed in the LivingRoom
#     room_name = "LivingRoom"
#     room = get_room(home, room_name)
#     if room:
#         # Turn on lights to low brightness
#         lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
#         for light in lights:
#             light.turn_on()
#             light.set_brightness_level("low")
#
#         # Turn on the TV
#         tvs = [actuator for actuator in room.actuators if isinstance(actuator, SmartTV)]
#         for tv in tvs:
#             tv.turn_on()
#             tv.play_channel("Movie Channel")  # or any preferred channel/streaming service
#
#         # Turn on the sound system/music player (if any)
#         music_players = [actuator for actuator in room.actuators if isinstance(actuator, MusicPlayer)]
#         for player in music_players:
#             player.turn_on()
#             player.play_music("Movie Playlist")  # or any preferred playlist
#
#         # Adjust temperature
#         temperature_sensors = get_all_sensors(home, "IndoorTemperature")
#         for sensor in temperature_sensors:
#             if sensor.room_name == room_name:
#                 current_temp = sensor.get_reading()
#                 if current_temp > TEMP_HIGH:
#                     acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
#                     for ac in acs:
#                         ac.turn_on()
#                         ac.set_target_temperature(TEMP_LOW)
#                 elif current_temp < TEMP_LOW:
#                     heaters = [actuator for actuator in room.actuators if isinstance(actuator, Heater)]
#                     for heater in heaters:
#                         heater.turn_on()
#                         heater.set_target_temperature(TEMP_HIGH)
#
#         # Send a notification
#         notification_senders = [actuator for actuator in room.actuators if isinstance(actuator, NotificationSender)]
#         for sender in notification_senders:
#             sender.turn_on()
#             sender.notification_sender("Enjoy your movie!")
#
# if __name__ == "__main__":
#     # Test the functions
#     morning_plan()
#     #