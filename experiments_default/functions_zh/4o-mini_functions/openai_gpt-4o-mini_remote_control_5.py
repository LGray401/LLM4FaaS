# Based on your functional description and the provided source code files, I will create a `function.py` file that includes a main function. This function will demonstrate how to use the classes from your smart home project and will integrate the various components you've defined.
# 
# Here's how the `function.py` file will look:

# functions/function.py
from home.home_plan import home_plan, print_home_plan, get_room, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, OutdoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.actuator import Light, AC, Heater, CoffeeMachine, NotificationSender, MusicPlayer

def main():
    # Create the home plan
    home = home_plan()
    
    # Print the home plan
    print_home_plan(home)

    # Example: Get a specific room and its sensors
    room_name = "LivingRoom"
    living_room = get_room(home, room_name)
    
    if living_room:
        print(f"--- Sensors in {room_name} ---")
        sensors = get_room_sensors(home, room_name)
        for sensor in sensors:
            sensor.turn_on()
            sensor.get_reading()
            sensor.turn_off()
        
        # Example: Control actuators in the living room
        print(f"--- Actuators in {room_name} ---")
        actuators = get_room_actuators(home, room_name)
        for actuator in actuators:
            actuator.turn_on()
            if isinstance(actuator, Light):
                actuator.set_brightness_level("high")
            elif isinstance(actuator, AC):
                actuator.set_target_temperature(22)
            elif isinstance(actuator, Heater):
                actuator.set_target_temperature(20)
            elif isinstance(actuator, CoffeeMachine):
                actuator.make_coffee("Espresso")
            actuator.get_status()

    # Example: Get all sensors of a specific type
    print("--- All Indoor Temperature Sensors ---")
    indoor_temp_sensors = get_all_sensors(home, 'IndoorTemperature')
    for sensor in indoor_temp_sensors:
        sensor.turn_on()
        print(sensor.get_reading())
        sensor.turn_off()

if __name__ == "__main__":
    main()