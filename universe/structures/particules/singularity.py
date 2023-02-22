from universe.structures.particules import Particule

class Singularity(Particule):

    origin_time = 0
    origin_space = 0

    origin_mass = 0
    origin_radius = 0
    origin_temperature = 0
    origin_brightness = 0
    
    def __init__(self, origin_time=origin_time, origin_mass=origin_mass, origin_radius=origin_radius, origin_temperature=origin_temperature, origin_brightness=origin_brightness) -> None:
        super().__init__(model = "point", scale = 1)
        self.origin_time = origin_time * ((8.852 * (10**20) * (origin_radius **0.571) * ((origin_temperature) ** 1.142)) / origin_mass) ** 2.5
        self.radius, self.temperture, self.lifetime = origin_radius, origin_temperature, self.origin_time
        self.luminenecence = lambda: origin_brightness * (4 * pi * (self.radius**2)) * (self.temperture**4)
        self.mass = lambda: (self.lifetime / origin_time)**(1/2.5) * origin_mass
    
    def update(self) -> None:
        self.radius = (((self.lifetime / origin_time) ** (1/2.5) * origin_mass) / (8.852 * 10**20 * (self.temperture ** 1.142)) ) ** (1/0.571)
        self.temperture = (((self.lifetime / origin_time) ** (1/2.5) * origin_mass) / (8.852 * 10**20 * (self.radius ** 0.571)) ) ** (1/1.142)
        self.color = color.black
        self.scale = self.radius*2 / 10**8
