# Based on the functional description and the provided source code, I'll create the `function.py` file that activates the energy-saving mode in the smart home project. This mode will typically involve turning off unnecessary lights and adjusting the temperature settings of HVAC systems (like heaters and air conditioners) based on the current readings from the sensors.
# 
# Here's the `function.py` file:

# functions/function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH

def activate_energy_saving_mode(home):
    for room in home:
        # Turn off all lights in the room
        for actuator in room.actuators:
            if isinstance(actuator, Light):
                actuator.turn_off()
        
        # Adjust HVAC systems based on temperature readings
        current_temp_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        if current_temp_sensor:
            current_temp = current_temp_sensor.get_reading()
            if current_temp is not None:
                for actuator in room.actuators:
                    if isinstance(actuator, Heater):
                        if current_temp < TEMP_LOW:
                            actuator.turn_on()
                        else:
                            actuator.turn_off()
                    elif isinstance(actuator, AC):
                        if current_temp > TEMP_HIGH:
                            actuator.turn_on()
                        else:
                            actuator.turn_off()

def main():
    home = home_plan()
    activate_energy_saving_mode(home)
    print("Energy Saving Mode Activated.")

if __name__ == "__main__":
    main()