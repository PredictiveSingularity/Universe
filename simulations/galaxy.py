#!/usr/bin/env python

from ursina import *

import numpy as np

app = Ursina()

a = 1
linear_space_between = 60
theta = np.linspace(0, 3 * np.pi, linear_space_between)

b = 0.2
x1 = a * np.cos(theta) * np.exp(b * theta)
y1 = a * np.sim(theta) * np.exp(b * theta)
e1 = [None] * linear_space_between

x2 = -1 * a * np.cos(theta) * np.exp(b * theta)
y2 = -1 * a * np.sin(theta) * np.exp(b * theta)
e2 = [None] * linear_space_between

b = 0.25

x3 = -1 * a * np.cos(theta) * np.exp(b * theta)
y3 = -1 * a * np.sin(theta) * np.exp(b * theta)
e3 = [None] * linear_space_between

b = 0.25

x4 = -1 * a * np.cos(theta) * np.exp(b * theta)
y4 = -1 * a * np.sin(theta) * np.exp(b * theta)
e4 = [None] * linear_space_between

for i in range(linear_space_between):
    e1[i] = Entity(
        model="sphere",
        scale=0.1,
        color=color.red,
        position=(x1[i], y1[i])
    )
    e2[i] = Entity(
        model="sphere",
        scale=0.1,
        color=color.green,
        position=(x2[i], y2[i])
    )
    e3[i] = Entity(
        model="sphere",
        scale=0.1,
        color=color.yellow,
        position=(x3[i], y3[i])
    )
    e4[i] = Entity(
        model="sphere",
        scale=0.1,
        color=color.cyan,
        position=(x4[i], y4[i])
    )

app.run()