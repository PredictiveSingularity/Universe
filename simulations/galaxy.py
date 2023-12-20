#!/usr/bin/env python

from universe import *

import numpy as np
application.asset_folder = Path(application.asset_folder).parent

app = Universe(asset_folder=application.asset_folder)

class ParticleSystem(Entity):
    
    def __init__(
        self,
        number_of_particles = 1000,
        number_of_frames = 120,
        frame_rate = 1,
        collision_hit = Vec3(
                np.random.choice(np.random.uniform([0, 1])), # x
                np.random.choice(np.random.uniform([0, 1])), # y
                np.random.choice(np.random.uniform([0, 1]))  # z
            ),
        **kwargs
    ):
        self.number_of_particles, self.number_of_frames, self.frame_rate = number_of_particles, number_of_frames, frame_rate
        self.collision_hit = collision_hit
        self.time_delta = 0
        
        self.particles, self.life_vector, self.frames = self.generate_particules(number_of_particles=number_of_particles, number_of_frames=number_of_frames)
        
        super().__init__(
            model=Mesh(
                vertices=self.particles,
                mode='point',
                static=False,
                render_points_in_3d=True,
                thickness=.1
            ),
            t=0,
            duration=1,
            **kwargs
        )

        for key, value in kwargs.items():
            setattr(self, key, value)


    def update(self):
        self.t += time.dt
        if self.t >= self.duration:
            destroy(self)
            p = ParticleSystem(position=Vec3(random.random(),random.random(),random.random())*2*np.pi, color=color.random_color(), rotation_y=random.random()*360/self.number_of_particles)
            #camera.parent = p
            return
        self.model.vertices = self.frames[floor(self.t * self.duration * self.number_of_frames*self.frame_rate)]
        self.model.generate()
    
    def get_point_on_sphere(self, radius=0, theta=Vec3(0), get_random=False):
        
        if get_random:
            return Vec3(
                (random.choice(range(-1 * radius, self.number_of_frames*self.frame_rate)) % np.pi) - .5,
                (random.choice(range(-1 * radius, self.number_of_frames*self.frame_rate)) % np.pi) - .5,
                (random.choice(range(-1 * radius, self.number_of_frames*self.frame_rate)) % np.pi) - .5
            )
        
        # sign = 1 # or -1
        normalized_theta = theta.normalize()
        sign = normalized_theta
        
        x = sign * np.cos(theta) * np.exp(self.collision_hit.x * theta)
        y = sign * np.exp(self.collision_hit.y * theta)
        z = sign * np.tan(theta) * np.exp(self.collision_hit.z * theta)

        theta_prime = Vec3(x[int(radius-1)], y[int(radius-1)], z[int(radius-1)])

        return theta_prime
    
    def generate_particules(self, number_of_particles = 1000, number_of_frames = 120):
        '''
        number_of_particles: Keep as low as possible
        number_of_frames: Integer number of frames to compute
        '''
        # Generate all the particules
        self.particles = np.array([Vec3(0,0,0) for i in range(number_of_particles)])
        # Give them a life (trajectory)
        self.life_vector = np.array([self.get_point_on_sphere(radius=i) for i in range(number_of_particles)])
        # Generate frames
        self.frames = []

        # simulate the particles once and cache the positions in a list.
        for i in range(number_of_frames*self.frame_rate):
            # if i < number_of_frames:
            self.particles += self.life_vector
            self.frames.append(copy(self.particles))
        
        return self.particles, self.life_vector, self.frames

#cbr = CosmicBackgroundRadiation(texture="assets/texture/milky-way", scale=1)

p = ParticleSystem()

# info = Text('press [Space] to Spawn particles', origin=(0,0), y=-.40)
info = Text('press [Shift] + [Q] to Quit', origin=(0,0), y=-.45)

ec = EditorCamera()
# ec.rotation_x = 180
# ec.rotation_y = 90


# def input(key):
    # if key == 'space':
        
        #p.fade_out(duration=.2, delay=1-.2, curve=curve.linear)

# def update():
    # p = ParticleSystem(position=Vec3(random.random(),random.random(),random.random())*2*np.pi, color=color.random_color(), rotation_y=random.random()*360/number_of_particles)
    #print(time.dt)

app.run()