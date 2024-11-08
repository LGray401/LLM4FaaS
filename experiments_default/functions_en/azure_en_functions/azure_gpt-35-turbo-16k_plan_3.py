# Sure, here is the 'function.py' file based on your functional description:

from home.home_plan import get_room_actuators, get_room_sensors

def morning_plan(home):
    coffee_machine = get_room_actuators(home, "Kitchen")[0]
    coffee_machine.turn_on()
    coffee_machine.make_coffee("black")

def leave_home_plan(home):
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()

def movie_plan(home):
    curtains = get_room_actuators(home, "LivingRoom")[2]
    curtains.close()

def main():
    home = home_plan()
    plan = input("Enter the plan (morning, leave home, movie): ")
    
    if plan == "morning":
        morning_plan(home)
    elif plan == "leave home":
        leave_home_plan(home)
    elif plan == "movie":
        movie_plan(home)
    else:
        print("Invalid plan!")

if __name__ == "__main__":
    main()