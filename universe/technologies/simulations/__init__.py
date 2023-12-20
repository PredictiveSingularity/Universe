from ursina import Ursina, EditorCamera, time, window, application, held_keys

from universe.technologies.simulations.universe import *
# from universe.technologies.simulations.origin import *
from universe.technologies.units.international_system import second, meter

#from universe.structures.bodies.stars import Star
#from universe.structures.atoms.reactive_non_metals.hydrogen import Hydrogen
from universe.structures.particules.bosons.gauge.photon import Photon

class Simulation:

    engine = None

    title = "Universe Simulation"
    fullscreen = False
    vsync = False
    development_mode = False
    editor_ui_enabled = False

    universe = None

    target = None
    target_info = None

    space_time = None

    scale_factor = meter(1)
    time_factor = second(1)

    def __init__(
            self,
            structures={},
            filepath="Singularity.universe",
            title=title,
            fullscreen=fullscreen,
            vsync=vsync,
            development_mode=development_mode,
            editor_ui_enabled=editor_ui_enabled,
            scale_factor=scale_factor,
            time_factor=time_factor,
        ):
        self.origin_time = time.time()
        self.engine = Ursina(title=title, fullscreen=fullscreen, vsync=vsync, development_mode=development_mode, editor_ui_enabled=editor_ui_enabled)
        self.scale_factor = scale_factor
        self.time_factor = time_factor
        self.time = time
        self.window = window
        self.application = application
        self.universe = Universe(structures, filepath, scale_factor=scale_factor, time_factor=time_factor)
        self.universe.structures['Photon'] = Photon(universe=self.universe, name="Photon", wavelength=0.6)
        #self.universe.update()
        self.camera = EditorCamera(parent=self.universe.structures['Photon'])
        
        print(f"Initialized Universe Simulation in {float(time.time() - self.origin_time):.7f} second(s).")
    
    def update(self):
        self.engine.update()

    def input(self, key):
        if any([
            held_keys['control'] and key == 'q',
            held_keys['control'] and key == 'x',
            key == 'q',
            key == 'escape',
        ]):
            print("[Q]uitting.")
            self.application.exit(1)
        #super().input(key)
        

    def run(self):
        self.engine.run()