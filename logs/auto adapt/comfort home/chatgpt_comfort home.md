### Preparation
1. Hi~ I would like to get a function code from you based on my current project setup. I will first provide you the necessary code files and then describe the function I need to you. The project is based on smart home scenario.
2. I will give you three python files: sensor.py, actuator.py and home-plan.py, which shows the distribution of sensors and actuators at home 
3. provide 3 python files
4. the three provided python files are in the 'home' folder and the required function should be in the 'functions' folder.  can you provide an improved version?


### Prompts 
I would like to let my home is always comfortable to me from the temperature, humidity and light intensive perspective.
      1)    For the temperature:
            a.    If it is too cold or too hot at home, please first check it can be compemised by opening window.
            b.    If not, please use the AC or heater
      2)    For the humidity:
            a.    Similar to temperature, if it is too dry or too wet inside, first check the outdoor situation to see if we can improve indoor condition by opening window.
      3)    For the light intensive:
            a.    If it is too bright inside, then close the curtain.
            b.    If it is too dark inside, try open the curtain first. If the curtain is already open, send a message to me.
### Result

```
Traceback (most recent call last):
  File "/Users/minghe/llm4faas/functions/new_auto_adapt.py", line 75, in <module>
    ensure_comfort()
  File "/Users/minghe/llm4faas/functions/new_auto_adapt.py", line 13, in ensure_comfort
    indoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
  File "/Users/minghe/llm4faas/functions/new_auto_adapt.py", line 13, in <genexpr>
    indoor_temp_sensor = next((sensor for sensor in sensors if isinstance(sensor, IndoorTemperatureSensor)), None)
NameError: name 'IndoorTemperatureSensor' is not defined
```

1. the generated code does not import class in the provided 3 python files.
2. add the reference from these three files.
```
      IndoorTemperature sensor in LivingRoom is currently OFF. Cannot get reading.
      Humidity sensor in LivingRoom is currently OFF. Cannot get reading.
      LightIntensive sensor in LivingRoom is currently OFF. Cannot get reading.
      IndoorTemperature sensor in Bedroom is currently OFF. Cannot get reading.
      Humidity sensor in Bedroom is currently OFF. Cannot get reading.
      LightIntensive sensor in Bedroom is currently OFF. Cannot get reading.
      Humidity sensor in Kitchen is currently OFF. Cannot get reading.
      IndoorTemperature sensor in Bathroom is currently OFF. Cannot get reading.
      Humidity sensor in Bathroom is currently OFF. Cannot get reading.
      Humidity sensor in Balcony is currently OFF. Cannot get reading.
```
      

### Result without 4. & add importing

```
      IndoorTemperature sensor in LivingRoom is currently OFF. Cannot get reading.
      Humidity sensor in LivingRoom is currently OFF. Cannot get reading.
      LightIntensive sensor in LivingRoom is currently OFF. Cannot get reading.
      IndoorTemperature sensor in Bedroom is currently OFF. Cannot get reading.
      Humidity sensor in Bedroom is currently OFF. Cannot get reading.
      LightIntensive sensor in Bedroom is currently OFF. Cannot get reading.
      Humidity sensor in Kitchen is currently OFF. Cannot get reading.
      IndoorTemperature sensor in Bathroom is currently OFF. Cannot get reading.
      Humidity sensor in Bathroom is currently OFF. Cannot get reading.
      Humidity sensor in Balcony is currently OFF. Cannot get reading.

```
### Result after input 'the sensors need to be turn on  before get readings'
1. need to additionaly import classes from sensor & actuator.py
2. some class can work because the code import the home-plan.py

```
LightIntensive sensor '/Sensor/LightIntensive/LivingRoom/1' in LivingRoom is now ON.
IndoorTemperature sensor '/Sensor/IndoorTemperature/LivingRoom/1' in LivingRoom is now ON.
Humidity sensor '/Sensor/Humidity/LivingRoom/1' in LivingRoom is now ON.
IndoorTemperature reading in LivingRoom: 29.19
Window actuator '/Actuator/Window/LivingRoom/1' in LivingRoom is now ON.
Humidity reading in LivingRoom: 46.64
LightIntensive reading in LivingRoom: 940.84
Curtain actuator '/Actuator/Curtain/LivingRoom/1' in LivingRoom is now ON.
IndoorTemperature sensor '/Sensor/IndoorTemperature/Bedroom/1' in Bedroom is now ON.
Humidity sensor '/Sensor/Humidity/Bedroom/1' in Bedroom is now ON.
LightIntensive sensor '/Sensor/LightIntensive/Bedroom/1' in Bedroom is now ON.
IndoorTemperature reading in Bedroom: 31.96
Window actuator '/Actuator/Window/Bedroom/1' in Bedroom is now ON.
Humidity reading in Bedroom: 6.7
Window actuator '/Actuator/Window/Bedroom/1' in Bedroom is now ON.
LightIntensive reading in Bedroom: 988.91
Curtain actuator '/Actuator/Curtain/Bedroom/1' in Bedroom is now ON.
Humidity sensor '/Sensor/Humidity/Kitchen/1' in Kitchen is now ON.
Smoke sensor '/Sensor/Smoke/Kitchen/1' in Kitchen is now ON.
Humidity reading in Kitchen: 75.29
Window actuator '/Actuator/Window/Kitchen/1' in Kitchen is now ON.
IndoorTemperature sensor '/Sensor/IndoorTemperature/Bathroom/1' in Bathroom is now ON.
Humidity sensor '/Sensor/Humidity/Bathroom/1' in Bathroom is now ON.
IndoorTemperature reading in Bathroom: 30.32
Window actuator '/Actuator/Window/Bathroom/1' in Bathroom is now ON.
Humidity reading in Bathroom: 78.42
Window actuator '/Actuator/Window/Bathroom/1' in Bathroom is now ON.
OutdoorTemperature sensor '/Sensor/OutdoorTemperature/Balcony/1' in Balcony is now ON.
Humidity sensor '/Sensor/Humidity/Balcony/1' in Balcony is now ON.
Humidity reading in Balcony: 39.65
```

1. the code check if we have window at specific room, not the outdoor temperature.
2. the code only check the 'indoor temperature sensor' readings
3. When too bright inside, should close curtain but the code opened the curtaion


