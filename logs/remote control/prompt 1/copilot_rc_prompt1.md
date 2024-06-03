### preparation are copy-paste from the chatgpt one
1. we list the root architecture in the preparation -> that's why the function imports files at the very beginning (maybe)

### result
1. copilot can easily upload the python files to the chat without using copy-paste.
2. the code can compile, but cannot control the actuators.
3. seems taking longer to give solution, feels like chatgpt is the fastest, gemini is the slowest.




[//]: # (second try with referring files)
### preparation
1. Hi~ I would like to get a function code from you based on my current project setup. The project is based on smart home scenario. 
2. Here are the three necessary code files and I will provide the function description to you in the next message.
3. refer files here

### prompt1 with refer files
I need a function that I can control a device or several devices at home remotely by specifying what device is in which room. for the devices have additional mode, please provide the matching feature to control them as well.

### result by adding reference ❎
1. only give out the function logic and does not provide imports ❎
2. give main function example without asking for it ✅
3. can find room, but not device in that room ❎
4. cannot control actuators even if turning on/off ❎

### result by adding reference again ❎
1. can turnon/off the devices ✅
2. cannot set_brightness()/ music_player()❎

