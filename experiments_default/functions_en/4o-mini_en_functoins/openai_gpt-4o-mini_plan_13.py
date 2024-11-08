# Based on your functional description and the provided source code, I'll create the `function.py` file that contains the main function to implement the three plans: "MORNING PLAN", "LEAVE HOME PLAN", and "MOVIE PLAN". 
# 
# The `function.py` file will utilize the classes defined in your existing source files to perform the required operations.
# 
# Here's the `function.py` that you can place in your `functions` folder:

# function.py
from home.home_plan import home_plan, get_room
from home.actuator import Light, Curtain, CoffeeMachine, MusicPlayer, SmartTV, Door

def morning_plan():
    print("Executing Morning Plan...")
    living_room = get_room(home_plan(), "LivingRoom")

    # Open curtains
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()
    
    # Dim lights
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.set_brightness_level("low")
            actuator.turn_on()

    # Start coffee machine
    for actuator in living_room.actuators:
        if isinstance(actuator, CoffeeMachine):
            actuator.turn_on()
            actuator.make_coffee("Espresso")

    # Play music
    for actuator in living_room.actuators:
        if isinstance(actuator, MusicPlayer):
            actuator.turn_on()
            actuator.play_music("Morning Playlist")

def leave_home_plan():
    print("Executing Leave Home Plan...")
    living_room = get_room(home_plan(), "LivingRoom")
    
    # Turn off lights
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.turn_off()

    # Draw curtains
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_off()

    # Turn off sockets
    for actuator in living_room.actuators:
        if isinstance(actuator, SmartSocket):
            actuator.turn_off()

    # Lock the door
    for actuator in living_room.actuators:
        if isinstance(actuator, Door):
            actuator.lock()

def movie_plan():
    print("Executing Movie Plan...")
    living_room = get_room(home_plan(), "LivingRoom")

    # Draw gauze curtains
    for actuator in living_room.actuators:
        if isinstance(actuator, Curtain):
            actuator.turn_on()

    # Dim lights
    for actuator in living_room.actuators:
        if isinstance(actuator, Light):
            actuator.set_brightness_level("low")
            actuator.turn_on()

    # Watch TV
    for actuator in living_room.actuators:
        if isinstance(actuator, SmartTV):
            actuator.turn_on()
            actuator.play_channel("Favorite Movie Channel")

def main():
    while True:
        print("\nSelect a plan to execute:")
        print("1. Morning Plan")
        print("2. Leave Home Plan")
        print("3. Movie Plan")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            morning_plan()
        elif choice == '2':
            leave_home_plan()
        elif choice == '3':
            movie_plan()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()