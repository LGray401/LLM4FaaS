# Based on your functional description of "Energy Saving" and the provided source code for your smart home project, I will create a `function.py` file that incorporates a main function. This function will make use of the existing sensors and actuators to create a simple energy-saving routine, such as adjusting the temperature based on readings and managing light usage based on the light intensity.
# 
# Here's the content for the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, print_home_plan
from home.config import TEMP_LOW, TEMP_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light

def energy_saving_mode(home):
    for room in home:
        print(f"Checking energy saving options in {room.name}...")

        # Check temperature and adjust heating/cooling
        temperature_sensors = [sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        heaters = [actuator for actuator in room.actuators if isinstance(actuator, Heater)]
        ac_units = [actuator for actuator in room.actuators if isinstance(actuator, AC)]

        for sensor in temperature_sensors:
            current_temp = sensor.get_reading()
            if current_temp is not None:
                if current_temp < TEMP_LOW:
                    for heater in heaters:
                        heater.set_target_temperature(TEMP_HIGH)
                        heater.adjust_temperature(current_temp)
                elif current_temp > TEMP_HIGH:
                    for ac in ac_units:
                        ac.set_target_temperature(TEMP_LOW)
                        ac.adjust_temperature(current_temp)

        # Check light intensity and adjust lights
        light_sensors = [sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)]
        lights = [actuator for actuator in room.actuators if isinstance(actuator, Light)]

        for sensor in light_sensors:
            current_light = sensor.get_reading()
            if current_light is not None:
                if current_light < LIGHT_INTENSITY_LOW:
                    for light in lights:
                        light.turn_on()  # Turn on the light if it's too dark
                else:
                    for light in lights:
                        light.turn_off()  # Turn off the light if there's enough light

def main():
    home = home_plan()  # Create home plan with rooms and components
    print_home_plan(home)  # Print the home plan for reference
    energy_saving_mode(home)  # Run the energy saving routine

if __name__ == "__main__":
    main()