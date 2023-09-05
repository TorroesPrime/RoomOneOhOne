# command

## fields

### command_name

a string representing the test version of the command

#### description –

a string describing what the command is used for.

#### usage –

a string demonstrating how to use the command

#### usage_details –

a string describing possible variants or alternate uses of
this command.

## methods

### execute() –

abstract method here to be over ridden in the individual command classes.

### details(Self) –

returns a string that is combination of the command_name, description and usage_details attributes. Used when reading the help command for a given command.
