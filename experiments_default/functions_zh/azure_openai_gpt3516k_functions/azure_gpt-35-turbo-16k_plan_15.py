# Sure! I have created the 'function.py' file based on your functional description and the provided source code. Here is the content of the 'function.py' file:

from home.home_plan import home_plan, print_home_plan, get_room_sensors, get_all_sensors, get_all_actuators
from home.actuator import Heater, AC, Curtain, MusicPlayer, NotificationSender

def main():
    # Create home plan
    home = home_plan()

    # Print home plan
    print_home_plan(home)

    # Get sensors in a specific room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    print("Living Room Sensors:")
    for sensor in living_room_sensors:
        print("-", sensor.id)

    # Get all temperature sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    print("Temperature Sensors:")
    for sensor in temperature_sensors:
        print("-", sensor.id)

    # Get all music players
    music_players = get_all_actuators(home, "MusicPlayer")
    print("Music Players:")
    for music_player in music_players:
        print("-", music_player.id)

    # Perform actions with actuators
    for music_player in music_players:
        music_player.turn_on()
        music_player.play_music("Jazz")
        music_player.turn_off()

    # Example of thermostat control with heater and AC actuators
    living_room_heater = get_all_actuators(home, "Heater")[0]
    living_room_ac = get_all_actuators(home, "AC")[0]
    living_room_temperature_sensor = get_all_sensors(home, "IndoorTemperature")[0]
    target_temperature = 20

    current_temperature = living_room_temperature_sensor.get_reading()
    if current_temperature < target_temperature:
        living_room_heater.set_target_temperature(target_temperature)
        living_room_heater.adjust_temperature(current_temperature)
    else:
        living_room_ac.set_target_temperature(target_temperature)
        living_room_ac.adjust_temperature(current_temperature)

    # Example of curtain control with curtain actuator
    living_room_curtains = get_all_actuators(home, "Curtain")
    for curtain in living_room_curtains:
        curtain.open()

    # Example of sending notification with notification sender actuator
    notification_senders = get_all_actuators(home, "NotificationSender")
    for notification_sender in notification_senders:
        notification_sender.turn_on()
        notification_sender.notification_sender("Reminder: Don't forget to water the plants!")
        notification_sender.turn_off()

if __name__ == "__main__":
    main()