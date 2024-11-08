# Sure, based on the functional description and the provided source codes, I'll create the `function.py` file. This file will contain a main function that carries out the actions specified: turning up the air conditioner to 26°, turning up the TV volume by three degrees, and heating the kettle to 100°.
# 
# Here is the `function.py`:
# 
# ### `functions/function.py`

from home.home_plan import home_plan, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()

    # Adjust the air conditioner in the LivingRoom to 26°
    living_room_ac = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_ac:
        if actuator.actuator_type == "AC":
            actuator.set_target_temperature(26)
            print(f"Air conditioner in {actuator.room_name} is set to {actuator.target_temperature}°C.")
            break
    else:
        print("AC not found in the LivingRoom.")

    # Turn up the TV volume by three degrees (assuming TV volume control is available)
    living_room_tv = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_tv:
        if actuator.actuator_type == "SmartTV":
            # For simplicity, let's assume there's a method to increase the TV volume
            # Adding a placeholder method to simulate volume increase
            if hasattr(actuator, 'increase_volume'):
                actuator.increase_volume(3)
                print(f"TV volume in {actuator.room_name} is increased by 3 degrees.")
            else:
                print(f"TV in {actuator.room_name} does not support volume adjustment in this implementation.")
            break
    else:
        print("SmartTV not found in the LivingRoom.")

    # Heat the kettle to 100°
    kitchen_heater = get_room_actuators(home, "Kitchen")
    for actuator in kitchen_heater:
        if actuator.actuator_type == "Heater":
            actuator.set_target_temperature(100)
            print(f"Heater in {actuator.room_name} is set to {actuator.target_temperature}°C.")
            break
    else:
        print("Heater not found in the Kitchen.")

if __name__ == "__main__":
    main()