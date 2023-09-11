from command import command

class lookCommand(command):
    """class definition for lookCommand"""
    def __init__(self):
        self.name = "move command"
        self.description = "The move command is used to permit the player to move from one room to another room that is connected via an exit."
        self.usage = ">>> move <direction> or >>> <direction>"
        self.usage_details = "Generic usage details"