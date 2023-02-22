from ursina import *

app = Ursina()

e1 = Entity(position = (0,0,0))
e2 = Entity(position = (0,1,1))
distance(e1, e2)
distance_xz(e1, e2.position)

between_color = lerp(color.lime, color.magenta, .5)
print(between_color)
print(lerp((0,0), (0,1), .5))
print(lerp(Vec2(0,0), Vec2(0,1), .5))
print(lerp([0,0], [0,1], .5))

print(round(Vec3(.38, .1351, 353.26), 2))

p = (1,0)
print(p, 'rotated ->', rotate_point_2d(p, (0,0), 90))

app.run()