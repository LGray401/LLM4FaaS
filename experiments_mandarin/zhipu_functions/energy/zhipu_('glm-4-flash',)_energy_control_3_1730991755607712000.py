# Based on your functional description "开窗关空调" (Open the window and turn off the air conditioner), and the provided source code, I will now provide you with the `function.py` file located in the `functions` folder.
# 
# This `function.py` will contain the main function that will open the window and turn off the air conditioner based on the current temperature and humidity.

# functions/function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor
from home.actuator import Window, AC
from home_plan import home

def main():
    # Get the indoor temperature and humidity sensors
    indoor_temp_sensor = get_room_sensors(home, "LivingRoom")[0]  # Assuming the sensor is in the LivingRoom
    humidity_sensor = get_room_sensors(home, "LivingRoom")[1]  # Assuming the sensor is in the LivingRoom

    # Check the current temperature and humidity
    current_temp = indoor_temp_sensor.get_reading()
    current_humidity = humidity_sensor.get_reading()

    # Define thresholds for temperature and humidity
    temp_threshold = 20  # Celsius
    humidity_threshold = 50  # Percentage

    # If the temperature is above the threshold, open the window and turn off the AC
    if current_temp > temp_threshold:
        print(f"Temperature is high: {current_temp}°C. Opening the window and turning off the AC.")
        logger.info(f"Temperature is high: {current_temp}°C. Opening the window and turning off the AC.")

        # Open the window
        living_room_window = get_room_actuators(home, "Window")[0]  # Assuming the window is in the LivingRoom
        living_room_window.turn_on()

        # Turn off the AC
        living_room_ac = get_room_actuators(home, "AC")[0]  # Assuming the AC is in the LivingRoom
        living_room_ac.turn_off()

    # If the humidity is above the threshold, turn off the AC
    elif current_humidity > humidity_threshold:
        print(f"Humidity is high: {current_humidity}%.")
        logger.info(f"Humidity is high: {current_humidity}%.")

        # Turn off the AC
        living_room_ac = get_room_actuators(home, "AC")[0]  # Assuming the AC is in the LivingRoom
        living_room_ac.turn_off()

    else:
        print(f"Temperature and humidity are within acceptable limits.")
        logger.info(f"Temperature and humidity are within acceptable limits.")

# Run the main function
if __name__ == "__main__":
    main()