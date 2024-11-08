from home.home_plan import home_plan, get_room, get_room_actuators, get_room_sensors, get_all_actuators, \
    get_all_sensors
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, Door, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW
from home.logger_config import logger

# Function to simulate the morning plan
def morning_plan(home):
    print("\n---Morning Plan---")
    living_room = get_room(home, "LivingRoom")
    bedroom = get_room(home, "Bedroom")
    kitchen = get_room(home, "Kitchen")

    # Turn on lights in living room and bedroom
    living_room_lights = get_room_actuators(living_room, "Light")
    for light in living_room_lights:
        light.turn_on()

    bedroom_lights = get_room_actuators(bedroom, "Light")
    for light in bedroom_lights:
        light.turn_on()

    # Open curtains in living room
    living_room_curtains = get_room_actuators(living_room, "Curtain")
    for curtain in living_room_curtains:
        curtain.turn_on()

    # Play relaxing music in living room
    living_room_music_player = get_room_actuators(living_room, "MusicPlayer")[0]
    living_room_music_player.turn_on()
    living_room_music_player.play_music("Relaxing Music")

    # Make coffee in the kitchen
    kitchen_coffee_machine = get_room_actuators(kitchen, "CoffeeMachine")[0]
    kitchen_coffee_machine.turn_on()
    kitchen_coffee_machine.make_coffee("Espresso")

    print("Morning plan executed.")


# Function to simulate the leave home plan
def leave_home_plan(home):
    print("\n---Leave Home Plan---")
    living_room = get_room(home, "LivingRoom")

    # Close the front door
    living_room_door = get_room_actuators(living_room, "Door")[0]
    living_room_door.lock()

    # Turn off lights in the living room
    living_room_lights = get_room_actuators(living_room, "Light")
    for light in living_room_lights:
        light.turn_off()

    print("Leave home plan executed.")


# Function to simulate the movie plan
def movie_plan(home):
    print("\n---Movie Plan---")
    living_room = get_room(home, "LivingRoom")

    # Turn on the TV
    living_room_tv = get_room_actuators(living_room, "SmartTV")[0]
    living_room_tv.turn_on()
    living_room_tv.play_channel("Netflix")

    # Close the curtains
    living_room_curtains = get_room_actuators(living_room, "Curtain")
    for curtain in living_room_curtains:
        curtain.turn_off()

    # Dim the lights
    living_room_lights = get_room_actuators(living_room, "Light")
    for light in living_room_lights:
        light.set_brightness_level("low")

    print("Movie plan executed.")


# Function to simulate temperature regulation
def temperature_regulation(home):
    print("\n---Temperature Regulation---")

    # Get all temperature sensors and heaters/ACs
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")

    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        room_name = sensor.room_name

        # Check if there's a heater/AC in the room
        heater_in_room = None
        ac_in_room = None
        for heater in heaters:
            if heater.room_name == room_name:
                heater_in_room = heater
                break
        for ac in acs:
            if ac.room_name == room_name:
                ac_in_room = ac
                break

        # Adjust temperature based on current temperature
        if current_temp < TEMP_LOW:
            if heater_in_room:
                heater_in_room.turn_on()
                print(f"Turning on heater in {room_name} to increase temperature.")
                logger.info(f"Turning on heater in {room_name} to increase temperature.")
        elif current_temp > TEMP_HIGH:
            if ac_in_room:
                ac_in_room.turn_on()
                print(f"Turning on AC in {room_name} to decrease temperature.")
                logger.info(f"Turning on AC in {room_name} to decrease temperature.")
        else:
            if heater_in_room and heater_in_room.status == "on":
                heater_in_room.turn_off()
                print(f"Turning off heater in {room_name} as temperature is comfortable.")
                logger.info(f"Turning off heater in {room_name} as temperature is comfortable.")
            if ac_in_room and ac_in_room.status == "on":
                ac_in_room.turn_off()
                print(f"Turning off AC in {room_name} as temperature is comfortable.")
                logger.info(f"Turning off AC in {room_name} as temperature is comfortable.")

        # Simulate temperature change over time (for demonstration purposes)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)


# Function to simulate humidity regulation
def humidity_regulation(home):
    print("\n---Humidity Regulation---")

    # Get all humidity sensors and humidifiers
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        current_humidity = sensor.get_reading()
        room_name = sensor.room_name

        # Check if there's a humidifier in the room
        humidifier_in_room = None
        for humidifier in humidifiers:
            if humidifier.room_name == room_name:
                humidifier_in_room = humidifier
                break

        # Adjust humidity based on current humidity
        if current_humidity < HUMIDITY_LOW:
            if humidifier_in_room:
                humidifier_in_room.increase_humidity()
                print(f"Increasing humidity in {room_name}.")
                logger.info(f"Increasing humidity in {room_name}.")
        elif current_humidity > HUMIDITY_HIGH:
            if humidifier_in_room:
                humidifier_in_room.decrease_humidity()
                print(f"Decreasing humidity in {room_name}.")
                logger.info(f"Decreasing humidity in {room_name}.")
        else:
            print(f"Humidity level in {room_name} is comfortable.")
            logger.info(f"Humidity level in {room_name} is comfortable.")


# Function to simulate light regulation
def light_regulation(home):
    print("\n---Light Regulation---")

    # Get all light intensity sensors and lights
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    lights = get_all_actuators(home, "Light")

    for sensor in light_intensity_sensors:
        current_light_intensity = sensor.get_reading()
        room_name = sensor.room_name

        # Check if there are lights in the room
        lights_in_room = []
        for light in lights:
            if light.room_name == room_name:
                lights_in_room.append(light)

        # Adjust light brightness based on current light intensity
        if current_light_intensity < LIGHT_INTENSITY_LOW:
            for light in lights_in_room:
                light.turn_on()
                print(f"Turning on lights in {room_name} as it's dark.")
                logger.info(f"Turning on lights in {room_name} as it's dark.")
        elif current_light_intensity > LIGHT_INTENSITY_HIGH:
            for light in lights_in_room:
                light.turn_off()
                print(f"Turning off lights in {room_name} as it's bright enough.")
                logger.info(f"Turning off lights in {room_name} as it's bright enough.")
        else:
            print(f"Light level in {room_name} is comfortable.")
            logger.info(f"Light level in {room_name} is comfortable.")


# Main function to execute all the functions
def main():
    home = home_plan()

    # Execute the plans
    morning_plan(home)
    leave_home_plan(home)
    movie_plan(home)

    # Simulate environmental regulation
    temperature_regulation(home)
    humidity_regulation(home)
    light_regulation(home)

    print("\nSmart home simulation complete.")


if __name__ == "__main__":
    main()
