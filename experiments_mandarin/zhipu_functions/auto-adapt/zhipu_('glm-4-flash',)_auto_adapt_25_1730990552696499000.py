# Based on the provided functional description and source code, here is the `function.py` file that should be placed in the `functions` folder of your project:

# function.py
import time
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Curtain

def main():
    # Define the home plan
    home = home_plan()

    # Get sensors and actuators for the LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room:
        temp_sensor = get_room_sensors(living_room, "IndoorTemperature")
        humidity_sensor = get_room_sensors(living_room, "Humidity")
        light_sensor = get_room_sensors(living_room, "LightIntensive")
        ac = get_room_actuators(living_room, "AC")
        curtain = get_room_actuators(living_room, "Curtain")

        # Initialize the AC and Curtain
        if ac and curtain:
            ac[0].set_target_temperature(26)
            curtain[0].turn_on()

    # Continuously check for sensor readings and adjust actuators accordingly
    while True:
        if temp_sensor and temp_sensor[0].get_reading() >= 26:
            if ac:
                ac[0].turn_on()
            else:
                print("AC not found in the system.")
        
        if humidity_sensor and humidity_sensor[0].get_reading() < 36:
            if ac:
                ac[0].turn_on()
            else:
                print("AC not found in the system.")
        
        if light_sensor and light_sensor[0].get_reading() > 80:
            if curtain:
                curtain[0].turn_on()
            else:
                print("Curtain not found in the system.")
        
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

if __name__ == "__main__":
    main()