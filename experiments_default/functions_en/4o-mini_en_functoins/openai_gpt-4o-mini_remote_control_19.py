# Based on your provided functional description and the existing code structure, I will create a `function.py` file that includes the main function to turn on the air conditioner in the living room and set it to 26 degrees.
# 
# Here's how the `function.py` file will look:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import AC
from home.sensor import IndoorTemperatureSensor

def main():
    # Create the home plan
    home = home_plan()
    
    # Find the living room
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    
    if living_room:
        # Get the AC actuator
        ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
        
        if ac:
            # Turn on the AC and set the target temperature
            ac.turn_on()
            ac.set_target_temperature(26)
            print(f"The AC in the Living Room is set to {ac.target_temperature}°C.")
        else:
            print("AC not found in the Living Room.")
    else:
        print("Living Room not found in the home.")

if __name__ == "__main__":
    main()