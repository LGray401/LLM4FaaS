# Based on the functional description and the provided source code, here's a `function.py` file that contains the main function to control the smart home system as per the requirements:

# function.py

from home.home_plan import home_plan, get_room, get_all_sensors, get_all_actuators
from home.sensor import SmokeSensor, IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, Light, SmokeAlarm
import time

def main():
    # Initialize the home plan
    home = home_plan()
    
    while True:
        # Check smoke level in the kitchen
        kitchen = get_room(home, "Kitchen")
        if kitchen:
            smoke_sensors = [sensor for sensor in kitchen.sensors if isinstance(sensor, SmokeSensor)]
            for sensor in smoke_sensors:
                sensor.turn_on()  # Turn on the smoke sensor
                reading = sensor.get_reading()
                if reading is not None and reading > 50:  # Assuming smoke level threshold is 50
                    # Turn on smoke alarm
                    smoke_alarm = next((actuator for actuator in kitchen.actuators if isinstance(actuator, SmokeAlarm)), None)
                    if smoke_alarm and smoke_alarm.status == "off":
                        smoke_alarm.turn_on()
                sensor.turn_off()  # Turn off the smoke sensor to save power

        # Check indoor temperature and control AC
        for room in home:
            temp_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
            acs = [actuator for actuator in room.actuators if isinstance(actuator, AC)]
            for sensor in temp_sensors:
                sensor.turn_on()  # Turn on the temperature sensor
                reading = sensor.get_reading()
                if reading is not None:
                    for ac in acs:
                        if reading < 20:  # Temperature below 20 degrees Celsius
                            if ac.status == "on":
                                ac.turn_off()
                        elif reading > 25:  # Temperature above 25 degrees Celsius
                            if ac.status == "off":
                                ac.turn_on()
                sensor.turn_off()  # Turn off the temperature sensor to save power

        # Check light intensity and control lights
        for room in home:
            light_sensors = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]
            lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]
            for sensor in light_sensors:
                sensor.turn_on()  # Turn on the light sensor
                reading = sensor.get_reading()
                if reading is not None:
                    presence_detected = reading > 300  # Assuming a threshold of 300 lux for presence detection
                    for light in lights:
                        if presence_detected and light.status == "off":
                            light.turn_on()
                        elif not presence_detected and light.status == "on":
                            light.turn_off()
                sensor.turn_off()  # Turn off the light sensor to save power
        
        # Sleep for a while before the next check
        time.sleep(10)

if __name__ == "__main__":
    main()