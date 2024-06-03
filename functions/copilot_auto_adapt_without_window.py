from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.actuator import AC, Heater, Curtain, NotificationSender
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def comfort_home():
    home = home_plan()
    for room in home:
        room_sensors = get_room_sensors(home, room.name)
        room_actuators = get_room_actuators(home, room.name)

        temperature_sensor = next((sensor for sensor in room_sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        humidity_sensor = next((sensor for sensor in room_sensors if isinstance(sensor, HumiditySensor)), None)
        light_sensor = next((sensor for sensor in room_sensors if isinstance(sensor, LightIntensiveSensor)), None)

        ac = next((actuator for actuator in room_actuators if isinstance(actuator, AC)), None)
        heater = next((actuator for actuator in room_actuators if isinstance(actuator, Heater)), None)
        curtain = next((actuator for actuator in room_actuators if isinstance(actuator, Curtain)), None)
        notifier = next((actuator for actuator in room_actuators if isinstance(actuator, NotificationSender)), None)

        if temperature_sensor:
            # manual added
            temperature_sensor.turn_on()
            temperature = temperature_sensor.get_reading()
            if temperature < TEMP_LOW and heater:
                heater.turn_on()
            elif temperature > TEMP_HIGH and ac:
                ac.turn_on()

        if humidity_sensor:
            # manual added
            humidity_sensor.turn_on()
            humidity = humidity_sensor.get_reading()
            if humidity < HUMIDITY_LOW or humidity > HUMIDITY_HIGH:
                # Assuming there's a humidifier actuator, turn it on/off based on the humidity level
                pass

        if light_sensor and curtain and notifier:
            light_sensor.turn_on()
            light_intensity = light_sensor.get_reading()
            if light_intensity > LIGHT_INTENSITY_HIGH:
                curtain.turn_on()
                if curtain.get_status() == "on":
                    notifier.notification_sender(f"The curtain in {room.name} is open and the light intensity is high.")
            elif light_intensity < LIGHT_INTENSITY_LOW:
                curtain.turn_off()

if __name__ == "__main__":
    comfort_home()