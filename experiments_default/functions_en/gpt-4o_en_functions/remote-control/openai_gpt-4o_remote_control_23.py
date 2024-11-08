# Let's create the `function.py` file in the `functions` folder with a main function that establishes the network control system. This function will utilize the provided classes and methods from the `sensor.py`, `actuator.py`, `home_plan.py`, and `config.py` files. The main function will create the home plan, start the sensors, and control the actuators based on sensor readings.
# 
# Here's the `function.py`:

# functions/function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor
from home.actuator import Heater, AC, CoffeeMachine, Window, Door, Curtain, CleaningRobot, NotificationSender, MusicPlayer, Light, SmartTV, SmartSocket, Humidifier
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH


def main():
    # Create the home plan
    home = home_plan()

    for room in home:
        print(f"Configuring {room.name}...")

        # Turn on all sensors
        for sensor in room.sensors:
            sensor.turn_on()

        # Get sensor readings and perform actions based on values
        for sensor in room.sensors:
            reading = sensor.get_reading()

            # Act based on sensor type and reading
            if isinstance(sensor, IndoorTemperatureSensor) or isinstance(sensor, OutdoorTemperatureSensor):
                actuators = get_room_actuators(home, room.name)
                for actuator in actuators:
                    if isinstance(actuator, Heater):
                        actuator.set_target_temperature(TEMP_HIGH)
                        actuator.adjust_temperature(reading)
                    elif isinstance(actuator, AC):
                        actuator.set_target_temperature(TEMP_LOW)
                        actuator.adjust_temperature(reading)
            elif isinstance(sensor, HumiditySensor):
                actuators = get_room_actuators(home, room.name)
                for actuator in actuators:
                    if isinstance(actuator, Humidifier):
                        if reading < HUMIDITY_LOW:
                            actuator.turn_on()
                            actuator.increase_humidity()
                        elif reading > HUMIDITY_HIGH:
                            actuator.turn_on()
                            actuator.decrease_humidity()
                        else:
                            actuator.turn_off()
            elif isinstance(sensor, LightIntensiveSensor):
                actuators = get_room_actuators(home, room.name)
                for actuator in actuators:
                    if isinstance(actuator, Light):
                        if reading < LIGHT_INTENSITY_LOW:
                            actuator.turn_on()
                            actuator.set_brightness_level("high")
                        elif reading > LIGHT_INTENSITY_HIGH:
                            actuator.turn_off()
                        else:
                            actuator.set_brightness_level("medium")

    print("Home configuration complete.")

if __name__ == "__main__":
    main()