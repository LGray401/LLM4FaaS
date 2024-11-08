# Based on the functional description you provided and the source code from your smart home project, here is the `function.py` file that will serve as the main entry point for your application. This file will import necessary classes from other modules, simulate readings from sensors, and control actuators based on these readings.

# functions/function.py

from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Heater, AC, Light

def main():
    # Initialize home plan
    home = home_plan()
    
    # Display the home plan
    print_home_plan(home)
    
    # Example room name, adjust as needed
    room_name = "LivingRoom"
    
    # Get the specified room
    room = get_room(home, room_name)
    
    if room:
        # Get sensors in the room
        sensors = get_room_sensors(home, room_name)
        actuators = get_room_actuators(home, room_name)
        
        # Simulating sensor readings
        temp_sensor = next((s for s in sensors if isinstance(s, IndoorTemperatureSensor)), None)
        humidity_sensor = next((s for s in sensors if isinstance(s, HumiditySensor)), None)
        light_sensor = next((s for s in sensors if isinstance(s, LightIntensiveSensor)), None)
        
        if temp_sensor and humidity_sensor and light_sensor:
            # Turn sensors on to get readings
            temp_sensor.turn_on()
            humidity_sensor.turn_on()
            light_sensor.turn_on()
            
            # Get readings
            current_temp = temp_sensor.get_reading()
            current_humidity = humidity_sensor.get_reading()
            current_light = light_sensor.get_reading()
            
            # Display readings
            print(f"Current Temperature: {current_temp}°C")
            print(f"Current Humidity: {current_humidity}%")
            print(f"Current Light Intensity: {current_light} lux")
            
            # Control actuators based on readings
            heater = next((a for a in actuators if isinstance(a, Heater)), None)
            ac = next((a for a in actuators if isinstance(a, AC)), None)
            light = next((a for a in actuators if isinstance(a, Light)), None)

            if heater:
                heater.set_target_temperature(26)  # Target temperature
                heater.adjust_temperature(current_temp)  # Adjust heater based on current temperature
            
            if ac:
                ac.set_target_temperature(24)  # Adjust AC target temperature
                ac.adjust_temperature(current_temp)  # Adjust AC based on current temperature
            
            if light:
                light.set_brightness_level("high" if current_light < 80 else "low")  # Set brightness based on light reading

            # Turn off sensors after reading
            temp_sensor.turn_off()
            humidity_sensor.turn_off()
            light_sensor.turn_off()

if __name__ == "__main__":
    main()