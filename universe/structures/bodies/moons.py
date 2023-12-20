from ursina import Vec3
from universe.structures.bodies import CelestialBody

from universe.dimentions.time import year
from universe.forces.gravity import kilo_gram
from universe.technologies.mathematics.numbers.complex.real.rational.constants import BILLION, MILLION

class ExoMoon(CelestialBody):
    pass

class Moon(ExoMoon):

    luna_name = "Luna"

    luna_timestamp = year(4.5 * BILLION) # 4.5 billion years
    moon_position = Vec3(scale_factor / light_year(26_673), scale_factor / kilo_meter(149.6 * MILLION), scale_factor / kilo_meter(384_400)) # 384_400 km from earth

    moon_mass = kilo_gram(5.972168 * 1_024) # 5.972168×1024 kg
    moon_radius=12_742 #12,742 in average (earth is not strictly a sphere but more an squished oval du to centrifugal force applied)
    moon_temperature=287.91 #287.91 K
    moon_brightness = 0 # Planets are black-bodies they dont emit light only reflect part of it (see scattering rays)
    moon_lifespan = year(7.5 * BILLION) # in 7.5 billion years earth is absorbed by the expansion of the dying Sun


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
