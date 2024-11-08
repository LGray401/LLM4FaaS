# Based on your functional description and the provided source code, I'll create a `function.py` file that implements the main function to control your smart home system. This function will handle the morning plan, leave home plan, and movie plan.

# functions/function.py
import time
from home.home_plan import home_plan, get_room, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW
from datetime import datetime

def main():
    home = home_plan()

    def morning_plan():
        bedroom = get_room(home, "Bedroom")
        if bedroom:
            # 7:00 AM - Wake up
            time.sleep(0)  # Simulating time passing for demo purposes
            print("7:00 AM - Wake up")
            
            # 7:05 AM - Play music
            time.sleep(5 * TEMP_CHANGE_DURATION_WINDOW)
            music_player = next((a for a in bedroom.actuators if isinstance(a, MusicPlayer)), None)
            if music_player:
                music_player.turn_on()
                music_player.play_music("周杰伦歌单")
            
            # 7:20 AM - Make coffee
            time.sleep(15 * TEMP_CHANGE_DURATION_WINDOW)
            kitchen = get_room(home, "Kitchen")
            if kitchen:
                coffee_machine = next((a for a in kitchen.actuators if isinstance(a, CoffeeMachine)), None)
                if coffee_machine:
                    coffee_machine.turn_on()
                    coffee_machine.make_coffee("Black Coffee")

    def leave_home_plan():
        current_time = datetime.now().time()
        if current_time > datetime.strptime("07:30", "%H:%M").time():
            # Lock doors and turn off lights and sockets
            doors = get_all_actuators(home, "Door")
            for door in doors:
                door.lock()

            lights = get_all_actuators(home, "Light")
            for light in lights:
                light.turn_off()

            sockets = get_all_actuators(home, "SmartSocket")
            for socket in sockets:
                socket.turn_off()

    def movie_plan():
        living_room = get_room(home, "LivingRoom")
        if living_room:
            # Close curtains and dim lights
            curtain = next((a for a in living_room.actuators if isinstance(a, Curtain)), None)
            if curtain:
                curtain.turn_on()
                print("Curtains are closed")

            lights = get_all_actuators(home, "Light")
            for light in lights:
                light.set_brightness_level("low")

    # Execute plans
    morning_plan()
    leave_home_plan()
    movie_plan()

if __name__ == "__main__":
    main()