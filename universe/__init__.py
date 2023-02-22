# Define the Universe here
__name__="universe"
__version__="0.0.0a1"
__age__= 13.7
__age_scale__ = 1_000_000_000
#__age_seconds__ = year(__age__ * __age_scale__) # precision: +/-200 million years

from ursina import *
from universe.technologies.simulations.universe import Universe, CosmicBackgroundRadiation
from universe.structures.bodies.stars import Star, Sol