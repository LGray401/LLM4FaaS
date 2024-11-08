# Certainly! Here is the code for the 'function.py' file based on your functional description and the provided source code files:

from home.home_plan import home_plan, get_room_actuators, get_room_sensors, print_home_plan

def main():
    # Create the home plan
    home = home_plan()

    # Print the home plan
    print_home_plan(home)
    
    # Get the kitchen room
    kitchen = get_room_actuators(home, "Kitchen")
    
    # Get the kitchen sensors
    kitchen_sensors = get_room_sensors(home, "Kitchen")
    
    # Handle kitchen functions
    handle_kitchen_smoke_alarm(kitchen_sensors, kitchen)
    handle_kitchen_temperature_control(kitchen_sensors, kitchen)
    handle_kitchen_light_control(kitchen_sensors, kitchen)

def handle_kitchen_smoke_alarm(sensors, actuators):
    smoke_sensor = [sensor for sensor in sensors if sensor.sensor_type == "Smoke"]
    smoke_sensor = smoke_sensor[0] if len(smoke_sensor) > 0 else None
    smoke_alarm = [actuator for actuator in actuators if actuator.actuator_type == "NotificationSender"]
    smoke_alarm = smoke_alarm[0] if len(smoke_alarm) > 0 else None
    
    if smoke_sensor and smoke_alarm:
        reading = smoke_sensor.get_reading()
        
        if reading > 50:
            smoke_alarm.notification_sender("Kitchen Smoke Alarm: Smoke Level Exceeded!")
        else:
            smoke_alarm.notification_sender("Kitchen Smoke Alarm: Smoke Level Normal")

def handle_kitchen_temperature_control(sensors, actuators):
    indoor_temp_sensor = [sensor for sensor in sensors if sensor.sensor_type == "IndoorTemperature"]
    indoor_temp_sensor = indoor_temp_sensor[0] if len(indoor_temp_sensor) > 0 else None
    ac = [actuator for actuator in actuators if actuator.actuator_type == "AC"]
    ac = ac[0] if len(ac) > 0 else None
    heater = [actuator for actuator in actuators if actuator.actuator_type == "Heater"]
    heater = heater[0] if len(heater) > 0 else None
    
    if indoor_temp_sensor and ac and heater:
        current_temp = indoor_temp_sensor.get_reading()
        
        if current_temp < 20:
            ac.turn_off()
            heater.turn_off()
        elif current_temp > 25:
            ac.turn_on()
            heater.turn_off()
        else:
            ac.turn_off()
            heater.turn_off()

def handle_kitchen_light_control(sensors, actuators):
    light_sensor = [sensor for sensor in sensors if sensor.sensor_type == "LightIntensive"]
    light_sensor = light_sensor[0] if len(light_sensor) > 0 else None
    light = [actuator for actuator in actuators if actuator.actuator_type == "Light"]
    light = light[0] if len(light) > 0 else None
    
    if light_sensor and light:
        reading = light_sensor.get_reading()
        
        if reading > 0:
            light.set_brightness_level("high")
        else:
            light.set_brightness_level("low")

if __name__ == "__main__":
    main()