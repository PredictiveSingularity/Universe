from ursina import *
import numpy as np

from ursina.prefabs.first_person_controller import FirstPersonController


def update():
    global t
    t+=0.01

def input(key):
    if any([
        held_keys['control'] and key == 'q',
        held_keys['control'] and key == 'x',
        key == 'q',
        key == 'escape',
    ]):
        print("[Q]uitting.")
        application.quit()


class Star(Entity):
    def __init__(self,
            position=Vec3(0),
            color=color.yellow,
            model="sphere",
            scale=1.5,
            **kwargs
        ):
        super().__init__(
                position=position,
                model=model,
                color=color,
                scale=scale,
                **kwargs
            )
    
    def update(self):
        global t
        self.rotation_y+=time.dt*100

class Planet(Entity):
    def __init__(self,
            position=Vec3(1, 0, 0),
            color=color.green,
            model="sphere",
            scale=0.4,
            orbit_radius=1.8,
            orbit_angle=np.pi*40/180,
            number_closest_neighbors=2,
            orbit_period_factor=2,
            **kwargs
        ):
        super().__init__(
                position=position,
                model=model,
                color=color,
                scale=scale,
                **kwargs
            )
        self.orbit_radius = orbit_radius
        self.orbit_angle = orbit_angle
        self.number_closest_neighbors = number_closest_neighbors
        self.orbit_period_factor = orbit_period_factor
    
    def update(self):
        global t

        self.y = np.cos(self.orbit_period_factor * t + self.orbit_angle * self.number_closest_neighbors) * self.orbit_radius
        self.z = np.sin(self.orbit_period_factor * t + self.orbit_angle * self.number_closest_neighbors) * self.orbit_radius
        self.x = self.y * np.sin(self.orbit_angle * self.number_closest_neighbors)
        self.y = self.y * np.cos(self.orbit_angle * self.number_closest_neighbors)
        
        self.position = Vec3(self.x, self.y, self.z)

        self.rotation_y+=time.dt*100

class Moon(Entity):
    def __init__(self,
            position=Vec3(1, 0, 0),
            color=color.gray,
            model="sphere",
            scale=0.2,
            orbit_radius=1.8,
            orbit_angle=np.pi*40/180,
            number_closest_neighbors=2,
            orbit_period_factor=2,
            **kwargs
        ):
        super().__init__(
                position=position,
                model=model,
                color=color,
                scale=scale,
                **kwargs
            )
        self.orbit_radius = orbit_radius
        self.orbit_angle = orbit_angle
        self.number_closest_neighbors = number_closest_neighbors
        self.orbit_period_factor = orbit_period_factor
    
    def update(self):
        self.rotation_y+=time.dt*100

app = Ursina()

sun = Star(
    name="Sol",
    scale=1.5,

)

earth = Planet(
        parent=sun,
        name="Tellus",
        color=color.blue,
        scale=0.4,
    )

moon = Moon(
        parent=earth,
        name="Luna",
        color=color.white,
        scale=0.3,
    )

# human = FirstPersonController(
#         parent=earth,
#         name="Homo Spiens"
#     )

system = [sun, earth, moon]

t = -np.pi

print(f"Distance between {sun.name} and {earth.name} is {distance(earth, sun)}.")

app.run()