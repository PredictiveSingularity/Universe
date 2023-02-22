import sys

from ursina import time, held_keys, application
from universe.main import main

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

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
