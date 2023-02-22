#!/usr/bin/env python

import numpy as np

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

G = 6.74e-11 # 0.0000000000674
C = 299_792_458 # m/s**2

def second(s=1):
    unit = 1
    return unit * s

def minute(m=1):
    unit = second(60)
    return unit * m

def hour(h=1):
    unit = minute(60)
    return unit * h

def day(d=1):
    unit = hour(23) + minute(56) + second(4)
    return unit * d

def year(y=1):
    unit = day(365.2425)
    return unit * y

def meter(m=1):
    unit = 1
    return unit * m

def kilo_meter(km=1):
    unit = meter(1000)
    return unit * km

def astonomical_unit(au=1):
    unit = kilo_meter(149.6 * 1_000_000)
    return unit * au

def light_year(ly=1):
    unit = C
    return unit * ly

def gram(g=1):
    unit = 1
    return unit * g

def kilo_gram(kg=1):
    unit = gram(1000)
    return unit * kg

#scale_factor = 1 # 1:1
scale_factor = meter(1) # 1:au
time_factor = second(1) # 1:1/144s

# def update():
#     add_new_ship(universe, ship_position)
#     new_ship_position(ship, ship_position, universe, z_scale)
#     change_camera_pos()

# heightmap = 'assets/level//heightmap_demonstration.jpg'  # ścieżka mapy wysokości
# z_scale = 1  # współczynnik skalowania wizualizacji pionowej osi

def input(key):
    if any([
        held_keys['control'] and key == 'q',
        held_keys['control'] and key == 'x',
        key == 'q',
        key == 'escape',
    ]):
        print("[Q]uitting.")
        application.quit()


class CosmicBackgroundRadiation(Sky):
    def __init__(self,
            **kwargs
        ):
        super().__init__(
                **kwargs
            )

class Structure(Entity):
    current_velocity = Vec3(0)
    current_position = Vec3(0)

    current_mass = 0
    current_temperature = 0
    current_brightness = 0

    timespan = 0
    timestamp = 0

    def __init__(
            self,
            initial_velocity=current_velocity,
            position=current_position,
            mass=current_mass,
            temperature=current_temperature,
            brightness=current_brightness,
            lifespan=timespan,
            timestamp=timestamp,
            **kwags
        ):
        super().__init__(
            position=position,
            **kwags
        )
        self.current_velocity = initial_velocity
        self.position = position
        self.mass = mass
        self.temperature = temperature
        self.brightness = brightness
        self.lifespan = lifespan
    
    def update(self):
        self.update_temperature()
        self.update_electro_magnetic_emissions()
        self.update_velocity()
        self.update_position()
        self.update_lifespan()
    
    def update_temperature(self):
        pass
    
    def update_electro_magnetic_emissions(self):
        pass

    def update_lifespan(self):
        pass
    
    def update_velocity(self):
        global G, sim
        for exo_body in self.universe:
            if exo_body != self:
                distance_to_exo_body = distance(self, exo_body)
                force_direction = (exo_body.position - self.position).normalized()
                force = Vec3(force_direction * G * self.mass() * exo_body.mass() / distance_to_exo_body)
                acceleration = force / self.mass()
                self.current_velocity += acceleration * time.dt

    def update_position(self):
        self.position += self.current_velocity * time.dt

class Life(FirstPersonController):
    
    current_velocity = Vec3(0)
    current_position = Vec3(0)

    current_mass = 0
    current_temperature = 0
    current_brightness = 0

    timespan = 0
    timestamp = 0

    def __init__(
            self,
            initial_velocity=current_velocity,
            position=current_position,
            mass=current_mass,
            temperature=current_temperature,
            brightness=current_brightness,
            lifespan=timespan,
            timestamp=timestamp,
            **kwags
        ):
        super().__init__(
            position=position,
            **kwags
        )
        self.current_velocity = initial_velocity
        self.position = position
        self.mass = mass
        self.temperature = temperature
        self.brightness = brightness
        self.lifespan = lifespan

    def update(self):
        self.update_perspective()
        self.update_temperature()
        self.update_electro_magnetic_emissions()
        self.update_direction()
        self.update_position()
        self.update_velocity()
        self.update_lifespan()
    
    def update_perspective(self):
        # Update axe Y
        self.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[1]

        # Update axe X
        self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[0]
        self.camera_pivot.rotation_x= clamp(self.camera_pivot.rotation_x, -90, 90)

    def update_temperature(self):
        pass
    
    def update_electro_magnetic_emissions(self):
        pass

    def update_lifespan(self):
        pass
    
    def update_direction(self):
        self.direction = Vec3(
            self.forward * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()

    def update_position(self):
        feet_ray = raycast(self.position+Vec3(0,0.5,0), self.direction, ignore=(self,), distance=.5, debug=False)
        head_ray = raycast(self.position+Vec3(0,self.height-.1,0), self.direction, ignore=(self,), distance=.5, debug=False)
        if not feet_ray.hit and not head_ray.hit:
            move_amount = self.direction * time.dt * self.speed

            if raycast(self.position+Vec3(-.0,1,0), Vec3(1,0,0), distance=.5, ignore=(self,)).hit:
                move_amount[0] = min(move_amount[0], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(-1,0,0), distance=.5, ignore=(self,)).hit:
                move_amount[0] = max(move_amount[0], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,1), distance=.5, ignore=(self,)).hit:
                move_amount[2] = min(move_amount[2], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,-1), distance=.5, ignore=(self,)).hit:
                move_amount[2] = max(move_amount[2], 0)
            self.position += move_amount

    def update_velocity(self):
        # global G, sim
        # for exo_body in sim.system:
        #     if exo_body != self:
        #         distance_to_exo_body = distance(self, exo_body)
        #         force_direction = (exo_body.position - self.position).normalized()
        #         force = Vec3(force_direction * G * self.mass() * exo_body.mass() / distance_to_exo_body)
        #         acceleration = force / self.mass()
        #         self.current_velocity += acceleration * time.dt

        if self.gravity:
            # gravity
            ray = raycast(self.world_position+(0,self.height,0), self.down, ignore=(self,))
            # ray = boxcast(self.world_position+(0,2,0), self.down, ignore=(self,))

            if ray.distance <= self.height+.1:
                if not self.grounded:
                    self.land()
                self.grounded = True
                # make sure it's not a wall and that the point is not too far up
                if ray.world_normal.y > .7 and ray.world_point.y - self.world_y < .5: # walk up slope
                    self.y = ray.world_point[1]
                return
            else:
                self.grounded = False

            # if not on ground and not on way up in jump, fall
            self.y -= min(self.air_time, ray.distance-.05) * time.dt * 100
            self.air_time += time.dt * .25 * self.gravity

    # def update_position(self):
    #     self.position += self.current_velocity * time.dt

class Domain(Life):
    pass

class Kingdom(Domain):
    pass

class Animalia(Kingdom):
    pass

class Phylum(Kingdom):
    pass

class Chlordata(Phylum):
    pass

class Class(Phylum):
    pass

class Mammalia(Chlordata):
    pass

class Order(Class):
    pass

class Primate(Mammalia):
    pass

class SubOrder(Order):
    pass

class Haplorhini(Primate):
    pass

class InfraOrder(Order):
    pass

class SimiiForm(Haplorhini):
    pass

class Familiy(Class):
    pass

class Hominidae(SimiiForm):
    pass

class Tribe(Familiy):
    pass

class Hominini(Hominidae):
    pass

class Genus(Familiy):
    pass

class Homo(Hominini):
    pass

class Spiecies(Genus):
    pass

class HomoSapiens(Homo):
    pass

class Man(HomoSapiens):
    pass

class Player(Man):
    pass

class CelestialBody(Structure):
    pass

class Star(CelestialBody):

    sol_name = "Sol"
    sol_timestamp = year(4.6 * 1_000_000_000)
    sol_position = Vec3(0, light_year(26_673), 0)
    sol_mass = 1.989 * 10**30
    sol_radius = 6.957 * (10**8)
    sol_temperature = 5778 # Kelvin
    sol_brightness = 5.670367 * 10**-8
    sol_lifespan = 10**10
    #sol_scale = 2 * sol_radius / scale_factor
    colours = [
        "#0000FF", # >=30_000 Kelvin
        "#dbe9f4", # 30_000 K > k >= 20_000 K
        "#FFFFFF", # 20_000 K > k >= 10_000 K
        "#ffffd4", # 10_000 K > k >= 7_000 K
        "#FFFF00", # 7_000 K > k >= 6_000 K
        "#FFA500", # 5_000 K > k >= 3_000 K 
        "#FF0000"  # Else red
        ]
    
    def __init__(self,
            name=sol_name,
            timestamp=sol_timestamp,
            position=Vec3(0),
            model="sphere",
            scale=1,
            colours=colours,
            mass=sol_mass,
            radius=sol_radius,
            temperature=sol_temperature,
            **kwargs
        ):
        super().__init__(
                name=name,
                position=position,
                model=model,
                scale=scale,
                **kwargs
            )
        self.position = position
        self.timestamp = timestamp * ((8.852 * (10**20) * (radius **0.571) * ((temperature) ** 1.142)) / mass) ** 2.5
        self.radius, self.temperture, self.lifetime = radius, temperature, self.timestamp
        self.luminenecence = lambda: brightness * (4 * pi * (self.radius**2)) * (self.temperture**4)
        self.mass = lambda: (self.lifetime / timestamp)**(1/2.5) * mass
        self.colours = colours
    
    def update(self) -> None:
        self.update_radius()
        self.update_scale()

        super().update()

    def update_radius(self):
        self.radius = (((self.lifetime / self.timestamp) ** (1/2.5) * self.mass()) / (8.852 * 10**20 * (self.temperture ** 1.142)) ) ** (1/0.571)

    def update_scale(self):
        # Needs self.radius
        # Run self.update_radius() first
        self.scale = scale_factor * self.radius * 2 / 10 ** 8

    def update_temperature(self):
        self.temperture = (((self.lifetime / self.timestamp) ** (1/2.5) * self.mass()) / (8.852 * 10**20 * (self.radius ** 0.571)) ) ** (1/1.142)

    def update_electro_magnetic_emissions(self):
        if self.temperture >= 30000: self.color =  self.colours[0]
        if 30000 > self.temperture >= 20000: self.color =  self.colours[1]
        if 20000 > self.temperture >= 10000: self.color =  self.colours[2]
        if 10000 > self.temperture >= 7000: self.color =  self.colours[3]
        if 7000 > self.temperture >= 6000: self.color =  self.colours[4]
        if 5000 > self.temperture >= 3000: self.color =  self.colours[5]

class Planet(CelestialBody):

    tellus_name = "Tellus"
    tellus_timestamp = year(4.5 * 1_000_000_000) # 4.5 billion years
    planet_position = Vec3(scale_factor / light_year(26_673), scale_factor / kilo_meter(149.6 * 1_000_000), 0) # 149.6 million km from the sun
    planet_mass = kilo_gram(5.972168 * 1024) # 5.972168×1024 kg
    planet_radius=12_742 #12,742 in average (earth is not strictly a sphere but more an squished oval du to centrifugal force applied)
    planet_temperature=287.91 #287.91 K
    planet_brightness = 0 # Planets are black-bodies they dont emit light only reflect part of it (see scattering rays)
    planet_lifespan = year(7.5 * 1_000_000_000) # in 7.5 billion years earth is absorbed by the expansion of the dying Sun

    def __init__(
            self,
            name=tellus_name,
            timestamp=tellus_timestamp,
            position=planet_position,
            # scale=0.4,
            mass=planet_mass,
            radius=planet_radius,
            temperature=planet_temperature,
            color=color.green,
            **kwags
        ) -> None:
        super().__init__(
            name = name,
            model = "sphere",
            position = position,
            color = color,
            **kwags
        )
        self.position = position
        self.timestamp = timestamp * ((8.852 * (10**20) * (radius **0.571) * ((temperature) ** 1.142)) / mass) ** 2.5
        self.radius, self.temperture, self.lifetime = radius, temperature, self.timestamp
        self.luminenecence = 0
        self.mass = lambda: (self.lifetime / radius)**(1/2.5) * mass
        self.scale = scale_factor * self.radius * 2

class Moon(CelestialBody):

    luna_name = "Luna"

    luna_timestamp = year(4.5 * 1_000_000_000) # 4.5 billion years
    moon_position = Vec3(scale_factor / light_year(26_673), scale_factor / kilo_meter(149.6 * 1_000_000), scale_factor / kilo_meter(384_400)) # 384_400 km from earth

    moon_mass = kilo_gram(5.972168 * 1024) # 5.972168×1024 kg
    moon_radius=12_742 #12,742 in average (earth is not strictly a sphere but more an squished oval du to centrifugal force applied)
    moon_temperature=287.91 #287.91 K
    moon_brightness = 0 # Planets are black-bodies they dont emit light only reflect part of it (see scattering rays)
    moon_lifespan = year(7.5 * 1_000_000_000) # in 7.5 billion years earth is absorbed by the expansion of the dying Sun


    def __init__(
            self,
            name=luna_name,
            timestamp=luna_timestamp,
            position=moon_position,
            mass=moon_mass,
            radius=moon_radius,
            temperature=moon_temperature,
            color=color.gray,
            **kwags
        ) -> None:
        super().__init__(
            name = name,
            model = "sphere",
            position = position,
            color = color,
            **kwags
        )
        self.position = position
        self.timestamp = timestamp * ((8.852 * (10**20) * (radius **0.571) * ((temperature) ** 1.142)) / mass) ** 2.5
        self.radius, self.temperture, self.lifetime = radius, temperature, self.timestamp
        self.luminenecence = 0
        self.mass = lambda: (self.lifetime / radius)**(1/2.5) * mass

class SpaceTime(Entity):
    pass

class Simulation:
    
    sun_system = [
        #Star(name='Sol', universe=self.universe),
    ]

    def __init__(self, universe=sun_system):
        self.engine = Ursina()
        self.camera = EditorCamera()
        self.bg_rad = CosmicBackgroundRadiation(color=color.black, parent=self.camera)
        self.universe = universe
        self.universe.append(Star(universe=self.universe))

    
    def update(self):
        pass
    
    def run(self):
        self.engine.run()

def main():

    simulacre = Simulation()
    simulacre.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(1)


#sun = Star()

# earth = Planet(
    #     parent=sun,
    #     name="Tellus",
    #     color=color.blue,
    #     collider='sphere',
    # )

# earth_label = Text(f"{earth.scale=}")

# moon = Moon(
#         parent=earth,
#         name="Luna",
#         color=color.white,
#         # scale=0.3,
#         # position=Vec3(3, 0, 0)
#     )
# moon_label = Text(f"{moon}")

# camera = EditorCamera(parent=earth)

# human = Player(
#         parent=earth,
#         name="Homo Spiens",
#         height=meter(1.8),
#     )

# topology = Mesh(
#         vertices=[
#                 [0, 0, 0],
#                 [1, 0, 0],
#                 [1, 0, 1],
#                 [0, 0, 1],
#             ],
#         triangles=[
#                 [0, 1, 2, 3]
#             ],
#         normals=[
#                 [],
#             ],
#         uvs=[
#                 [],
#             ]
#     )

#space_time = SpaceTime(model=topology)

#system = [earth]

# target = system[0]
# target_info = Text(
#         text=f"{target.name}\n{target.mass()=}\n{target.radius=}\n{target.current_velocity=}\n{target.temperature=}\n{target.position=}",
#     )

# t = -np.pi

#print(f"Distance between {earth.name} and {moon.name} is {meter(distance(earth, moon) * scale_factor) / kilo_meter(1)} km.")

