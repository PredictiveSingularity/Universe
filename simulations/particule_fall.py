from ursina import *
import numpy as np

# def update():
#     global e1,e2,e3,e4,e5
#     speed = 0.005

#     angle = 0
#     for entity in e1:
#         radius = entity.x/np.cos(angle)
#         radius -= speed       
#         entity.x = radius*np.cos(angle)
#         entity.z = radius*np.sin(angle)
#         entity.y = -3/abs(entity.x) +3   
#         if radius < 0.3:
#             entity.x = 4*np.cos(angle)
#             entity.z = 4*np.sin(angle)
#             entity.y = -3/abs(entity.x/np.cos(angle))+3   

#     angle = 60/180*np.pi
#     for entity in e2:
#         radius = entity.x/np.cos(angle)
#         radius -= speed        
#         entity.x = radius*np.cos(angle)
#         entity.z = radius*np.sin(angle)
#         entity.y = -3/abs(entity.x/np.cos(angle))+3   
#         if radius < 0.3:
#             entity.x = 4*np.cos(angle)
#             entity.z = 4*np.sin(angle)
#             entity.y = -3/abs(entity.x/np.cos(angle))+3   

#     angle = 90/180*np.pi
#     for entity in e3:
#         radius = entity.x/np.cos(angle)
#         radius -= speed        
#         entity.x = radius*np.cos(angle)
#         entity.z = radius*np.sin(angle)
#         entity.y = -3/abs(entity.x/np.cos(angle))+3   
#         if radius < 0.3:
#             entity.x = 4*np.cos(angle)
#             entity.z = 4*np.sin(angle)
#             entity.y = -3/abs(entity.x/np.cos(angle))+3   

#     angle = 120/180*np.pi
#     for entity in e4:
#         radius = entity.x/np.cos(angle)
#         radius -= speed       
#         entity.x = radius*np.cos(angle)
#         entity.z = radius*np.sin(angle)
#         entity.y = -3/abs(entity.x/np.cos(angle))+3   
#         if radius < 0.3:
#             entity.x = 4*np.cos(angle)
#             entity.z = 4*np.sin(angle)
#             entity.y = -3/abs(entity.x/np.cos(angle))+3   

#     angle = 180/180*np.pi
#     for entity in e5:
#         radius = entity.x/np.cos(angle)
#         radius -= speed        
#         entity.x = radius*np.cos(angle)
#         entity.z = radius*np.sin(angle)
#         entity.y = -3/abs(entity.x/np.cos(angle))+3   
#         if radius < 0.3:
#             entity.x = 4*np.cos(angle)
#             entity.z = 4*np.sin(angle)
#             entity.y = -3/abs(entity.x/np.cos(angle))+3   
                   
app = Ursina()

# num = 40
# radius = np.linspace(0,10,num)

# angle = 0
# x1 = radius*np.cos(angle)
# z1 = radius*np.sin(angle)
# y1 = -3/abs(x1) + 3

# angle = 60/180*np.pi
# x2 = radius*np.cos(angle)
# z2 = radius*np.sin(angle)
# y2 = y1

# angle = 90/180*np.pi
# x3 = radius*np.cos(angle)
# z3 = radius*np.sin(angle)
# y3 = y1

# angle = 120/180*np.pi
# x4 = radius*np.cos(angle)
# z4 = radius*np.sin(angle)
# y4 = y1

# angle = 180/180*np.pi
# x5 = radius*np.cos(angle)
# z5 = radius*np.sin(angle)
# y5 = y1

# e1= [None]*num
# e2= [None]*num
# e3= [None]*num
# e4= [None]*num
# e5= [None]*num

# for i in range(num):
#     e1[i] = Entity(model="sphere",color=color.red,
#                   scale=0.1,position=(x1[i],y1[i],z1[i]))
#     e2[i] = Entity(model="sphere",color=color.yellow,
#                   scale=0.1,position=(x2[i],y2[i],z2[i]))
#     e3[i] = Entity(model="sphere",color=color.white,
#                   scale=0.1,position=(x3[i],y3[i],z3[i]))
#     e4[i] = Entity(model="sphere",color=color.cyan,
#                   scale=0.1,position=(x4[i],y4[i],z4[i]))
#     e5[i] = Entity(model="sphere",color=color.green,
#                   scale=0.1,position=(x5[i],y5[i],z5[i]))

#Text(text='Singularity',position=(0,0.4),origin=(0,0),background=True)

class Energy(Entity):

    def __init__(self, level=0, origin_radius=0, origin_theta=0, time_scale=1, speed = 0.005, model = Mesh(vertices=[], uvs=[]), **kwargs):
        self.time_delta = self.time_delta = 0
        self.time_scale = time_scale
        self.level = level
        self.origin_radius = origin_radius
        self.origin_theta = origin_theta
        self.origin_tree = self.generate_origin_tree()
        self.speed = speed

        super().__init__(model=model, **kwargs)
        #self.generate_sphere_map()

    def generate_origin_tree(self):
        origin = [None]*self.level

        for p in range(self.level):
            x = self.origin_radius*np.cos(self.origin_theta)
            z = self.origin_radius*np.sin(self.origin_theta)
            y = 0/abs(x)

            origin[p - 1] = [None]*self.level

            for t in range(self.level):
                origin[p - 1][t - 1] = Entity(parent=self, model="sphere", color=color.red, scale=0.1, position=(x[t - 1],y[t - 1],z[t - 1]))

        return origin

    def update(self):
        self.update_time()
        self.update_emission()
        self.update_velocity()
        self.update_position()
        self.update_mass()
        self.update_scale()
        self.origin_tree = self.generate_origin_tree()

    def update_time(self):
        dt = time.dt
        past = int(self.time_delta)
        self.time_delta += dt
        self._time_delta = self.time_delta % 2 - 1
        self.level = int(self.time_delta * self.time_scale)
        
        b1 = self.level * self._time_delta
        b2 = -1 * b1
        #print(self.origin[int(self.level+b1)][int(self.level+b2)])
        #print(self.origin_tree)

    def update_emission(self):
        pass
    
    def update_velocity(self):
        pass

    def update_position(self):
        pass
    
    def update_mass(self):
        pass
    
    def update_scale(self):
        pass

Energy()

EditorCamera()

app.run()