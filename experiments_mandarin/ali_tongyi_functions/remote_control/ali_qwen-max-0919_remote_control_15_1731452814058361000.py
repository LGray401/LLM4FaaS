# Based on the provided functional description and source code, I will create a `function.py` file that contains the main function to control and interact with the smart home system. The main function will initialize the home plan, allow for interaction with sensors and actuators, and perform some basic operations like turning on/off devices, getting sensor readings, and more.
# 
# Here is the `function.py` file:
# 
# ```python
# # functions/function.py
# 
# import time
# from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor
# from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV, Humidifier
# from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
# from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION
# 
# def main():
#     # Initialize the home plan
#     home = home_plan()
#     print_home_plan(home)
# 
#     while True:
#         print("\n--- Smart Home Control Menu ---")
#         print("1. Get all rooms info")
#         print("2. Get room sensors info")
#         print("3. Get room actuators info")
#         print("4. Turn on/off a specific actuator")
#         print("5. Get sensor reading")
#         print("6. Set target temperature for heater/AC")
#         print("7. Make coffee")
#         print("8. Start cleaning robot routine")
#         print("9. Send notification")
#         print("10. Play music")
#         print("11. Play TV channel")
#         print("12. Adjust light brightness")
#         print("13. Adjust humidity")
#         print("0. Exit")
#         
#         choice = input("Enter your choice: ")
# 
#         if choice == '1':
#             print_home_plan(home)
#         elif choice == '2':
#             room_name = input("Enter room name: ")
#             sensors = get_room_sensors(home, room_name)
#             if sensors:
#                 for sensor in sensors:
#                     print(f"- {sensor.id} (Status: {sensor.get_status()})")
#         elif choice == '3':
#             room_name = input("Enter room name: ")
#             actuators = get_room_actuators(home, room_name)
#             if actuators:
#                 for actuator in actuators:
#                     print(f"- {actuator.id} (Status: {actuator.get_status()})")
#         elif choice == '4':
#             room_name = input("Enter room name: ")
#             actuator_id = input("Enter actuator ID: ")
#             action = input("Enter 'on' or 'off': ")
#             actuators = get_room_actuators(home, room_name)
#             if actuators:
#                 for actuator in actuators:
#                     if actuator.id == actuator_id:
#                         if action == 'on':
#                             actuator.turn_on()
#                         elif action == 'off':
#                             actuator.turn_off()
#                         else:
#                             print("Invalid action. Please enter 'on' or 'off'.")
#                         break
#                 else:
#                     print(f"Actuator {actuator_id} not found in {room_name}.")
#         elif choice == '5':
#             room_name = input("Enter room name: ")
#             sensor_id = input("Enter sensor ID: ")
#             sensors = get_room_sensors(home, room_name)
#             if sensors:
#                 for sensor in sensors:
#                     if sensor.id == sensor_id:
#                         sensor.turn_on()
#                         reading = sensor.get_reading()
#                         if reading is not None:
#                             print(f"Reading from {sensor.id}: {reading}")
#                         sensor.turn_off()
#                         break
#                 else:
#                     print(f"Sensor {sensor_id} not found in {room_name}.")
#         elif choice == '6':
#             room_name = input("Enter room name: ")
#             actuator_type = input("Enter actuator type (Heater/AC): ").capitalize()
#             target_temp = float(input("Enter target temperature: "))
#             actuators = get_room_actuators(home, room_name)
#             if actuators:
#                 for actuator in actuators:
#                     if actuator.actuator_type == actuator_type and (isinstance(actuator, Heater) or isinstance(actuator, AC)):
#                         actuator.set_target_temperature(target_temp)
#                         break
#                 else:
#                     print(f"{actuator_type} not found in {room_name}.")
#         elif choice == '7':
#             room_name = input("Enter room name: ")
#             coffee_type = input("Enter coffee type: ")
#             actuators = get_room_actuators(home, room_name)
#             if actuators:
#                 for actuator in actuators:
#                     if isinstance(actuator, CoffeeMachine):
#                         actuator.make_coffee(coffee_type)
#                         break
#                 else:
#                     print(f"CoffeeMachine not found in {room_name}.")
#         elif choice == '8':
#             room_name = input("Enter room name: ")
#             actuators = get_room_actuators(home, room_name)
#             if actuators:
#                 for actuator in actuators:
#                     if isinstance(actuator, CleaningRobot):
#                         actuator.daily_routine()
#                         break
#                 else:
#                     print(f"CleaningRobot not found in {room_name}.")
#         elif choice == '9':
#             room_name = input("Enter room name: ")
#             message = input("Enter message: ")
#             actuators = get_room_actuators(home, room_name)
#             if actuators:
#                 for actuator in actuators:
#                     if isinstance(actuator, NotificationSender):
#                         actuator.notification_sender(message)
#                         break
#                 else:
#                     print(f"NotificationSender not found in {room_name}.")
#         elif choice == '10':
#             room_name = input("Enter room name: ")
#             playlist = input("Enter playlist: ")
#             actuators = get_room_actuators(home, room_name)
#             if actuators:
#                 for actuator in actuators:
#                     if isinstance(actuator, MusicPlayer):
#                         actuator.play_music(playlist)
#                         break
#                 else:
#                     print(f"MusicPlayer not found in {room_name}.")
#         elif choice == '11':
#             room_name = input("Enter room name: ")
#             channel_name = input("Enter channel name: ")
#             actuators = get_room_actuators(home, room_name)
#             if actuators:
#                 for actuator in actuators:
#                     if isinstance(actuator, SmartTV):
#                         actuator.play_channel(channel_name)
#                         break
#                 else:
#                     print(f"SmartTV not found in {room_name}.")
#         elif choice == '12':
#             room_name = input("Enter room name: ")
#             level_name = input("Enter brightness level (low/medium/high): ").lower()
#             actuators = get_room_actuators(home, room_name)
#             if actuators:
#                 for actuator in actuators:
#                     if isinstance(actuator, Light):
#                         actuator.set_brightness_level(level_name)
#                         break
#                 else:
#                     print(f"Light not