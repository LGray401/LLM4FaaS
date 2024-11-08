# Here is the 'function.py' file based on your functional description and the given source code:

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, NotificationSender, Curtain
from home.home_plan import home_plan, get_all_sensors, get_all_actuators


def main():
    home = home_plan()

    # Get all the sensors
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_sensors = get_all_sensors(home, "LightIntensive")

    # Get all the actuators
    ac_units = get_all_actuators(home, "AC")
    notification_senders = get_all_actuators(home, "NotificationSender")
    curtains = get_all_actuators(home, "Curtain")

    # Check temperature
    for sensor in temperature_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            if reading >= 26:
                for ac in ac_units:
                    ac.set_target_temperature(24)
                    ac.turn_on()

    # Check humidity
    for sensor in humidity_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            if reading < 36:
                for ac in ac_units:
                    ac.turn_on()
                    ac.set_target_temperature(25)

    # Check light intensity
    for sensor in light_sensors:
        reading = sensor.get_reading()
        if reading is not None:
            if reading > 80:
                for curtain in curtains:
                    curtain.open()

    # Send notifications
    for sender in notification_senders:
        sender.notification_sender("Temperature, humidity, or light intensity is out of range.")


if __name__ == "__main__":
    main()