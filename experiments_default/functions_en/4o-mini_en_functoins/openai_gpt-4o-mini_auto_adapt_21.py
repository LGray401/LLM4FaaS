# Based on your functional description and the provided code files, here is a `function.py` file that implements the main function for your smart home project. This file will utilize the sensors and actuators defined in your other files to achieve the desired functionality regarding temperature, humidity, and light intensity.
# 
# ### function.py

from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, LIGHT_INTENSITY_HIGH
from home.actuator import AC, Curtain
from home.sensor import IndoorTemperatureSensor, LightIntensiveSensor

def main():
    # Create the home layout
    home = home_plan()

    # Assuming we are focusing on the LivingRoom for this example
    living_room = next(room for room in home if room.name == "LivingRoom")

    # Get sensors and actuators in the LivingRoom
    temperature_sensors = [sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
    light_sensors = [sensor for sensor in living_room.sensors if isinstance(sensor, LightIntensiveSensor)]
    actuators = living_room.actuators

    # Find the AC actuator
    ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
    curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)

    # Check temperature readings
    for sensor in temperature_sensors:
        sensor.turn_on()  # Ensure the sensor is on
        current_temperature = sensor.get_reading()
        
        if current_temperature is not None:
            # Control the AC based on temperature
            if current_temperature > TEMP_HIGH:
                if ac:
                    ac.set_target_temperature(TEMP_HIGH)
                    ac.adjust_temperature(current_temperature)

    # Check light intensity readings
    for sensor in light_sensors:
        sensor.turn_on()  # Ensure the sensor is on
        current_light_intensity = sensor.get_reading()
        
        if current_light_intensity is not None:
            # Control curtains based on light intensity
            if current_light_intensity > LIGHT_INTENSITY_HIGH:
                if curtain:
                    curtain.turn_on()
                    print(f"Curtains in {living_room.name} are now opened due to high light intensity.")
            else:
                if curtain:
                    curtain.turn_off()
                    print(f"Curtains in {living_room.name} are now closed as light intensity is normal.")

    # Turn off sensors and actuators after checking
    for sensor in temperature_sensors + light_sensors:
        sensor.turn_off()

    if ac:
        ac.turn_off()
    if curtain:
        curtain.turn_off()


if __name__ == "__main__":
    main()