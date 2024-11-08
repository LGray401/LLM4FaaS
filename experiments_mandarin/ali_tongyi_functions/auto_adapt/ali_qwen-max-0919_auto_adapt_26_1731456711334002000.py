# Based on your provided functional description and source code, I will create a `function.py` file that includes the main function to control the temperature, humidity, and light intensity according to your requirements. The main function will be placed in the `functions` folder.
# 
# ### Functional Description Recap:
# 1. **Temperature**: Maintain the indoor temperature at 26°C.
# 2. **Humidity**: Maintain the indoor humidity at 60%.
# 3. **Light Intensity**:
#    - Brighter during work.
#    - Dimmer during relaxation.
#    - Off during rest.
# 
# ### `function.py` Implementation:

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Humidifier, Light
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
import time

def maintain_temperature(home, room_name, target_temperature=26):
    room_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    for sensor in room_sensors:
        if isinstance(sensor, IndoorTemperatureSensor):
            current_temperature = sensor.get_reading()
            if current_temperature is not None:
                for actuator in room_actuators:
                    if isinstance(actuator, Heater) or isinstance(actuator, AC):
                        actuator.set_target_temperature(target_temperature)
                        actuator.adjust_temperature(current_temperature)

def maintain_humidity(home, room_name, target_humidity=60):
    room_sensors = get_room_sensors(home, room_name)
    room_actuators = get_room_actuators(home, room_name)

    for sensor in room_sensors:
        if isinstance(sensor, HumiditySensor):
            current_humidity = sensor.get_reading()
            if current_humidity is not None:
                for actuator in room_actuators:
                    if isinstance(actuator, Humidifier):
                        if current_humidity < target_humidity:
                            actuator.increase_humidity()
                        elif current_humidity > target_humidity:
                            actuator.decrease_humidity()

def adjust_light_intensity(home, room_name, activity):
    room_actuators = get_room_actuators(home, room_name)

    for actuator in room_actuators:
        if isinstance(actuator, Light):
            if activity == "work":
                actuator.set_brightness_level("high")
            elif activity == "relax":
                actuator.set_brightness_level("medium")
            elif activity == "rest":
                actuator.turn_off()

def main():
    home = home_plan()

    # Example usage
    room_name = "LivingRoom"
    
    # Turn on all sensors in the room
    room_sensors = get_room_sensors(home, room_name)
    for sensor in room_sensors:
        sensor.turn_on()

    # Turn on all actuators in the room
    room_actuators = get_room_actuators(home, room_name)
    for actuator in room_actuators:
        actuator.turn_on()

    while True:
        # Maintain temperature
        maintain_temperature(home, room_name, target_temperature=26)

        # Maintain humidity
        maintain_humidity(home, room_name, target_humidity=60)

        # Adjust light intensity based on activity
        # You can change the activity as needed
        activity = "work"  # Change to "relax" or "rest" as needed
        adjust_light_intensity(home, room_name, activity)

        # Sleep for a short duration before the next check
        time.sleep(5)

if __name__ == "__main__":
    main()