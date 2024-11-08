from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.actuator import CoffeeMachine, Light, MusicPlayer, Curtain, Door, CleaningRobot, SmartTV
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_HIGH, LIGHT_INTENSITY_LOW
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.logger_config import logger

def morning_plan(home):
    """Turns on bedroom light, opens curtains, sets music player, and starts coffee machine."""
    bedroom = get_room(home, "Bedroom")
    if bedroom:
        bedroom_lights = get_room_actuators(home, "Bedroom")
        if bedroom_lights:
            for light in bedroom_lights:
                if light.actuator_type == "Light":
                    light.turn_on()
        bedroom_curtains = get_room_actuators(home, "Bedroom")
        if bedroom_curtains:
            for curtain in bedroom_curtains:
                if curtain.actuator_type == "Curtain":
                    curtain.turn_on()

        music_player = get_room_actuators(home, "Bedroom")
        if music_player:
            for player in music_player:
                if player.actuator_type == "MusicPlayer":
                    player.play_music("Morning playlist")

        coffee_machine = get_room_actuators(home, "Kitchen")
        if coffee_machine:
            for machine in coffee_machine:
                if machine.actuator_type == "CoffeeMachine":
                    machine.make_coffee("Espresso")
    else:
        logger.error("Bedroom not found in home plan.")

def leave_home_plan(home):
    """Turns off all lights, locks the front door, and closes sockets."""
    all_lights = get_all_actuators(home, "Light")
    if all_lights:
        for light in all_lights:
            light.turn_off()

    front_door = get_room_actuators(home, "LivingRoom")
    if front_door:
        for door in front_door:
            if door.actuator_type == "Door":
                door.lock()

    all_sockets = get_all_actuators(home, "SmartSocket")
    if all_sockets:
        for socket in all_sockets:
            socket.turn_off()

def movie_plan(home):
    """Closes curtains, dims lights, turns on TV, and sets program."""
    living_room = get_room(home, "LivingRoom")
    if living_room:
        living_room_curtains = get_room_actuators(home, "LivingRoom")
        if living_room_curtains:
            for curtain in living_room_curtains:
                if curtain.actuator_type == "Curtain":
                    curtain.turn_on()

        living_room_lights = get_room_actuators(home, "LivingRoom")
        if living_room_lights:
            for light in living_room_lights:
                if light.actuator_type == "Light":
                    light.set_brightness_level("low")

        living_room_tv = get_room_actuators(home, "LivingRoom")
        if living_room_tv:
            for tv in living_room_tv:
                if tv.actuator_type == "SmartTV":
                    tv.play_channel("Movie Channel")
    else:
        logger.error("Living Room not found in home plan.")

def adjust_temperature(home):
    """Adjusts heater and AC based on temperature sensors."""
    all_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    if all_temp_sensors:
        for sensor in all_temp_sensors:
            if isinstance(sensor, IndoorTemperatureSensor):
                current_temp = sensor.get_reading()
                if current_temp is not None:
                    room_name = sensor.room_name
                    heaters = get_room_actuators(home, room_name)
                    if heaters:
                        for heater in heaters:
                            if heater.actuator_type == "Heater":
                                heater.adjust_temperature(current_temp)

                    acs = get_room_actuators(home, room_name)
                    if acs:
                        for ac in acs:
                            if ac.actuator_type == "AC":
                                ac.adjust_temperature(current_temp)

def adjust_humidity(home):
    """Adjusts humidifier based on humidity sensors."""
    all_humidity_sensors = get_all_sensors(home, "Humidity")
    if all_humidity_sensors:
        for sensor in all_humidity_sensors:
            if isinstance(sensor, HumiditySensor):
                current_humidity = sensor.get_reading()
                if current_humidity is not None:
                    room_name = sensor.room_name
                    # Find humidifiers in the room
                    humidifiers = get_room_actuators(home, room_name)
                    if humidifiers:
                        for humidifier in humidifiers:
                            if humidifier.actuator_type == "Humidifier":
                                if current_humidity < HUMIDITY_LOW:
                                    humidifier.increase_humidity()
                                elif current_humidity > HUMIDITY_HIGH:
                                    humidifier.decrease_humidity()

def adjust_lighting(home):
    """Adjusts lights based on light intensity sensors."""
    all_light_sensors = get_all_sensors(home, "LightIntensive")
    if all_light_sensors:
        for sensor in all_light_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                current_light_intensity = sensor.get_reading()
                if current_light_intensity is not None:
                    room_name = sensor.room_name
                    lights = get_room_actuators(home, room_name)
                    if lights:
                        for light in lights:
                            if light.actuator_type == "Light":
                                if current_light_intensity < LIGHT_INTENSITY_LOW:
                                    light.turn_on()
                                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                                    light.turn_off()

def main():
    home = home_plan()
    # Example plan execution
    morning_plan(home)
    adjust_temperature(home)
    adjust_humidity(home)
    adjust_lighting(home)
    # Leave home plan
    leave_home_plan(home)
    # Movie plan
    movie_plan(home)

if __name__ == "__main__":
    main()
