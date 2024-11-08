# Based on your functional description and the provided code, I will create a `function.py` file that contains the main function to "open windows to cool down" the room. This will involve checking the indoor temperature and, if it exceeds a certain threshold (defined in `config.py`), opening the windows to reduce the temperature.
# 
# Here's the `function.py` file:

from home.home_plan import home_plan, get_room, get_all_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor
from home.actuator import Window
from home.config import TEMP_HIGH

def open_windows_to_cool_down(room_name):
    # Get the home plan
    home = home_plan()
    
    # Get the specified room
    room = get_room(home, room_name)
    if not room:
        return
    
    # Get all indoor temperature sensors in the room
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    if not temperature_sensors:
        print(f"No IndoorTemperature sensors found in {room_name}.")
        return
    
    # Check if any of the temperature sensors in the room exceed the threshold
    for sensor in temperature_sensors:
        if sensor.room_name == room_name:
            sensor.turn_on()  # Turn on the sensor to get the latest reading
            reading = sensor.get_reading()
            if reading > TEMP_HIGH:
                # Get all windows in the room
                actuators = get_room_actuators(home, room_name)
                if actuators:
                    for actuator in actuators:
                        if isinstance(actuator, Window) and actuator.status == "off":
                            actuator.turn_on()  # Open the window
                            print(f"Opened window {actuator.id} in {room_name} to cool down.")
                else:
                    print(f"No actuators found in {room_name}.")
                break
            else:
                print(f"Temperature in {room_name} is within acceptable range: {reading}°C.")

if __name__ == "__main__":
    # Example usage: open windows in the LivingRoom to cool down if it's too hot
    open_windows_to_cool_down("LivingRoom")