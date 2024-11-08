# Given the functional description and the source code provided, I will now create a `function.py` file that contains a `main` function to control the smart home system according to the user's requests.
# 
# The `main` function will:
# 1. Initialize the home plan with the defined rooms and their sensors and actuators.
# 2. Parse the user's requests to adjust the home's environment.
# 3. Use the sensors to get the current readings and actuators to make changes as per the requests.
# 
# Here is the `function.py` file:

# function.py
from home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from sensor import IndoorTemperatureSensor, AC
from actuator import Heater

def set_temperature(target_temperature, room_name):
    # First, get the AC in the specified room
    room = get_room(home_plan(), room_name)
    if room:
        ac = next((a for a in room.actuators if isinstance(a, AC)), None)
        if ac:
            ac.set_target_temperature(target_temperature)
            print(f"AC in {room_name} set to target temperature of {target_temperature}°C.")
        else:
            print(f"No AC found in {room_name}. Cannot adjust temperature.")
    else:
        print(f"No room named {room_name} found.")

def adjust_light_volume(volume_change, room_name):
    # First, get the AC in the specified room
    room = get_room(home_plan(), room_name)
    if room:
        ac = next((a for a in room.actuators if isinstance(a, AC)), None)
        if ac:
            ac.adjust_temperature(volume_change)  # Assuming volume_change is a change in temperature
            print(f"AC volume in {room_name} adjusted by {volume_change}°C.")
        else:
            print(f"No AC found in {room_name}. Cannot adjust volume.")
    else:
        print(f"No room named {room_name} found.")

def boil_water(room_name):
    # First, get the Heater in the specified room
    room = get_room(home_plan(), room_name)
    if room:
        heater = next((a for a in room.actuators if isinstance(a, Heater)), None)
        if heater:
            heater.set_target_temperature(100)  # Set target temperature to 100°C
            print(f"Heater in {room_name} set to boil water.")
        else:
            print(f"No Heater found in {room_name}. Cannot boil water.")
    else:
        print(f"No room named {room_name} found.")

def main():
    # User's requests
    set_temperature(26, "LivingRoom")
    adjust_light_volume(3, "LivingRoom")
    boil_water("Kitchen")

    # Print the home plan for verification
    print_home_plan(home_plan())

if __name__ == "__main__":
    main()