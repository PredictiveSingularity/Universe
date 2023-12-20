# Define the Universe here
from universe.technologies.mathematics.numbers.complex.real.rational.constants import BILLION

__name__="universe"
__version__="0.0.0a2"
__age__= 13.7
__age_scale__ = BILLION # 1_000_000_000
#__age_seconds__ = year(__age__ * __age_scale__) # precision: +/-200 million years

from ursina import *
#from physics3d import *
# from physics3d import Debugger, BoxCollider, MeshCollider, SphereCollider
#from panda3d.bullet import BulletWorld

from universe.technologies import *
from universe.structures import *
#from universe.technologies.simulations.universe import Universe, CosmicBackgroundRadiation
#from universe.structures.bodies.stars import Star, Sol
from universe.main import Universe
