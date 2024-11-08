# Based on your functional description and the provided source code, I will create a `function.py` file with a main function that integrates the sensor and actuator components to automate the smart home system according to the specified rules.
# 
# Here's the content for `function.py`:

# function.py
from home.sensor import IndoorTemperatureSensor
from home.actuator import AC, LightIntensiveSensor
from home_plan import home_plan
from config import TEMP_HIGH, LIGHT_INTENSITY_HIGH

def main():
    # Initialize the home plan
    home = home_plan()
    
    # Get all indoor temperature sensors
    indoor_temp_sensors = []
    for room in home:
        indoor_temp_sensors.extend(room.sensors)
    indoor_temp_sensors = [s for s in indoor_temp_sensors if isinstance(s, IndoorTemperatureSensor)]
    
    # Get all AC units
    ac_units = []
    for room in home:
        ac_units.extend(room.actuators)
    ac_units = [a for a in ac_units if isinstance(a, AC)]
    
    # Get all light intensive sensors
    light_intensity_sensors = []
    for room in home:
        light_intensity_sensors.extend(room.sensors)
    light_intensity_sensors = [s for s in light_intensity_sensors if isinstance(s, LightIntensiveSensor)]
    
    # Monitor and control the smart home
    try:
        while True:
            # Check temperature and control AC units
            for sensor in indoor_temp_sensors:
                reading = sensor.get_reading()
                if reading is not None:
                    for ac_unit in ac_units:
                        if reading > TEMP_HIGH:
                            ac_unit.turn_on()
                        else:
                            ac_unit.turn_off()

            # Check light intensity and control curtains
            for sensor in light_intensity_sensors:
                reading = sensor.get_reading()
                if reading is not None and reading > LIGHT_INTENSITY_HIGH:
                    for curtain in get_room_actuators(home, "Curtain"):
                        curtain.turn_on()

            # Sleep for a while before checking again
            time.sleep(60)
    except KeyboardInterrupt:
        print("Smart home automation stopped.")
        for ac_unit in ac_units:
            ac_unit.turn_off()

if __name__ == "__main__":
    main()