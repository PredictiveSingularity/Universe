from ursina import Vec3, color, Color, application

class Origin:
    
    def __init__(
            self,
            structures: list = [],
            # Allows you to see nothing as gray...
            background: Color = color.gray,
            # And everything as black
            colour: Color = color.black,
        ):
        # super().__init__()
        application.background = background
        self.color = colour
        self.structures = structures

    def update(self, delta_time):
        pass
