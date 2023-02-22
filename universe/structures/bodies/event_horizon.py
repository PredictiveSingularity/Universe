from universe.structures.bodies import CelestialBody
from universe.technologies.units.international_system import year, light_year
from universe.technologies.mathematics.numbers.complex.real.rational.constants import *

class EventHorizon(CelestialBody):

    eh_time = year(10 * THOUSAND) # more than 10_000
    eh_space = 0

    eh_mass = 4.1 * MILLION  * 1.989 * 10**30
    eh_radius = 31.6 * 6.957 * (10**8)
    eh_temperature = 0
    eh_brightness = 0
    eh_lifespan = 10**10


    def __init__(self, eh_time=eh_time, eh_mass=eh_mass, eh_radius=eh_radius, eh_temperature=eh_temperature) -> None:
        super().__init__(model = "sphere", scale = 1)
        self.eh_time = eh_time * ((8.852 * (10**20) * (eh_radius **0.571) * ((eh_temperature) ** 1.142)) / eh_mass) ** 2.5
        self.radius, self.temperture, self.lifetime = eh_radius, eh_temperature, self.eh_time
        self.luminenecence = lambda: eh_brightness * (4 * pi * (self.radius**2)) * (self.temperture**4)
        self.mass = lambda: (self.lifetime / eh_time)**(1/2.5) * eh_mass
    
    def update(self) -> None:
        self.radius = (((self.lifetime / eh_time) ** (1/2.5) * eh_mass) / (8.852 * 10**20 * (self.temperture ** 1.142)) ) ** (1/0.571)
        self.temperture = (((self.lifetime / eh_time) ** (1/2.5) * eh_mass) / (8.852 * 10**20 * (self.radius ** 0.571)) ) ** (1/1.142)
        colours=["#0000FF","#dbe9f4","#FFFFFF","#ffffd4","#FFFF00","#FFA500","#FF0000"]
        if self.temperture >= 30000: self.color =  colours[0]
        if 30000 > self.temperture >= 20000: self.color =  colours[1]
        if 20000 > self.temperture >= 10000: self.color =  colours[2]
        if 10000 > self.temperture >= 7000: self.color =  colours[3]
        if 7000 > self.temperture >= 6000: self.color =  colours[4]
        if 5000 > self.temperture >= 3000: self.color =  colours[5]
        self.scale = self.radius*2 / 10**8


