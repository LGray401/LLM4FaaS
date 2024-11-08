# Certainly! Based on your requirements and the provided source code, I'll create a `function.py` file which will include a main function to maintain the specified conditions for temperature, humidity, and light intensity.
# 
# Here's the `function.py` file:

# functions/function.py
from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.config import TEMP_HIGH, HUMIDITY_HIGH, LIGHT_INTENSITY_HIGH
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import AC, Heater, Humidifier, Light, Curtain

def main():
    # Initialize home plan
    home = home_plan()

    # Iterate through each room in the home
    for room in home:
        print(f"\nChecking room: {room.name}")
        
        # Get sensors and actuators for the room
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)
        
        # Initialize variables to keep track of sensor readings
        temperature_reading = None
        humidity_reading = None
        light_intensity_reading = None

        # Turn on sensors and get readings
        for sensor in sensors:
            sensor.turn_on()
            reading = sensor.get_reading()
            
            if isinstance(sensor, IndoorTemperatureSensor):
                temperature_reading = reading
            elif isinstance(sensor, HumiditySensor):
                humidity_reading = reading
            elif isinstance(sensor, LightIntensiveSensor):
                light_intensity_reading = reading

        # Control temperature
        if temperature_reading is not None:
            for actuator in actuators:
                if isinstance(actuator, AC):
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(temperature_reading)
                elif isinstance(actuator, Heater):
                    actuator.set_target_temperature(TEMP_HIGH)
                    actuator.adjust_temperature(temperature_reading)
        
        # Control humidity
        if humidity_reading is not None:
            for actuator in actuators:
                if isinstance(actuator, Humidifier):
                    if humidity_reading > HUMIDITY_HIGH:
                        actuator.decrease_humidity()
                    else:
                        actuator.increase_humidity()

        # Control light intensity
        if light_intensity_reading is not None:
            for actuator in actuators:
                if isinstance(actuator, Light):
                    if light_intensity_reading < LIGHT_INTENSITY_HIGH:
                        actuator.turn_on()
                    else:
                        actuator.turn_off()
                elif isinstance(actuator, Curtain):
                    if light_intensity_reading > LIGHT_INTENSITY_HIGH:
                        actuator.turn_off()  # Close curtain
                    else:
                        actuator.turn_on()  # Open curtain

if __name__ == "__main__":
    main()