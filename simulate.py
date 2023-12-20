#!/usr/bin/env python

# Import Modules
# Make sure all modules are installed before running the Simulation
# To build a binary of the Simulation, make sure all modules are gived to the engine compiler
import sys

# Import Everthing from the Universe
# Singularity
from universe import *
from ursina.shaders import lit_with_shadows_shader

simulacre = cbr = None
time_delta = 0

def get_parsed_args():
    import argparse

    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ("oui", "yes", "true", "t", "o", "y", "1"):
            return True
        if v.lower() in ("non", "no", "false", "f", "n", "0"):
            return False
        raise argparse.ArgumentTypeError("Boolean value expected.")

    parser = argparse.ArgumentParser(description='Simulate the Universe')
    parser.add_argument('-v', '--version', action='store_true', help="output version information and exit")
    # parser.add_argument('-u', '--universe', type=str, default="Singularity.universe", required=False, help="Universe file to load and simulate.")
    parser.add_argument('-n', '--name', type=str, default="Singularity", required=False, help="Universe name to load and simulate.")
    parser.add_argument("--fullscreen", type=str2bool, default=False, help="Set true to simulate in fullscreen mode.")
    parser.add_argument("--vsync", type=str2bool, default=False, help="Set true to simulate using vertical synchronization.")
    parser.add_argument("--debug", type=str2bool, default=False, help="Set true to simulate with debug mode.")

    return parser.parse_args()

def input(key):
    if any([
        held_keys['control'] and key == 'q',
        held_keys['control'] and key == 'x',
        key == 'q',
        key == 'escape',
    ]):
        print("[Q]uit -> User has ended the Simulation")
        application.quit()

def update():
        global cbr, time_delta
        
        time_delta += time.dt
        if cbr:
            if time_delta < 1:
                cbr.texture = None
                cbr.color = Color(-1 * time_delta)
            elif time_delta < 2:
                cbr.texture = 'assets/texture/milky-way'
                cbr.color = None
            elif time_delta < 3:
                cbr.texture = None
                cbr.color = color.white

#from universe.main import main
def main():
    global simulacre

    args = get_parsed_args()

    if args.version:
        from universe import __version__, __age__,  __name__, __age_scale__
        print(f"{__name__} version {__version__}")
        print(f"For at least {__age__} {'billion' if __age_scale__ == 1_000_000_000 else f'times {__age_scale__}'} years.")
        sys.exit()

    universe_name = args.name

    # universe_path = args.universe or f'{universe_name}.universe'
    # print(f'Loading {universe_path}')

    simulacre = Universe(
        title=universe_name,
        fullscreen=args.fullscreen,
        vsync=args.vsync,
        development_mode=args.debug,
        editor_ui_enabled=args.debug,
    )

    # Define the Universe here.
    
    cbr = CosmicBackgroundRadiation(scale=100)
    
    # sol = Sol()

    # print(f"{sol.name} has a temperature of {sol.temperature} Kelvin")
    # print(f"{sol.mass()=}")
    # print(f"{sol.color=}")
    
    # sol = Entity(
    #     model = 'sphere',
    #     # color = color.yellow,
    #     scale = 1.5,
    #     texture='assets/texture/sol',
    #     collider='sphere',
    #     shader = lit_with_shadows_shader
    # )
    # sol.unlit = True

    # sol.light = PointLight(parent=sol, shadows=True, color=color.red, position=sol.position)

    # earth = Entity(
    #     world_parent = sol,
    #     model = 'sphere',
    #     # color = color.blue,
    #     scale = 0.4,
    #     texture='assets/texture/earth',
    #     collider='sphere',
    #     position=Vec3(40, 0, 0),
    #     rotation_x=420,
    #     rotation_z=180,
    #     shader = lit_with_shadows_shader
    # )

    observer = EditorCamera()

    simulacre.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
