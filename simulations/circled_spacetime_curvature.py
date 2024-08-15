from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
import numpy as np
import random

app = Ursina()

# Create a grid of dots
num_rings = 20
num_dots_per_ring = 100
dot_spacing = 1.0
dots = np.zeros((num_rings, num_dots_per_ring, 3))

for ring in range(num_rings):
    for dot in range(num_dots_per_ring):
        angle = 2 * math.pi * dot / num_dots_per_ring
        radius = ring * dot_spacing
        dots[ring, dot] = [radius * math.cos(angle), 10, radius * math.sin(angle)]

# Define the gravity function
def gravity(x, z):
    distance = math.sqrt(x**2 + z**2)
    if distance == 0:
        return -100
    else:
        return -10 / (distance**2)

# Create a mesh to represent the grid of dots
mesh = Mesh(vertices=dots.reshape(-1, 3), mode='point', thickness=0.1, render_points_in_3d=True)

# Create an entity to hold the mesh
entity = Entity(model=mesh, color=color.white)

# Update the dot positions
velocities = np.zeros((num_rings, num_dots_per_ring, 3))
def update():
    for ring in range(num_rings):
        for dot in range(num_dots_per_ring):
            # Calculate the direction towards the origin
            direction_x = -dots[ring, dot, 0] / math.sqrt(dots[ring, dot, 0]**2 + dots[ring, dot, 2]**2 + 0.001)
            direction_z = -dots[ring, dot, 2] / math.sqrt(dots[ring, dot, 0]**2 + dots[ring, dot, 2]**2 + 0.001)
            # Calculate the gravitational force
            force = gravity(dots[ring, dot, 0], dots[ring, dot, 2])
            # Update the velocity
            velocities[ring, dot, 0] += direction_x * 0.01
            velocities[ring, dot, 2] += direction_z * 0.01
            velocities[ring, dot, 1] += force * time.dt
            # Update the position
            dots[ring, dot, 0] += velocities[ring, dot, 0] * time.dt
            dots[ring, dot, 2] += velocities[ring, dot, 2] * time.dt
            dots[ring, dot, 1] += velocities[ring, dot, 1] * time.dt
            # Check if the dot has reached the singularity
            if dots[ring, dot, 1] < 0:
                # Create a new dot at a random position along the edge of the fabric
                angle = 2 * math.pi * random.random()
                radius = num_rings * dot_spacing
                dots[ring, dot] = [radius * math.cos(angle), 10, radius * math.sin(angle)]
                velocities[ring, dot] = [0, 0, 0]
    mesh.vertices = dots.reshape(-1, 3)
    entity.model = mesh
    entity.model.generate()

# Create a camera and light
editor_camera = EditorCamera()
editor_camera.position = (0, 10, 0)
editor_camera.target_z = -50
editor_camera.rotation = (11, 18, 0)

mouse.visible = False

# Add a light
light = DirectionalLight()
light.position = (0, 10, 0)

# Run the game
app.run()