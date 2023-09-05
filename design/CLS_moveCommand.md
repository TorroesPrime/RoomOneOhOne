# MoveCommand

Inherites from [command](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/design/CLS_comand.md) class.

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

### dir –

A string denoting the direction the player intends to move
in.

## methods

### execute() –

gets the list of the current [room](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/design/CLS_room.md)'s [exits](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/design/CLS_exit.md) and checks if there is an [exit](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/design/CLS_exit.md) that has a dir that corresponds to the supplied dir. If there is, it checks to see if the exit's isLocked is false. If it is, it calls the rooms leave_by() method to leave the
current room and enter the selected exits destination room.

### details(Self) –

returns a string that is a combination of the commandName, description and usageDetails attributes. Used when reading the help command for a given command.