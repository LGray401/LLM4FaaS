# # functions/comfort_control.py
# from home.home_plan import home_plan
#
# # new added: second try
# from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, OutdoorTemperatureSensor
# from home.actuator import Window, Curtain, AC, Heater, NotificationSender
# # end added
#
# def ensure_comfort():
#     home = home_plan()
#
#     for room in home:
#         sensors = room.sensors
#         actuators = room.actuators
#
#         # Temperature control
#         indoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
#         if indoor_temp_sensor:
#             temperature = indoor_temp_sensor.get_reading()
#             if temperature:
#                 if temperature < 18:  # Example threshold for too cold
#                     # Check if opening window can help
#                     window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
#                     if window:
#                         window.turn_on()
#                     else:
#                         # Use heater
#                         heater = next((actuator for actuator in actuators if isinstance(actuator, Heater)), None)
#                         if heater:
#                             heater.turn_on()
#                 elif temperature > 25:  # Example threshold for too hot
#                     # Check if opening window can help
#                     window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
#                     if window:
#                         window.turn_on()
#                     else:
#                         # Use AC
#                         ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
#                         if ac:
#                             ac.turn_on()
#
#         # Humidity control
#         humidity_sensor = next((sensor for sensor in sensors if isinstance(sensor, HumiditySensor)), None)
#         if humidity_sensor:
#             humidity = humidity_sensor.get_reading()
#             if humidity:
#                 if humidity < 30:  # Example threshold for too dry
#                     # Check if opening window can help
#                     window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
#                     if window:
#                         window.turn_on()
#                 elif humidity > 70:  # Example threshold for too wet
#                     # Check if opening window can help
#                     window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
#                     if window:
#                         window.turn_on()
#
#         # Light intensity control
#         light_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)
#         if light_sensor:
#             light_intensity = light_sensor.get_reading()
#             if light_intensity:
#                 if light_intensity > 800:  # Example threshold for too bright
#                     # Close curtain
#                     curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)
#                     if curtain:
#                         curtain.turn_on()
#                 elif light_intensity < 200:  # Example threshold for too dark
#                     # Open curtain if not already open
#                     curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)
#                     if curtain and curtain.get_status() == "off":
#                         notification_sender = next((actuator for actuator in actuators if isinstance(actuator, NotificationSender)), None)
#                         if notification_sender:
#                             notification_sender.notification_sender("It's too dark inside. I'm opening the curtain.")
#                         curtain.turn_on()
#
# # Example usage
# if __name__ == "__main__":
#     ensure_comfort()



# first try

# from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, OutdoorTemperatureSensor
# from home.actuator import Window, Curtain, AC, Heater, NotificationSender
#
# def ensure_comfort(home):
#     for room in home:
#         sensors = room.sensors
#         actuators = room.actuators
#
#         # Temperature control
#         indoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
#         if indoor_temp_sensor:
#             temperature = indoor_temp_sensor.get_reading()
#             if temperature:
#                 if temperature < 18:  # Example threshold for too cold
#                     # Check if opening window can help
#                     window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
#                     if window:
#                         window.turn_on()
#                     else:
#                         # Use heater
#                         heater = next((actuator for actuator in actuators if isinstance(actuator, Heater)), None)
#                         if heater:
#                             heater.turn_on()
#                 elif temperature > 25:  # Example threshold for too hot
#                     # Check if opening window can help
#                     window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
#                     if window:
#                         window.turn_on()
#                     else:
#                         # Use AC
#                         ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
#                         if ac:
#                             ac.turn_on()
#
#         # Humidity control
#         humidity_sensor = next((sensor for sensor in sensors if isinstance(sensor, HumiditySensor)), None)
#         if humidity_sensor:
#             humidity = humidity_sensor.get_reading()
#             if humidity:
#                 if humidity < 30:  # Example threshold for too dry
#                     # Check if opening window can help
#                     window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
#                     if window:
#                         window.turn_on()
#                 elif humidity > 70:  # Example threshold for too wet
#                     # Check if opening window can help
#                     window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
#                     if window:
#                         window.turn_on()
#
#         # Light intensity control
#         light_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)
#         if light_sensor:
#             light_intensity = light_sensor.get_reading()
#             if light_intensity:
#                 if light_intensity > 800:  # Example threshold for too bright
#                     # Close curtain
#                     curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)
#                     if curtain:
#                         curtain.turn_on()
#                 elif light_intensity < 200:  # Example threshold for too dark
#                     # Open curtain if not already open
#                     curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)
#                     if curtain and curtain.get_status() == "off":
#                         notification_sender = next((actuator for actuator in actuators if isinstance(actuator, NotificationSender)), None)
#                         if notification_sender:
#                             notification_sender.notification_sender("It's too dark inside. I'm opening the curtain.")
#                         curtain.turn_on()
#
# # Example usage
# if __name__ == "__main__":
#     home = home_plan()
#     ensure_comfort(home)


# third try: notify chatgpt that need to turn on sensor before get readings
# functions/comfort_control.py

from home.home_plan import home_plan

# new added: third try
from home.sensor import IndoorTemperatureSensor, HumiditySensor, LightIntensiveSensor, OutdoorTemperatureSensor
from home.actuator import Window, Curtain, AC, Heater, NotificationSender
# end added


def ensure_comfort():
    home = home_plan()

    for room in home:
        sensors = room.sensors
        actuators = room.actuators

        # Turn on sensors
        for sensor in sensors:
            sensor.turn_on()

        # Temperature control
        indoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
        if indoor_temp_sensor:
            temperature = indoor_temp_sensor.get_reading()
            if temperature:
                if temperature < 18:  # Example threshold for too cold
                    # Check if opening window can help
                    window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
                    if window:
                        window.turn_on()
                    else:
                        # Use heater
                        heater = next((actuator for actuator in actuators if isinstance(actuator, Heater)), None)
                        if heater:
                            heater.turn_on()
                elif temperature > 25:  # Example threshold for too hot
                    # Check if opening window can help
                    window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
                    if window:
                        window.turn_on()
                    else:
                        # Use AC
                        ac = next((actuator for actuator in actuators if isinstance(actuator, AC)), None)
                        if ac:
                            ac.turn_on()

        # Humidity control
        humidity_sensor = next((sensor for sensor in sensors if isinstance(sensor, HumiditySensor)), None)
        if humidity_sensor:
            humidity = humidity_sensor.get_reading()
            if humidity:
                if humidity < 30:  # Example threshold for too dry
                    # Check if opening window can help
                    window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
                    if window:
                        window.turn_on()
                elif humidity > 70:  # Example threshold for too wet
                    # Check if opening window can help
                    window = next((actuator for actuator in actuators if isinstance(actuator, Window)), None)
                    if window:
                        window.turn_on()

        # Light intensity control
        light_sensor = next((sensor for sensor in sensors if isinstance(sensor, LightIntensiveSensor)), None)
        if light_sensor:
            light_intensity = light_sensor.get_reading()
            if light_intensity:
                if light_intensity > 800:  # Example threshold for too bright
                    # Close curtain
                    curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)
                    if curtain:
                        curtain.turn_on()
                elif light_intensity < 200:  # Example threshold for too dark
                    # Open curtain if not already open
                    curtain = next((actuator for actuator in actuators if isinstance(actuator, Curtain)), None)
                    if curtain and curtain.get_status() == "off":
                        notification_sender = next((actuator for actuator in actuators if isinstance(actuator, NotificationSender)), None)
                        if notification_sender:
                            notification_sender.notification_sender("It's too dark inside. I'm opening the curtain.")
                        curtain.turn_on()

# Example usage
if __name__ == "__main__":
    ensure_comfort()



