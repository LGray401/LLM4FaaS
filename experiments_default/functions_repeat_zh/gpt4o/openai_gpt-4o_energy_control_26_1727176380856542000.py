# Sure, I'll help you create the `function.py` file according to the functional description you provided. The main function should handle the logic to close the window when the air conditioner (AC) is turned on in the bedroom or living room, and open the window if the indoor temperature is above 26°C and the outdoor temperature is below 26°C.
# 
# Here is the `function.py` file:

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import AC, Window
from home.home_plan import home_plan, get_room
from home.config import TEMP_HIGH

def main():
    home = home_plan()

    # Define the rooms we are interested in
    rooms_of_interest = ["Bedroom", "LivingRoom"]

    for room_name in rooms_of_interest:
        room = get_room(home, room_name)

        if room:
            # Get the AC and window actuators in the room
            ac_units = [act for act in room.actuators if isinstance(act, AC)]
            windows = [act for act in room.actuators if isinstance(act, Window)]

            # Turn on the AC and close the window
            for ac in ac_units:
                ac.turn_on()
                for window in windows:
                    window.turn_off()  # Assume 'turn_off' means closing the window

            # Get the indoor temperature sensor reading
            indoor_temp_sensors = [sen for sen in room.sensors if isinstance(sen, IndoorTemperatureSensor)]
            for sensor in indoor_temp_sensors:
                sensor.turn_on()
                indoor_temp = sensor.get_reading()

                if indoor_temp > TEMP_HIGH:
                    # Get the outdoor temperature sensor reading
                    outdoor_temp_sensors = [sen for sen in home_plan() if isinstance(sen, OutdoorTemperatureSensor)]
                    for sensor in outdoor_temp_sensors:
                        sensor.turn_on()
                        outdoor_temp = sensor.get_reading()

                        if outdoor_temp < TEMP_HIGH:
                            for window in windows:
                                window.turn_on()  # Assume 'turn_on' means opening the window

if __name__ == "__main__":
    main()