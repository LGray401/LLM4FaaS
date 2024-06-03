
### Preparation
Hi~ I would like to get a function code from you based on my current project setup. The project is based on smart home scenario.
Here are the three necessary code files and I will provide the function description to you in the next message.

### prompt without window checking

I would like to have an always comfort home from the temperature, humidity and light intensity perspectives.
For the temperature:  you can use the AC or heater to adjust room temperature if there exists in the room based on the sensor readings.
For the humidity: you can use the humidifier if it is too wet or dry in the room.
For the light intensive: when it is too bright, then close the curtain; when it is too dark inside, then open the curtian. If the curtain is currently open, then send me a message about this situation.

### result
```
Traceback (most recent call last):
  File "/Users/minghe/llm4faas/functions/copilot_auto_adapt_without_window.py", line 44, in <module>
    comfort_home()
  File "/Users/minghe/llm4faas/functions/copilot_auto_adapt_without_window.py", line 23, in comfort_home
    if temperature < TEMP_LOW and heater:
TypeError: '<' not supported between instances of 'NoneType' and 'int'
IndoorTemperature sensor in LivingRoom is currently OFF. Cannot get reading.
```
1. cannot get sensor readings ❎ need to turn on the sensor first.
2. so, cannot compare NoneType with int ❎

3. modify the code to turn on the sensor first before getting the reading:
   1) temperature does not change when using AC/Heater even we have implementation in the actuator.py
   2) open the curtain when it is too bright ❎, need to turn it off
   3) close the curtain when it is too dark ❎, need to turn it on
   4) need to turn on the notification sender before sending the message
   5) check room one by one
   6) I forget to add smoke control in the prompt



   