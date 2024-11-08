from home.home_plan import home_plan, get_room_actuators, get_room, get_all_actuators
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger
from home.sensor import IndoorTemperatureSensor
from home.actuator import Light, Heater, AC, CoffeeMachine, MusicPlayer, SmartTV
from datetime import datetime, timedelta


def morning_plan(home):
    # Wake up at 7:00 AM
    wake_up_time = datetime.now().replace(hour=7, minute=0, second=0, microsecond=0)
    while datetime.now() < wake_up_time:
        time.sleep(1)
    print(f"Good morning! It's {datetime.now().strftime('%H:%M')}. Time to wake up!")
    logger.info(f"Good morning! It's {datetime.now().strftime('%H:%M')}. Time to wake up!")

    # Turn on the music at 7:05 AM
    music_time = datetime.now().replace(hour=7, minute=5, second=0, microsecond=0)
    while datetime.now() < music_time:
        time.sleep(1)
    living_room = get_room(home, "LivingRoom")
    music_player = get_room_actuators(living_room, "MusicPlayer")[0]
    music_player.turn_on()
    music_player.play_music("Jay Chou's playlist")
    print(f"It's {datetime.now().strftime('%H:%M')}. Playing Jay Chou's playlist!")
    logger.info(f"It's {datetime.now().strftime('%H:%M')}. Playing Jay Chou's playlist!")

    # Make coffee at 7:20 AM
    coffee_time = datetime.now().replace(hour=7, minute=20, second=0, microsecond=0)
    while datetime.now() < coffee_time:
        time.sleep(1)
    kitchen = get_room(home, "Kitchen")
    coffee_machine = get_room_actuators(kitchen, "CoffeeMachine")[0]
    coffee_machine.turn_on()
    coffee_machine.make_coffee("Americano")
    print(f"It's {datetime.now().strftime('%H:%M')}. Making a cup of Americano!")
    logger.info(f"It's {datetime.now().strftime('%H:%M')}. Making a cup of Americano!")


def leave_home_plan(home):
    # After 7:30 AM, lock the door and turn off lights and sockets
    leave_time = datetime.now().replace(hour=7, minute=30, second=0, microsecond=0)
    while datetime.now() < leave_time:
        time.sleep(1)

    print(f"It's {datetime.now().strftime('%H:%M')}. Time to leave home!")
    logger.info(f"It's {datetime.now().strftime('%H:%M')}. Time to leave home!")

    # Lock the door
    living_room = get_room(home, "LivingRoom")
    door = get_room_actuators(living_room, "Door")[0]
    door.lock()
    print(f"Locking the door in the living room.")
    logger.info(f"Locking the door in the living room.")

    # Turn off lights and sockets
    lights = get_all_actuators(home, "Light")
    for light in lights:
        light.turn_off()
        print(f"Turning off the light in the {light.room_name}.")
        logger.info(f"Turning off the light in the {light.room_name}.")

    sockets = get_all_actuators(home, "SmartSocket")
    for socket in sockets:
        socket.turn_off()
        print(f"Turning off the socket in the {socket.room_name}.")
        logger.info(f"Turning off the socket in the {socket.room_name}.")


def movie_plan(home):
    print("Starting the Movie plan")
    # Close curtains
    living_room = get_room(home, "LivingRoom")
    curtain = get_room_actuators(living_room, "Curtain")[0]
    curtain.turn_on()
    print(f"Closing the curtains in the living room.")
    logger.info(f"Closing the curtains in the living room.")

    # Dim the lights
    light = get_room_actuators(living_room, "Light")[0]
    light.set_brightness_level("low")
    print(f"Dimming the lights in the living room.")
    logger.info(f"Dimming the lights in the living room.")

    # Start the movie
    tv = get_room_actuators(living_room, "SmartTV")[0]
    tv.turn_on()
    tv.play_channel("Netflix")
    print(f"Starting Netflix on the TV.")
    logger.info(f"Starting Netflix on the TV.")


def temperature_control(home):
    # Temperature control based on indoor temperature sensors
    indoor_temp_sensors = get_all_actuators(home, "IndoorTemperatureSensor")
    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        if current_temp is not None:
            room = get_room(home, sensor.room_name)
            heater = get_room_actuators(room, "Heater")[0]
            ac = get_room_actuators(room, "AC")[0]

            if current_temp < TEMP_LOW:
                heater.turn_on()
                print(f"Turning on the heater in the {sensor.room_name} because the temperature is below {TEMP_LOW}°C.")
                logger.info(f"Turning on the heater in the {sensor.room_name} because the temperature is below {TEMP_LOW}°C.")
            elif current_temp > TEMP_HIGH:
                ac.turn_on()
                print(f"Turning on the AC in the {sensor.room_name} because the temperature is above {TEMP_HIGH}°C.")
                logger.info(f"Turning on the AC in the {sensor.room_name} because the temperature is above {TEMP_HIGH}°C.")
            else:
                heater.turn_off()
                ac.turn_off()
                print(f"The temperature in the {sensor.room_name} is comfortable. No need to adjust.")
                logger.info(f"The temperature in the {sensor.room_name} is comfortable. No need to adjust.")


def humidity_control(home):
    # Humidity control based on humidity sensors
    humidity_sensors = get_all_actuators(home, "HumiditySensor")
    for sensor in humidity_sensors:
        current_humidity = sensor.get_reading()
        if current_humidity is not None:
            room = get_room(home, sensor.room_name)
            humidifier = get_room_actuators(room, "Humidifier")[0]

            if current_humidity < HUMIDITY_LOW:
                humidifier.increase_humidity()
                print(f"Increasing humidity in the {sensor.room_name} because the humidity is below {HUMIDITY_LOW}%.")
                logger.info(f"Increasing humidity in the {sensor.room_name} because the humidity is below {HUMIDITY_LOW}%.")
            elif current_humidity > HUMIDITY_HIGH:
                humidifier.decrease_humidity()
                print(f"Decreasing humidity in the {sensor.room_name} because the humidity is above {HUMIDITY_HIGH}%.")
                logger.info(f"Decreasing humidity in the {sensor.room_name} because the humidity is above {HUMIDITY_HIGH}%.")
            else:
                print(f"The humidity in the {sensor.room_name} is comfortable. No need to adjust.")
                logger.info(f"The humidity in the {sensor.room_name} is comfortable. No need to adjust.")


def light_intensity_control(home):
    # Light intensity control based on light intensity sensors
    light_intensity_sensors = get_all_actuators(home, "LightIntensiveSensor")
    for sensor in light_intensity_sensors:
        current_intensity = sensor.get_reading()
        if current_intensity is not None:
            room = get_room(home, sensor.room_name)
            light = get_room_actuators(room, "Light")[0]

            if current_intensity < LIGHT_INTENSITY_LOW:
                light.turn_on()
                print(f"Turning on the light in the {sensor.room_name} because the light intensity is below {LIGHT_INTENSITY_LOW} lux.")
                logger.info(f"Turning on the light in the {sensor.room_name} because the light intensity is below {LIGHT_INTENSITY_LOW} lux.")
            elif current_intensity > LIGHT_INTENSITY_HIGH:
                light.turn_off()
                print(f"Turning off the light in the {sensor.room_name} because the light intensity is above {LIGHT_INTENSITY_HIGH} lux.")
                logger.info(f"Turning off the light in the {sensor.room_name} because the light intensity is above {LIGHT_INTENSITY_HIGH} lux.")
            else:
                print(f"The light intensity in the {sensor.room_name} is comfortable. No need to adjust.")
                logger.info(f"The light intensity in the {sensor.room_name} is comfortable. No need to adjust.")

def main():
    home = home_plan()

    while True:
        morning_plan(home)
        leave_home_plan(home)
        movie_plan(home)
        temperature_control(home)
        humidity_control(home)
        light_intensity_control(home)

        time.sleep(1)  # Check every second

if __name__ == '__main__':
    main()