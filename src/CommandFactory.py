"""class definition for CommandFactory"""

class CommandFactory:
    """defines a command factory which will take a string and parse a command from it."""
    def __init__(self,game_state):
        self.game_state = game_state
    def executeCommand(self,command_string):
           """takes a command_string and attempts to parse it out to create a command object."""
           cmd = command_string.split()
           if command[0] == "move" or command[0] in "NSEWUDudnsew":
                cmd = moveCommand()
            elif command[0] == "look":
                cmd = lookCommand()
            elif command[0] == "help":
                cmd = helpCommand(command[1])
