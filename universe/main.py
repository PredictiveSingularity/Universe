import sys

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
    parser.add_argument('-u', '--universe', type=str, default="Singularity.universe", required=False, help="Universe file to load and simulate.")
    parser.add_argument('-n', '--name', type=str, default="Singularity", required=False, help="Universe name to load and simulate.")
    parser.add_argument("--fullscreen", type=str2bool, default=False, help="Set true to simulate in fullscreen mode.")
    parser.add_argument("--vsync", type=str2bool, default=False, help="Set true to simulate using vertical synchronization.")
    parser.add_argument("--debug", type=str2bool, default=False, help="Set true to simulate with debug mode.")

    return parser.parse_args()

def update():
    # print(f"This is an update at. {time.dt}")
    pass

def input(key):
    if any([
        held_keys['control'] and key == 'q',
        held_keys['control'] and key == 'x',
        key == 'q',
        key == 'escape',
    ]):
        print("[Q]uit -> User has ended the Simulation")
        application.quit()

def main():
    args = get_parsed_args()

    if args.version:
        from universe import __version__, __age__,  __name__, __age_scale__
        print(f"{__name__} version {__version__}")
        print(f"For at least {__age__} {'billion' if __age_scale__ == 1_000_000_000 else f'times {__age_scale__}'} years.")
        sys.exit()

    from universe.technologies.simulations import Simulation

    universe_name = args.name

    universe_path = args.universe or f'{universe_name}.universe'
    
    print(f'Loading {universe_path}')

    simulacre = Simulation(
        filepath=args.universe,
        title=universe_name,
        fullscreen=args.fullscreen,
        vsync=args.vsync,
        development_mode=args.debug,
        editor_ui_enabled=args.debug,
    )

    simulacre.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
