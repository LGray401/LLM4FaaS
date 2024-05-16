### Link
https://g.co/gemini/share/5bf7502eaacb


### Preparation
1. Hi~ I would like to get a function code from you based on my current project setup. I will first provide you the necessary code files and then describe the function I need you to provide.
2. I will send you four code snippets to you in 4 messages and one messages for one file. They are: sensor.py, actuator.py, config.py and home-plan.py. 
3. These 4 python files are in the 'home' folder and the required function should be in the 'functions' folder under the same root with the 'home' folder.
4. I will now send you the function description, and please give me the function code.


### prompt without window checking

I would like to have an always comfort home from the temperature, humidity and light intensity perspectives.
For the temperature:  you can use the AC or heater to adjust room temperature if there exists in the room based on the sensor readings.
For the humidity: you can use the humidifier if it is too wet or dry in the room.
For the light intensive: when it is too bright, then close the curtain; when it is too dark inside, then open the curtian. If the curtain is currently open, then send me a message about this situation.

### result
1. cannot compile because of some wrong imports
2. manually checking:
   1) onle one parater in get_room_sensor() function, however, the function need both the room plan and the room name.
   2) does not turn on the sensor before get reading
   3) add a new get_room_actuator() function to get specific kind of actuator in a specific room.
   4) close the curtain-> turn_on()
   5) in line 82: it checks if the curtain.status is on, then print the curtain is open.
3. but generally it would like to use the current home plan to control the whole home temp & humidity & light intensity