# Ground Truth Expected Output Request

Given this smart-home requirement, estimate expected console behavior when the function.py is invoked with the correct implementation of the user requirement. Please reason deeply using the Source Code from the Requirement what should be the console output when the requiements is fullfilled.
**Example Ouptut**:
Standard Output:
/Actuator/Light/LivingRoom/1 is turned on.
/Actuator/Light/LivingRoom/2 is turned on.
/Actuator/Light/Bedroom/1 is turned on.
/Actuator/Light/Bedroom/2 is turned on.
/Actuator/Light/Kitchen/1 is turned on.
/Actuator/Light/Bathroom/1 is turned on.
Successfully turned on 6 light(s) in the home.
Standard Error:
Return code: 0

## Requirement

{requirement}

## Allowed Console Line Patterns (smart_home)

Use these as the canonical possible stdout line patterns produced by the shared smart_home runtime.
Only include lines that are required by the given requirement and execution path.

Placeholder legend:
- ACTUATOR_ID: /Actuator/<Type>/<Room>/<N>
- SENSOR_ID: /Sensor/<Type>/<Room>/<N>
- ROOM, MESSAGE, PLAYLIST, CHANNEL, COFFEE_TYPE, LEVEL_NAME: runtime values
- TARGET_TEMP, READING: numeric values
- STATUS_VALUE: runtime status string

Allowed stdout patterns:
- ACTUATOR_ID is turned on.
- ACTUATOR_ID is turned off.
- ACTUATOR_ID current status is on
- ACTUATOR_ID current status is off
- Set the target temperature of ACTUATOR_ID to TARGET_TEMP°C.
- ACTUATOR_ID Start making COFFEE_TYPE
-  ACTUATOR_ID is OFF now
- There is Some Error with the Coffee MachineACTUATOR_ID.
- Lock the door ACTUATOR_ID.
- Unlock the door ACTUATOR_ID.
- Cleaning Robot ACTUATOR_ID is OFF now, Need to Turn it ON First
- Cleaning Robot ACTUATOR_ID Starts Daily Cleaning Routine
- ACTUATOR_ID Finish Daily Cleaning Routine, Will Turn it OFF
- There is Some Error with the Cleaning Robot ACTUATOR_ID.
- Notification Sender ACTUATOR_ID send message: MESSAGE
- Notification Sender ACTUATOR_ID is OFF, please turn it on then send the message again.
- Fail to send the message. There is some error with the Notification Sender.
- ACTUATOR_ID start playing PLAYLIST
- Music Player ACTUATOR_ID is OFF now, Turn it ON First
- Fail to play PLAYLIST, There is some error with the music player.
- Set ACTUATOR_ID light brightness level to LEVEL_NAME_UPPER
- Light ACTUATOR_ID is OFF. Please turn it on before setting the brightness level.
- There is an error with the Light.
- Invalid brightness level: LEVEL_NAME. Available levels are ['low', 'medium', 'high'].
- Start playing CHANNEL on the ACTUATOR_ID in ROOM
- 'ACTUATOR_ID' is OFF now, Need to Turn it ON First.
- Fail to play CHANNEL, There is some error with the TV.
- ACTUATOR_ID Increasing humidity in ROOM
- ACTUATOR_ID Decreasing humidity in ROOM
- 'SENSOR_ID' is now ON.
- SENSOR_ID is now OFF.
- Cannot Get Sensor Reading, SENSOR_ID is Currently OFF. 
- SENSOR_ID reading is: READING
- Status Error with status: STATUS_VALUE
- SENSOR_ID current status is: STATUS_VALUE
- ROOM:
- Sensors:
- - SENSOR_ID
- Actuators:
- - ACTUATOR_ID
- ---Home Plan---
- We find ROOM!
- there is no room called ROOM at home
- there is no Sensor found in ROOM
- there is no Actuator found in ROOM

## Output Format

Return strict XML using exactly this structure:
<ground_truth_output>
	<stdout>...</stdout>
	<stderr>...</stderr>
	<return_code>0</return_code>
</ground_truth_output>

Do not include markdown fences or explanations.
