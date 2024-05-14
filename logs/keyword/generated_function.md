### keyword triggered function: log in the /logs folder
<!-- Input Prompt -->
<!-- 1.	I would like to have morning routine at 7 am and evening routine at 11 pm every day.
Additionally, I also want to set plans for Home, Away and Movie times.
Here are what I want for each of the plan or routine.
1)	For the morning routine: 
I want to get up at 7am and have a cup of coffee. I also want to listen to the daily news.
 So, at 7am, please open the curtain, turn on the light if it is too dark, play daily news and make a cup of coffee for me.
2)	For the evening routine: 
I want to go to bed at 11pm. So, at 11 pm, please close the curtain, play bedtime music for me. Turn the light to medium level, then turn it off after half an hour.
3)	For the Home plan: 
Please turn on the Livingroom light for me, close Living room curtain, and turn on all sockets.
4)	For the Away plan:
Please turn off all lights at home, close all windows, lock the home door, and start the cleaning robot. Also, turn off all sockets except for the kitchen ones.
5)	For the Movie plan:
Please turn off all lights except for the one or ones in the living room.
And set the light in living room to medium level.
Close the curtain and turn on the TV. -->

1. Home Plan:
	- Turn on Living Room light ✅
	- Close Living Room curtain ❎
	- Turn on all sockets ❎
<!-- Result -->
Executing Home Plan
Light actuator '/Actuator/Light/LivingRoom/1' in LivingRoom is now ON.
Curtain actuator '/Actuator/Curtain/LivingRoom/1' in LivingRoom is now ON.
Light actuator '/Actuator/Light/Kitchen/1' in Kitchen is now ON.
Window actuator '/Actuator/Window/Kitchen/1' in Kitchen is now ON.
Heater actuator '/Actuator/Heater/Kitchen/1' in Kitchen is now ON.
Coffee actuator '/Actuator/Coffee/Kitchen/1' in Kitchen is now ON.
SmartSocket actuator '/Actuator/SmartSocket/Kitchen/1' in Kitchen is now ON.
SmartSocket actuator '/Actuator/SmartSocket/Kitchen/2' in Kitchen is now ON.
SmartSocket actuator '/Actuator/SmartSocket/Kitchen/3' in Kitchen is now ON.
Door actuator '/Actuator/Door/Kitchen/1' in Kitchen is now ON.

2. Away Plan:
	- Turn off all lights ✅
	- Close all windows ✅
	- Lock home door ❎
	- Start cleaning robot ❎
	- turn off all sockets except for the kitchen ones ❎ ✅
<!-- Result -->
<!-- cannot run cleaning robot feature-->
Executing Away Plan
Light actuator in LivingRoom is now OFF.
Light actuator in Bedroom is now OFF.
Light actuator in Kitchen is now OFF.
Light actuator in Bathroom is now OFF.
Window actuator in LivingRoom is now OFF.
Window actuator in LivingRoom is now OFF.
Window actuator in Bedroom is now OFF.
Window actuator in Kitchen is now OFF.
Window actuator in Bathroom is now OFF.
Door actuator '/Actuator/Door/Balcony/1' in Balcony is now ON.
Traceback (most recent call last):
  File "/Users/minghe/llm4faas/functions/new_keyword_test.py", line 142, in <module>
    home_plan_execution(home, "Away")
  File "/Users/minghe/llm4faas/functions/new_keyword_test.py", line 103, in home_plan_execution
    cleaning_robot_actuator.daily_routine()
AttributeError: 'Light' object has no attribute 'daily_routine'

Process finished with exit code 1

3. Movie Plan:
	- Turn off all lights except for the living room one(s) ✅ 
	- Set light level to medium ❎ => need to turn it/them on first
	- Close curtain ❎
	- Turn on TV ✅
<!-- Result -->
Executing Movie Plan
Light actuator in Bedroom is now OFF. 
Light actuator in Kitchen is now OFF.
Light actuator in Bathroom is now OFF.
Light is OFF. Please turn it on before setting the brightness level.
Curtain actuator '/Actuator/Curtain/LivingRoom/1' in LivingRoom is now ON.
SmartTV actuator '/Actuator/SmartTV/LivingRoom/1' in LivingRoom is now ON.

4. Evening Routine: at 11 pm
	- close the curtain ✅
	- play bedtime music ✅
	- turn light to medium level ❎
	- turn it off after half an hour ✅
<!-- Result -->
Evening Routine started at 11:00 PM
Curtain actuator in Bedroom is now OFF.
Music Player in Bedroom is OFF now
MusicPlayer actuator '/Actuator/MusicPlayer/Bedroom/1' in Bedroom is now ON.
Turn it on and Start playing bedtime music list
Light is OFF. Please turn it on before setting the brightness level.
Light actuator in Bedroom is now OFF.

5. Morning routine: at 7 
	- open the curtain ❎
	- turn on the light if it is too dark ❎
	- play daily news ✅
	- make a cup of coffee ❎
<!-- Result -->
Morning Routine started at 7:00 AM
Curtain actuator '/Actuator/Curtain/LivingRoom/1' in LivingRoom is now ON.
Light actuator in LivingRoom current status is off
Light is OFF. Please turn it on before setting the brightness level.
Music Player in LivingRoom is OFF now
MusicPlayer actuator '/Actuator/MusicPlayer/LivingRoom/1' in LivingRoom is now ON.
Turn it on and Start playing daily news list
Traceback (most recent call last):
  File "/Users/minghe/llm4faas/functions/new_keyword_test.py", line 137, in <module>
    morning_routine(home)
  File "/Users/minghe/llm4faas/functions/new_keyword_test.py", line 34, in morning_routine
    coffee_machine_actuator = [actuator for actuator in living_room_actuators if actuator.actuator_type == "Coffee"][0]
IndexError: list index out of range

<!-- Discussion -->

1. all lights have problem with set brightness because the code does not turn on the light first.
2. there is also some misunderstanding for assigning opening/closing the curtain to the turn_on()/ turn_off() function, however, for evening plan the curtain is triggered properly.
3. the morning and evening routines are only triggered by time. 
(I forget to include that in the prompt, i.e., some of 'users' might miss some function points in their prompts as well) 
<!-- details -->
4. evening plan is almost perfect except setting light brightness.
5. morning plan:
	- triggered actuators in the living room because the prompt does not point it out, however it is obvious that it should happend in the bedroom.
	- does check 'if it is too dark', and it for some reason go to set the light brightness.
	- if we do not say 'turn on the coffee' instead saying 'make a cup of coffee' -> ChatGPT cannot understand
6. home plan:
	- it can turn on the light(it only take the first light in the list, maybe because of the home_plan.py file)
	- should close the curtain, but it open it.(may be caused by misunderstanding)
	- it only turn on all sockets in the kitchen not all sockets at home
7. away plan:
	- turn off all lights and close all windows can be combined (but it is not a problem)
	- I would like to lock the home door, but the code called turn_on()
	- I have two cleaning robots in the living room and bedroom seperately, but it only use the living room one.
	- even for the living room cleaning robot, the code found light not robot, so the 'daily routine()' function cannot be called.
	- because the 'robot' part problem, the sockets cannot be controlled
	- after commenting out the robot part code, the socket part is fine.
8. movie plan:
	almost perfect except setting light brightness & controlling curtain.

