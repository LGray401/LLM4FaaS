# Based on your functional description "开窗关空调" (which translates to "Open the window and turn off the air conditioning"), here is a `function.py` file that implements the required functionality. This script will handle the logic of checking the status of the temperature sensor and the air conditioning unit, and it will open the window if needed and turn off the air conditioning.
# 
# Here is the content for `function.py`:

# function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH
from home.actuator import Window, AC
from home.sensor import IndoorTemperatureSensor

def main():
    # Initialize the home with rooms and components
    home = home_plan()

    # Assume we're working with the LivingRoom for this example
    living_room = next((room for room in home if room.name == "LivingRoom"), None)
    
    if living_room:
        # Get the indoor temperature sensor and the AC from the living room
        temperature_sensors = [sensor for sensor in living_room.sensors if isinstance(sensor, IndoorTemperatureSensor)]
        ac_units = [actuator for actuator in living_room.actuators if isinstance(actuator, AC)]
        windows = [actuator for actuator in living_room.actuators if isinstance(actuator, Window)]

        if temperature_sensors and ac_units and windows:
            # Assume we take the first temperature sensor for reading
            temp_sensor = temperature_sensors[0]
            ac_unit = ac_units[0]
            window = windows[0]

            # Get the current temperature reading
            current_temperature = temp_sensor.get_reading()
            
            if current_temperature is not None:
                print(f"Current temperature is: {current_temperature}°C")

                # Check if the temperature is within the specified range
                if current_temperature < TEMP_LOW:
                    print("Temperature is too low. Opening the window.")
                    window.turn_on()  # Open the window (turn on the window actuator)
                    ac_unit.turn_off()  # Turn off the air conditioning
                elif current_temperature > TEMP_HIGH:
                    print("Temperature is too high. Turning off the air conditioning.")
                    ac_unit.turn_off()  # Turn off the air conditioning
                    window.turn_on()  # Optionally open the window
                
                else:
                    print("Temperature is within the acceptable range. No action needed.")

if __name__ == "__main__":
    main()