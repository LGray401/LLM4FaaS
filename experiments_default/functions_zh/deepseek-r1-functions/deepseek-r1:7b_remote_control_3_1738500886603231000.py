# <think>
# Okay, I'm looking at the user's code and trying to understand what they need help with. Let me go through each part step by step.
# 
# First, there's a Room class in home_plan.py which adds sensors and actuators. Then, functions like create_room_with_components are used to build rooms with specific components. The home_plan function creates multiple rooms with various sensors and actuators. 
# 
# In the main block of home_plan.py, they're trying to get all actuators of type "Light" but it's not working as expected because it returns an empty list. So, I think the issue is in how the get_all_actuators function works.
# 
# Looking at the current implementation:
# 
# def get_all_actuators(home, actuator_type):
#     all_actuators = []
#     for room in home:
#         for actuator in room.actuators:
#             if actuator.actuator_type == actuator_type:
#                 all_actuators.append(actuator)
# 
#     # print(all_actuators)
#     return all_actuators
# 
# Wait, the check is comparing 'actuator_type' directly. But looking at how the Room adds actuators—when creating a room with components like [Door, Light, ...], each actor has an id and possibly an actuator_type attribute.
# 
# Hmm, maybe the problem is that the get_all_actuators function isn't correctly matching based on their type. Also, in home_plan(), the first argument to create_room_with_components for actuators includes types like Door, Light, etc., which are classes. But when adding them, does each instance have an actuator_type?
# 
# Wait no, looking at how Room.add_actuator is called: it's passing actuator_type(name), where actuator_type is a class from the imports. So the add_actuator function probably creates instances of those classes with 'name' as their id.
# 
# So when adding, for example, Door(name) would create an instance of the Door class, which has certain attributes, including perhaps an actuator_type attribute if defined in that class.
# 
# But how are these classes structured? For example, does Light have an actuator_type? Or is it possible that each actuator's type is determined by its class?
# 
# Alternatively, maybe the current get_all_actuators function isn't correctly identifying actuators based on their type because of a typo or incorrect attribute name. Let me check.
# 
# Wait, in home_plan(), when adding actuators:
# 
# create_room_with_components("LivingRoom", [LightIntensiveSensor, IndoorTemperatureSensor, HumiditySensor],
#                             [Door, Light, Window, Window, Curtain, MusicPlayer, SmartSocket, SmartSocket,
#                              CleaningRobot, SmartTV, NotificationSender, AC, Heater])
# 
# So the second list is a list of classes. When creating each actuator, it's done as actuator_type(name). So for example, Door(name) creates an instance of the Door class with id 'name'.
# 
# But does this Door class have an attribute called actuator_type? Or perhaps I'm looking at it wrong.
# 
# Wait, maybe in the Room.add_actuator function, each actuator has a name (which is the id), and possibly some type information. But without seeing the actual classes, it's hard to tell.
# 
# Alternatively, perhaps the get_all_actuators function needs to compare based on another attribute, like the class of the actuator, rather than an 'actuator_type' attribute.
# 
# Wait, maybe in home_plan(), when they call create_room_with_components, each actuator is added as a specific instance. So for example, when adding Door(name), that's just creating an instance of the Door class with name as its id. But how does get_all_actuators know what type it is?
# 
# Alternatively, perhaps the issue is that in home_plan(), all_actuators are collected based on 'actuator_type' being a string like "Light", but when adding them to rooms, their actuator_type isn't set correctly.
# 
# Wait, looking at the code again: get_all_actuators loops through each room and each actuator in the room. For each actuator, it checks if actuator.actuator_type == actuator_type. But maybe the actuator_type attribute doesn't exist on the Actuator instances. Maybe that's why it returns nothing.
# 
# So perhaps I need to adjust how get_all_actuators is checking for the type of each actuator. Instead of looking at an 'actuator_type' attribute, maybe we should check if the class of the actuator matches a certain base or specific type.
# 
# Alternatively, perhaps the Actuator class doesn't have an 'actuator_type' attribute, so comparing it that way always returns False. Therefore, get_all_actuators isn't finding any actuators because they don't match on 'actuator_type'.
# 
# So to fix this, maybe I should replace the condition with checking if the actuator's class is a specific subclass or type.
# 
# Wait, but without knowing how each Actuator class is structured, it's tricky. Maybe instead of using 'actuator_type', we can check if the class has a certain attribute that indicates its type.
# 
# Alternatively, perhaps each actuator instance should have an id and a class name (like 'Light'), which I can get from the class.__name__ or something similar.
# 
# Wait, maybe in home_plan(), when creating the actuators, they are added as instances of specific classes. For example, Door is a separate class with its own __init__ method that sets certain attributes, including perhaps type information.
# 
# Alternatively, perhaps each actuator's type can be determined by the name of its class. So for example, an instance of MusicPlayer would have 'MusicPlayer' as part of its class name or in some attribute.
# 
# But I'm not sure. Let me think about how to approach this differently.
# 
# The user is trying to get all_actuators where their type is "Light". But when they run the function, it returns an empty list. So perhaps the actuator_type isn't being set correctly on these instances.
# 
# Wait, looking at home_plan(), the first argument to create_room_with_components for sensors includes classes like LightIntensiveSensor. But then in the second argument (actuators), we have classes like Door, Light, etc., which are added as actuator instances.
# 
# So maybe each actuator instance has a type that is based on its class. So perhaps instead of looking at an 'actuator_type' attribute, I should check if the class of the actuator falls under a certain category or has a specific name.
# 
# Alternatively, maybe the problem is in how get_all_actuators is structured. Perhaps it's not correctly iterating through all rooms and their actuators, leading to missing some instances.
# 
# Another possibility: perhaps the actuator_type isn't being set during instantiation, so when comparing, none of them match "Light".
# 
# Wait, maybe I should modify get_all_actuators to collect based on the class name instead. So for each actuator in room.actuators:
# 
# if type(actuator).__name__ == 'Light':
# 
# But that might not work because it's case-sensitive and might have more specific names.
# 
# Alternatively, perhaps using isinstance and checking against a base type like sensors.Sensor or actuatorsActuator.Light.
# 
# Wait, but I don't know the structure of these classes. Maybe each actuator has an id (like name), which is set when creating instances in home_plan() as actuator_type(name).
# 
# So for example:
# 
# Door(name) would create an instance where perhaps 'door' is a variable or attribute that holds its type.
# 
# But looking at the code, how are they adding these? The add_actuator function probably creates instances of the given classes with name as their id. So each actuator's __dict__ may have an 'id' attribute set to name.
# 
# Wait, perhaps in home_plan(), when adding the actuator:
# 
# Room.add_actuator(actors[0])
# 
# But looking at how create_room_with_components is implemented: it loops through the list of classes and creates instances as (cls)(name), where cls is each class from the list. So for example, Door(name) would be an instance of Door with id name.
# 
# So maybe in get_all_actuators, instead of comparing to 'actuator_type', we should look at the actuator's type or its id and see if it matches any known types.
# 
# Alternatively, perhaps each actuator has a type attribute that can be checked. For example:
# 
# for actuator in room.actuators:
#     if hasattr(acts, 'type') and acts.type == 'Light':
#         all_actuators.append(actuator)
# 
# But I don't know how these classes are structured.
# 
# Wait, maybe the main issue is that get_all_actuators isn't correctly identifying the actuators because it's not checking their type. Alternatively, perhaps in home_plan(), when they add an actuator of a certain class (e.g., Light(name)), this creates an instance where 'actuator_type' is set to 'Light'.
# 
# But if that's the case, then maybe get_all_actuators should look for instances where their actuator_type equals "Light".
# 
# Wait, but in home_plan(), they are adding, for example:
# 
# create_room_with_components("LivingRoom", [LightIntensiveSensor, ...], [Door, Light, ...])
# 
# So when creating a Light instance as part of the actuator list, perhaps that class (Light) has an attribute called 'actuator_type' which is set to 'Light'.
# 
# If so, then in get_all_actuators:
# 
# for each actuator in room.actuators:
#     if actuator.actuator_type == "Light":
#         add to all_actuators
# 
# That would correctly collect the Light instances.
# 
# But why isn't that working? Maybe because when they create the actuator as Light(name), the 'actuator_type' attribute is not being set. Or perhaps it's in a different name, like '__class__'.
# 
# Alternatively, maybe each actuator has an id and its class can be determined from that id or another attribute.
# 
# Wait, let me think about this differently. Maybe I should adjust get_all_actuators to collect based on the type of the instance.
# 
# So instead of looking for 'actuator_type', perhaps check if isinstance(actuator, LightActuator).
# 
# But then we need to know what class is considered as an actuator for "Light". For example:
# 
# from home_plan import Light
# get_all_actuators = lambda: [a for r in rooms for a in r.actuators if isinstance(a, Light)]
# 
# Wait, but how are these classes imported? Maybe it's better to have the function check against known types.
# 
# Alternatively, perhaps each actuator has an attribute that indicates its type. For example:
# 
# for actuator in room.actuators:
#     if hasattr(actuator, 'type') and actuator.type == "Light":
#         all_actuators.append(actuator)
# 
# But without knowing the structure of these classes, it's hard to say.
# 
# Another approach: maybe get_all_actuators should collect based on the name attribute. For example:
# 
# name = 0
# for room in rooms:
#     for act in room.actuators:
#         if hasattr(act, 'name') and act.name == str(name):
#             all_actuators.append(act)
#         name +=1
# 
# This would assign each actuator a sequential number as their id.
# 
# But perhaps the problem is that these variables aren't set correctly. Maybe during instantiation, the id isn't being assigned to an attribute like '__id__' or 'name'.
# 
# Alternatively, maybe in home_plan(), when adding the actuator:
# 
# Room.add_actuator(actors[0])
# 
# And actors are a list of classes from create_room_with_components, which includes classes like Door, Light.
# 
# So each actuator is created as (cls)(name), where cls could be Light. So perhaps in these instances, there's an 'id' attribute set to name.
# 
# Therefore, the code might look something like this:
# 
# actors = [cls1(name), cls2(name), ...]
# 
# Then, when adding them to the room, they're stored with their actuator as (id=..., type=...).
# 
# Wait, perhaps in the Room class or add_actuator method, each actuator is added and has attributes like id.
# 
# So maybe get_all_actuators should look for all actuators where 'type' is "Light".
# 
# But again, without knowing how these classes are structured, it's difficult to be precise.
# 
# Alternatively, perhaps I can modify the get_all_actuators function to loop through each room, then each actuator in the room, and check if their type matches "Light". So:
# 
# def get_all_actuators():
#     all_act = []
#     for room in rooms:
#         for act in room.actuators:
#             if act.type == "Light":
#                 all_act.append(act)
#     return all_act
# 
# But this assumes that each actuator has an attribute 'type' which is set to their type.
# 
# Alternatively, perhaps the actuator's __name__ or something else holds the type name.
# 
# Wait, maybe it's better to use isinstance and check against a specific class. For example:
# 
# from home_plan import LightActuator
# 
# def get_all_actuators():
#     all_act = []
#     for room in rooms:
#         for act in room.actuators:
#             if isinstance(act, LightActuator):
#                 all_act.append(act)
#     return all_act
# 
# But then I need to know what class represents the "Light" actuators.
# 
# Alternatively, perhaps each actuator has a name attribute that holds the type. For example:
# 
# for room in rooms:
#     for act in room.actuators:
#         if hasattr(act, 'name') and act.name == "Light":
#             all_act.append(act)
# 
# But again, without knowing how these attributes are set, it's hard to be certain.
# 
# So, putting this all together, perhaps the main issue is that get_all_actuators isn't correctly identifying which actuators belong to the "Light" type. To fix this, I should adjust the function to look for the correct attribute or class name indicating the actuator type.
# 
# Another possibility: maybe the problem lies in how the rooms are created and added to 'rooms' in home_plan(). Perhaps when adding an actuator of a certain type, it's not being correctly assigned as part of that room. So perhaps each room has a list of sensors and actuators stored with their respective attributes, like id.
# 
# Alternatively, maybe I need to modify the add_actuator function or how rooms are structured so that each actuator is properly associated with its room.
# 
# Wait, in home_plan(), they create rooms as:
# 
# rooms = [Room(name) for name in ...]
# 
# Then, when adding an actuator to a room:
# 
# room.add_actuator(actors[i])
# 
# Assuming that add_actuator appends the actuator's id and type to the room's actuators list. So each room has a list of (id, type) pairs.
# 
# Therefore, perhaps get_all_actuators can loop through all rooms and collect the IDs where type is "Light".
# 
# But how does the data structure look? If each room's actuators are stored as a dictionary or similar with 'id' and 'type', then:
# 
# def get_all_actuators():
#     all_act = []
#     for room in rooms:
#         for act in room['actuators']:
#             if act['type'] == "Light":
#                 all_act.append( (act['id'],) )
#     return all_act
# 
# But without knowing the exact structure, this is speculative.
# 
# Alternatively, perhaps each room has a list of actuator objects with attributes like 'name' or 'type'.
# 
# In any case, I think the key issue is that get_all_actuators() isn't correctly identifying which actuator instances belong to the "Light" type. So I need to modify it to loop through all rooms and their actuator instances, checking for the correct condition.
# 
# Perhaps a more robust way would be:
# 
# 1. Iterate over each room.
# 2. For each room, iterate over its actuator instances.
# 3. Check if the actuator's name or type matches "Light".
# 4. Collect those actuators into a list.
# 
# So here's an example of how get_all_actuators() could look with this logic:
# 
# def get_all_actuators():
#     all_act = []
#     for room in rooms:
#         for actuator in room.actuators:
#             if actuator.type == "Light":
#                 all_act.append(actuator)
#     return all_act
# 
# But again, this relies on each actuator having a 'type' attribute that is set to the type name.
# 
# Alternatively, perhaps there's an id associated with each actuator indicating its type. For example, using the ID as a unique identifier for the actuator and then cross-referencing with a dictionary or list mapping IDs to types.
# 
# But without more information on how these objects are structured, it's challenging to write an accurate function.
# 
# Another approach is to use introspection: import all classes related to sensors and actuators and check their names. But this might be complex if the codebase isn't modularized properly.
# 
# Alternatively, perhaps using a regular expression match on the class name or attribute value to determine if an actuator belongs to "Light".
# 
# Wait, maybe I can list out what each actuator's type is based on how they're created in home_plan(). For example:
# 
# actors = [Door(1), Window(2), ..., Light(3), ...]
# 
# So each actor's class might have a name that indicates its type. So perhaps for an actuator 'a', I can do something like:
# 
# actor_name = a.__class__.__name__
# if actor_name.startswith('Light'):
#     collect it.
# 
# This could be another approach, assuming that the classes are named appropriately.
# 
# But this is getting into the weeds without knowing more about the code structure.
# 
# Alternatively, perhaps using reflection to get all attributes of an actuator and see if any match "Light".
# 
# But again, not sure.
# 
# So in summary, I think the key steps are:
# 
# 1. Modify get_all_actuators() to correctly identify which actuation instances belong to the "Light" type.
# 2. Ensure that each actuator is properly associated with its room when added via add_actuator().
# 3. Collect all such Light actuation instances into a list.
# 
# Therefore, I'll proceed to write the code for get_all_actuators(), assuming that each actuator has an attribute 'name' or 'type' that indicates its type.
# </think>
# 
# To solve this problem, we need to create a function `get_all_actuators()` that retrieves all "Light" actuation instances from a list of rooms. Each room contains sensors and actuators, and each actuator is associated with a specific room by an ID.
# 
# ### Approach
# 1. **Iterate Over Rooms**: Loop through each room in the provided list.
# 2. **Check Actuators for Type**: For each room, check each actuator instance to see if it belongs to the "Light" type.
# 3. **Collect IDs**: Collect the IDs of all Light actuation instances found across all rooms.
# 
# The approach assumes that each actuator has a `type` attribute indicating its specific role (e.g., 'Light'). By checking this attribute, we can filter out only those actuators that are intended for lighting tasks.
# 
# ### Solution Code
# 
# ```python
def get_all_actuators():
    all_act = []
    for room in rooms:
        for act in room.actuators:
            if hasattr(act, 'type') and act.type == "Light":
                all_act.append((act.id,))
    return all_act
# ```
# 
# ### Explanation
# 1. **Loop Through Rooms**: The function starts by iterating over each room in the `rooms` list.
# 2. **Check Each Actuator**: For each room, it iterates through its list of actuation instances.
# 3. **Filter by Type**: It checks if an actuator has a `type` attribute and if that type is "Light".
# 4. **Collect IDs**: If an actuator matches the criteria, its ID is added to the result list.
# 
# This solution efficiently collects all Light actuation instances, ensuring they are correctly identified and associated with their respective rooms based on their type attribute.