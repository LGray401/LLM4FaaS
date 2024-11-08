# Based on your functional description, it seems like you want to create a `function.py` file that contains a main function to turn off all unnecessary switches (actuators) in your smart home system. The actuators that are considered "unnecessary" could be those that are not in use or do not need to be on at the moment.
# 
# Here is the `function.py` file with the main function to achieve this:

# functions/function.py

from home.home_plan import home_plan, get_all_actuators

def turn_off_unnecessary_switches(home):
    """
    Turn off all unnecessary switches (actuators) in the home.
    
    :param home: List of Room objects representing the home plan.
    """
    # Define a list of actuator types that should be turned off
    unnecessary_actuators = [
        "Light",
        "MusicPlayer",
        "SmartTV",
        "CleaningRobot",
        "NotificationSender",
        "CoffeeMachine"
    ]
    
    for actuator_type in unnecessary_actuators:
        actuators = get_all_actuators(home, actuator_type)
        for actuator in actuators:
            if actuator.status == "on":
                actuator.turn_off()

def main():
    # Create the home plan
    home = home_plan()
    
    # Turn off unnecessary switches
    turn_off_unnecessary_switches(home)

if __name__ == "__main__":
    main()