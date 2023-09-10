# gameState

a gameState object is a record of the present status and condition of everything in the game.

![image](https://raw.githubusercontent.com/TorroesPrime/RoomOneOhOne/main/gfx/base%20relations-base%20relations-gamestate.drawio.png)

## fields

### save_file_version –

a String representing the supported version of the system this game is running

### current_room_leader –

A string “Current room: “ that is used to record the player's current room in a .sav file.

### default_save_filename –

A string “zorkSave” used for the default .sav file name

### save_file_ext –

a String “.sav” used for the save file extension.

### location_map –

the locationMap object for this particular game.

### adventurers_current_room –

A room object representing the name of the room currently occupied by the player.

### debug –

A Boolean used to control trouble shooting functions and displays.

### player_character –

A character object that is the character the player controls.

### characters –

A list containing all the characters that are included in a locationMap.

## methods

storeState –

Method to write the present gameState to a .sav file

#### get_adventurers_current_room

returns the adventures current room

#### set_adventurers_current_room

sets the players current room as they move from room to room.

#### set_player_character –

A character object that the player controls.

#### add_characters –

takes a list of characters and adds them to the characters
list.

#### set_test –

method to switch the debug. Used for testing and trouble
shooting
