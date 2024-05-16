<!-- Preparation -->
1. Hi~ I would like to get a function code from you based on my current project setup. I will first provide you the necessary code files and then describe the function I need to you. The project is based on smart home scenario.
2. I will give you three python files: sensor.py, actuator.py and home-plan.py, which shows the distribution of sensors and actuators at home 
3. the three provided python files are in the 'home' folder and the required function should be in the 'functions' folder. 

<!-- prompt 2-->
1.	I need a function that I can control a device or several devices at home remotely by specifying what device is in which room.
<!-- 
=> 
Got it. We can create a function that takes the following parameters:

home: The list of rooms in the home, which contains sensors and actuators.
room_name: The name of the room where the device is located.
device_type: The type of device you want to control.
action: The action you want to perform on the device (e.g., turn on, turn off, set brightness, etc.).
Based on these parameters, the function will locate the specified device in the specified room and perform the specified action on it.

Shall we proceed with implementing this function? 
=>
yes
-->

<!-- result -->
1. the control function only allow user to 'turn on/off' actuators
2. cannot control sensors & cannot call additional actuator functions (it makes sense, we usually only need to turn on/off the actuators.)
3. give example in the sample main function, however, import from a wrong folder, so doesn't work ❎
4. importing right file => works for turn on/off actuators ✅
or
4. interate with chatgpt using error msg twice, got the runnable code.


