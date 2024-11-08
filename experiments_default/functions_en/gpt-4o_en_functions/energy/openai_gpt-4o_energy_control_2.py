# Based on your functional description and the provided source code, we will create a `function.py` file that will contain the necessary logic to achieve the desired automation behaviors.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, LIGHT_INTENSITY_HIGH
from time import sleep

def main():
    home = home_plan()
    
    while True:
        # Automatically close windows when the air conditioner is turned on
        acs = get_all_actuators(home, "AC")
        windows = get_all_actuators(home, "Window")
        for ac in acs:
            if ac.get_status() == "on":
                for window in windows:
                    if window.room_name == ac.room_name:
                        window.turn_off()
        
        # Automatically turn off the air conditioner when the indoor temperature is below 20 degrees
        indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
        for sensor in indoor_temp_sensors:
            acs = get_all_actuators(home, "AC")
            for ac in acs:
                if ac.room_name == sensor.room_name:
                    current_temp = sensor.get_reading()
                    if current_temp is not None and current_temp < 20:
                        ac.turn_off()

        # Automatically turn off or dim the lights when the light is strong
        light_sensors = get_all_sensors(home, "LightIntensive")
        lights = get_all_actuators(home, "Light")
        for sensor in light_sensors:
            current_light_intensity = sensor.get_reading()
            if current_light_intensity is not None and current_light_intensity > LIGHT_INTENSITY_HIGH:
                for light in lights:
                    if light.room_name == sensor.room_name:
                        light.set_brightness_level("low")
                        light.turn_off()

        # Automatically turn off the music player and TV when people leave the house
        music_players = get_all_actuators(home, "MusicPlayer")
        tvs = get_all_actuators(home, "SmartTV")
        for mp in music_players:
            mp.turn_off()
        for tv in tvs:
            tv.turn_off()

        # Wait for a while before checking again
        sleep(5)

if __name__ == "__main__":
    main()