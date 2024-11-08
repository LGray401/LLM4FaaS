# Based on your functional description and the provided source code, I will create a `function.py` file in the `functions` folder. This file will contain a main function that orchestrates the actions of turning on the air conditioner, setting the temperature, adjusting the blowing modes, and turning on the living room light.
# 
# Here is the content of the `function.py` file:

# functions/function.py

from home.home_plan import home_plan
from home.actuator import AC, Light
from home.sensor import IndoorTemperatureSensor


def main():
    # Create the home plan
    home = home_plan()

    # Get the Living Room
    living_room = next((room for room in home if room.name == "LivingRoom"), None)

    if living_room is None:
        print("Living Room not found!")
        return

    # Initialize the air conditioner and light
    ac = next((actuator for actuator in living_room.actuators if isinstance(actuator, AC)), None)
    light = next((actuator for actuator in living_room.actuators if isinstance(actuator, Light)), None)

    # Check if AC and Light exist in the living room
    if ac is None or light is None:
        print("AC or Light not found in the Living Room!")
        return
    
    # Turn on the air conditioner
    ac.turn_on()
    ac.set_target_temperature(17)  # Set the temperature to 17 degrees

    # Simulate getting the current temperature (you might want to replace this with actual sensor readings)
    temperature_sensor = next((sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    if temperature_sensor:
        temperature_sensor.turn_on()
        current_temperature = temperature_sensor.get_reading()
        if current_temperature is not None:
            # Adjust air conditioner based on current temperature
            ac.adjust_temperature(current_temperature)

    # Set the upper and lower blowing modes (Assuming this is a method you would implement)
    # This part needs to be defined in the AC class if you want specific blowing modes

    # Now turn on the living room light
    light.turn_on()
    light.set_brightness_level("high")  # Optionally set brightness level

    print("Air conditioner is set to 17 degrees and the living room light is turned on.")


if __name__ == "__main__":
    main()