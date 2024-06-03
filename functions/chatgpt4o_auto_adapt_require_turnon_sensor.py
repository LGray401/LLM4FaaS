# functions/maintain_comfortable_home.py

from home.home_plan import home_plan, get_room_actuators, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import NotificationSender


def maintain_comfortable_home():
    home = home_plan()

    # Maintain Temperature
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    for sensor in indoor_temp_sensors:
        current_temp = sensor.get_reading()
        if current_temp is None:
            continue
        if current_temp < TEMP_LOW or current_temp > TEMP_HIGH:
            # Check if opening window can help
            windows = get_room_actuators(home, sensor.room_name, "Window")
            outdoor_temp = next((s.get_reading() for s in outdoor_temp_sensors if s.room_name == sensor.room_name), None)
            if outdoor_temp is not None:
                if (current_temp < TEMP_LOW and outdoor_temp > current_temp) or (current_temp > TEMP_HIGH and outdoor_temp < current_temp):
                    for window in windows:
                        window.turn_on()
                else:
                    ac_or_heater = get_room_actuators(home, sensor.room_name, "AC") if current_temp > TEMP_HIGH else get_room_actuators(home, sensor.room_name, "Heater")
                    for device in ac_or_heater:
                        device.turn_on()

    # Maintain Humidity
    indoor_humidity_sensors = get_all_sensors(home, "Humidity")
    outdoor_humidity_sensors = get_all_sensors(home, "Humidity", room_name="Balcony")
    for sensor in indoor_humidity_sensors:
        current_humidity = sensor.get_reading()
        if current_humidity is None:
            continue
        if current_humidity < HUMIDITY_LOW or current_humidity > HUMIDITY_HIGH:
            # Check if opening window can help
            windows = get_room_actuators(home, sensor.room_name, "Window")
            outdoor_humidity = next((s.get_reading() for s in outdoor_humidity_sensors if s.room_name == sensor.room_name), None)
            if outdoor_humidity is not None:
                if (current_humidity < HUMIDITY_LOW and outdoor_humidity > current_humidity) or (current_humidity > HUMIDITY_HIGH and outdoor_humidity < current_humidity):
                    for window in windows:
                        window.turn_on()

    # Maintain Light Intensity
    light_sensors = get_all_sensors(home, "LightIntensive")
    for sensor in light_sensors:
        current_light = sensor.get_reading()
        if current_light is None:
            continue
        curtains = get_room_actuators(home, sensor.room_name, "Curtain")
        if current_light < LIGHT_INTENSITY_LOW:
            for curtain in curtains:
                curtain.turn_on()
            # Check if curtains are already open, send notification if too dark
            if all(curtain.get_status() == "on" for curtain in curtains):
                notifier = get_room_actuators(home, sensor.room_name, "NotificationSender")
                for notification in notifier:
                    notification.turn_on()
                    notification.notification_sender("The room is too dark and the curtains are already open.")
        elif current_light > LIGHT_INTENSITY_HIGH:
            for curtain in curtains:
                curtain.turn_off()


if __name__ == "__main__":
    maintain_comfortable_home()
