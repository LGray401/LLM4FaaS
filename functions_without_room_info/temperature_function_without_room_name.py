import time

from home.config import TEMP_LOW, TEMP_CHANGE_DURATION_WINDOW
from sensor_without_room_name import IndoorTemperatureSensor, OutdoorTemperatureSensor
from actuator_without_room_name import Heater, AC, Window, simulate_temperature_change


# todo: comfortable home, i.e., not only temperature related + UV + humidity


def temperature_control():
    # sensor and actor instances
    indoor_sensor = IndoorTemperatureSensor()
    outdoor_sensor = OutdoorTemperatureSensor()
    heater = Heater()
    ac = AC()
    window = Window()

    if indoor_sensor.status == "off":
        indoor_sensor.turn_on()
    if outdoor_sensor.status == "off":
        outdoor_sensor.turn_on()

    indoor_temperature = indoor_sensor.get_reading()
    outdoor_temperature = outdoor_sensor.get_reading()

    if indoor_temperature < TEMP_LOW:
        temperature_difference = outdoor_temperature - indoor_temperature
        # too cold inside but outside is warmer
        if temperature_difference > 0:
            window.turn_on()
            print("Too cold inside now, Open window to balance indoor and outdoor temperature.")
            print("Simulating temperature changes after opening window...")
            temp_count = 1
            while temperature_difference > 0 and indoor_temperature < TEMP_LOW:
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                indoor_temperature = simulate_temperature_change(indoor_temperature, "cold_open_window")
                if indoor_temperature > outdoor_temperature:
                    indoor_temperature = outdoor_temperature
                    print(f"Indoor temperature after {temp_count * 5} seconds: {indoor_temperature:.2f} °C")
                    break
                print(f"Indoor temperature after {temp_count * 5} seconds: {indoor_temperature:.2f} °C")
                temp_count = temp_count + 1
            window.turn_off()

    if indoor_temperature < TEMP_LOW:
            print("Heater is turned on.")
            heater.turn_on()
            # temp increase
            heater_count = 1
            while indoor_temperature < TEMP_LOW:
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                indoor_temperature = simulate_temperature_change(indoor_temperature, "turn_on_heater")
                print(f"Indoor temperature after {heater_count * TEMP_CHANGE_DURATION_WINDOW} seconds: {indoor_temperature:.2f} °C")
                heater_count = heater_count + 1
            print("indoor is warm enough, turn Heater off.")
            heater.turn_off()

    elif indoor_temperature > TEMP_HIGH:
        temperature_difference = indoor_temperature - outdoor_temperature
        # too hot inside but outside is cooler
        if temperature_difference > 0:
            window.turn_on()
            print("Too hot inside now, Open window to balance indoor and outdoor temperature.")
            # temperature changes need time
            print("Simulating temperature changes after opening window...")
            # check current indoor temperature every 5 seconds
            temp_count = 1
            while temperature_difference > 0 and indoor_temperature >= TEMP_HIGH:
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                indoor_temperature = simulate_temperature_change(indoor_temperature, "hot_open_window")
                if indoor_temperature < outdoor_temperature:
                    indoor_temperature = outdoor_temperature
                    print(f"Indoor temperature after {temp_count * TEMP_CHANGE_DURATION_WINDOW} seconds: {indoor_temperature:.2f} °C")
                    break
                print(f"Indoor temperature after {temp_count * TEMP_CHANGE_DURATION_WINDOW} seconds: {indoor_temperature:.2f} °C")
                temp_count = temp_count + 1
            window.turn_off()

        if indoor_temperature > TEMP_HIGH:
            print("AC is turned on.")
            ac.turn_on()
            # temp decrease
            ac_count = 1
            while indoor_temperature > TEMP_HIGH:
                time.sleep(TEMP_CHANGE_DURATION_WINDOW)
                indoor_temperature = simulate_temperature_change(indoor_temperature, "turn_on_ac")
                print(f"Indoor temperature after {ac_count * TEMP_CHANGE_DURATION_WINDOW} seconds: {indoor_temperature:.2f} °C")
                ac_count = ac_count + 1
            print("indoor is cool enough, turn AC off.")
            ac.turn_off()

    else:
        print("Temperature is within the comfortable range. No action needed.")

    # turn off sensors
    indoor_sensor.turn_off()
    outdoor_sensor.turn_off()

if __name__ == "__main__":
    temperature_control()
