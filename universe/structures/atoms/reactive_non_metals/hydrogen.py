import numpy as np
from ursina import Vec3, Mesh
from universe.structures.atoms.reactive_non_metals import ReactiveNonMetal
from universe.structures.particules.fermions.leptons.electron import Electron
from universe.structures.particules.fermions.quarks.hadron.baryon.proton import Proton

class Hydrogen(ReactiveNonMetal):
    # 1p+ 1e-
    # mass number : 1
    isotrop = 1
    nucleus = {}
    atomic_mass = 1.00784 # u

    def __init__(self, universe, mass=atomic_mass, **kwargs):
        self.atom = [
            Proton(universe=universe, name="Proton"),
            Electron(universe=universe, name="Electron"),
        ]
        self.number_of_particles = lambda: len(self.atom)
        self.points = np.array([Vec3(0,0,0) for i in range(self.number_of_particles())])
        super().__init__(universe, model=Mesh(vertices=self.points, mode='point', static=False, render_points_in_3d=True, thickness=.1), **kwargs)

        for key, value in kwargs.items():
            setattr(self, key, value)


    def update(self):
        pass

class Deterium(ReactiveNonMetal):
    isotrop = 2
    nucleus = {}

class Tritum(ReactiveNonMetal):
    isotrop = 2
    nucleus = {}
