# Sure, here is the 'function.py' file based on the functional description and the given source code:

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor
from home.actuator import AC

def start_energy_saving_mode():
    outdoor_temp_sensor = OutdoorTemperatureSensor("Outdoor")
    indoor_temp_sensor = IndoorTemperatureSensor("LivingRoom")
    humidity_sensor = HumiditySensor("LivingRoom")
    ac = AC("LivingRoom")

    outdoor_temp = outdoor_temp_sensor.get_reading()
    indoor_temp = indoor_temp_sensor.get_reading()
    humidity = humidity_sensor.get_reading()

    if outdoor_temp is not None and indoor_temp is not None and humidity is not None:
        if outdoor_temp > 30 and humidity > 50:
            ac.turn_off()
            print("Energy saving mode activated. AC is turned off.")
        else:
            ac.turn_on()
            print("Energy saving mode deactivated. AC is turned on.")


if __name__ == "__main__":
    start_energy_saving_mode()