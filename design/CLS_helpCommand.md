# helpCommand
Inherites from [command](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/design/CLS_command.md) class.
![image](https://github.com/TorroesPrime/RoomOneOhOne/blob/main/gfx/base%20relations-command%20system-commands.drawio.png?raw=true)


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

### execute(command) –

Returns the results of the result fo the details() method of supplied command, if command supplied. If no command supplied, displays the result of the details() method of the help command.

### details(Self) –

returns a string that is combination of the command_name, description and usageDetails
attributes. Used when reading the help command for a given command.


>Room 101's command system uses an [verb] [item] [modifier] [target] structure, meaning the >first word of a command will be an action you wish to perform.  A few examples of verbs that >are commands include 'move', 'look', 'examine', and 'eat'. [target] is the target of the verb, >so in the case of "eat apple", 'eat' is the verb while 'apple' is the target. 
>
>it is possible to execute more complex commands by supplying an [item] and a [modifier]. when >using an [item] and a [modifier] you are indicating that you wish to perform [verb] on the >[item] associated with [target]. For instance 'view stats of John Jones' is how you would view >the core stats for a character named John Jones. `