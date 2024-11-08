from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_HIGH, TEMP_LOW, HUMIDITY_HIGH, HUMIDITY_LOW, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger


def turn_on_temperature_sensors(home):
    """Turn on all temperature sensors in the home."""
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    for sensor in temp_sensors:
        sensor.turn_on()
    temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    for sensor in temp_sensors:
        sensor.turn_on()

def turn_on_lights(home, room_name):
    """Turn on all lights in the given room."""
    lights = get_room_actuators(home, room_name)
    for light in lights:
        if light.actuator_type == "Light":
            light.turn_on()
            print(f"Turning on light in {room_name}")
            logger.info(f"Turning on light in {room_name}")
            
def open_windows(home, room_name):
    """Open all windows in the given room."""
    windows = get_room_actuators(home, room_name)
    for window in windows:
        if window.actuator_type == "Window":
            window.turn_on()
            print(f"Opening window in {room_name}")
            logger.info(f"Opening window in {room_name}")
            
def adjust_temperature(home, room_name, target_temperature):
    """Adjust the temperature in the given room using heater/AC."""
    room = get_room(home, room_name)
    if room is not None:
        heaters = get_room_actuators(room, room_name)
        acs = get_room_actuators(room, room_name)
        for heater in heaters:
            if heater.actuator_type == "Heater":
                heater.set_target_temperature(target_temperature)
                print(f"Setting target temperature of heater in {room_name} to {target_temperature}°C")
                logger.info(f"Setting target temperature of heater in {room_name} to {target_temperature}°C")
        for ac in acs:
            if ac.actuator_type == "AC":
                ac.set_target_temperature(target_temperature)
                print(f"Setting target temperature of AC in {room_name} to {target_temperature}°C")
                logger.info(f"Setting target temperature of AC in {room_name} to {target_temperature}°C")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")
        
def check_and_adjust_temperature(home, room_name):
    """Check the temperature in the given room and adjust heater/AC if needed."""
    room = get_room(home, room_name)
    if room is not None:
        temp_sensors = get_room_sensors(room, room_name)
        for temp_sensor in temp_sensors:
            if temp_sensor.sensor_type == "IndoorTemperature":
                current_temperature = temp_sensor.get_reading()
                if current_temperature is not None:
                    if current_temperature < TEMP_LOW:
                        adjust_temperature(home, room_name, TEMP_HIGH)
                    elif current_temperature > TEMP_HIGH:
                        adjust_temperature(home, room_name, TEMP_LOW)
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")
        
def check_and_adjust_humidity(home, room_name):
    """Check the humidity in the given room and adjust humidifier/dehumidifier if needed."""
    room = get_room(home, room_name)
    if room is not None:
        humidity_sensors = get_room_sensors(room, room_name)
        for humidity_sensor in humidity_sensors:
            if humidity_sensor.sensor_type == "Humidity":
                current_humidity = humidity_sensor.get_reading()
                if current_humidity is not None:
                    if current_humidity < HUMIDITY_LOW:
                        # TODO: Increase humidity in the room
                        print(f"Humidity is low in {room_name}. Increase humidity.")
                        logger.info(f"Humidity is low in {room_name}. Increase humidity.")
                    elif current_humidity > HUMIDITY_HIGH:
                        # TODO: Decrease humidity in the room
                        print(f"Humidity is high in {room_name}. Decrease humidity.")
                        logger.info(f"Humidity is high in {room_name}. Decrease humidity.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")
        
def check_and_adjust_light_intensity(home, room_name):
    """Check the light intensity in the given room and adjust lights if needed."""
    room = get_room(home, room_name)
    if room is not None:
        light_intensity_sensors = get_room_sensors(room, room_name)
        for light_intensity_sensor in light_intensity_sensors:
            if light_intensity_sensor.sensor_type == "LightIntensive":
                current_light_intensity = light_intensity_sensor.get_reading()
                if current_light_intensity is not None:
                    if current_light_intensity < LIGHT_INTENSITY_LOW:
                        # TODO: Turn on lights in the room
                        print(f"Light intensity is low in {room_name}. Turn on lights.")
                        logger.info(f"Light intensity is low in {room_name}. Turn on lights.")
                    elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                        # TODO: Turn off lights in the room
                        print(f"Light intensity is high in {room_name}. Turn off lights.")
                        logger.info(f"Light intensity is high in {room_name}. Turn off lights.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")
        
def check_and_adjust_smoke_sensor(home, room_name):
    """Check the smoke sensor in the given room and send notification if needed."""
    room = get_room(home, room_name)
    if room is not None:
        smoke_sensors = get_room_sensors(room, room_name)
        for smoke_sensor in smoke_sensors:
            if smoke_sensor.sensor_type == "Smoke":
                smoke_level = smoke_sensor.get_reading()
                if smoke_level is not None:
                    if smoke_level > 50:
                        # TODO: Send notification to residents
                        print(f"High smoke level detected in {room_name}. Sending notification.")
                        logger.warning(f"High smoke level detected in {room_name}. Sending notification.")
    else:
        print(f"Room {room_name} not found.")
        logger.warning(f"Room {room_name} not found.")

def main():
    """Main function to demonstrate smart home functionality."""
    home = home_plan()

    # Turn on all temperature sensors
    turn_on_temperature_sensors(home)

    # Check and adjust temperature in the Living Room
    check_and_adjust_temperature(home, "LivingRoom")

    # Turn on lights in the Bedroom
    turn_on_lights(home, "Bedroom")

    # Open windows in the Kitchen
    open_windows(home, "Kitchen")

    # Check and adjust humidity in the Bathroom
    check_and_adjust_humidity(home, "Bathroom")

    # Check and adjust light intensity in the Balcony
    check_and_adjust_light_intensity(home, "Balcony")

    # Check and adjust smoke sensor in the Kitchen
    check_and_adjust_smoke_sensor(home, "Kitchen")

    print("Smart home functions executed.")
    logger.info("Smart home functions executed.")

if __name__ == "__main__":
    main()

# This `function.py` file provides several functions to automate basic smart home tasks:

# - **`turn_on_temperature_sensors(home)`:** Turns on all temperature sensors in the house.
# - **`turn_on_lights(home, room_name)`:** Turns on all lights in a specified room.
# - **`open_windows(home, room_name)`:** Opens all windows in a specified room.
# - **`adjust_temperature(home, room_name, target_temperature)`:** Sets the target temperature for the heater/AC in a room.
# - **`check_and_adjust_temperature(home, room_name)`:** Reads the temperature in a room and adjusts the heater/AC to maintain a comfortable range.
# - **`check_and_adjust_humidity(home, room_name)`:** Reads the humidity in a room and triggers actions (not implemented) to adjust humidity levels.
# - **`check_and_adjust_light_intensity(home, room_name)`:** Reads the light intensity in a room and triggers actions (not implemented) to adjust lighting.
# - **`check_and_adjust_smoke_sensor(home, room_name)`:** Reads the smoke sensor value in a room and sends a notification if smoke levels are high.
# - **`main()`:** The main function that demonstrates how to use these functions.

# Remember, this is a basic example. You can expand it with more complex logic, integrations with real-world sensors and actuators, and additional functionalities to build a more sophisticated smart home system.
