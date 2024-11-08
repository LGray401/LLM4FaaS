from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, \
    SmokeSensor
from home.actuator import Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, \
    CleaningRobot, NotificationSender, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW


def main():
    # Create a home plan
    home = home_plan()

    # Get a room from the home plan
    living_room = get_room(home, "LivingRoom")

    # Get sensors in the living room
    living_room_sensors = get_room_sensors(home, "LivingRoom")
    for sensor in living_room_sensors:
        print(sensor.id)
        print(sensor.status)

    # Get actuators in the living room
    living_room_actuators = get_room_actuators(home, "LivingRoom")
    for actuator in living_room_actuators:
        print(actuator.id)
        print(actuator.status)

    # Get all lights in the home
    all_lights = get_all_actuators(home, "Light")
    for light in all_lights:
        print(light.id)
        print(light.status)

    # Turn on the light in the living room
    living_room_light = get_room_actuators(home, "LivingRoom")[0]
    living_room_light.turn_on()
    print(living_room_light.status)

    # Get the temperature sensor in the living room
    living_room_temp_sensor = get_room_sensors(home, "LivingRoom")[0]
    print(living_room_temp_sensor.id)
    print(living_room_temp_sensor.status)

    # Get the heater in the living room
    living_room_heater = get_room_actuators(home, "LivingRoom")[11]  # Assuming heater is the 11th actuator
    print(living_room_heater.id)
    print(living_room_heater.status)

    # Get the AC in the living room
    living_room_ac = get_room_actuators(home, "LivingRoom")[10]  # Assuming AC is the 10th actuator
    print(living_room_ac.id)
    print(living_room_ac.status)

    # Check temperature and adjust heater/AC accordingly
    current_temperature = living_room_temp_sensor.get_reading()
    if current_temperature is not None:
        print(f"Current temperature: {current_temperature}")
        if current_temperature < TEMP_LOW:
            print(f"Turning on the heater in the living room...")
            living_room_heater.turn_on()
        elif current_temperature > TEMP_HIGH:
            print(f"Turning on the AC in the living room...")
            living_room_ac.turn_on()
        else:
            print(f"Temperature is comfortable.")

    # Check humidity and adjust humidifier
    humidity_sensor = get_room_sensors(home, "LivingRoom")[1]  # Assuming humidity sensor is the 2nd sensor
    humidity_reading = humidity_sensor.get_reading()
    if humidity_reading is not None:
        print(f"Current humidity: {humidity_reading}")
        living_room_humidifier = get_room_actuators(home, "LivingRoom")[12]  # Assuming humidifier is the 12th actuator
        if humidity_reading < HUMIDITY_LOW:
            print(f"Increasing humidity in the living room...")
            living_room_humidifier.increase_humidity()
        elif humidity_reading > HUMIDITY_HIGH:
            print(f"Decreasing humidity in the living room...")
            living_room_humidifier.decrease_humidity()
        else:
            print(f"Humidity is comfortable.")

    # Check light intensity and adjust lights
    light_intensity_sensor = get_room_sensors(home, "LivingRoom")[0]  # Assuming light intensity sensor is the 1st sensor
    light_intensity_reading = light_intensity_sensor.get_reading()
    if light_intensity_reading is not None:
        print(f"Current light intensity: {light_intensity_reading}")
        if light_intensity_reading < LIGHT_INTENSITY_LOW:
            print(f"Turning on the lights in the living room...")
            living_room_light.turn_on()
        else:
            print(f"Light intensity is sufficient.")

    # Example of using other actuators
    print(f"Playing music in the living room...")
    living_room_music_player = get_room_actuators(home, "LivingRoom")[5]
    living_room_music_player.play_music("Classical")

    # Example of using notification sender
    print(f"Sending notification to the living room...")
    notification_sender = get_room_actuators(home, "LivingRoom")[9]
    notification_sender.notification_sender("It's time for dinner!")

    # Example of using cleaning robot
    print(f"Starting cleaning robot in the living room...")
    cleaning_robot = get_room_actuators(home, "LivingRoom")[8]
    cleaning_robot.daily_routine()

    # Example of using smart TV
    print(f"Playing channel 'CNN' on the TV in the living room...")
    smart_tv = get_room_actuators(home, "LivingRoom")[7]
    smart_tv.play_channel("CNN")

    # Example of using coffee machine
    print(f"Making coffee in the kitchen...")
    kitchen = get_room(home, "Kitchen")
    coffee_machine = get_room_actuators(kitchen, "Kitchen")[3]
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Espresso")

    # Example of using window
    print(f"Opening a window in the living room...")
    living_room_window = get_room_actuators(home, "LivingRoom")[3]
    living_room_window.turn_on()

    # Example of using curtain
    print(f"Closing the curtains in the living room...")
    living_room_curtain = get_room_actuators(home, "LivingRoom")[4]
    living_room_curtain.turn_off()

    # Example of using door
    print(f"Locking the door in the living room...")
    living_room_door = get_room_actuators(home, "LivingRoom")[0]
    living_room_door.lock()

    # Example of using smart socket
    print(f"Turning on the smart socket in the living room...")
    smart_socket = get_room_actuators(home, "LivingRoom")[6]
    smart_socket.turn_on()

    # Example of using outdoor temperature sensor
    print(f"Getting outdoor temperature...")
    outdoor_temp_sensor = get_all_sensors(home, "OutdoorTemperature")[0]
    outdoor_temp_reading = outdoor_temp_sensor.get_reading()
    print(f"Outdoor temperature: {outdoor_temp_reading}")

    # Example of using smoke sensor
    print(f"Checking smoke in the kitchen...")
    smoke_sensor = get_room_sensors(kitchen, "Kitchen")[1]
    smoke_reading = smoke_sensor.get_reading()
    if smoke_reading > 50:  # Adjust this threshold as needed
        print(f"Smoke detected! Sending notification...")
        notification_sender.notification_sender("Smoke detected in the kitchen!")

    # Example of using smart socket to turn on/off devices
    print(f"Turning on the kettle using the smart socket...")
    smart_socket.turn_on()
    time.sleep(5)  # Wait for kettle to boil
    print(f"Turning off the kettle using the smart socket...")
    smart_socket.turn_off()


if __name__ == "__main__":
    main()

# **Explanation:**

# 1. **Import necessary modules:**
#    - `home.home_plan` for room and device management.
#    - `home.sensor` for sensor classes (temperature, humidity, light intensity, etc.).
#    - `home.actuator` for actuator classes (lights, heater, AC, coffee machine, etc.).
#    - `home.config` for configuration settings (temperature thresholds, etc.).

# 2. **`main` function:**
#    - **Create a home plan:** Calls `home_plan()` to create a list of `Room` objects.
#    - **Get rooms and devices:** Uses functions from `home.home_plan` to get specific rooms, sensors, and actuators.
#    - **Turn on lights and adjust temperature:** Shows examples of controlling lights and heater/AC based on temperature readings.
#    - **Check humidity and adjust humidifier:** Shows how to monitor humidity and use a humidifier to maintain a comfortable level.
#    - **Check light intensity and adjust lights:** Demonstrates how to control lights based on light intensity readings.
#    - **Examples of other actuator usage:** Provides examples of using other actuators like `MusicPlayer`, `NotificationSender`, `CleaningRobot`, `SmartTV`, `CoffeeMachine`, `Window`, `Curtain`, `Door`, `SmartSocket`, and `OutdoorTemperatureSensor`.
#    - **Demonstrates smoke detection and notification:** Shows how to use a `SmokeSensor` to detect smoke and send notifications.

# **To run this code:**

# 1. Make sure you have all the files from your `home` and `functions` folders.
# 2. Run `function.py` from your terminal: `python functions/function.py`

# **Key Improvements:**

# - **Organization:** The code is better organized, making it easier to understand and modify.
# - **Real-world scenarios:** The code incorporates real-world scenarios like temperature and humidity control, along with examples of how to use other actuators.
# - **User-friendly output:** The code provides clear and informative messages to the user, indicating the actions being taken.
# - **Comments:** The code includes comments explaining the purpose of different sections and functions.

# This code provides a basic framework for your smart home project. You can expand upon this foundation by adding more sensors, actuators, and functionalities. Remember to adjust the configuration settings (`home.config.py`) to match your specific needs.
