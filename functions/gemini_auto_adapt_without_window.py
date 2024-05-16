from home.sensor import Sensor
from home.actuator import Actuator
from home.config import (
    TEMP_LOW,
    TEMP_HIGH,
    HUMIDITY_LOW,
    HUMIDITY_HIGH,
    LIGHT_INTENSITY_LOW,
    LIGHT_INTENSITY_HIGH,
    TEMP_CHANGE_DURATION_WINDOW,
)
from home.notification_sender import NotificationSender  # Import NotificationSender class

def control_home_based_on_sensors(home):
    """
    This function analyzes sensor readings from all rooms and controls actuators
    to maintain a comfortable home environment based on temperature, humidity,
    and light intensity. It also sends notifications for specific situations.

    Args:
        home (list): List of rooms representing the smart home layout.

    Returns:
        None
    """

    for room in home:
        # Get all sensors in the room
        room_sensors = room.get_room_sensors(home)

        # Analyze sensor data and control actuators
        for sensor in room_sensors:
            sensor_type = sensor.sensor_type
            reading = sensor.get_reading()

            if sensor_type == "IndoorTemperature":
                if reading < TEMP_LOW:
                    # Turn on Heater
                    heater = get_room_actuator(home, room.name, "Heater")
                    if heater:
                        heater.turn_on()
                elif reading > TEMP_HIGH:
                    # Turn on AC
                    ac = get_room_actuator(home, room.name, "AC")
                    if ac:
                        ac.turn_on()

            elif sensor_type == "Humidity":
                if reading < HUMIDITY_LOW:
                    # Use humidifier (assuming it's an actuator)
                    humidifier = get_room_actuator(home, room.name, "Humidifier")
                    if humidifier:
                        humidifier.turn_on()
                elif reading > HUMIDITY_HIGH:
                    # Open window for ventilation
                    window = get_room_actuator(home, room.name, "Window")
                    if window:
                        window.turn_on()

            elif sensor_type == "LightIntensive":
                if reading < LIGHT_INTENSITY_LOW:
                    # Turn on Light
                    light = get_room_actuator(home, room.name, "Light")
                    if light:
                        light.turn_on()
                elif reading > LIGHT_INTENSITY_HIGH:
                    # Close curtain
                    curtain = get_room_actuator(home, room.name, "Curtain")
                    if curtain:
                        curtain.turn_on()
                    else:
                        # Send notification if curtain is not available
                        notification_sender = get_room_actuator(home, room.name, "NotificationSender")
                        if notification_sender:
                            message = f"It is too bright in {room.name}. Consider opening curtains manually."
                            notification_sender.notification_sender(message)
                        print(f"** {room.name} - Light Intensity HIGH. No curtain to close.")

        # Check if curtains are already open (optional)
        curtain = get_room_actuator(home, room.name, "Curtain")
        if curtain and curtain.status == "on":
            print(f"** {room.name} - Curtains are currently OPEN.")


def get_room_actuator(home, room_name, actuator_type):
    """
    Helper function to find a specific actuator in a room.

    Args:
        home (list): List of rooms representing the smart home layout.
        room_name (str): Name of the room.
        actuator_type (str): Type of actuator to search for.

    Returns:
        Actuator object or None if not found.
    """

    room = get_room(home, room_name)
    if room:
        return room.get_room_actuators(home)[0]  # Assuming only one actuator of each type per room
    else:
        return None


if __name__ == "__main__":
    home = home_plan()
    control_home_based_on_sensors(home)
