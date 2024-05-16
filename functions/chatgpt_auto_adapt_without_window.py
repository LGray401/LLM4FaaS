import time
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def maintain_home_comfort():
    home = home_plan()

    while True:
        for room in home:
            # Get sensors and actuators for the current room
            sensors = get_room_sensors(home, room.name)
            actuators = get_room_actuators(home, room.name)

            # Turn on sensors
            for sensor in sensors:
                sensor.turn_on()

            # Adjust temperature
            for sensor in sensors:
                if sensor.sensor_type == "IndoorTemperature":
                    temperature = sensor.get_reading()
                    if temperature > 25:  # If temperature is too high
                        for actuator in actuators:
                            if actuator.actuator_type == "AC":
                                actuator.turn_on()
                    elif temperature < 20:  # If temperature is too low
                        for actuator in actuators:
                            if actuator.actuator_type == "Heater":
                                actuator.turn_on()
                    else:
                        for actuator in actuators:
                            if actuator.actuator_type in ["AC", "Heater"]:
                                actuator.turn_off()

            # Adjust humidity (if necessary)
            for sensor in sensors:
                if sensor.sensor_type == "Humidity":
                    humidity = sensor.get_reading()
                    # Add logic to control humidifier/dehumidifier based on humidity

            # Adjust light intensity
            for sensor in sensors:
                if sensor.sensor_type == "LightIntensive":
                    light_intensity = sensor.get_reading()
                    if light_intensity > 800:  # If light intensity is too high
                        for actuator in actuators:
                            if actuator.actuator_type == "Curtain":
                                actuator.turn_on()
                    elif light_intensity < 200:  # If light intensity is too low
                        for actuator in actuators:
                            if actuator.actuator_type == "Curtain":
                                actuator.turn_off()
                    else:
                        for actuator in actuators:
                            if actuator.actuator_type == "Curtain":
                                if actuator.get_status() == "on":
                                    # Send a notification about the curtain status
                                    notification_sender = None
                                    for a in actuators:
                                        if a.actuator_type == "NotificationSender":
                                            notification_sender = a
                                            break
                                    if notification_sender:
                                        notification_sender.notification_sender(f"The curtain in {room.name} is already open.")
                                    break

            # Turn off sensors
            for sensor in sensors:
                sensor.turn_off()

        # Sleep for some time before checking again
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    maintain_home_comfort()
