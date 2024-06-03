from home.home_plan import home_plan, get_room_sensors, get_room_actuators
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, OutdoorTemperatureSensor
from home.actuator import AC, Heater, Curtain, Window, NotificationSender
from home.config import TEMP_LOW, TEMP_HIGH, HUMIDITY_LOW, HUMIDITY_HIGH, LIGHT_INTENSITY_LOW, LIGHT_INTENSITY_HIGH

def ensure_comfort():
    home = home_plan()
    for room in home:
        sensors = get_room_sensors(home, room.name)
        actuators = get_room_actuators(home, room.name)

        temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        humidity_sensor = next((sensor for sensor in sensors if isinstance(sensor, HumiditySensor)), None)
        light_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)
        outdoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, OutdoorTemperatureSensor)), None)

        window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
        curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)
        ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
        heater = next((actuator for actuator in actuators if isinstance(actuator, Heater)), None)
        notifier = next((actuator for actuator in actuators if isinstance(actuator, NotificationSender)), None)

        if temp_sensor and window and ac and heater:
            temp_sensor.turn_on() # Turn on the sensor
            temp = temp_sensor.get_reading()
            if temp < TEMP_LOW:
                # outdoor_temp_sensor.turn_on()# Turn on the outdoor sensor
                # if outdoor_temp_sensor.get_reading() > temp:
                #     window.turn_on()
                # else:
                    heater.turn_on()
            elif temp > TEMP_HIGH:
                # outdoor_temp_sensor.turn_on()# Turn on the outdoor sensor
                # if outdoor_temp_sensor.get_reading() < temp:
                #     window.turn_on()
                # else:
                    ac.turn_on()

        if humidity_sensor and window:
            humidity_sensor.turn_on()
            humidity = humidity_sensor.get_reading()
            if humidity < HUMIDITY_LOW or humidity > HUMIDITY_HIGH:
                window.turn_on()

        if light_sensor and curtain and notifier:
            light_sensor.turn_on()
            light = light_sensor.get_reading()
            if light < LIGHT_INTENSITY_LOW:
                if curtain.get_status() == "off":
                    curtain.turn_on()
                else:
                    notifier.notification_sender("The room is too dark even with the curtain open.")
            elif light > LIGHT_INTENSITY_HIGH:
                curtain.turn_off()

if __name__ == "__main__":
    ensure_comfort()