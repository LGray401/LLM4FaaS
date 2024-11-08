from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Light, MusicPlayer
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def main():
    """
    This function contains the main logic for your smart home system.
    """

    home = home_plan()  # Create the home plan

    # Get the living room
    living_room = get_room(home, "LivingRoom")

    # Get the living room sensors
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get the living room actuators
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Example logic for temperature control
    for sensor in living_room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature_reading = sensor.get_reading()
            if temperature_reading is not None:
                for actuator in living_room_actuators:
                    if isinstance(actuator, AC) and temperature_reading > TEMP_HIGH:
                        actuator.turn_on()
                    elif isinstance(actuator, Heater) and temperature_reading < TEMP_LOW:
                        actuator.turn_on()

    # Example logic for humidity control
    for sensor in living_room_sensors:
        if isinstance(sensor, HumiditySensor):
            humidity_reading = sensor.get_reading()
            if humidity_reading is not None:
                for actuator in living_room_actuators:
                    if isinstance(actuator, AC) and humidity_reading > HUMIDITY_HIGH:
                        actuator.turn_on()

    # Example logic for light control
    for sensor in living_room_sensors:
        if isinstance(sensor, LightIntensiveSensor):
            light_intensity_reading = sensor.get_reading()
            if light_intensity_reading is not None:
                for actuator in living_room_actuators:
                    if isinstance(actuator, Light) and light_intensity_reading < LIGHT_INTENSITY_LOW:
                        actuator.turn_on()
                    elif isinstance(actuator, Light) and light_intensity_reading > LIGHT_INTENSITY_HIGH:
                        actuator.turn_off()

    # Example logic for playing music
    for actuator in living_room_actuators:
        if isinstance(actuator, MusicPlayer):
            # Check if there is a trigger for playing music (e.g., time of day, presence of people, etc.)
            # If yes, call actuator.play_music()
            pass

    # Example logic for turning on the lights when someone enters the room
    # (You would need additional logic to detect presence using a sensor)
    # for actuator in living_room_actuators:
    #     if isinstance(actuator, Light):
    #         actuator.turn_on()

    # This is just an example. You can extend this logic to handle more complex scenarios, such as:
    # - Turning on lights based on light intensity
    # - Controlling AC based on temperature and humidity
    # - Turning on coffee machine based on time of day
    # - Controlling smart sockets based on various conditions

if __name__ == "__main__":
    main()
