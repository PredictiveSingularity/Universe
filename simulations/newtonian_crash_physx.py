from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import numpy as np
import random

app = Ursina()

# Window Title info
window.title = 'Ursina Solar System Simulation'
window.fps_counter.enabled = True
max_frames = 30

window.fps_counter.max = 30

G = 6.74e-11 # 0.0000000000674

#music = Audio(sound_file_name='assets/leonell-cassio-music.mp3', loop=True, autoplay=True, volume=10)

earth_t = venus_t = mars_t = mercury_t = jupiter_t = saturn_t = uranus_t = neptune_t = -np. pi

able_text = True

paused = False


def year(y=1):
    return y * 60 * 60

def meter(m=1):
    return m

def kilo_meter(km=1):
    return 1000 * km

def light_year(ly=1):
    return 299_792_458 * ly

def gram(g=1):
    return g

def kilo_gram(kg=1):
    return 1000 * kg


def update():
    if not paused:
        global bodies
        # global earth_t, venus_t, mars_t, mercury_t, jupiter_t, saturn_t, uranus_t, neptune_t
        
        # Update bodies velocities
        # for body in bodies:
        #     body.update_velocity()

        # # Update bodies position
        # for body in bodies:
        #     body.update_position()
        
        # mercury_t += .47 * time.dt
        # venus_t += .35 * time.dt
        # earth_t += .29 * time.dt
        # mars_t += .24 * time.dt
        # jupiter_t += .13 * time.dt
        # saturn_t += .0969 * time.dt
        # uranus_t += .0681 * time.dt
        # neptune_t += .0543 * time.dt
        # angle = np.pi * 40 / 180

        # radius_1 = 96.75 + 500
        # mercury.x = np.cos(mercury_t) * radius_1
        # mercury.z = np.sin(mercury_t) * radius_1

        # radius_2 = 180.75 + 600
        # venus.x = np.cos(venus_t + angle) * radius_2
        # venus.z = np.sin(venus_t + angle) * radius_2

        # radius_3 = 250 + 750
        # earth.x = np.cos(earth_t + angle * 2) * radius_3
        # earth.z = np.sin(earth_t + angle * 2) * radius_3

        # radius_4 = 381 + 800
        # mars.x = np.cos(mars_t + angle * 3) * radius_4
        # mars.z = np.sin(mars_t + angle * 3) * radius_4

        # radius_5 = 1300 + 800
        # jupiter.x = np.cos(jupiter_t + angle * 4) * radius_5
        # jupiter.z = np.sin(jupiter_t + angle * 4) * radius_5

        # radius_6 = 2375+800
        # saturn.x = np.cos(saturn_t + angle * 5) * radius_6
        # saturn.z = np.sin(saturn_t + angle * 5) * radius_6

        # radius_7 = 4800+800
        # uranus.x = np.cos(uranus_t + angle * 6) * radius_7
        # uranus.z = np.sin(uranus_t + angle * 6) * radius_7

        # radius_8 = 7525+800
        # neptune.x = np.cos(neptune_t + angle * 7) * radius_8
        # neptune.z = np.sin(neptune_t + angle * 7) * radius_8

        # human.x, human.y, human.z = earth.x - 40, earth.y + 20, earth.z
        

t = -np. pi


def input(key):
    global paused
    if any([
        held_keys['control'] and key == 'q',
        held_keys['control'] and key == 'x',
        key == 'q',
        key == 'escape',
    ]):
        print("[Q]uitting.")
        application.quit()
    if key == 'p':
        paused = not paused
    
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
        global G, bodies
        for exo_body in bodies:
            if exo_body != self:
                distance_to_exo_body = distance(self, exo_body)
                force_direction = (exo_body.position - self.position).normalized()
                force = Vec3(force_direction * G * self.mass() * exo_body.mass() / distance_to_exo_body)
                acceleration = force / self.mass()
                self.current_velocity += acceleration * time.dt

    def update_position(self):
        self.position += self.current_velocity * time.dt


class CelestialBody(Structure):
    pass
    # def __init__(
    #         self,
    #         **kwags
    #     ):
    #     super().__init__(
    #         **kwags
    #     )

 
class Star(CelestialBody):

    sol_name = "Sol"

    sol_timestamp = year(4.6 * 1_000_000_000)
    sol_position = Vec3(0, light_year(26_673), 0)

    sol_mass = 1.989 * 10**30
    sol_radius = 6.957 * (10**8)
    sol_temperature = 5778
    sol_brightness = 5.670367 * 10**-8
    sol_lifespan = 10**10

    colours = [
        "#0000FF", # >=30_000 Kelvin
        "#dbe9f4", # 30_000 K > k >= 20_000 K
        "#FFFFFF", # 20_000 K > k >= 10_000 K
        "#ffffd4", # 10_000 K > k >= 7_000 K
        "#FFFF00", # 7_000 K > k >= 6_000 K
        "#FFA500", # 5_000 K > k >= 3_000 K 
        "#FF0000"  # Else red
        ]


    def __init__(
            self,
            name=sol_name,
            timestamp=sol_timestamp,
            position=sol_position,
            mass=sol_mass,
            radius=sol_radius,
            temperature=sol_temperature,
            colours=colours,
            **kwags
        ) -> None:
        super().__init__(
                name = name,
                model = "sphere",
                scale = 1,
                position = position,
                color = color.yellow,
                **kwags
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
        self.scale = self.radius * 2 / 10 ** 8

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
    planet_position = Vec3(0, light_year(26_673) + kilo_meter(149.6 * 1_000_000), 0) # 149.6 million km from the sun

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
            mass=planet_mass,
            radius=planet_radius,
            temperature=planet_temperature,
            **kwags
        ) -> None:
        super().__init__(
            name = name,
            model = "sphere",
            position = position,
            color = color.blue,
            **kwags
        )
        self.position = position
        self.timestamp = timestamp * ((8.852 * (10**20) * (radius **0.571) * ((temperature) ** 1.142)) / mass) ** 2.5
        self.radius, self.temperture, self.lifetime = radius, temperature, self.timestamp
        self.luminenecence = 0
        self.mass = lambda: (self.lifetime / radius)**(1/2.5) * mass
    
    def input(self, key):
        def text_abler():
            global able_text
            able_text = True
        global paused, able_text
        if self.hovered and able_text:
            name_text = Text(text=self.name)
            able_text = False
            name_text.appear(speed=0.15)
            destroy(name_text, delay=3)
            invoke(text_abler, delay=3)

bodies = []

sun = Star(position=Vec3(0))
bodies.append(sun)

#tellus = Planet(position=Vec3(100))
#bodies.append(tellus)

#human = FirstPersonController(y=2, origin_y=-.5)
editor = EditorCamera()

app.run()