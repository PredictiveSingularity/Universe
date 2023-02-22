from ursina import Vec3
from universe.structures.bodies import CelestialBody
from universe.technologies.mathematics.numbers.complex.real.rational.constants import BILLION as billion
from universe.technologies.units.international_system import year, light_year

class Star(CelestialBody):

    sol_name = "Star"
    sol_timestamp = 0
    sol_position = Vec3(0, 0, 0)
    sol_mass = 0
    sol_radius = 0
    sol_temperature = 0 # Kelvin
    sol_brightness = 0
    sol_lifespan = 0
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
        if mass > 0:
            self.timestamp = timestamp * ((8.852 * (10**20) * (radius **0.571) * ((temperature) ** 1.142)) / mass) ** 2.5
        else:
            self.timestamp = 0
        
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
        self.scale = self.scale_factor * self.radius * 2 / 10 ** 8

    def update_temperature(self):
        self.temperture = (((self.lifetime / self.timestamp) ** (1/2.5) * self.mass()) / (8.852 * 10**20 * (self.radius ** 0.571)) ) ** (1/1.142)

    def update_electro_magnetic_emissions(self):
        if self.temperture >= 30000: self.color =  self.colours[0]
        if 30000 > self.temperture >= 20000: self.color =  self.colours[1]
        if 20000 > self.temperture >= 10000: self.color =  self.colours[2]
        if 10000 > self.temperture >= 7000: self.color =  self.colours[3]
        if 7000 > self.temperture >= 6000: self.color =  self.colours[4]
        if 5000 > self.temperture >= 3000: self.color =  self.colours[5]

class Sol(Star):
    sol_name = "Sol"
    sol_timestamp = year(4.6 * 1_000_000_000)
    sol_position = Vec3(0, light_year(26_673), 0)
    sol_mass = 1.989 * 10**30
    sol_radius = 6.957 * (10**8)
    sol_temperature = 5778 # Kelvin
    sol_brightness = 5.670367 * 10**-8
    sol_lifespan = 10**10

    def __init__(self,
            name=sol_name,
            timestamp=sol_timestamp,
            position=sol_position,
            model="sphere",
            scale=1,
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
                timestamp=timestamp,
                mass=mass,
                radius=radius,
                temperature=temperature,
                **kwargs
            )