# Here is the `function.py` file that contains the main function based on the provided functional description and the source code files:

# function.py
from home.home_plan import home_plan, get_all_actuators, get_room_actuators

def main():
    # Create the home plan
    home = home_plan()

    # MORNING PLAN: Make a cup of coffee
    def morning_plan():
        coffee_machines = get_all_actuators(home, "CoffeeMachine")
        if coffee_machines:
            for coffee_machine in coffee_machines:
                coffee_machine.turn_on()
                coffee_machine.make_coffee("Espresso")
        else:
            print("No CoffeeMachine found in the home.")

    # LEAVE HOME PLAN: Turn off all lights
    def leave_home_plan():
        lights = get_all_actuators(home, "Light")
        if lights:
            for light in lights:
                light.turn_off()
        else:
            print("No Lights found in the home.")

    # MOVIE PLAN: Close the curtains and turn on the SmartTV
    def movie_plan():
        curtains = get_all_actuators(home, "Curtain")
        smart_tvs = get_all_actuators(home, "SmartTV")
        
        if curtains:
            for curtain in curtains:
                curtain.turn_on()
        else:
            print("No Curtains found in the home.")
        
        if smart_tvs:
            for tv in smart_tvs:
                tv.turn_on()
                tv.play_channel("Movie Channel")
        else:
            print("No SmartTV found in the home.")

    # Execute the plans
    morning_plan()
    leave_home_plan()
    movie_plan()

if __name__ == "__main__":
    main()