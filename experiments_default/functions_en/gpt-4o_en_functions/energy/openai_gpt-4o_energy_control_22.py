# Based on your functional description and the provided source code files, I'll create a `function.py` file to handle the required functionality: 
# 
# - Monitoring the kitchen smoke levels to control the smoke alarm.
# - Controlling the air conditioner based on indoor temperature.
# - Managing the sensor light based on occupancy.
# 
# Here's the `function.py` file:

# function.py
import time
from home.sensor import SmokeSensor, IndoorTemperatureSensor, LightIntensiveSensor
from home.actuator import AC, Light, NotificationSender
from home.home_plan import home_plan, get_room_sensors, get_room_actuators

class SmartHomeController:
    def __init__(self, home):
        self.home = home
        self.kitchen_sensors = get_room_sensors(self.home, "Kitchen")
        self.kitchen_actuators = get_room_actuators(self.home, "Kitchen")
        
        self.living_room_sensors = get_room_sensors(self.home, "LivingRoom")
        self.living_room_actuators = get_room_actuators(self.home, "LivingRoom")

    def monitor_kitchen_smoke(self):
        smoke_sensor = next((sensor for sensor in self.kitchen_sensors if isinstance(sensor, SmokeSensor)), None)
        notification_sender = next((actuator for actuator in self.kitchen_actuators if isinstance(actuator, NotificationSender)), None)
        
        if not smoke_sensor or not notification_sender:
            print("Smoke sensor or NotificationSender not found in the kitchen.")
            return
        
        smoke_sensor.turn_on()
        notification_sender.turn_on()
        
        smoke_level = smoke_sensor.get_reading()
        if smoke_level and smoke_level > 50:
            notification_sender.notification_sender("Smoke level exceeds the standard in the kitchen!")

    def monitor_temperature(self):
        temp_sensor = next((sensor for sensor in self.living_room_sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        ac = next((actuator for actuator in self.living_room_actuators if isinstance(actuator, AC)), None)
        
        if not temp_sensor or not ac:
            print("Temperature sensor or AC not found in the living room.")
            return
        
        temp_sensor.turn_on()
        ac.turn_on()

        temperature = temp_sensor.get_reading()
        if temperature:
            if temperature < 20:
                ac.turn_off()
            elif temperature > 25:
                ac.turn_on()

    def monitor_light(self):
        light_sensor = next((sensor for sensor in self.living_room_sensors if isinstance(sensor, LightIntensiveSensor)), None)
        light = next((actuator for actuator in self.living_room_actuators if isinstance(actuator, Light)), None)
        
        if not light_sensor or not light:
            print("Light sensor or Light not found in the living room.")
            return
        
        light_sensor.turn_on()
        light.turn_on()

        light_intensity = light_sensor.get_reading()
        if light_intensity and light_intensity < 950:
            light.turn_on()
        else:
            light.turn_off()

    def run(self):
        while True:
            self.monitor_kitchen_smoke()
            self.monitor_temperature()
            self.monitor_light()
            time.sleep(5)

if __name__ == "__main__":
    home = home_plan()
    controller = SmartHomeController(home)
    controller.run()