from ursina import Vec3
from universe.structures.bodies import CelestialBody

from universe.dimentions.time import year
from universe.forces.gravity import kilo_gram
from universe.technologies.mathematics.numbers.complex.real.rational.constants import BILLION, MILLION

class Planet(CelestialBody):

    tellus_name = "Tellus"
    tellus_timestamp = year(4.5 * BILLION) # 4.5 billion years
    planet_position = Vec3(scale_factor / light_year(26_673), scale_factor / kilo_meter(149.6 * MILLION), 0) # 149.6 million km from the sun
    planet_mass = kilo_gram(5.972168 * 1024) # 5.972168×1024 kg
    planet_radius=12_742 #12,742 in average (earth is not strictly a sphere but more an squished oval du to centrifugal force applied)
    planet_temperature=287.91 #287.91 K
    planet_brightness = 0 # Planets are black-bodies they dont emit light only reflect part of it (see scattering rays)
    planet_lifespan = year(7.5 * BILLION) # in 7.5 billion years earth is absorbed by the expansion of the dying Sun

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

