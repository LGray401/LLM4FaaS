# Based on the functional description and the provided source code, I will create a `function.py` file that performs the following tasks:
# 
# 1. Initializes the home setup using the existing `home_plan` function.
# 2. Retrieves the current readings for temperature, humidity, and light intensity.
# 3. Depending on the readings, it will control actuators such as the Heater or AC for temperature, a Humidifier for humidity, and a Light actuator for light intensity.
# 4. The main function will implement this logic and output the status of the actuators.
# 
# Here is the `function.py` file:

# function.py
from home.home_plan import home_plan
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH
from home.actuator import Heater, AC, Humidifier, Light

def main():
    # Initialize home
    home = home_plan()

    # Example room to check
    room_name = "LivingRoom"
    
    # Get room
    room = next((r for r in home if r.name == room_name), None)

    if room:
        # Get sensors
        temperature_sensors = [s for s in room.sensors if s.sensor_type == "IndoorTemperature"]
        humidity_sensors = [s for s in room.sensors if s.sensor_type == "Humidity"]
        light_sensors = [s for s in room.sensors if s.sensor_type == "LightIntensive"]

        # Get readings
        current_temperature = temperature_sensors[0].get_reading() if temperature_sensors else None
        current_humidity = humidity_sensors[0].get_reading() if humidity_sensors else None
        current_light_intensity = light_sensors[0].get_reading() if light_sensors else None

        # Control temperature
        heater = next((a for a in room.actuators if a.actuator_type == "Heater"), None)
        ac = next((a for a in room.actuators if a.actuator_type == "AC"), None)

        if current_temperature is not None:
            if current_temperature < TEMP_LOW and heater:
                heater.set_target_temperature(TEMP_HIGH)  # Set target temperature to high
                heater.adjust_temperature(current_temperature)
            elif current_temperature > TEMP_HIGH and ac:
                ac.set_target_temperature(TEMP_LOW)  # Set target temperature to low
                ac.adjust_temperature(current_temperature)

        # Control humidity
        humidifier = next((a for a in room.actuators if a.actuator_type == "Humidifier"), None)

        if current_humidity is not None:
            if current_humidity < HUMIDITY_LOW and humidifier:
                humidifier.increase_humidity()
            elif current_humidity > HUMIDITY_HIGH and humidifier:
                humidifier.decrease_humidity()

        # Control light
        light = next((a for a in room.actuators if a.actuator_type == "Light"), None)

        if current_light_intensity is not None:
            if current_light_intensity < LIGHT_INTENSITY_LOW and light:
                light.turn_on()  # Turn on light if it's too dark
            elif current_light_intensity > LIGHT_INTENSITY_HIGH and light:
                light.turn_off()  # Turn off light if it's too bright

    else:
        print(f"Room '{room_name}' not found!")

if __name__ == "__main__":
    main()