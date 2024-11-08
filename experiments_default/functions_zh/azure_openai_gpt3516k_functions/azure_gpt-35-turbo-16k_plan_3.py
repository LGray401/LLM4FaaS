# Here is the `function.py` file for your smart home project. It contains the main function and imports the necessary modules and functions from the other code files.

from home_plan import home_plan, get_room_actuators, get_room_sensors, get_all_actuators, get_all_sensors
from actuator import Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, SmartSocket, Door, CleaningRobot, SmartTV
from sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, OutdoorTemperatureSensor

def main():
    # Create the home plan
    home = home_plan()

    # Retrieve the actuators and sensors for a specific room
    room_name = "LivingRoom"
    actuators = get_room_actuators(home, room_name)
    sensors = get_room_sensors(home, room_name)

    # Perform actions based on the functional description
    for sensor in sensors:
        if isinstance(sensor, LightIntensiveSensor):
            reading = sensor.get_reading()
            if reading > 900:
                for actuator in actuators:
                    if isinstance(actuator, Light):
                        actuator.turn_off()

    room_name = "Bedroom"
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if isinstance(actuator, Window) or isinstance(actuator, Curtain):
            actuator.close()

    room_name = "LivingRoom"
    actuators = get_room_actuators(home, room_name)
    for actuator in actuators:
        if isinstance(actuator, Curtain):
            actuator.open()

    # Perform additional actions based on your project requirements
    # ...
    
if __name__ == "__main__":
    main()