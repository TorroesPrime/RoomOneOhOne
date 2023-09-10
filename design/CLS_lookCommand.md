# LookCommand

Inherites from [command](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/design/CLS_command.md) class.

Allows the player to view a more detailed description of the room.
![image](https://raw.githubusercontent.com/TorroesPrime/RoomOneOhOne/main/gfx/cmd_look.png)

## fields

### command_name –

a string representing the test version of the command

### description –

a string describing what the command is used for.

### usage –

a string demonstrating how to use the command

### usage_details –

a string describing possible variants or alternate uses of
this command.

## methods

### execute() –

Returns the results of the fullDescribe method of the player's current room.

### details(Self) –

returns a string that is combination of the commandName,
description, or a combination of the commandName, description and usageDetails
attributes. Used when reading the help command for a given command.
