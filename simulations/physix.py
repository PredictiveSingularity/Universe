from universe import *
import numpy as np

application.asset_folder = Path(application.asset_folder).parent

simulacre = Universe(asset_folder=application.asset_folder) #Ursina(size=(1280,720))

G = 50

physics_entities = []
class PhysicsEntity(Entity):
    def __init__(self, mass, orbit_radius, velocity=Vec3(0), **kwargs):
        self.mass, self.velocity = mass, velocity
        self.orbit_radius = orbit_radius
        self.acceleration = Vec3(0)

        super().__init__(**kwargs)
        physics_entities.append(self)

    def set_velocity(self, velocity):
        self.velocity = velocity
    
    def set_acceleration(self, acceleration):
        self.acceleration = acceleration
    
    def set_position(self, position):
        self.position = position

    def update(self):
        if hasattr(self.parent, "mass") and self.orbit_radius > 0 and not self.intersects():
            self.gravitate_to(self.parent)
            self.update_velocity(self.acceleration)
            self.update_position(self.velocity)
        # else:
        #    return
            #self.fusion(self.parent)
            #self.destroy()
        self.rotation_y += time.dt
        self.rotation_x += time.dt
        #print(f"{self}: {self.position=} {self.velocity=} {self.acceleration=} {self.mass=}")
        # self.velocity = lerp(self.velocity, Vec3(0), time.dt)
        # self.velocity += Vec3(0,-1,0) * time.dt * 5
        # self.position += (self.velocity + Vec3(0,-4,0)) * time.dt

    def update_velocity(self, velocity):
        self.velocity += velocity
    
    def update_position(self, position):
        self.position += position

    def gravitate_to(self, exobody):
        #print(f"{self.name} is graviting towards {exobody.name}")
        dx = abs(self.x - exobody.x)
        dy = abs(self.y - exobody.y)
        dz = abs(self.z - exobody.z)

        if dx < 0 and dy < 0 and dz < 0:
            print(f"{self} and {exobody} have collided")
        else:
            try:
                r = np.sqrt(dx**2 + dy**2)
                a = G * exobody.mass / r**2
                theta = np.arcsin(dy/r)

                if self.x > exobody.x:
                    _xsign = -1
                else:
                    _xsign = 1
                _ax = _xsign * a * np.cos(theta) * time.dt
                
                if self.y > exobody.y:
                    _ysign = -1
                else:
                    _ysign = 1
                _ay = _ysign * a * np.sin(theta) * time.dt

                if self.z > exobody.z:
                    _zsign = -1
                else:
                    _zsign = 1
                _az = _zsign * a * np.tanh(theta) * time.dt

                _acceleration = Vec3(_ax, _ay, _az).normalized()
                print(f"{self}: {_acceleration}")
                self.set_acceleration(_acceleration)
            except ZeroDivisionError:
                pass

    def stop(self):
        self.velocity = Vec3(0,0,0)
        if self in physics_entities:
            physics_entities.remove(self)

    def on_destroy(self):
        self.stop()

    def throw(self, direction, force):
        pass

from ursina.shaders import lit_with_shadows_shader
Entity.default_shader = lit_with_shadows_shader
#DirectionalLight().look_at(Vec3(1,-1,-1))
sol = PhysicsEntity(15, 1, name="Sol", model="sphere", collider='sphere', color=color.yellow, velocity=Vec3(0), texture="assets/texture/sol")
PointLight(parent=sol)
#physics_entities.append(sol)

earth = PhysicsEntity(4, 1, name="Earth", parent = sol, model="sphere", collider='sphere', velocity=Vec3(-G), position=Vec3(5, 0, 0), texture="assets/texture/earth")
#ground = Entity(model='plane', scale=32, texture='white_cube', texture_scale=Vec2(32), collider='box')

#from ursina.prefabs.first_person_controller import FirstPersonController
#player = FirstPersonController()

ec = EditorCamera(parent=earth)
ec.lookAt(sol)

# def input(key):
#     if key == 'left mouse down':
#         e = PhysicsEntity(model='cube', color=color.azure, velocity=Vec3(0), position=player.position+Vec3(0,1.5,0)+player.forward, collider='sphere')
#         e.velocity = (camera.forward + Vec3(0,.5,0)) * 10
#         # physics_entities.append(e)


#Sky()
cbr = CosmicBackgroundRadiation(texture="assets/texture/milky-way", scale=100)
simulacre.run()