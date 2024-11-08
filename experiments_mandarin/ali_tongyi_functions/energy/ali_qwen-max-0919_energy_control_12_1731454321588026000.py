# Based on the provided functional description and source code, I will create a `function.py` file that includes a main function to enable an energy-saving mode. This function will decide whether to turn on the air conditioner (AC) based on the outdoor temperature and humidity.
# 
# ### `functions/function.py`

from home.sensor import OutdoorTemperatureSensor, HumiditySensor
from home.actuator import AC
from home.home_plan import home_plan, get_room_actuators, get_all_sensors
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH

def start_energy_saving_mode():
    # Initialize the home plan
    home = home_plan()

    # Get all outdoor temperature sensors
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")

    # Check if there are any outdoor temperature or humidity sensors
    if not outdoor_temp_sensors:
        print("No outdoor temperature sensors found.")
        return
    if not humidity_sensors:
        print("No humidity sensors found.")
        return

    # Get the readings from the first outdoor temperature and humidity sensor
    outdoor_temp_sensor = outdoor_temp_sensors[0]
    humidity_sensor = humidity_sensors[0]

    # Turn on the sensors if they are off
    if outdoor_temp_sensor.get_status() == "off":
        outdoor_temp_sensor.turn_on()
    if humidity_sensor.get_status() == "off":
        humidity_sensor.turn_on()

    # Get the current outdoor temperature and humidity
    outdoor_temperature = outdoor_temp_sensor.get_reading()
    humidity = humidity_sensor.get_reading()

    # Get all ACs in the home
    acs = get_all_actuators(home, "AC")

    # Check if there are any ACs
    if not acs:
        print("No ACs found in the home.")
        return

    # Determine if the AC should be turned on based on the outdoor conditions
    for ac in acs:
        room_name = ac.room_name
        actuators = get_room_actuators(home, room_name)

        # Check if the AC is already on
        if ac.status == "on":
            print(f"AC in {room_name} is already ON.")
            continue

        # Check the outdoor conditions
        if outdoor_temperature > TEMP_HIGH and humidity > HUMIDITY_HIGH:
            print(f"Turning on AC in {room_name} due to high outdoor temperature and humidity.")
            ac.turn_on()
        elif outdoor_temperature < TEMP_LOW and humidity < HUMIDITY_LOW:
            print(f"Turning on AC in {room_name} due to low outdoor temperature and humidity.")
            ac.turn_on()
        else:
            print(f"AC in {room_name} remains OFF as outdoor conditions are within acceptable range.")

if __name__ == "__main__":
    start_energy_saving_mode()