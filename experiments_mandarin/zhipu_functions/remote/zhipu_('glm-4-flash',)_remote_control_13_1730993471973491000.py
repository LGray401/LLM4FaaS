# # function.py

from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, SmokeSensor, \
    OutdoorTemperatureSensor
from home.actuator import Heater, AC, Curtain, Humidifier
from home_plan import home_plan

def main():
    # Create the home plan
    home = home_plan()

    # Initialize actuators and sensors
    # Example: Heater
    living_room_heater = home[0].actuators[10]  # Assuming the 11th actuator in LivingRoom is the heater
    living_room_heater.set_target_temperature(22)  # Set target temperature to 22 degrees Celsius

    # Example: AC
    living_room_ac = home[0].actuators[11]  # Assuming the 12th actuator in LivingRoom is the AC
    living_room_ac.set_target_temperature(22)  # Set target temperature to 22 degrees Celsius

    # Example: Humidifier
    living_room_humidifier = home[0].actuators[-1]  # Assuming the last actuator in LivingRoom is the humidifier
    living_room_humidifier.increase_humidity()  # Increase humidity

    # Example: Light
    living_room_light = home[0].actuators[2]  # Assuming the 3rd actuator in LivingRoom is the light
    living_room_light.set_brightness_level("high")  # Set light to high brightness

    # Example: Curtain
    living_room_curtain = home[0].actuators[3]  # Assuming the 4th actuator in LivingRoom is the curtain
    living_room_curtain.turn_on()  # Open the curtain

    # Example: Temperature and Humidity Sensors
    living_room_temp_sensor = get_room_sensors(home, "LivingRoom")[0]  # Assuming the first sensor in LivingRoom is the temperature sensor
    living_room_humidity_sensor = get_room_sensors(home, "LivingRoom")[1]  # Assuming the second sensor in LivingRoom is the humidity sensor

    # Print the sensor readings
    print(f"Living Room Temperature: {living_room_temp_sensor.get_reading()}°C")
    print(f"Living Room Humidity: {living_room_humidity_sensor.get_reading()}%")

if __name__ == "__main__":
    main()