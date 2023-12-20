from universe import *
import numpy as np
import itertools

application.asset_folder = Path(application.asset_folder).parent

simulacre = Universe()

G = 0.05

class Body(Entity):
    
    def __init__(self, mass, orbit_radius, position = Vec2(0), velocity = Vec2(0), model = "point", **kwargs):
        self.mass, self.velocity = mass, velocity
        self.orbit_radius = orbit_radius
        self.acceleration = Vec2(0)
        
        super().__init__(model=model, position=position, **kwargs)

    def set_velocity(self, velocity):
        self.velocity = velocity
    
    def set_acceleration(self, acceleration):
        self.acceleration = acceleration
    
    def set_position(self, position):
        self.position = position
    
    def update_velocity(self, velocity):
        self.velocity += velocity
    
    def update_position(self, position):
        self.position += position

    def gravitate_to(self, exobody):
        dx = abs(self.x - exobody.x)
        dy = abs(self.y - exobody.y)

        if dx < 2*self.orbit_radius and dy < 2*self.orbit_radius:
            pass
        else:
            try:
                r = np.sqrt(dx**2 + dy**2)
                a = G * exobody.mass / r**2
                theta = np.arcsin(dy/r)

                if self.x > exobody.x:
                    _xsign = -1
                else:
                    _xsign = 1
                _ax = _xsign * a * np.cos(theta)
                
                if self.y > exobody.y:
                    _ysign = -1
                else:
                    _ysign = 1
                _ay = _ysign * a * np.sin(theta)
                _acceleration = Vec2(_ax, _ay)
                
                self.set_acceleration(_acceleration)
            except ZeroDivisionError:
                pass
    
    def update(self):
        self.update_velocity(self.acceleration)
        self.update_position(self.velocity)
        
    
number_of_bodies = 100
bodies = []

for i in range(number_of_bodies):
    if i == 0:
        bodies.append(
            Body(100, 10, model="sphere", position=Vec2(0, 0), name=f"Body {i}", color=color.yellow, scale=10)
            )
    else:
        bodies.append(
            Body(1, 3, model="sphere", position=Vec2(random.randrange(-10, 10), random.randrange(-10, 10)), name=f"Body {i}")
            )

body_pairs = list(itertools.combinations(bodies, 2))

# editor_camera = EditorCamera()
EditorCamera(parent=bodies[0])

def update():
    for body, exobody in body_pairs:
        body.gravitate_to(exobody)
        exobody.gravitate_to(body)

simulacre.run()