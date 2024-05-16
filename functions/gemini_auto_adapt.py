from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH  # Import thresholds
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor  # Import sensor classes
from home.actuator import Window, AC, Heater, NotificationSender, Curtain  # Import actuator classes
from home.home_plan import home_plan, get_room_sensors, get_room_actuators  # Import functions from home_plan.py


def regulate_climate(room_name):
    """
    Regulates temperature, humidity, and light in a room.

    Args:
        room_name (str): The name of the room to regulate.
    """
    # todo: new added to check other logic
    home = home_plan()

    # Get sensor readings
    # room_sensors = get_room_sensors(room_name)
    # todo: new added to check other logic
    room_sensors = get_room_sensors(home, room_name)
    indoor_temp = None
    humidity = None
    light_intensity = None
    for sensor in room_sensors:
        if sensor.sensor_type == "IndoorTemperature":
            sensor.turn_on()    # todo: new added to check other logic
            indoor_temp = sensor.get_reading()
        elif sensor.sensor_type == "Humidity":
            sensor.turn_on()    # todo: new added to check other logic
            humidity = sensor.get_reading()
        elif sensor.sensor_type == "LightIntensive":
            sensor.turn_on()    # todo: new added to check other logic
            light_intensity = sensor.get_reading()

    # Get room actuators
    # room_actuators = get_room_actuators(room_name)
    # todo: new added to check other logic
    room_actuators = get_room_actuators(home, room_name)
    window = None
    ac = None
    heater = None
    notification_sender = None
    curtain = None
    for actuator in room_actuators:
        if actuator.actuator_type == "Window":
            window = actuator
        elif actuator.actuator_type == "AC":
            ac = actuator
        elif actuator.actuator_type == "Heater":
            heater = actuator
        elif actuator.actuator_type == "NotificationSender":
            notification_sender = actuator
        elif actuator.actuator_type == "Curtain":
            curtain = actuator

    # Regulate temperature
    if indoor_temp is not None:
        if indoor_temp < TEMP_LOW and window:
            window.turn_on()
            print(f"Window opened in {room_name} to increase temperature.")
        elif indoor_temp > TEMP_HIGH and window:
            window.turn_on()
            print(f"Window opened in {room_name} to decrease temperature.")
        elif indoor_temp < TEMP_LOW:
            if heater:
                heater.turn_on()
                print(f"Heater turned on in {room_name} to increase temperature.")
            else:
                print(f"Warning: No heater found in {room_name} to regulate temperature.")
        elif indoor_temp > TEMP_HIGH:
            if ac:
                ac.turn_on()
                print(f"AC turned on in {room_name} to decrease temperature.")
            else:
                print(f"Warning: No AC found in {room_name} to regulate temperature.")

    # Regulate humidity
    # if humidity is not None:
    # Humidity control logic can be implemented similarly to temperature control,
    # considering outdoor humidity and using window to improve indoor condition.

    # Regulate light intensity
    if light_intensity is not None:
        if light_intensity > LIGHT_INTENSITY_HIGH and curtain:
            curtain.turn_on()
            print(f"Curtain closed in {room_name} to decrease light intensity.")
        elif light_intensity < LIGHT_INTENSITY_HIGH and curtain:
            curtain.turn_off()
            print(f"Curtain opened in {room_name} to increase light intensity.")
        elif light_intensity < LIGHT_INTENSITY_HIGH and not curtain:
            if notification_sender:
                message = f"Light intensity in {room_name} is low. Consider opening the curtain."
                notification_sender.notification_sender(message)
                print(f"Sent notification about low light intensity in {room_name}.")


if __name__ == '__main__':

    # Example usage (assuming you have a function to get the room name)
    # room_name = get_room_name()
    regulate_climate("Bedroom")
