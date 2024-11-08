# Based on the provided functional description and source code, it seems like you want to create a `function.py` file that contains a main function to control the temperature sensor, window, and light in your smart home project. The main function will open the temperature sensor, open the window, and turn on the light for a specific room.
# 
# Here's the `function.py` file that you can place in the `functions` folder:

# functions/function.py

from home.sensor import IndoorTemperatureSensor
from home.actuator import Window, Light
from home.home_plan import home_plan, get_room_actuators, get_room_sensors

def main():
    # Define the room name
    room_name = "LivingRoom"

    # Create the home plan
    home = home_plan()

    # Get the room
    room = get_room(home, room_name)
    if room is None:
        print(f"Room '{room_name}' not found.")
        return

    # Get the indoor temperature sensor and turn it on
    sensors = get_room_sensors(home, room_name)
    temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    if temp_sensor:
        temp_sensor.turn_on()
        print(f"Temperature Sensor in {room_name} is now ON.")
        temp_reading = temp_sensor.get_reading()
        if temp_reading is not None:
            print(f"Current temperature in {room_name} is: {temp_reading}°C")
    else:
        print(f"No Indoor Temperature Sensor found in {room_name}.")

    # Get the window actuator and open it
    actuators = get_room_actuators(home, room_name)
    window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
    if window:
        window.turn_on()
        print(f"Window in {room_name} is now OPEN.")
    else:
        print(f"No Window found in {room_name}.")

    # Get the light actuator and turn it on
    light = next((actuator for actuator in actuators if isinstance(actuator, Light)), None)
    if light:
        light.turn_on()
        print(f"Light in {room_name} is now ON.")
    else:
        print(f"No Light found in {room_name}.")

if __name__ == "__main__":
    main()