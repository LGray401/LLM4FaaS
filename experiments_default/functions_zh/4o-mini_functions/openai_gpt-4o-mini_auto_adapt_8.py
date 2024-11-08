# Based on your functional description and the provided source code, I will create the `function.py` file for your smart home project. This file will include a main function that manipulates the sensors and actuators as per your requirements.
# 
# ### `function.py`

# function.py
from home.home_plan import home_plan
from home.actuator import Heater, Humidifier, Light
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor

def main():
    # Create a home plan
    home = home_plan()
    
    # Define the room to operate on (you can change this as needed)
    room_name = "LivingRoom"  # Example room name

    # Get the relevant sensors and actuators from the room
    room = next((room for room in home if room.name == room_name), None)

    if room is None:
        print(f"Room {room_name} not found.")
        return

    temperature_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
    humidity_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, HumiditySensor)), None)
    light_sensor = next((sensor for sensor in room.sensors if isinstance(sensor, LightIntensiveSensor)), None)

    heater = next((actuator for actuator in room.actuators if isinstance(actuator, Heater)), None)
    humidifier = next((actuator for actuator in room.actuators if isinstance(actuator, Humidifier)), None)
    light = next((actuator for actuator in room.actuators if isinstance(actuator, Light)), None)

    # Set temperature to 17 degrees Celsius
    if heater and temperature_sensor:
        heater.set_target_temperature(17)
        temperature_sensor.turn_on()
        current_temp = temperature_sensor.get_reading()
        if current_temp is not None:
            heater.adjust_temperature(current_temp)

    # Check and maintain humidity
    if humidity_sensor and humidifier:
        humidity_sensor.turn_on()
        current_humidity = humidity_sensor.get_reading()
        if current_humidity is not None and HUMIDITY_LOW <= current_humidity <= HUMIDITY_HIGH:
            print("Humidity is normal.")
        else:
            # Adjust humidity as needed (example: turn on humidifier)
            humidifier.turn_on()
            humidifier.increase_humidity()

    # Turn off the light if the light intensity is detected
    if light_sensor and light:
        light_sensor.turn_on()
        current_light_intensity = light_sensor.get_reading()
        if current_light_intensity is not None and current_light_intensity > LIGHT_INTENSITY_LOW:
            light.turn_off()

if __name__ == "__main__":
    main()