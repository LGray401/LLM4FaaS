# Based on your functional description and the provided source code, I'll create a `function.py` file for your smart home project. This file will implement the "Morning Plan", "Leave Home Plan", and "Movie Plan" functionalities as described.
# 
# Here’s how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.actuator import Light, Curtain, SmartTV
from home.sensor import OutdoorTemperatureSensor

def main():
    # Create home plan
    home = home_plan()

    # Retrieve the outdoor temperature sensor to check for rain
    outdoor_sensors = get_all_sensors(home, "OutdoorTemperature")
    
    # Assuming the first outdoor temperature sensor is the one we want
    if outdoor_sensors:
        outdoor_sensor = outdoor_sensors[0]
        outdoor_sensor.turn_on()  # Turn on the sensor to get readings
        outdoor_temp = outdoor_sensor.get_reading()

        # Morning Plan: Turn on the light if it is raining
        if outdoor_temp is not None and outdoor_temp < 15:  # Assuming < 15 indicates rain
            living_room = get_room(home, "LivingRoom")
            lights = get_all_actuators(home, "Light")
            for light in lights:
                light.turn_on()
        
        # Leave Home Plan: Open the curtains when it rains
        if outdoor_temp is not None and outdoor_temp < 15:
            bedroom = get_room(home, "Bedroom")
            curtains = get_all_actuators(home, "Curtain")
            for curtain in curtains:
                curtain.turn_on()

        # Movie Plan: Turn on the TV
        living_room_tv = get_all_actuators(home, "SmartTV")
        if living_room_tv:
            living_room_tv[0].turn_on()  # Turn on the SmartTV
            living_room_tv[0].play_channel("Movie Channel")  # Play a specified channel

if __name__ == "__main__":
    main()