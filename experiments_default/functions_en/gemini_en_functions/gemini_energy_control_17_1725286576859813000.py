from home.home_plan import home_plan, get_room, get_room_sensors, get_room_actuators, get_all_sensors, \
    get_all_actuators, print_home_plan
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import NotificationSender, Light, Window, Curtain, MusicPlayer, Heater, AC, CoffeeMachine, \
    SmartSocket, Door, \
    CleaningRobot, SmartTV
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH, \
    TEMP_CHANGE_DURATION_WINDOW, DAILY_ROUTINE_DURATION
import time


def save_energy_function():
    # get home plan
    home = home_plan()

    # get all sensors
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    outdoor_temp_sensors = get_all_sensors(home, "OutdoorTemperature")
    humidity_sensors = get_all_sensors(home, "Humidity")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")
    smoke_sensors = get_all_sensors(home, "Smoke")

    # get all actuators
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")
    windows = get_all_actuators(home, "Window")
    curtains = get_all_actuators(home, "Curtain")

    # loop for every 1 second
    while True:
        # get sensor readings
        indoor_temp_readings = []
        for indoor_temp_sensor in indoor_temp_sensors:
            indoor_temp_sensor.turn_on()
            indoor_temp_reading = indoor_temp_sensor.get_reading()
            indoor_temp_readings.append(indoor_temp_reading)
        outdoor_temp_readings = []
        for outdoor_temp_sensor in outdoor_temp_sensors:
            outdoor_temp_sensor.turn_on()
            outdoor_temp_reading = outdoor_temp_sensor.get_reading()
            outdoor_temp_readings.append(outdoor_temp_reading)
        humidity_readings = []
        for humidity_sensor in humidity_sensors:
            humidity_sensor.turn_on()
            humidity_reading = humidity_sensor.get_reading()
            humidity_readings.append(humidity_reading)
        light_intensity_readings = []
        for light_intensity_sensor in light_intensity_sensors:
            light_intensity_sensor.turn_on()
            light_intensity_reading = light_intensity_sensor.get_reading()
            light_intensity_readings.append(light_intensity_reading)
        smoke_readings = []
        for smoke_sensor in smoke_sensors:
            smoke_sensor.turn_on()
            smoke_reading = smoke_sensor.get_reading()
            smoke_readings.append(smoke_reading)

        # adjust actuators based on readings
        for heater in heaters:
            heater.set_target_temperature(TEMP_HIGH)
            heater.adjust_temperature(indoor_temp_reading)
        for ac in acs:
            ac.set_target_temperature(TEMP_LOW)
            ac.adjust_temperature(indoor_temp_reading)
        for light in lights:
            if light_intensity_reading > LIGHT_INTENSITY_HIGH:
                light.turn_off()
            elif light_intensity_reading < LIGHT_INTENSITY_LOW:
                light.turn_on()
                light.set_brightness_level("low")
        for window in windows:
            if indoor_temp_reading > outdoor_temp_reading and indoor_temp_reading > TEMP_HIGH:
                window.turn_on()
            elif indoor_temp_reading < outdoor_temp_reading and indoor_temp_reading < TEMP_LOW:
                window.turn_off()
        for curtain in curtains:
            if light_intensity_reading > LIGHT_INTENSITY_HIGH:
                curtain.turn_on()
            elif light_intensity_reading < LIGHT_INTENSITY_LOW:
                curtain.turn_off()

        # wait for some time
        time.sleep(TEMP_CHANGE_DURATION_WINDOW)

        # print home plan
        print_home_plan(home)


if __name__ == "__main__":
    save_energy_function()

# **Explanation of the code:**

# 1. **Import necessary modules:** Imports modules from `home.home_plan`, `home.sensor`, `home.actuator`, and `home.config`.
# 2. **`save_energy_function()`:**
#    - **Get home plan:** Obtains the `home` object from the `home_plan()` function.
#    - **Get all sensors:** Uses `get_all_sensors()` to retrieve lists of all sensors of different types (indoor/outdoor temperature, humidity, light intensity, smoke).
#    - **Get all actuators:** Uses `get_all_actuators()` to get lists of actuators like heaters, ACs, lights, windows, and curtains.
#    - **Loop for every second:** Uses a `while True` loop to run the energy-saving logic every second.
#    - **Get sensor readings:**
#      - Iterates through each sensor type, turning on the sensors, getting readings, and storing them in lists.
#    - **Adjust actuators based on readings:**
#      - Iterates through each actuator type:
#        - **Heaters:** Sets the target temperature to `TEMP_HIGH` and uses `adjust_temperature()` to turn on/off heaters based on the indoor temperature.
#        - **ACs:** Sets the target temperature to `TEMP_LOW` and uses `adjust_temperature()` to turn on/off ACs based on the indoor temperature.
#        - **Lights:** Turns off lights if the light intensity is above the threshold (`LIGHT_INTENSITY_HIGH`) or sets the brightness to low if below the threshold (`LIGHT_INTENSITY_LOW`).
#        - **Windows:** Opens windows if the indoor temperature is higher than the outdoor temperature and above the threshold (`TEMP_HIGH`), and closes them if the indoor temperature is lower and below the threshold (`TEMP_LOW`).
#        - **Curtains:** Opens curtains if the light intensity is above the threshold (`LIGHT_INTENSITY_HIGH`) and closes them if below the threshold (`LIGHT_INTENSITY_LOW`).
#    - **Wait for some time:** Uses `time.sleep()` to wait for `TEMP_CHANGE_DURATION_WINDOW` seconds before repeating the loop.
#    - **Print home plan:** Prints the current status of the home plan using `print_home_plan()`.
# 3. **`if __name__ == "__main__":`:** This block executes the `save_energy_function()` when the script is run directly (not imported as a module).

# This code demonstrates a basic energy-saving system that adjusts actuators based on sensor readings. It continuously monitors the environment and adjusts the heating, cooling, lighting, and ventilation systems to save energy. 
