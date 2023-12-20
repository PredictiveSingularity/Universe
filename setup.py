#!/usr/bin/env python
import os
import multiprocessing

import universe

from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
    long_description = f.read()

setup(
    name='universalis-vita-singularis',
    author='Danny Waser',
    version=universe.__version__,
    license='LICENSE',
    url='https://github.com/PredictiveSingularity/Universe',
    description='Energy in All Space & Time is falling together towards the Singularity.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages('.'),
    python_requires='>=3.8,<4',
    install_requires = [
        'numpy~=1.22.4',
        # 'siunits~=0.0.6',
        'ursina~=5.2.0',
        # 'cython-setuptools~=0.2.3',
        'physics3d==1.0',
        # 'git+https://github.com/LooksForFuture/Bullet-for-ursina.git',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'simulate = universe.main:main',
    #     ]
    # },
)
