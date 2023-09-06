# helpCommand

Inherites from [command](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/design/CLS_command.md) class.

Allows the player to view the usage details of the supplied command or to view the usage information about the help command if no command supplied.

## fields

### command_name –

a string representing the name of the command

### description –

a string describing what the command is used for.

### usage –

a string demonstrating how to use the command

### usage_details –

a string describing possible variants or alternate uses of this command.

## methods

### execute() –

Returns the results of the result fo the details() method of supplied command, if command supplied. If no command supplied, displays the result of the details() method of the help command.

### details(Self) –

returns a string that is combination of the command_name, description and usageDetails
attributes. Used when reading the help command for a given command.