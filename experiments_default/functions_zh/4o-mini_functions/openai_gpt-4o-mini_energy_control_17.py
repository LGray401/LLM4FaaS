# Based on your functional description of "节约能源" (energy saving) and the provided code files, I'll create a `function.py` file that integrates the various components of your smart home system to manage energy consumption effectively. This will involve monitoring the sensors and controlling the actuators to optimize energy usage. 
# 
# Here's the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_all_sensors, get_all_actuators
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
import time

def energy_saving_routine(home):
    print("Starting Energy Saving Routine...\n")
    
    for room in home:
        print(f"Checking room: {room.name}")
        
        # Get sensors and actuators in the room
        temperature_sensors = get_all_sensors(home, "IndoorTemperature")
        light_sensors = get_all_sensors(home, "LightIntensive")
        heaters = get_all_actuators(home, "Heater")
        ac_units = get_all_actuators(home, "AC")
        lights = get_all_actuators(home, "Light")
        
        # Check indoor temperature
        for sensor in temperature_sensors:
            sensor.turn_on()  # Ensure the sensor is on
            temperature = sensor.get_reading()
            if temperature is not None:
                print(f"Current temperature in {room.name}: {temperature}°C")
                
                # Control heater or AC based on temperature
                for heater in heaters:
                    heater.set_target_temperature(TEMP_HIGH)
                    heater.adjust_temperature(temperature)
                
                for ac in ac_units:
                    ac.set_target_temperature(TEMP_LOW)
                    ac.adjust_temperature(temperature)

        # Check light intensity
        for sensor in light_sensors:
            sensor.turn_on()
            light_intensity = sensor.get_reading()
            if light_intensity is not None:
                print(f"Current light intensity in {room.name}: {light_intensity} lux")

                # Control lights based on light intensity
                for light in lights:
                    if light_intensity < LIGHT_INTENSITY_LOW:
                        light.turn_on()
                    elif light_intensity > LIGHT_INTENSITY_HIGH:
                        light.turn_off()

        time.sleep(1)  # Simulate time between room checks

    print("\nEnergy Saving Routine Completed.")

def main():
    home = home_plan()
    print_home_plan(home)
    energy_saving_routine(home)

if __name__ == "__main__":
    main()