### Preparation
1. Hi~ I would like to get a function code from you based on my current project setup. I will first provide you the necessary code files and then describe the function I need to you. The project is based on smart home scenario.
2. I will give you three python files: sensor.py, actuator.py and home-plan.py, which shows the distribution of sensors and actuators at home
3. the three provided python files are in the 'home' folder and the required function should be in the 'functions' folder. 

#### provide 3 python files

### Prompt 1
I need a function that I can control a device or several devices at home remotely by specifying what device is in which room. for the devices have additional mode, please provide the matching feature to control them as well.


### Result

#### For the provided sample main function
Light in LivingRoom does not support different modes.
Heater in Bedroom does not support different modes.
No AC found in Kitchen.


#### manual test ❎
1. this control function switch the actuator's state, not turn on/off. <- similar to Gemini
2. cannot control sensors as well.
3. cannot control multiple devices at once
4. cannot set_brightness for light also for the player