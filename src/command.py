"""define command object"""

class command():
    """class definition for command class"""
    def __init__(self):
        self.name = "generic command"
        self.description = "genertic description"
        self.usage = "generic usage"
        self.usage_details = "Generic usage details"

    def execute(self,game_state):
        pass

    def details(self):
        pass