### Preparation
1. Hi~ I would like to get a function code from you based on my current project setup. I will first provide you the necessary code files and then describe the function I need to you. The project is based on smart home scenario.
2. I will give you three python files: sensor.py, actuator.py and home-plan.py, which shows the distribution of sensors and actuators at home 
3. the three provided python files are in the 'home' folder and the required function should be in the 'functions' folder. 
4. provide 3 python files


### prompt without window checking

I would like to have a always comfort home from the temperature, humidity and light intensity perspectives.
For the temperature:  you can use the AC or heater to adjust room temperature if there exists in the room based on the sensor readings.
For the humidity: you can use the humidifier if it is too wet or dry in the room.
For the light intensive: when it is too bright, then close the curtain; when it is too dark inside, then open the curtian. If the curtain is currently open, then send me a message about this situation.

### result
As the code does not turn on sensors before using them, I iterate once and here is the result.

```
LightIntensive sensor '/Sensor/LightIntensive/LivingRoom/1' in LivingRoom is now ON.
IndoorTemperature sensor '/Sensor/IndoorTemperature/LivingRoom/1' in LivingRoom is now ON.
Humidity sensor '/Sensor/Humidity/LivingRoom/1' in LivingRoom is now ON.
IndoorTemperature reading in LivingRoom: 31.07
AC actuator '/Actuator/AC/LivingRoom/1' in LivingRoom is now ON.
Humidity reading in LivingRoom: 35.5
LightIntensive reading in LivingRoom: 962.24
Curtain actuator '/Actuator/Curtain/LivingRoom/1' in LivingRoom is now ON.
LightIntensive sensor in LivingRoom is now OFF.
IndoorTemperature sensor in LivingRoom is now OFF.
Humidity sensor in LivingRoom is now OFF.
IndoorTemperature sensor '/Sensor/IndoorTemperature/Bedroom/1' in Bedroom is now ON.
Humidity sensor '/Sensor/Humidity/Bedroom/1' in Bedroom is now ON.
LightIntensive sensor '/Sensor/LightIntensive/Bedroom/1' in Bedroom is now ON.
IndoorTemperature reading in Bedroom: 27.11
AC actuator '/Actuator/AC/Bedroom/1' in Bedroom is now ON.
Humidity reading in Bedroom: 46.82
LightIntensive reading in Bedroom: 944.98
Curtain actuator '/Actuator/Curtain/Bedroom/1' in Bedroom is now ON.
IndoorTemperature sensor in Bedroom is now OFF.
Humidity sensor in Bedroom is now OFF.
LightIntensive sensor in Bedroom is now OFF.
Humidity sensor '/Sensor/Humidity/Kitchen/1' in Kitchen is now ON.
Smoke sensor '/Sensor/Smoke/Kitchen/1' in Kitchen is now ON.
Humidity reading in Kitchen: 86.74
Humidity sensor in Kitchen is now OFF.
Smoke sensor in Kitchen is now OFF.
IndoorTemperature sensor '/Sensor/IndoorTemperature/Bathroom/1' in Bathroom is now ON.
Humidity sensor '/Sensor/Humidity/Bathroom/1' in Bathroom is now ON.
IndoorTemperature reading in Bathroom: 39.42
Humidity reading in Bathroom: 85.52
IndoorTemperature sensor in Bathroom is now OFF.
Humidity sensor in Bathroom is now OFF.
OutdoorTemperature sensor '/Sensor/OutdoorTemperature/Balcony/1' in Balcony is now ON.
Humidity sensor '/Sensor/Humidity/Balcony/1' in Balcony is now ON.
Humidity reading in Balcony: 38.99
OutdoorTemperature sensor in Balcony is now OFF.
Humidity sensor in Balcony is now OFF.
```

1. The function can compile and will check sensor readings every minutes.
2. The function will turn off the sensors every time got the readings.
3. The operation of curtain still have misunderstandings, similar to the other sceanrio.
4. The temperature does not change after turn on AC or heater.
5. For example, if the temperature becomes fine, and theh AC or heater still on, the function will not turn them off.
6. 