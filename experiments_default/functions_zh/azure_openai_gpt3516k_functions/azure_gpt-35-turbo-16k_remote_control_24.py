# Sure! I've created the `function.py` file for your smart home project. You can find it in the 'functions' folder. Here's the code:

from home.sensor import LightIntensiveSensor
from home.actuator import Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

def main():
    home = home_plan()
    room_name = "Bedroom"
    sensor_type = "LightIntensive"
    actuator_type = "Light"

    room_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    if room_sensors and room_actuators:
        for sensor in room_sensors:
            if isinstance(sensor, LightIntensiveSensor):
                sensor.turn_off()

        for actuator in room_actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
    else:
        print("Room or components not found.")


if __name__ == "__main__":
    main()