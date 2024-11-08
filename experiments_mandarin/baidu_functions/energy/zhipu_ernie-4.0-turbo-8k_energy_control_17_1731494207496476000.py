# Based on your functional description and the provided source code, I will create a `function.py` file that contains a main function to help manage and control the smart home devices with a focus on energy saving. The main function will incorporate logic to turn on/off devices based on sensor readings to save energy.
# 
# Here is the `function.py` file:

from home.home_plan import home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.logger_config import logger

def energy_saving_routine(home):
    """
    Energy saving routine that adjusts actuators based on sensor readings.
    """
    # Get all temperature sensors
    temp_sensors = get_all_sensors(home, "IndoorTemperature")
    # Get all humidity sensors
    humidity_sensors = get_all_sensors(home, "Humidity")
    # Get all light intensity sensors
    light_sensors = get_all_sensors(home, "LightIntensive")
    
    # Get all heaters and ACs
    heaters = get_all_actuators(home, "Heater")
    acs = get_all_actuators(home, "AC")
    lights = get_all_actuators(home, "Light")
    
    for sensor in temp_sensors:
        room_name = sensor.room_name
        reading = sensor.get_reading()
        if reading is not None:
            # Adjust heaters
            for heater in heaters:
                if heater.room_name == room_name:
                    if reading < TEMP_LOW:
                        if heater.status == "off":
                            heater.turn_on()
                            heater.set_target_temperature(TEMP_LOW)
                    elif reading > TEMP_HIGH:
                        if heater.status == "on":
                            heater.turn_off()
            
            # Adjust ACs
            for ac in acs:
                if ac.room_name == room_name:
                    if reading > TEMP_HIGH:
                        if ac.status == "off":
                            ac.turn_on()
                            ac.set_target_temperature(TEMP_HIGH)
                    elif reading < TEMP_LOW:
                        if ac.status == "on":
                            ac.turn_off()
    
    for sensor in humidity_sensors:
        room_name = sensor.room_name
        reading = sensor.get_reading()
        if reading is not None:
            # Logic for humidity control (e.g., turn on/off humidifiers)
            # Assume we have Humidifier and Dehumidifier as part of Actuators
            humidifiers = get_all_actuators(home, "Humidifier")
            for humidifier in humidifiers:
                if humidifier.room_name == room_name:
                    if reading < HUMIDITY_LOW:
                        if humidifier.status == "off":
                            humidifier.turn_on()
                            humidifier.increase_humidity()
                    elif reading > HUMIDITY_HIGH:
                        if humidifier.status == "on":
                            humidifier.turn_off()
                            # If dehumidifier exists, turn it on (not implemented in the provided code)
    
    for sensor in light_sensors:
        room_name = sensor.room_name
        reading = sensor.get_reading()
        if reading is not None:
            for light in lights:
                if light.room_name == room_name:
                    if reading < LIGHT_INTENSITY_LOW:
                        if light.status == "on":
                            light.turn_off()
                    elif reading > LIGHT_INTENSITY_HIGH:
                        if light.status == "off":
                            light.turn_on()
                            light.set_brightness_level("high")  # Adjust as needed

def main():
    """
    Main function to run the smart home energy saving routine.
    """
    # Initialize the home plan
    home = home_plan()
    
    # Run the energy saving routine
    energy_saving_routine(home)
    
    # Optionally, print the home plan after adjustments
    # for room in home:
    #     room.print_info()

if __name__ == "__main__":
    main()