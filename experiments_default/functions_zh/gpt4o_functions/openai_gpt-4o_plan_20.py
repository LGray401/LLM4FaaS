# Here's the `function.py` file that implements the main functions based on the provided functional description and source code:

# function.py

from home.home_plan import home_plan, get_all_actuators

def morning_plan(home):
    curtains = get_all_actuators(home, "Curtain")
    for curtain in curtains:
        curtain.turn_on()

def leave_home_plan(home):
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def movie_plan(home):
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_on()  # Ensure lights are on before setting brightness
        light.set_brightness_level("low")  # Adjust brightness for movie plan

def main():
    home = home_plan()

    # Execute different plans based on some condition or input
    print("Executing Morning Plan...")
    morning_plan(home)

    print("\nExecuting Leave Home Plan...")
    leave_home_plan(home)

    print("\nExecuting Movie Plan...")
    movie_plan(home)

if __name__ == "__main__":
    main()