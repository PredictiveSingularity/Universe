from universe.structures.particules.photon import C

# Define special relativity

# Define mass-energy equivalence

# Define mass
def get_mass(energy, speed):
    # m = E/c**2
    return energy / speed ** 2

# Define energy
def get_energy(mass, speed=C):
    # E = m*c**2
    return mass * speed ** 2

