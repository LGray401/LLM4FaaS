from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
from home.logger_config import logger


def main():
    home = home_plan()  # Initialize the home plan

    # Scenario 1: Opening the entrance door
    entrance_door = get_room_actuators(home, "LivingRoom")[0]
    entrance_door.turn_on()  # Open the entrance door
    curtain = get_room_actuators(home, "LivingRoom")[5]
    curtain.turn_on()  # Open the curtain
    music_player = get_room_actuators(home, "LivingRoom")[6]
    music_player.play_music("Classical Music")  # Play music

    # Scenario 2: Temperature control
    indoor_temp_sensor = get_room_sensors(home, "LivingRoom")[1]
    indoor_temperature = indoor_temp_sensor.get_reading()

    if indoor_temperature > TEMP_HIGH:
        window = get_room_actuators(home, "LivingRoom")[4]
        window.turn_off()  # Close the window
        ac = get_room_actuators(home, "LivingRoom")[12]
        ac.turn_on()  # Turn on the AC
        ac.set_target_temperature(24)  # Set the target temperature for the AC
    elif indoor_temperature > 24:
        window = get_room_actuators(home, "LivingRoom")[4]
        window.turn_on()  # Open the window

    # Scenario 3: Humidity control
    humidity_sensor = get_room_sensors(home, "LivingRoom")[2]
    humidity = humidity_sensor.get_reading()
    if humidity < HUMIDITY_LOW:
        humidifier = get_room_actuators(home, "LivingRoom")[13]
        humidifier.increase_humidity()  # Increase the humidity
        ac = get_room_actuators(home, "LivingRoom")[12]
        ac.turn_off()  # Turn off the AC


    # Scenario 4: Light control
    light_intensive_sensor = get_room_sensors(home, "LivingRoom")[0]
    light_intensity = light_intensive_sensor.get_reading()
    if light_intensity < LIGHT_INTENSITY_LOW:
        light = get_room_actuators(home, "LivingRoom")[1]
        light.turn_on()  # Turn on the light

    # Scenario 5: Turning on the TV
    tv = get_room_actuators(home, "LivingRoom")[11]
    tv.turn_on()  # Turn on the TV
    tv.play_channel("News")  # Play the news channel
    music_player.turn_off()  # Turn off the music player
    curtain.turn_off()  # Close the curtain
    light.set_brightness_level("medium")  # Dim the light


    # Scenario 6: Cleaning Robot Daily Routine
    cleaning_robot = get_room_actuators(home, "LivingRoom")[9]
    cleaning_robot.turn_on()  # Turn on the cleaning robot
    cleaning_robot.daily_routine()  # Start the cleaning robot's daily routine

    # Scenario 7: Coffee Machine
    coffee_machine = get_room_actuators(home, "Kitchen")[4]
    coffee_machine.turn_on()  # Turn on the coffee machine
    coffee_machine.make_coffee("Cappuccino")  # Make a cappuccino

    # Scenario 8: Heating
    heater = get_room_actuators(home, "LivingRoom")[12]
    if indoor_temperature < TEMP_LOW:
        heater.turn_on()  # Turn on the heater
        heater.set_target_temperature(20)  # Set the target temperature for the heater

    # Scenario 9: Notification Sender
    notification_sender = get_room_actuators(home, "LivingRoom")[10]
    notification_sender.notification_sender("Reminder: You have a meeting at 3 PM.")

    # Scenario 10: Control temperature and humidity in the bathroom
    bathroom = get_room("home", "Bathroom")
    temp_sensor = get_all_sensors(home, "IndoorTemperature")[1]
    humidity_sensor = get_all_sensors(home, "Humidity")[2]
    if temp_sensor.get_reading() > 25:
        bathroom.actuators[4].turn_on()  # turn on the heater
        bathroom.actuators[4].set_target_temperature(23)
    if humidity_sensor.get_reading() < 40:
        bathroom.actuators[5].increase_humidity()  # turn on the humidifier
        bathroom.actuators[4].turn_off()  # turn off the heater

    # Scenario 11: Control temperature in the Bedroom
    bedroom = get_room("home", "Bedroom")
    temp_sensor = get_all_sensors(home, "IndoorTemperature")[0]
    if temp_sensor.get_reading() > 28:
        bedroom.actuators[4].turn_on()  # turn on the AC
        bedroom.actuators[4].set_target_temperature(25)
    elif temp_sensor.get_reading() < 20:
        bedroom.actuators[5].turn_on()  # turn on the heater
        bedroom.actuators[5].set_target_temperature(23)

    # Scenario 12: Control temperature and humidity in the kitchen
    kitchen = get_room("home", "Kitchen")
    temp_sensor = get_all_sensors(home, "IndoorTemperature")[2]
    humidity_sensor = get_all_sensors(home, "Humidity")[3]
    if temp_sensor.get_reading() > 25:
        kitchen.actuators[3].turn_on()  # turn on the heater
        kitchen.actuators[3].set_target_temperature(23)
    if humidity_sensor.get_reading() < 35:
        kitchen.actuators[4].increase_humidity()  # turn on the humidifier
        kitchen.actuators[3].turn_off()  # turn off the heater


if __name__ == "__main__":
    main()