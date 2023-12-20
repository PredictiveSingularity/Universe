from universe import *

application.asset_folder = Path(application.asset_folder).parent

app = Universe(asset_folder=application.asset_folder)

#from ursina.prefabs.platformer_controller_2d import PlatformerController2d
#player = PlatformerController2d(y=0.001, z=.01, scale_y=0.001, max_jumps=2)

#ground = Entity(model='quad', scale_x=10, collider='box', color=color.black)

quad = load_model('quad', use_deepcopy=True)

level_parent = Entity(model=Mesh(vertices=[], uvs=[]))
def make_level(texture):
    # destroy every child of the level parent.
    # This doesn't do anything the first time the level is generated, but if we want to update it several times
    # this will ensure it doesn't just create a bunch of overlapping entities.
    [destroy(c) for c in level_parent.children]

    for y in range(texture.height):
        collider = None
        for x in range(texture.width):
            col = texture.get_pixel(x,y)

            # If it's black, it's solid, so we'll place a tile there.
            if col == color.black:
                level_parent.model.vertices += [Vec3(*e) + Vec3(x+.5,y+.5,0) for e in quad.generated_vertices] # copy the quad model, but offset it with Vec3(x+.5,y+.5,0)
                level_parent.model.uvs += quad.uvs
                # Entity(parent=level_parent, position=(x,y), model='cube', origin=(-.5,-.5), color=color.gray, texture='white_cube', visible=True)
                if not collider:
                    collider = Entity(parent=level_parent, position=(x,y), model='quad', origin=(-.5,-.5), collider='box', visible=False)
                else:
                    # instead of creating a new collider per tile, stretch the previous collider right.
                    collider.scale_x += 1
            else:
                collider = None

            # If it's green, we'll place the player there. Store this in player.start_position so we can reset the plater position later.
            # if col == color.green:
            #     player.start_position = (x, y)
            #     player.position = player.start_position

    level_parent.model.generate()

#level = make_level(load_texture('assets/levelmap/milky-way'))   # generate the level

#camera.orthographic = True
#camera.position = (30/2,8)
#camera.fov = 16

EditorCamera(parent=level_parent)

#player.traverse_target = level_parent
#enemy = Entity(model='cube', collider='box', scale=0.01, color=color.red, position=(16,5,-.1))

time_delta = 0

def compute_mass(distance_to_origin, number_of_particles):
    dx, dy, dz, dt = distance_to_origin

    return (1 / (1 + dt) ** number_of_particles) * (1 + dt) ** number_of_particles % 1

def compute_velocity(distance_to_origin, mass):
    dx, dy, dz, dt = distance_to_origin
    return (1 - mass) * dt * dx * dy * dz % 1

def compute_energy(t, m, v):
    return m * v ** 2 * t % 1

def make_energy():
    [destroy(c) for c in level_parent.children]

    for x in range(number_of_particles):
        collider = None
        for y in range(number_of_particles):
            for z in range(number_of_particles):
                d = dx, dy, dz, dt = (-1 * x, -1 * y, -1 * z, -1 * (1 - _time_delta) )
                m = compute_mass(d, number_of_particles=number_of_particles)
                v = compute_velocity(d, m)
                e = compute_energy(_time_delta, m, v)
                
                #level_parent.model.vertices += [Vec3(*e) + Vec3(x-.5,y-.5,z-.5) for e in quad.generated_vertices] # copy the quad model, but offset it with Vec3(x+.5,y+.5,0)
                #level_parent.model.uvs += quad.uvs
                
                if not collider:
                    collider = Entity(parent=level_parent, position=Vec3(x, y, z), model='sphere', origin=(-1*m/2,-1*m/2,-1*m/2), collider='sphere', scale=m, visible=True, color=Color(e))
                else:
                    # instead of creating a new collider per tile, stretch the previous collider right.
                    collider.scale += Vec3(x, y, z)
                
                    # p.position = d
                    # p.color = Color(e)
                    # p.model = 'sphere'
                    # p.scale = m

                #print(d, m, v, e)
    level_parent.model.generate()

def update():
    global time_delta, level_parent

    dt = time.dt
    time_delta += dt

    _time_delta = time_delta % 2 - 1
    
    number_of_particles = int(time_delta) % 10

    
    #

    # if player.intersects(enemy).hit:
    #     print('die')
    #     player.position = player.start_position



app.run()