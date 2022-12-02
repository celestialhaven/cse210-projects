from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """calling the function __init__ using super()"""
    def __init__(self):
        super().__init__()
        self._message = ""
    """set message for every artifact being found"""
    def set_message(self, message):
        self._message = message
    """returns the value of the message to window"""
    def get_message(self):
        return self._message