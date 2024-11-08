from home.home_plan import get_room_actuators, get_room_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import Curtain, MusicPlayer, Window, Light, AC, Humidifier, SmartTV
from home.logger_config import logger

def main():
    home =  home_plan()
    
    # Door open trigger
    front_door = get_room_actuators(home, "LivingRoom")[0]
    if front_door.get_status() == 'on':
        logger.info("Front door is opened")
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_on()
        music_player = get_room_actuators(home, "LivingRoom")[5]
        music_player.play_music("default_playlist")
        print("Music player turned on and playing default playlist.")
        
    # Temperature control
    indoor_temp_sensors = get_room_sensors(home, "LivingRoom")[1]
    if isinstance(indoor_temp_sensors, IndoorTemperatureSensor):
        temp = indoor_temp_sensors.get_reading()
        if temp is not None:
            if temp > 24:
                windows = get_room_actuators(home, "LivingRoom")[3]
                windows.turn_on()
                print("Windows opened because temperature is higher than 24°C")
            if temp > 27:
                windows = get_room_actuators(home, "LivingRoom")[3]
                windows.turn_off()
                print("Windows closed because temperature is higher than 27°C")
                ac = get_room_actuators(home, "LivingRoom")[11]
                ac.turn_on()
                print("Air conditioner turned on")
            
    # Humidity control
    humidity_sensors = get_room_sensors(home, "LivingRoom")[2]
    if humidity_sensors.get_reading() < 36:
        humidifier = get_room_actuators(home, "LivingRoom")[12]
        humidifier.increase_humidity()
        print("Humidifier turned on to increase humidity")
    
    # Light intensity control
    light_intensity_sensors = get_room_sensors(home, "LivingRoom")[0]
    if light_intensity_sensors.get_reading() < 40:
        light = get_room_actuators(home, "LivingRoom")[1]
        light.turn_on()
        print("Indoor light turned on because light intensity is lower than 40 lux")

    # TV on trigger
    tv = get_room_actuators(home, "LivingRoom")[10]
    if tv.get_status() == 'on':
        music_player = get_room_actuators(home, "LivingRoom")[5]
        music_player.turn_off()
        print("Music player turned off because TV is on.")
        curtains = get_all_actuators(home, "Curtain")
        for curtain in curtains:
            curtain.turn_off()
        print("Curtains closed because TV is on.")
        light = get_room_actuators(home, "LivingRoom")[1]
        light.set_brightness_level("low")
        print("Indoor light dimmed because TV is on.")

if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Imports:**
#    - Import necessary functions from `home.home_plan`, `home.sensor`, `home.actuator`, and `home.logger_config`.

# 2. **`main()` Function:**
#    - This function is the heart of the script, implementing the logic based on your functional description.

# 3. **Door Open Trigger:**
#    - Retrieves the front door actuator from the "LivingRoom".
#    - If the door is open (`front_door.get_status() == 'on'`), it:
#      - Logs that the front door is open.
#      - Opens all curtains.
#      - Turns on the music player in the living room.

# 4. **Temperature Control:**
#    - Retrieves the indoor temperature sensor from the "LivingRoom".
#    - If the sensor is valid, it checks the temperature:
#      - If temperature is higher than 24°C, open windows.
#      - If temperature is higher than 27°C, close windows and turn on the air conditioner.

# 5. **Humidity Control:**
#    - Retrieves the humidity sensor from the "LivingRoom".
#    - If humidity is lower than 36%, turn on the humidifier to increase humidity.

# 6. **Light Intensity Control:**
#    - Retrieves the light intensity sensor from the "LivingRoom".
#    - If light intensity is lower than 40 lux, turn on the indoor light.

# 7. **TV On Trigger:**
#    - Retrieves the SmartTV actuator from the "LivingRoom".
#    - If the TV is on (`tv.get_status() == 'on'`), it:
#      - Turns off the music player.
#      - Closes curtains.
#      - Dims the indoor light to a low brightness level.

# **Remember:**

# - This code assumes you have the `home.home_plan`, `home.sensor`, `home.actuator`, and `home.logger_config` modules in your project.
# - You may need to adjust the room names, actuator types, and thresholds in the code to match your specific home plan and configurations.
# - You can extend this code to handle more complex scenarios, such as multiple rooms, different sensor types, and more sophisticated event handling.