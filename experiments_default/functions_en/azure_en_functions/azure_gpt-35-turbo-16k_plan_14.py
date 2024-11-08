# Sure! Here is the 'function.py' file based on your functional description:

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import NotificationSender, Light

def main():
    # Create home plan
    home = home_plan()

    # Print home plan
    print_home_plan(home)

    # Get room by name
    living_room = get_room(home, "LivingRoom")

    # Get sensors in a room
    living_room_sensors = get_room_sensors(home, "LivingRoom")

    # Get actuators in a room
    living_room_actuators = get_room_actuators(home, "LivingRoom")

    # Get all sensors of a specific type
    temperature_sensors = get_all_sensors(home, "IndoorTemperature")

    # Get all actuators of a specific type
    light_actuators = get_all_actuators(home, "Light")

    # Perform actions using the sensors and actuators
    for sensor in living_room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            temperature = sensor.get_reading()
            if temperature < 20:
                # Turn on the heater in the living room
                for actuator in living_room_actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_on()
        elif isinstance(sensor, HumiditySensor):
            humidity = sensor.get_reading()
            if humidity > 40:
                # Send notification if humidity is high
                for actuator in living_room_actuators:
                    if isinstance(actuator, NotificationSender):
                        actuator.notification_sender("Humidity is high in the living room!")
        elif isinstance(sensor, LightIntensiveSensor):
            light_intensity = sensor.get_reading()
            if light_intensity < 500:
                # Turn on the lights in the living room
                for actuator in living_room_actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_on()

if __name__ == "__main__":
    main()