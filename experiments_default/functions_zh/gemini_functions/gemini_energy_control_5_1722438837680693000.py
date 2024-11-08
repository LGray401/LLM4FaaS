from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_CHANGE_DURATION_WINDOW, TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, \
    LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, DAILY_ROUTINE_DURATION

def main():
    """
    Main function for the smart home system.
    """
    home = home_plan()

    # Example usage - adjust temperature in Living Room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        temperature_sensor = get_room_sensors(home, "LivingRoom")[0]  # Assuming there's only one temperature sensor
        heater = get_room_actuators(home, "LivingRoom")[0]  # Assuming there's only one heater

        if temperature_sensor.get_reading() < TEMP_LOW:
            print("It's cold! Turning on the heater...")
            heater.turn_on()
            heater.set_target_temperature(TEMP_HIGH)
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for the heater to warm up

        elif temperature_sensor.get_reading() > TEMP_HIGH:
            print("It's hot! Turning on the AC...")
            ac = get_room_actuators(home, "LivingRoom")[1]  # Assuming there's only one AC
            ac.turn_on()
            ac.set_target_temperature(TEMP_LOW)
            time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Wait for the AC to cool down

    # Example usage - adjust light intensity in Living Room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        light_sensor = get_room_sensors(home, "LivingRoom")[1]  # Assuming there's only one light sensor
        light = get_room_actuators(home, "LivingRoom")[1]  # Assuming there's only one light

        if light_sensor.get_reading() < LIGHT_INTENSITY_LOW:
            print("It's dark! Turning on the light...")
            light.turn_on()
            light.set_brightness_level("medium")

        elif light_sensor.get_reading() > LIGHT_INTENSITY_HIGH:
            print("It's too bright! Dimming the light...")
            light.set_brightness_level("low")

    # Example usage - controlling the coffee machine in Kitchen
    kitchen = get_room(home, "Kitchen")
    if kitchen:
        coffee_machine = get_room_actuators(home, "Kitchen")[3]  # Assuming there's only one coffee machine
        coffee_machine.turn_on()
        coffee_machine.make_coffee("Espresso")

    # Example usage - daily cleaning routine in Living Room
    living_room = get_room(home, "LivingRoom")
    if living_room:
        cleaning_robot = get_room_actuators(home, "LivingRoom")[9]  # Assuming there's only one cleaning robot
        cleaning_robot.turn_on()
        cleaning_robot.daily_routine()

    # Example usage - sending a notification to all rooms
    notification_sender = get_all_actuators(home, "NotificationSender")[0]  # Assuming there's only one notification sender
    notification_sender.turn_on()
    notification_sender.notification_sender("The cleaning robot is starting its daily routine!")

if __name__ == "__main__":
    main()

# This file uses the functionalities from `sensor.py`, `actuator.py`, and `home_plan.py` to create a simple example of a smart home system. 

# Here's a breakdown of the code:

# 1. **Imports**: The necessary modules are imported from the `home` package.
# 2. **`main` function**: This function is the entry point for the script. 
# 3. **Home initialization**: The `home_plan()` function is called to create the home structure.
# 4. **Example usage**: The code demonstrates simple actions for the smart home system:
#    - **Adjusting temperature**: 
#      - It checks the temperature in the living room and turns on the heater if it's below a certain threshold.
#      - It also turns on the AC if the temperature is above the threshold.
#    - **Adjusting light intensity**:
#      - It adjusts the light brightness in the living room based on the light intensity sensor reading.
#    - **Controlling the coffee machine**:
#      - It turns on the coffee machine and makes an espresso.
#    - **Running the daily cleaning routine**:
#      - It turns on the cleaning robot and initiates the daily cleaning routine.
#    - **Sending a notification**: 
#      - It sends a notification to all rooms about the cleaning robot's routine.

# This is just a basic example. You can expand upon this by adding more sensors, actuators, and logic to create a more complex and intelligent smart home system.
