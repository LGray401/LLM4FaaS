# Based on your functional description and source code files, here's the implementation of the `function.py` file for your smart home project. This file will ensure that the indoor temperature is maintained at 26°C, humidity is maintained at 60%, and light intensity is adjusted based on the activity (work, relax, rest).

# function.py
from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_CHANGE_DURATION_WINDOW
import time

def main():
    home = home_plan()

    # Maintain indoor temperature at 26°C
    target_temperature = 26
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    heaters = get_all_actuators(home, "Heater")
    ac_units = get_all_actuators(home, "AC")

    for heater in heaters:
        heater.set_target_temperature(target_temperature)
        
    for ac in ac_units:
        ac.set_target_temperature(target_temperature)

    for sensor in indoor_temp_sensors:
        sensor.turn_on()

    # Maintain indoor humidity at 60%
    target_humidity = 60
    humidity_sensors = get_all_sensors(home, "Humidity")
    humidifiers = get_all_actuators(home, "Humidifier")

    for sensor in humidity_sensors:
        sensor.turn_on()

    for humidifier in humidifiers:
        humidifier.turn_on()

    # Adjust light intensity based on activity
    lights = get_all_actuators(home, "Light")

    def set_lighting(activity):
        if activity == "work":
            for light in lights:
                light.turn_on()
                light.set_brightness_level("high")
        elif activity == "relax":
            for light in lights:
                light.turn_on()
                light.set_brightness_level("medium")
        elif activity == "rest":
            for light in lights:
                light.turn_off()
        else:
            print("Unknown activity. Valid activities are: work, relax, rest.")

    # Simulating activity changes
    activities = ["work", "relax", "rest"]
    for activity in activities:
        print(f"Setting light for {activity} activity.")
        set_lighting(activity)
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)  # Simulate time passing for each activity

if __name__ == "__main__":
    main()