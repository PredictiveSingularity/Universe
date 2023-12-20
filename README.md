sour# Universe
Energy in All Space & Time is pulling together towards the Singularity.

This Python tool is built on top of [Ursina Engine](https://www.ursinaengine.org/) using [Bullet for Ursina](https://github.com/LooksForFuture/Bullet-for-ursina) `physics3d` library. 

It provides an easy way to visualize the interaction of Energy trought Space and Time.

```python
# import Everything from the Universe
from universe import *

# Define the Universe
simulacre = Universe()

# Define Everything or Anything within the Universe here
origin = Singularity()

# Run the simulation
simulacre.run()
```

![Capture d’écran du 2023-02-22 01-25-43.png](assets/img/Capture%20d%E2%80%99%C3%A9cran%20du%202023-02-22%2001-25-43.png)

Everything is Always too much. Let's tone it down.

```python
simulacre = Universe()

cbr = CosmicBackgroundRadiation()

simulacre.run()
```

![Capture d’écran du 2023-02-24 18-54-09.png](assets/img/Capture%20d%E2%80%99%C3%A9cran%20du%202023-02-24%2018-54-09.png)

## Index

- [Installation](#installation)
- [Usage](#usage)
  - [Examples](#examples)
  - [Contributions](#contributions)

## Build from source
Clone this repository.
```zsh
❯ git clone https://github.com/PredictiveSingularity/Universe.git ./Universe
```

Build `simulate` binary.

Make sure `Cython` is installed.

```zsh
❯ cd Universe/
❯ pip install -r requirements.txt
❯ make build
❯ ls dist/
```

After you have built `simulate`, you can [install it](#installation).

Alternatively you could try to build for Windows using [Ursina's Build Engine](https://www.ursinaengine.org/building.html).

```
make windows
```

# Installation

Make sure you [build `simulate` first](#build-from-source).

```zsh
❯ file dist/simulate
❯ make install
❯ which simulate
❯ simulate --help
```

Then [start simulating](#usage).

# Usage

Using `simulate`:

```zsh 
❯ simulate --help
usage: simulate [-h] [-v] [-n NAME] [--debug DEBUG]

Simulate the Universe

options:
  -h, --help            show this help message and exit
  -v, --version         output version information and exit
  -n NAME, --name NAME  Universe name to load and simulate.
  --debug DEBUG         Set true to simulate with debug mode.

❯ simulate
```

Or have fun with [`simulate.py`](simulate.py).

```python
# Import Singularity
from universe import *

# You can catch any input from here
def input(key):
    if any([
        held_keys['control'] and key == 'q',
        held_keys['control'] and key == 'x',
        key == 'q',
        key == 'escape',
    ]):
        print("[Q]uit -> User has ended the Simulation")
        application.quit()

# You can update anything from here
def update():
    global simulacre

    # print(f"This is an update at. {time.dt}")

def main():
    global simulacre

    # This is the Universe
    simulacre = Universe()

    # Define the Universe here.

    # Background Radiation
    cbr = CosmicBackgroundRadiation()

    # Our Sun
    sol = Sol()

    earth = Earth()

    # Set us as observer
    observer = EditorCamera(parent=earth)

    # Everthing has been declared
    # The simulation of the Universe can be runned
    simulacre.run()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
```

Quickly update any parameter and see the results.

```zsh
❯ make simulation
# With parameters:
python simulate.py --help
```

![Capture d’écran du 2023-02-22 03-29-09.png](assets/img/Capture%20d%E2%80%99%C3%A9cran%20du%202023-02-22%2003-29-09.png)

## Examples

Checkout [`simulations/`](simulations/) for ideas.

Or just run the default simulation.

```zsh
❯ make run
# With parameters:
❯ python -m universe --help
```

## Contributions

This project is built on top of:

-   [Ursina Engine](https://www.ursinaengine.org/)
-   [Bullet for Ursina](https://github.com/LooksForFuture/Bullet-for-ursina)

Give their and our respective projects a start and checkout [`CONTRIBUTING`](CONTRIBUTING.md) to help improving it.
