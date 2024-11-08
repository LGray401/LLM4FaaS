# Sure, I'll create the `function.py` file which will contain the main function to manage your smart home project based on the functional description provided. The main functionality will include:
# - Automatically turning on the AC when the temperature rises above 26°C.
# - Managing humidity levels normally.
# - Automatically closing the curtains when the light intensity is high (e.g., during midday sunlight).
# 
# Here is the code for `function.py`:

from home_plan import home_plan, get_all_sensors, get_all_actuators
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, Curtain
import time

def main():
    # Initialize home and get sensors/actuators
    home = home_plan()
    indoor_temp_sensors = get_all_sensors(home, "IndoorTemperature")
    light_intensity_sensors = get_all_sensors(home, "LightIntensive")

    acs = get_all_actuators(home, "AC")
    curtains = get_all_actuators(home, "Curtain")

    while True:
        # Check temperature and control ACs
        for sensor in indoor_temp_sensors:
            sensor.turn_on()
            temp_reading = sensor.get_reading()
            if temp_reading is not None and temp_reading > 26:
                for ac in acs:
                    if ac.room_name == sensor.room_name:
                        ac.set_target_temperature(24)  # Example target temperature
                        ac.adjust_temperature(temp_reading)
            sensor.turn_off()

        # Check light intensity and control curtains
        for sensor in light_intensity_sensors:
            sensor.turn_on()
            light_reading = sensor.get_reading()
            if light_reading is not None and light_reading > 900:
                for curtain in curtains:
                    if curtain.room_name == sensor.room_name:
                        curtain.turn_on()
            sensor.turn_off()

        # Sleep for some time before next check
        time.sleep(60)

if __name__ == "__main__":
    main()