# Based on the provided functional description and source code, here is a `function.py` file that encapsulates the main logic for managing the smart home based on the rules provided:

# function.py
import time

from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, LightIntensiveSensor
from home.actuator import Heater, AC, Window, Door, Light, Humidifier, SmartSocket

# Load the home plan
home = home_plan()

# Main function
def main():
    try:
        # Continuously check and manage the smart home
        while True:
            # Check if the lights are on, and if not, turn them off
            for room in home:
                for light in room.actuators:
                    if isinstance(light, Light) and light.status == "on":
                        light.turn_off()
                        print(f"Turned off the light in {room.name}")

            # Check if the appliances are on, and if not, turn them off
            for room in home:
                for actuator in room.actuators:
                    if isinstance(actuator, SmartSocket) and actuator.status == "on":
                        actuator.turn_off()
                        print(f"Turned off the smart socket in {room.name}")

            # Check if the heater is on when it's too warm
            for room in home:
                indoor_temp_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
                outdoor_temp_sensor = next((s for s in room.sensors if isinstance(s, OutdoorTemperatureSensor)), None)
                if indoor_temp_sensor and outdoor_temp_sensor:
                    indoor_temp = indoor_temp_sensor.get_reading()
                    outdoor_temp = outdoor_temp_sensor.get_reading()
                    if indoor_temp > TEMP_HIGH and indoor_temp - outdoor_temp < TEMP_CHANGE_DURATION_WINDOW:
                        heater = next((a for a in room.actuators if isinstance(a, Heater)), None)
                        if heater and heater.status == "on":
                            heater.turn_off()
                            print(f"Turned off the heater in {room.name} due to high temperature")

            # Check if the AC is on when it's too cold
            for room in home:
                indoor_temp_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
                if indoor_temp_sensor:
                    indoor_temp = indoor_temp_sensor.get_reading()
                    if indoor_temp < TEMP_LOW:
                        ac = next((a for a in room.actuators if isinstance(a, AC)), None)
                        if ac and ac.status == "off":
                            ac.turn_on()
                            print(f"Turned on the AC in {room.name} due to low temperature")

            # Check if the windows are open when it's too hot
            for room in home:
                indoor_temp_sensor = next((s for s in room.sensors if isinstance(s, IndoorTemperatureSensor)), None)
                light_intensity_sensor = next((s for s in room.sensors if isinstance(s, LightIntensiveSensor)), None)
                if indoor_temp_sensor and light_intensity_sensor:
                    indoor_temp = indoor_temp_sensor.get_reading()
                    light_intensity = light_intensity_sensor.get_reading()
                    if indoor_temp > TEMP_HIGH and light_intensity < LIGHT_INTENSITY_LOW:
                        window = next((a for a in room.actuators if isinstance(a, Window)), None)
                        if window and window.status == "off":
                            window.turn_on()
                            print(f"Opened the window in {room.name} to cool down")

            # Check if the humidifier is on when the humidity is too low
            for room in home:
                humidity_sensor = next((s for s in room.sensors if isinstance(s, HumiditySensor)), None)
                if humidity_sensor:
                    humidity = humidity_sensor.get_reading()
                    if humidity < HUMIDITY_LOW:
                        humidifier = next((a for a in room.actuators if isinstance(a, Humidifier)), None)
                        if humidifier and humidifier.status == "off":
                            humidifier.turn_on()
                            print(f"Turned on the humidifier in {room.name} due to low humidity")

            # Wait for a while before checking again
            time.sleep(10)
    except KeyboardInterrupt:
        print("Smart home system is shutting down.")

if __name__ == "__main__":
    main()