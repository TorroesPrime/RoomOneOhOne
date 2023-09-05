# room

a 'room' represents a single location in a [locationMap](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/CLS_LocationMap.md).

## fields

### room_id

A UUID compliant string that is created the first-time a given room is instantiated for a particular play through of a particular adventure module. This string will be unique to each play through of the adventure the room is used in.

### name

A string representing the room name. Used to make it easier
to refer to a given room. If no name is supplied, a default name for the room
is created using the dungeon name and how many rooms that have been created for
this play through and incrementing that number by 1.

Example:

“TheWrathOfTheEmperor-0128”

“Lan's Horizon – Main Bridge”

### been_here

a boolean determining if the player has been in this room
before or not.

### desc

a list of strings describing the room. Each item in the list is a progressively more detailed description of the room.

### inventory

An inventory object representing the contents of the room

### light_level

an int representing how well it the room. 0 is total darkness, 10 is "bright day light”

### non_player_characters

A list containing other [character](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/CLS_character.md) objects

### enviroment_type

a list of strings representing different enviroment types that apply to this room.

### exits

a list of exit objects that exist in this room.

## methods

### add_exits(list_of_exits)

takes a list of exit objects, or a single exit object, and adds each of them to the room's exits attribute.

### store_state()

records the current state of the room in preperation for a save game operation.

### restore_state()

takes the data from a save game file to restore agiven state of the room.

### describe()

returns a string describing the room. The content of the string will be modified by the been_here values. If the been_here is true, then the describe only returns a string containing the room name and exit information.

### full_describe()

returns a string containing a full description of the room including the list of exits, the list of contents and NPCs and potential hints for additional hidden items. When the player enters the room, a sight check will be performed. The degree of pass or failure will determine how much additional information is contained in the string assuming the been_here is False.

example:

### leave_by()

returns a string that contains the visible exits in the room.

### add_item(list_of_items)

takes a list of item objects, or a single item object

### remove_item(name_of_item or item_id)

returns the first occurance of name_of_item or the item with the matching item_id and a message confirming the removal of the item if it is found. Returns only a message saying the item was not found otherwise.

### remove_npc(name_of_npc or char_id)

returns the first occurance of name_of_npc or the character with the matching char_id and message stating that the character has left the room, if the character is found. If the character is not found, only  message indicating that there is no character matching that criteria in the room.

### add_npcs(list_of_npcs)

takes a list of character objects and adds each one to the rooms non_player_characters list.

### change_light_level(amount)

takes an int amount and modifies the rooms light_level by that amount up to 10 or down to 0.
