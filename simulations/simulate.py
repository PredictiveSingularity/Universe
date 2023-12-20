#!/usr/bin/env python

from universe import *

application.asset_folder = Path(application.asset_folder).parent

class Energy(Entity):

    def __init__(self, name = "Energy", mass = 0, velocity = Vec3(0), time_scale=1, space_scale=1, **kwargs):
        self.position, self.velocity, self.mass = Vec3(0), velocity, mass
        super().__init__(name=name,)


    def update(self):
        global time_scale, space_scale, is_paused
        if not is_paused:
            delta_time = time_scale / time.dt
            distance_to_origin = distance(self, Vec3(0))
            if self.mass and distance_to_origin:
                force_direction = (Vec3(0) - self.position).normalized()
                force = Vec3(force_direction * G * self.mass * 1 / distance_to_origin)
                acceleration = force / self.mass
                self.velocity += acceleration * delta_time
            self.position += self.velocity *  delta_time

            print(f"{self}")
        #super().update()

    def __str__(self):
        global time_scale, space_scale, mass_scale
        delta_time = time_scale / time.dt
        return f"@(x={self.position.x:.2f}, y={self.position.y:.2f}, z={self.position.z:.2f}, dt={delta_time:.2f}): {self.name.capitalize()} = m({self.mass:.2f}) × c²(x={self.velocity.x:.2f}, y={self.velocity.y:.2f}, z={self.velocity.z:.2f}) = 1"


class EventHorizon(Energy):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Singularity(Energy):
    
    def __init__(self, mass = 1, velocity = Vec3(0), **kwargs):
        # assert mass + velocity == 1
        global time_scale, space_scale
        super().__init__()

        self.position, self.velocity, self.mass = Vec3(0), velocity, mass
        self.model = "point"
        self.horizon = EventHorizon(parent=self,
            model="sphere",
            color=color.black,
            #scale=2*(space_scale / schwarzshild_radius)
        )
        self.horizon.radius = kilo_meter(12_000_000) # 12 million km (SgtA*)
        self.horizon.scale = 2*(space_scale / self.horizon.radius)
        self.horizon.mass = (mass_scale / solar_mass(4.154 * 10 ** 6))
        self.horizon.color = color.black
        self.horizon.visible = True


class Vector(Entity):
    def __init__(self, **kwargs) -> None:
        super().__init__(model="sphere", color=color.white, scale=0, **kwargs)
        self.origin = Vec2(0, 0)
    
    def update(self) -> None:
        pass
        # self.position = Vec2(self.camera.x / 2, self.camera.y / 2)
        # self.rotation = (0, 0, degrees(atan(self.camera.x / (self.camera.y or 1))) + 90)
        # self.scale = distance(self.origin, self.camera)

simulacre = Universe(asset_folder=application.asset_folder)

space_scale = kilo_meter(400_000) #1:25,640ly
time_scale = day(1) # year(10 * BILLION) #1:10 billion years
mass_scale = 1 # 1:∞ gram
space_time_singularis = 1
age = 0

is_paused = True

#origin = Singularity(space_scale=space_scale, time_scale=time_scale)

# earth = Energy(
#     name = "Tellus",
#     mass=(mass_scale / kilo_gram(5.972168 * 10 ** 24)),
#     velocity=Vec3(0, 0, (space_scale * time_scale) / meter(9.80665) * second(1)),
#     color=color.blue,
#     scale=(space_scale / (2 * kilo_meter(6_371)) ),
#     position=Vec3(0),
#     model="sphere")

# moon = Energy(
#     name = "Luna",
#     mass=0.005,
#     velocity=Vec3(0.0981),
#     color=color.white,
#     scale=(space_scale / (2 * kilo_meter(1_737.4)) ),
#     position=Vec3(0, (space_scale / kilo_meter(384_400)), 0),
#     model="sphere")

journey = Vector()

editor_camera = EditorCamera()


def update():
    global is_paused, time_scale, space_scale, age, journey

    if held_keys['p']:
        is_paused = not is_paused
    
    if not is_paused:
        delta_time = time.dt
        print(f"{delta_time=} -> {age=}")
        age += delta_time

        journey.scale += Vec3(age * 100)
        journey.color = Color(-age, -age, -age, age)
        
    #origin.update(delta_time=delta_time)

simulacre.run()