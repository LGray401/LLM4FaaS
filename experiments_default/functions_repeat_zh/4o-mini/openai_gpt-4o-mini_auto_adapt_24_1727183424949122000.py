# Based on the functional description you provided and the existing code, I will create a `function.py` file that implements the functionality to maintain the indoor temperature, humidity, and light intensity as specified.
# 
# Here's the proposed `function.py` code:

# function.py
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light
from home.home_plan import home_plan
import time


def maintain_environment(home):
    for room in home:
        # Get sensors from the room
        temp_sensor = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)][0]
        humidity_sensor = [sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)][0]
        light_sensor = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)][0]

        # Get actuators from the room
        ac = [actor for actor in room.actuators if isinstance(actor, AC)][0]
        heater = [actor for actor in room.actuators if isinstance(actor, Heater)][0]
        humidifier = [actor for actor in room.actuators if isinstance(actor, Humidifier)][0]
        light = [actor for actor in room.actuators if isinstance(actor, Light)][0]

        # Maintain temperature
        current_temperature = temp_sensor.get_reading()
        if current_temperature is not None:
            if current_temperature > 26:
                ac.set_target_temperature(25)  # Set AC to lower the temperature
                ac.adjust_temperature(current_temperature)
            elif current_temperature < 20:
                heater.set_target_temperature(22)  # Set heater to raise the temperature
                heater.adjust_temperature(current_temperature)

        # Maintain humidity
        current_humidity = humidity_sensor.get_reading()
        if current_humidity is not None:
            if current_humidity > 30:
                humidifier.decrease_humidity()  # Decrease humidity if above 30%

        # Maintain light intensity
        current_light_intensity = light_sensor.get_reading()
        if current_light_intensity is not None:
            if current_light_intensity > 900:
                light.turn_off()  # Turn off light if it's too bright
            elif current_light_intensity < 300:
                light.turn_on()  # Turn on light if it's too dark

        time.sleep(1)  # Wait for a second before next iteration

def main():
    home = home_plan()
    while True:
        maintain_environment(home)

if __name__ == "__main__":
    main()