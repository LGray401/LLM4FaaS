# Based on your functional description "关闭客厅的灯" (which translates to "Turn off the living room light"), here is the `function.py` file that will locate the light actuator in the living room and turn it off.
# 
# Create a new file named `function.py` in the `functions` folder with the following content:

# functions/function.py

from home.home_plan import home_plan, get_room_actuators

def main():
    home = home_plan()
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    if living_room_actuators is not None:
        for actuator in living_room_actuators:
            if actuator.actuator_type == "Light":
                actuator.turn_off()
                break
    else:
        print("No actuators found in the living room.")

if __name__ == "__main__":
    main()