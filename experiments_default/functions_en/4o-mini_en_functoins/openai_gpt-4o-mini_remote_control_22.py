# Based on your functional description and the provided source code, I will create a `function.py` file that includes the main function to control the devices in your smart home project. This function will turn on the lights in the living room, bedroom, and bathroom, turn on the air conditioners in the living room and bedroom, turn on the heater in the bathroom, and turn on the TV in the living room.
# 
# Here is the `function.py` file:

# function.py
from home.home_plan import home_plan
from home.actuator import Light, AC, Heater, SmartTV

def main():
    # Create the home plan with rooms and components
    home = home_plan()
    
    # Define the rooms and their respective devices to control
    rooms_to_control = {
        "LivingRoom": {
            "lights": [Light],
            "acs": [AC],
            "tv": SmartTV
        },
        "Bedroom": {
            "lights": [Light],
            "acs": [AC]
        },
        "Bathroom": {
            "lights": [Light],
            "heaters": [Heater]
        }
    }

    # Turn on lights and actuators in the specified rooms
    for room_name, devices in rooms_to_control.items():
        room = next((r for r in home if r.name == room_name), None)
        if room is None:
            print(f"Room '{room_name}' not found.")
            continue
        
        # Turn on lights
        for light in devices.get("lights", []):
            light_instance = next((a for a in room.actuators if isinstance(a, light)), None)
            if light_instance:
                light_instance.turn_on()

        # Turn on air conditioners
        for ac in devices.get("acs", []):
            ac_instance = next((a for a in room.actuators if isinstance(a, ac)), None)
            if ac_instance:
                ac_instance.turn_on()

        # Turn on heaters
        for heater in devices.get("heaters", []):
            heater_instance = next((a for a in room.actuators if isinstance(a, heater)), None)
            if heater_instance:
                heater_instance.turn_on()

        # Turn on TV in Living Room
        if room_name == "LivingRoom":
            tv_instance = next((a for a in room.actuators if isinstance(a, SmartTV)), None)
            if tv_instance:
                tv_instance.turn_on()
    
if __name__ == "__main__":
    main()