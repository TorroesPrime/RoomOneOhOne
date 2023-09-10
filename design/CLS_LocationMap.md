# locationMap

A locationMap contains at least 2 rooms with at least 1 exit leading from the first room to the second with one of those rooms designated as the “entry”.

![image](https://raw.githubusercontent.com/TorroesPrime/RoomOneOhOne/main/gfx/base%20relations-base%20relations-locationMap.drawio.png)

### fields

#### filename –

a string representing the file name of the adventure module

#### title –

a String that is the name of the locationMap.

#### entry –

A room object that is the first room a player will be placed
when they first start a game with this locationMap, or if they enter this locationMap from another locationMap.

#### rooms –

A dictionary where the keys are the room names, and the
values are the room objects associated with those names.

#### characters –

a list of character objects.

#### items –

a list of item objects contained in this locationMap

### methods

#### store_state –

A method to record the present state of the locationMap to a
.sav file

#### restore_state –

method to read from a .sav file and restore a locationMap to the state described in the file.

#### add_rooms –

adds the contents of a list of rooms to the locationMap's rooms
field.

#### get_room –

method to return a room when supplied with the name of the
room

#### set_location –

manual instantiation method. Used for testing and trouble shooting.

#### set_player_character –

method to declare what character the player is controlling as they interact with the dungeon and it's contents.
