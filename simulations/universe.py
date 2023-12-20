from ursina import *
import numpy as np

# from ursina.prefabs.first_person_controller import FirstPersonController
from random import uniform, paretovariate, normalvariate

# Initialize Ursina engine
app = Ursina()

# Constants for universe

# Time tracking variables
time_elapsed = 0
max_time = 100
time_scale = 1

# Galaxies
max_distance_from_origin = 10
drag_factor = 0.01  # Decrease velocity as galaxies move away from origin
pull_strength = 0.005  # Increase velocity as galaxies move back towards origin
mass_gain_rate = 0.1  # Rate at which mass (and star count) increases
mass_loss_rate = 0.1  # Rate at which mass (and star count) decreases
min_mass = 10  # Minimum mass (and minimum number of stars) for a galaxy
num_galaxies = 1  # Number of galaxies to spawn
num_stars_per_galaxy = 1000
num_planets_per_star = 3
expansion_rate = 1  # Rate at which the universe expand
max_view_distance = 500  # Max distance for detailed models

# Constants for velocity threshold, set relative to your simulation's scale
# Let's say we define the speed of light in our simulation as 1 unit per update
speed_of_light = 1

# Threshold for a galaxy to be considered crossing the event horizon
# It could be a fraction of the speed of light, since no object with mass can reach it
event_horizon_threshold = 0.9 * speed_of_light

# Camera controller
camera = EditorCamera()
# camera.position = (10, 10, 10)  # Set to a position where galaxies should be visible
# camera.speed = 5  # Adjust the speed as needed

# Skybox for a space background
# sky = Sky()

# On-screen Text to display time
time_text = Text(text=str(time_elapsed), color=color.black, position=(-0.95, 0.45), scale=2)

def lerp_color(color1, color2, t):
    # Manually interpolate the RGB values
    new_r = (1 - t) * color1.r + t * color2.r
    new_g = (1 - t) * color1.g + t * color2.g
    new_b = (1 - t) * color1.b + t * color2.b
    # Create a new Color with the interpolated values
    return Color(new_r, new_g, new_b, 1)

# Planet class
class Planet(Entity):
    def __init__(self, star_position, star_entity):
        super().__init__(parent=star_entity)
        self.position = star_position + Vec3(uniform(-0.1, 0.1), uniform(-0.1, 0.1), uniform(-0.1, 0.1))
        self.model = 'sphere'
        self.color = color.random_color()
        self.scale = 0.01
        self.enabled = False  # Start with planets disabled

# Star class
class Star(Entity):
    def __init__(self, galaxy_entity, position=(0,0,0), mass=1, lifespan=10000):
        super().__init__(parent=galaxy_entity)
        self.position = position
        self.mass = mass  # Add a mass attribute
        self.model = 'sphere'
        self.color = self.set_color_based_on_mass(mass)
        self.scale = self.mass / 1000  # Example scale based on mass
        self.light = PointLight(parent=self, color=self.color, radius=self.mass * 5)  # Radius based on mass
        self.lifespan = lifespan  # Lifespan of the star in 'ticks' or updates
        self.planets = [Planet(self.position, self) for _ in range(num_planets_per_star)]

    def set_color_based_on_mass(self, mass):
        if mass < 5:
            return color.red
        elif mass < 10:
            return color.orange
        elif mass < 20:
            return color.yellow
        else:
            return color.white

    def update(self):
        self.lifespan -= 1
        if self.lifespan <= 0:
            destroy(self)
        
        # Enable/disable planets based on distance to the camera
        if distance(self.position, camera.world_position) < max_view_distance:
            for planet in self.planets:
                planet.enabled = True
        else:
            for planet in self.planets:
                planet.enabled = False

# Galaxy class
class Galaxy(Entity):
    
    def __init__(
            self, 
            position=(0,0,0), 
            mass=1, 
            galaxy_type='spiral',
            galaxy_kwargs={
                'num_arms': random.randint(2, 5),
                'arm_spread': np.pi/random.randint(5, 9),
                'rotation_factor': random.randrange(0, 1000, 1) / 1000 * random.choice([-1, 1]),
                'depth_factor': random.randrange(0, 100, 1) / 100,
            },
        ):
        super().__init__()
        
        self.position = position
        self.velocity = Vec3(uniform(-0.01, 0.01), uniform(-0.01, 0.01), uniform(-0.01, 0.01))
        self.mass = mass
        self.stars = []
        self.galaxy_type = galaxy_type
        
        if galaxy_type == 'spiral':
            num_arms = galaxy_kwargs['num_arms']
            arm_spread = galaxy_kwargs['arm_spread']
            rotation_factor = galaxy_kwargs['rotation_factor']
            depth_factor = galaxy_kwargs['depth_factor']
            
            self.num_arms = num_arms
            self.arm_spread = arm_spread
            self.rotation_factor = rotation_factor
            self.depth_factor = depth_factor
        
        self.generate_stars(initial=True)

    def generate_stars(self, initial=False):
        ''''If it's the initial generation, populate the galaxy with stars based on the galaxy type'''
        if initial:
            if self.galaxy_type == 'spiral':
                for arm in range(self.num_arms):
                    arm_offset = 2 * np.pi * arm / self.num_arms
                    for i in range(num_stars_per_galaxy // self.num_arms):
                        distance_from_center = paretovariate(alpha=1.16)  # Pareto distribution for denser center
                        angle = distance_from_center * self.rotation_factor  # Spiral arms
                        angle += arm_offset + normalvariate(mu=0, sigma=self.arm_spread)

                        x = np.cos(angle) * distance_from_center
                        y = np.sin(angle) * distance_from_center
                        z = normalvariate(mu=0, sigma=self.depth_factor)

                        star_position = self.position + Vec3(x, y, z)
                        new_star = Star(galaxy_entity=self, position=star_position)
                        self.stars.append(new_star)
            
        # If it's not the initial generation, adjust the number of stars based on mass
        else:
            current_star_count = len(self.stars)
            target_star_count = int(self.mass)
            
            if current_star_count < target_star_count:
                for _ in range(target_star_count - current_star_count):
                    self.stars.append(Star(self, position=self.position + Vec3(uniform(-1,1), uniform(-1,1), uniform(-1,1)) * 0.5, mass=uniform(1, 30)))
            elif current_star_count > target_star_count:
                for _ in range(current_star_count - target_star_count):
                    destroy(self.stars.pop())

    def update(self):
        global time_elapsed
        
        # Modifier la vitesse et la position basées sur time_elapsed pour refléter l'expansion
        if time_elapsed < max_time / 2:
            # Expansion phase
            self.velocity += (Vec3(0.01, 0.01, 0.01) * time_elapsed)
        else:
            # Contraction phase
            self.velocity -= (Vec3(0.01, 0.01, 0.01) * (max_time - time_elapsed))
        
        # Update galaxy position based on its velocity
        self.position += self.velocity * time.dt
        distance_from_origin = self.position.length()
        # As the galaxy moves away from the origin, decrease velocity and increase mass (and thus star count)
        if distance_from_origin < max_distance_from_origin:
            self.velocity -= self.velocity * drag_factor
            self.mass += mass_gain_rate * time.dt
            self.generate_stars()
        # As the galaxy moves towards the origin, increase velocity and decrease mass (and thus star count)
        else:
            self.velocity += (Vec3(0,0,0) - self.position).normalized() * pull_strength
            self.mass -= mass_loss_rate
            self.mass = max(self.mass, min_mass)  # Ensure mass doesn't go below a minimum value
            self.generate_stars()

        # Update the stars in the galaxy
        for star in self.stars:
            star.update()
        
            if not star.enabled:  # If the star is not enabled, it is 'dead'
                self.stars.remove(star)
                destroy(star)

        # Check for velocity and convert mass to energy (remove stars) if necessary
        if self.velocity.length() > event_horizon_threshold:
            while self.stars:
                star = self.stars.pop()
                destroy(star)
            # Here you might convert the mass to 'energy' or simply remove it from the simulation

# Create galaxies
galaxies = [Galaxy(position=Vec3(uniform(0,0), uniform(0,0), uniform(0,0))) for _ in range(num_galaxies)]

# Update function
def update():
    global time_elapsed
    
    # Update the time
    time_elapsed += time.dt * time_scale
    
    # Keep time in the range [0, max_time]
    if time_elapsed > max_time:
        time_elapsed = 0
    
    # Update the on-screen text
    time_text.text = f"Time: {time_elapsed:.2f} B Years"

    # Calculate the lerp value
    lerp_value = time_elapsed / max_time

    # Update the background color using the manual lerp
    window.color = lerp_color(color.white, color.black, lerp_value)
    time_text.color = lerp_color(color.black, color.white, lerp_value)
    
    # Update the galaxies
    for galaxy in galaxies:
        galaxy.rotation_y += time.dt * 5  # Add rotation to galaxies for a dynamic effect
        galaxy.update()
        for star in galaxy.stars:
            star.update()

# Run Ursina app
app.run()
