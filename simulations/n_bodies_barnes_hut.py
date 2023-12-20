
from universe import *
import numpy as np

application.asset_folder = Path(application.asset_folder).parent

simulacre = Universe(asset_folder=application.asset_folder)

window.color = color.black

n_bodies = 100
bodies = []
G = 0.35
qtree = None
sun = None

sz = 1000
sx, sy = window.screen_resolution

class Mover(Entity):

    def __init__(self, position, velocity, mass, radius=None, color=color.white, **kwargs):
        self.mass = mass
        self.velocity = velocity
        self.acceleration = Vec3(0)
        self.orbit_radius = np.sqrt(self.mass) * 2
        # Compute the schwarzshild radius given r_s = (2*G*M) / (c ** 2) if radius is None
        self.radius = radius or (2 * G * self.mass) / (C ** 2)
        super().__init__(position=position, model="sphere", scale=Vec2(self.radius), color=color, **kwargs)

    def update(self):
        self.velocity += self.acceleration
        self.position += self.velocity
        self.velocity = np.clip(self.velocity, -15, 15)
        self.acceleration = Vec3(0)

    def apply_force(self, force):
        f = force / mass
        self.acceleration += f

    def gravitate_to(self, exo_body):
        force = self.position - exo_body.position
        distance_squared = np.clip(np.sqrt(x.dot(force)), 100, 1000)
        strength = (G * (self.mass - exo_body.mass)) / distance_squared
        force *= strength
        exo_body.apply_force(force)


for b in range(n_bodies):
    rand_x, rand_y, rand_z = random.randrange(0, int(sx) / 2), random.randrange(0, int(sy) / 2), random.randrange(0, int(sz) / 2)
    position = velocity = Vec3(rand_x, rand_y, rand_z)
    velocity *= random.randrange(10, 15)
    position *= random.randrange(150, 200)
    mass = random.randrange(10, 15)
    
    body = Mover(position, velocity, mass, name=f"Body {b}")
    body.rotate(Vec3(np.pi / 2))
    
    bodies.append(body)

sun = Mover(Vec3(0), Vec3(0), 500, color=color.yellow)

EditorCamera(parent=sun)

simulacre.run()