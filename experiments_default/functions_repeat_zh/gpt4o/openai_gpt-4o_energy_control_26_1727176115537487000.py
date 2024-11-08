# Here's the `function.py` file based on your functional description and the provided source code:

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor
from home.actuator import Window, AC
from home.home_plan import home_plan, get_room, get_room_actuators
from home.config import TEMP_HIGH

def main():
    home = home_plan()

    # Iterate over each room in the home
    for room in home:
        room_name = room.name
        print(f"Checking room: {room_name}")

        ac = None
        window = None
        indoor_temp_sensor = None
        outdoor_temp_sensor = None

        # Find AC, Window, IndoorTemperatureSensor, and OutdoorTemperatureSensor in the room
        for actuator in room.actuators:
            if isinstance(actuator, AC):
                ac = actuator
            elif isinstance(actuator, Window):
                window = actuator

        for sensor in room.sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                indoor_temp_sensor = sensor
            elif isinstance(sensor, OutdoorTemperatureSensor):
                outdoor_temp_sensor = sensor

        # If there's an AC in the room and it's on, close the windows
        if ac and ac.get_status() == "on" and window:
            window.turn_off()  # Assuming turning off the window means closing it
            print(f"AC is on in {room_name}, closing the window.")
        
        # If indoor temp > 26 and outdoor temp < 26, open the window
        if (indoor_temp_sensor and outdoor_temp_sensor and 
            indoor_temp_sensor.get_reading() > TEMP_HIGH and 
            outdoor_temp_sensor.get_reading() < TEMP_HIGH and 
            window):
            window.turn_on()  # Assuming turning on the window means opening it
            print(f"Indoor temp > 26 and outdoor temp < 26 in {room_name}, opening the window.")

if __name__ == "__main__":
    main()