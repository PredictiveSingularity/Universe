#!/usr/bin/env python

from universe import *

import numpy as np

app = Ursina()

time_scale = year(MILLION / 100)
space_scale = light_year(MILLION)

class Energy(Entity):

    density = int((space_scale / light_year(THOUSAND)) * 10)
    theta = np.linspace(0, 3 * np.pi, density)

    def __init__(self, theta = theta, collision_hit = Vec3(np.random.choice(np.random.uniform([0, 1])), np.random.choice(np.random.uniform([0, 1])), np.random.choice(np.random.uniform([0, 1]))), density = density, **kwargs):
        # self.structures = structures
        self.trajectory = [None] * density
        self.density = density
        self.theta = theta = np.linspace(0, 3 * np.pi, self.density)
        self.collision_hit = collision_hit
        self.time_delta = 0
        
        super().__init__(
                name="Energy",
                model="sphere",
                color=color.white,
                collider='mesh',
                **kwargs
            )
    
    def update(self):
        self.time_delta += time.dt * 10
        if (
                self.x < 0.01 and
                self.y < 0.01 and
                self.z < 0.01
            ):
            x = 1 * np.cos(self.theta) * np.exp(self.collision_hit.x * self.theta)
            y = 1 * np.sin(self.theta) * np.exp(self.collision_hit.y * self.theta)
            z = 1 * np.tan(self.theta) * np.exp(self.collision_hit.z * self.theta)
            acceleration = Vec3(x[int(self.time_delta)], y[int(self.time_delta)], z[int(self.time_delta)])
            self.position += acceleration
        else:
            x = -1 * self.x * np.cos(self.theta) * np.exp(self.collision_hit.x * self.theta)
            y = -1 * self.y * np.sin(self.theta) * np.exp(self.collision_hit.y * self.theta)
            z = -1 * self.z * np.tan(self.theta) * np.exp(self.collision_hit.z * self.theta)
            deceleration = Vec3(x[int(self.time_delta)], y[int(self.time_delta)], z[int(self.time_delta)])
            self.position += deceleration
        
        print(f"{self.position}")
        
for i in range(10):
    e = Energy(theta=i)
    # e.rotate(Vec3(0, i*1, 0))

EditorCamera()

app.run()