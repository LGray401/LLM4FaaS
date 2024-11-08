# Based on the functional description provided and the existing code in your smart home project, I will create a `function.py` file. This file will contain the main function to execute the plans you've outlined: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN". Each plan will trigger specific actuators and sensors based on the room and actions described.
# 
# Here's how the `function.py` file will look:

# functions/function.py
from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators
from home.actuator import NotificationSender, SmartTV, MusicPlayer, CleaningRobot
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def morning_plan(home):
    print("\n--- Morning Plan ---")
    # Notification to wake up
    notification_sender = get_room_actuators(home, "LivingRoom")
    if notification_sender:
        for ns in notification_sender:
            if isinstance(ns, NotificationSender):
                ns.turn_on()
                ns.notification_sender("Good morning! It's time to wake up.")
    
    # Adjusting temperature and humidity in the Bedroom
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        temperature_sensors = get_room_sensors(home, "Bedroom")
        if temperature_sensors:
            for sensor in temperature_sensors:
                if sensor.sensor_type == "IndoorTemperature":
                    current_temp = sensor.get_reading()
                    if current_temp is not None:
                        # Example of using heater and AC
                        heater = next((act for act in bedroom.actuators if isinstance(act, Heater)), None)
                        ac = next((act for act in bedroom.actuators if isinstance(act, AC)), None)
                        if heater:
                            heater.set_target_temperature(TEMP_HIGH)
                            heater.adjust_temperature(current_temp)
                        if ac:
                            ac.set_target_temperature(TEMP_LOW)
                            ac.adjust_temperature(current_temp)

def leave_home_plan(home):
    print("\n--- Leave Home Plan ---")
    # Notification to say goodbye
    notification_sender = get_room_actuators(home, "LivingRoom")
    if notification_sender:
        for ns in notification_sender:
            if isinstance(ns, NotificationSender):
                ns.turn_on()
                ns.notification_sender("Goodbye! Have a nice day!")
    
    # Turn off all actuators in the house
    for room in home:
        for actuator in room.actuators:
            actuator.turn_off()

def movie_plan(home):
    print("\n--- Movie Plan ---")
    # Notification to start the movie
    notification_sender = get_room_actuators(home, "LivingRoom")
    if notification_sender:
        for ns in notification_sender:
            if isinstance(ns, NotificationSender):
                ns.turn_on()
                ns.notification_sender("Let's start the movie!")

    # Turn on the Smart TV and set it to a specific channel
    living_room = get_room(home, "LivingRoom")
    if living_room:
        smart_tv = next((act for act in living_room.actuators if isinstance(act, SmartTV)), None)
        if smart_tv:
            smart_tv.turn_on()
            smart_tv.play_channel("Movie Channel")

        # Optional: Play music
        music_player = next((act for act in living_room.actuators if isinstance(act, MusicPlayer)), None)
        if music_player:
            music_player.turn_on()
            music_player.play_music("Relaxing Playlist")

def main():
    home = home_plan()
    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

if __name__ == "__main__":
    main()