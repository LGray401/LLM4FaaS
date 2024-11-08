# Based on your provided functional description and the source code files, I will create a `function.py` that will serve as the main function for your smart home project. This main function will initialize the home plan, and demonstrate how to interact with the sensors and actuators in the system.
# 
# Here is the `function.py` file:

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def main():
    # Initialize home plan
    home = home_plan()
    print_home_plan(home)

    # Example: Interact with a specific room
    room_name = "LivingRoom"
    living_room = get_room(home, room_name)
    
    if living_room:
        # Turn on all sensors and actuators in the living room
        sensors = get_room_sensors(home, room_name)
        actuators = get_room_actuators(home, room_name)
        
        for sensor in sensors:
            sensor.turn_on()
            sensor.get_reading()
            
        for actuator in actuators:
            actuator.turn_on()
            
        # Example: Adjust temperature using Heater and AC based on sensor readings
        indoor_temp_sensors = [sensor for sensor in sensors if sensor.sensor_type == "IndoorTemperature"]
        if indoor_temp_sensors:
            current_temp = indoor_temp_sensors[0].get_reading()
            
            heaters = [actuator for actuator in actuators if actuator.actuator_type == "Heater"]
            acs = [actuator for actuator in actuators if actuator.actuator_type == "AC"]
            
            for heater in heaters:
                heater.set_target_temperature(TEMP_LOW)
                heater.adjust_temperature(current_temp)
                
            for ac in acs:
                ac.set_target_temperature(TEMP_HIGH)
                ac.adjust_temperature(current_temp)

        # Example: Adjust humidity using Humidifier based on sensor readings
        humidity_sensors = [sensor for sensor in sensors if sensor.sensor_type == "Humidity"]
        if humidity_sensors:
            current_humidity = humidity_sensors[0].get_reading()
            
            humidifiers = [actuator for actuator in actuators if actuator.actuator_type == "Humidifier"]
            for humidifier in humidifiers:
                if current_humidity < HUMIDITY_LOW:
                    humidifier.increase_humidity()
                elif current_humidity > HUMIDITY_HIGH:
                    humidifier.decrease_humidity()

        # Example: Set brightness level for lights based on Light Intensive Sensor readings
        light_intensive_sensors = [sensor for sensor in sensors if sensor.sensor_type == "LightIntensive"]
        if light_intensive_sensors:
            current_light_intensity = light_intensive_sensors[0].get_reading()
            
            lights = [actuator for actuator in actuators if actuator.actuator_type == "Light"]
            for light in lights:
                if current_light_intensity < LIGHT_INTENSITY_LOW:
                    light.set_brightness_level("high")
                elif current_light_intensity > LIGHT_INTENSITY_HIGH:
                    light.set_brightness_level("low")
                else:
                    light.set_brightness_level("medium")

if __name__ == "__main__":
    main()