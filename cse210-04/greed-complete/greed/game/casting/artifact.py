from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    """Calling the super """
    def __init__(self):
        super().__init__()
    
    def calculate_points(self):
        """Calculate points based on the artifact (*) and (O)"""
        points = 0
        
        if (self.get_text() == "*"):
            points = 1
        else:
            points = -1
        
        return points