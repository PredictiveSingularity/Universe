from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
import math
import numpy as np
import random

app = Ursina()

# Create a grid of dots
grid_size = 20
dot_spacing = 1.0
dots = np.zeros((grid_size*2+1, grid_size*2+1, 3))

for x in range(-grid_size, grid_size+1):
    for z in range(-grid_size, grid_size+1):
        dots[x+grid_size, z+grid_size] = [x*dot_spacing, 10, z*dot_spacing]

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
velocities = np.zeros((grid_size*2+1, grid_size*2+1, 3))
def update():
    for x in range(-grid_size, grid_size+1):
        for z in range(-grid_size, grid_size+1):
            # Calculate the direction towards the origin
            direction_x = -dots[x+grid_size, z+grid_size, 0] / math.sqrt(dots[x+grid_size, z+grid_size, 0]**2 + dots[x+grid_size, z+grid_size, 2]**2 + 0.001)
            direction_z = -dots[x+grid_size, z+grid_size, 2] / math.sqrt(dots[x+grid_size, z+grid_size, 0]**2 + dots[x+grid_size, z+grid_size, 2]**2 + 0.001)
            # direction_y = -1  # Make the dots move downwards
            
            # Calculate the gravitational force
            force = gravity(dots[x+grid_size, z+grid_size, 0], dots[x+grid_size, z+grid_size, 2])
            # Update the velocity
            velocities[x+grid_size, z+grid_size, 0] += direction_x * 0.01
            velocities[x+grid_size, z+grid_size, 2] += direction_z * 0.01
            # velocities[x+grid_size, z+grid_size, 1] += force * time.dt + direction_y * 0.1
            velocities[x+grid_size, z+grid_size, 1] += force * time.dt
            # Update the position
            dots[x+grid_size, z+grid_size, 0] += velocities[x+grid_size, z+grid_size, 0] * time.dt
            dots[x+grid_size, z+grid_size, 2] += velocities[x+grid_size, z+grid_size, 2] * time.dt
            dots[x+grid_size, z+grid_size, 1] += velocities[x+grid_size, z+grid_size, 1] * time.dt
            # Check if the dot has reached the singularity
            if dots[x+grid_size, z+grid_size, 1] < 0:
                # Create a new dot at a random position along the edge of the fabric
                if random.random() < 0.5:
                    dots[x+grid_size, z+grid_size, 0] = random.choice([-grid_size, grid_size]) * dot_spacing
                    dots[x+grid_size, z+grid_size, 2] = random.uniform(-grid_size, grid_size) * dot_spacing
                else:
                    dots[x+grid_size, z+grid_size, 0] = random.uniform(-grid_size, grid_size) * dot_spacing
                    dots[x+grid_size, z+grid_size, 2] = random.choice([-grid_size, grid_size]) * dot_spacing
                dots[x+grid_size, z+grid_size, 1] = 10
                velocities[x+grid_size, z+grid_size, 0] = 0
                velocities[x+grid_size, z+grid_size, 2] = 0
                velocities[x+grid_size, z+grid_size, 1] = 0
    mesh.vertices = dots.reshape(-1, 3)
    entity.model = mesh
    entity.model.generate()
    
    # Update the HUD
    # hud_text.text = f'Position: {camera.position}\nRotation: {camera.rotation}\nAngle: ({camera.world_rotation_x:.4f}, {camera.world_rotation_y:.4f}, {camera.world_rotation_z:.4f})'

# Create a camera and light
# camera = FirstPersonController(gravity=False)
editor_camera = EditorCamera()
editor_camera.position = (0, 10, 0)
editor_camera.target_z = -50
editor_camera.rotation = (11, 18, 0)

# Make a HUD to display the camera position, rotation and angle
# hud = Entity(parent=camera.ui)
# hud_text = Text(parent=hud, text=f'Position: {camera.position}\nRotation: {camera.rotation}\Angle: (0, 0, 0)', color=color.white)

# camera.position = (0, 20, -50)
# camera.rotation_x = 30

mouse.visible = False

# Add a light
light = DirectionalLight()
light.position = (0, 10, 0)

# Run the game
app.run()