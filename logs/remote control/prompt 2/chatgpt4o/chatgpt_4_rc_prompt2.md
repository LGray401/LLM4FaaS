### Preparation
Hi~ I would like to get a function code from you based on my current project setup. I will first provide you the necessary code files and then describe the function I need to you. The project is based on smart home scenario.
I will give you three python files: sensor.py, actuator.py and home-plan.py, which shows the distribution of sensors and actuators at home.
the three provided python files are in the 'home' folder and the required function should be in the 'functions' folder.

#### send 3 python files respectively

### Prompt 2
I need a function that I can control a device or several devices at home remotely by specifying what device is in which room.



### Result: cannot compile ❎(easy to fix ✅)
1. generated file cannot compile: the provided function code doesn't import all necessary funcitons, 
=> i.e., need to import 'get_room()' from home-plan.py
2. after importing 'get_room()', the code can compile and run successfully with turning on/off function. ✅
3. does not support the additional actions like 'set brightness level' or 'daily routine' as the actuators supported ❎
=> will return 'invalid operation......'✅ => showing the right error message in the function, it shouldn't, based on the setup.❎
4. the import error for this case can be solved easily by Intellij IDEA. 
=> but for the non-tech people, there is a question mark about if they can solve this.
5. cannot control sensors as well. ❎
6. can control multiple actuators at once. ✅
