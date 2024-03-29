""" Tutorial for a solar system using Ursina """

from universe import *
#from ursina.prefabs.first_person_controller import FirstPersonController
import random as ra
import numpy as np

application.asset_folder = Path(application.asset_folder).parent

simulacre = Universe(asset_folder=application.asset_folder)

window.color = color.black # color.rgb(0,0,0)

# Our list of planets.
planets = []

# Data from the real solar system!
# https://nssdc.gsfc.nasa.gov/planetary/factsheet/
# Let's name our solar system - Copernicus (daughter?).
# Million km
dataDist = [57.9,	108.2,	149.6,	227.9,	778.6,	1433.5,
            2872.5,	4495.1,	5906.4]
# Km/s
dataVel = [47.4,	35.0,	29.8,
           24.1,	13.1,	9.7,	6.8,	5.4,	4.7]
# Km
dataDia = [4879,	12104,	12756,	6792,	142984,	120536,
           51118,	49528,	2370]

scalar_Ov = 0.001
scalar_Di = 0.006
scalar_Dist = 2

def input(key):
    if key == 'escape' or key == 'q':
        quit()
    if key == 'space':
        sun.scale *= 2

def update():
    sol.rotation_y += time.dt
    sol.rotation_x += time.dt

    camera.z += -1 * time.dt

    for p in planets:
        p.orbit()

# Our Planet class -- for making planets.
class Planet:
    def __init__(this):
        randS = ra.randint(3,24)
        this.name = 'unamed body'
        this.orbitalTheta = ra.randint(0,360)
        this.orbitalVel = 0.01
        this.solarDist = 100
        this.ent = Entity(model='sphere',scale=randS,
                          color=color.lime,texture='assets/texture/moon')

    def orbit(this):
        this.ent.x = this.solarDist * np.cos(this.orbitalTheta) * 7
        this.ent.z = this.solarDist * np.sin(this.orbitalTheta)
        this.orbitalTheta += this.orbitalVel

# The sun (centre of the solar system -> )
sol = Entity(model='sphere',
             texture='assets/texture/sol',scale=964)


# Birth our planets in a loop. Add/append them to the planets[] list.
for p in range(9):
    baby = Planet()
    baby.solarDist = dataDist[p] * scalar_Dist + 964
    baby.orbitalVel = dataVel[p] * scalar_Ov
    baby.ent.scale = dataDia[p] * scalar_Di
    planets.append(baby)

# Colour of each planet.
planets[0].ent.color=color.gray
planets[1].ent.color=color.pink
planets[2].ent.color=color.cyan
planets[3].ent.color=color.red
planets[4].ent.color=color.brown
planets[5].ent.color=color.gold
planets[6].ent.color=color.cyan
planets[7].ent.color=color.blue

# Create a ring for Saturn :)
ring = Entity(model=load_model('assets/objects/torus.obj'))
ring.position = planets[5].ent.position
ring.scale = planets[5].ent.scale
ring.scale_y = 1
ring.rotation_x = 45
ring.reparent_to(planets[5].ent)
ring.color=color.yellow

# Show us earth

earth = planets[2].ent

earth.texture = load_texture('assets/texture/earth')

editor_camera = EditorCamera(move_speed=1000)
camera.clip_plane_far = 9**90

#camera.z = -1000 * 5
#camera.rotation_x = 90

cbr = CosmicBackgroundRadiation(scale=10000)
cbr.texture = 'assets/texture/milky-way'

simulacre.run()
