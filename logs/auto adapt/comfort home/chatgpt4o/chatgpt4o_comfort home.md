[### Preparation
Hi~ I would like to get a function code from you based on my current project setup.
I will first provide you the necessary code files and then describe the function I need to you. The project is based on smart home scenario.
I will give you four python files: sensor.py, actuator.py, config.py and home-plan.py, which shows the distribution of sensors and actuators at home
the four provided python files are in the 'home' folder and the required function should be in the 'functions' folder.


### Prompts 
I would like to let my home is always comfortable to me from the temperature, humidity and light intensive perspective.
      1)    For the temperature:
            a.    If it is too cold or too hot at home, please first check if it can be compromised by opening window.
            b.    If not, please use the AC or heater
      2)    For the humidity:
            a.    Similar to temperature, if it is too dry or too wet inside, first check the outdoor situation to see if we can improve indoor condition by opening window.
      3)    For the light intensive:
            a.    If it is too bright inside, then close the curtain.
            b.    If it is too dark inside, try open the curtain first. If the curtain is already open, send a message to me.
### Result
      /usr/bin/python3 /Users/minghe/llm4faas/functions/chatgpt4o_auto_adapt.py
      IndoorTemperature sensor in LivingRoom is currently OFF. Cannot get reading.
      IndoorTemperature sensor in Bedroom is currently OFF. Cannot get reading.
      IndoorTemperature sensor in Bathroom is currently OFF. Cannot get reading.
      Traceback (most recent call last):
      File "/Users/minghe/llm4faas/functions/chatgpt4o_auto_adapt.py", line 69, in <module>
      maintain_comfortable_home()
      File "/Users/minghe/llm4faas/functions/chatgpt4o_auto_adapt.py", line 33, in maintain_comfortable_home
      outdoor_humidity_sensors = get_all_sensors(home, "Humidity", room_name="Balcony")
      TypeError: get_all_sensors() got an unexpected keyword argument 'room_name'
      
      Process finished with exit code 1

### discussion
1. cannot collect data because of sensor again..., i.e., need to turn_on sensor before get reading.
2. maybe shorter prompts is better => it incrase the difficulty to understand the task
3. the function try to get both indoor and outdoor temperature and humidity sensors readings

### Result by turn_on sensors
      Traceback (most recent call last):
      File "/Users/minghe/llm4faas/functions/chatgpt4o_auto_adapt_require_turnon_sensor.py", line 90, in <module>
      maintain_comfortable_home()
      File "/Users/minghe/llm4faas/functions/chatgpt4o_auto_adapt_require_turnon_sensor.py", line 43, in maintain_comfortable_home
      outdoor_humidity_sensors = get_all_sensors(home, "Humidity", room_name="Balcony")
      TypeError: get_all_sensors() got an unexpected keyword argument 'room_name'
      
      Process finished with exit code 1

1. have some further problem with get all sensors in the balcony, i.e., the 'get_all_sensors()' does not support add another arugment 'room_name'