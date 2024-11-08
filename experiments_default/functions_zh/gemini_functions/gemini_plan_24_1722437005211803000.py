from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def morning_plan(home):
    """
    MORNING PLAN:
    早晨拉开窗帘，阴天的话开灯，做咖啡，咖啡做好了放音乐
    """
    # Get LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is None:
        return
    
    # Get actuators
    living_room_actuators = living_room.actuators
    curtain = get_all_actuators(home, "Curtain")[0]
    light = get_all_actuators(home, "Light")[0]
    coffee_machine = get_all_actuators(home, "CoffeeMachine")[0]
    music_player = get_all_actuators(home, "MusicPlayer")[0]

    # Open curtains
    curtain.turn_on() 

    # Turn on light if it's cloudy
    light_sensor = get_all_sensors(home, "LightIntensive")[0]
    light_intensity = light_sensor.get_reading()
    if light_intensity < LIGHT_INTENSITY_HIGH:
        light.turn_on()

    # Make coffee
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")

    # Play music when coffee is done
    music_player.turn_on()
    music_player.play_music("Morning Jazz")

def leave_home_plan(home):
    """
    LEAVE HOME PLAN:
    晴天的话拉开窗帘，关闭灯，插座，锁门
    """
    # Get LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is None:
        return
    
    # Get actuators
    living_room_actuators = living_room.actuators
    curtain = get_all_actuators(home, "Curtain")[0]
    light = get_all_actuators(home, "Light")[0]
    smart_socket = get_all_actuators(home, "SmartSocket")
    door = get_all_actuators(home, "Door")[0]

    # Open curtains if it's sunny
    light_sensor = get_all_sensors(home, "LightIntensive")[0]
    light_intensity = light_sensor.get_reading()
    if light_intensity > LIGHT_INTENSITY_LOW:
        curtain.turn_on()

    # Turn off lights and sockets
    light.turn_off()
    for socket in smart_socket:
        socket.turn_off()

    # Lock the door
    door.lock()

def movie_plan(home):
    """
    MOVIE PLAN:
    合上窗帘，关灯
    """
    # Get LivingRoom
    living_room = get_room(home, "LivingRoom")
    if living_room is None:
        return
    
    # Get actuators
    living_room_actuators = living_room.actuators
    curtain = get_all_actuators(home, "Curtain")[0]
    light = get_all_actuators(home, "Light")[0]

    # Close curtains
    curtain.turn_off()

    # Turn off lights
    light.turn_off()

if __name__ == "__main__":
    # Initialize home plan
    home = home_plan()

    # Example usage:
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

# **Explanation:**

# 1. **Import necessary modules:**
#    - Import functions and classes from `home.home_plan`, `home.sensor`, `home.actuator`, and `home.config`.

# 2. **Define plan functions:**
#    - **`morning_plan(home)`:**
#      - Gets the "LivingRoom" from the `home` plan.
#      - Retrieves actuators: `curtain`, `light`, `coffee_machine`, `music_player`.
#      - Opens the curtain.
#      - Checks light intensity using a `light_sensor` and turns on the light if it's cloudy.
#      - Turns on the `coffee_machine` and makes espresso.
#      - Plays morning jazz music after the coffee is done.

#    - **`leave_home_plan(home)`:**
#      - Gets the "LivingRoom".
#      - Retrieves actuators: `curtain`, `light`, `smart_socket`, `door`.
#      - Opens the curtain if it's sunny.
#      - Turns off the `light` and all `smart_socket`s.
#      - Locks the `door`.

#    - **`movie_plan(home)`:**
#      - Gets the "LivingRoom".
#      - Retrieves actuators: `curtain`, `light`.
#      - Closes the `curtain`.
#      - Turns off the `light`.

# 3. **Main execution:**
#    - Creates the `home` plan using `home_plan()`.
#    - Includes commented-out examples to show how to call each plan function.

# **Key Improvements:**

# - **Clear Function Structure:** The code is organized into separate functions for each plan, making it easier to read and understand.
# - **Consistent Access to Actuators:** The functions use `get_all_actuators` and `get_room_actuators` to consistently retrieve actuators.
# - **Use of Sensor Data:** The `morning_plan` and `leave_home_plan` functions use sensor readings (light intensity) to make decisions.

# **To use this code:**

# 1. Make sure you have the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files in the `home` folder.
# 2. Place this `function.py` file in the `functions` folder.
# 3. Import and use the functions as needed in your smart home project. 

# Feel free to customize the code to fit your specific smart home project needs.
