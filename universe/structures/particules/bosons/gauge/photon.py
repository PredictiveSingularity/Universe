# Define a photon γ
from ursina import Vec3, color
from universe.structures.particules.bosons.gauge import Gauge
from universe.technologies.mathematics.numbers.complex.real.rational.constants import *

class Photon(Gauge):
    '''
    γ
    Photon
    Electro-magnetic gauge boson
    https://en.wikipedia.org/wiki/Photon
    Mass: 0 (theoretical value) [< 1×10−18 eV/c2 (experimental limit)]
    Energyspan: ∞
    Interaction: electro-magnetism, weak nuclear force and gravity
    Spin: 1
    Electric charge: 0 (< 1×10−35 e)
    Spin states: +1 ℏ,  −1 ℏ
    Parity: −1
    C parity: −1
    Condensed: I(Jpc)=0,1(1--)

    Quatization of the electro-magnetic field
    Energy = number_photons * h * electro_magnetic_mode_frequency

    0 < wavelength (µm) < 3
    0 < specrtal_radiance (kW * sr**-1 * m**-2 * nm**-1 ) < 14

    Color 	Wavelength (nm) 	Frequency (THz) 	Photon energy (eV)
    violet  380–450        	    670–790 	        2.75–3.26
    blue    450–485             620–670 	        2.56–2.75
    cyan    485–500 	        600–620 	        2.48–2.56
    green   500–565 	        530–600 	        2.19–2.48
    yellow  565–590 	        510–530 	        2.10–2.19
    orange  590–625 	        480–510 	        1.98–2.10
    red     625–750 	        400–480 	        1.65–1.98 

    '''
    photon_name = "Light"
    photon_timestamp = ZERO
    photon_position = Vec3(ZERO, ZERO, ZERO)
    photon_mass = ZERO
    photon_temperature = ZERO # Kelvin
    photon_brightness = ZERO
    photon_lifespan = ZERO

    photon_wavelenth = ZERO # µm (visible light is between 0.38 µm and 0.75 µm)
    
    colours = [
        color.black,  # <= 380 nm
        color.violet, # >= 380 nm < w < 450 nm
        color.blue, # >= 450 nm < w < 485 nm
        color.cyan, # >= 485 nm < w < 500 nm
        color.green, # >= 500 nm < w < 565 nm
        color.yellow, # >= 565 nm < w < 590 nm
        color.orange, # >= 590 nm < w < 625 nm
        color.red, # >= 625 nm < w < 750 nm
        color.black  # >= 750 nm
        ]
    
    def __init__(
            self,
            name=photon_name,
            timestamp=photon_timestamp,
            position=photon_position,
            model="sphere",
            scale=1,
            colours=colours,
            mass=photon_mass,
            temperature=photon_temperature,
            wavelength=photon_wavelenth,
            **kwargs
        ):
        super().__init__(
                name=name,
                position=position,
                model=model,
                scale=scale,
                **kwargs
            )
        self.position = position
        # self.timestamp = timestamp * ((8.852 * (10**20) * (radius **0.571) * ((temperature) ** 1.142)) / mass) ** 2.5
        self.wavelength, self.temperture, self.lifetime = wavelength, temperature, self.timestamp
        # self.luminenecence = lambda: brightness * (4 * pi * (self.radius**2)) * (self.temperture**4)
        self.mass = mass
        self.colours = colours
    
    def update(self) -> None:
        super().update()
        self.update_electro_magnetic_emissions()

    def update_electro_magnetic_emissions(self):
        if self.wavelength >= 0.38: self.color =  self.colours[0]
        if 0.38 > self.wavelength >= 0.45: self.color =  self.colours[1]
        if 0.45 > self.wavelength >= 0.485: self.color =  self.colours[2]
        if 0.485 > self.wavelength >= 0.5: self.color =  self.colours[3]
        if 0.5 > self.wavelength >= 0.565: self.color =  self.colours[4]
        if 0.565 > self.wavelength >= 0.59: self.color =  self.colours[5]
        if 0.59 > self.wavelength >= 0.625: self.color =  self.colours[6]
        if 0.625 > self.wavelength >= 0.75: self.color =  self.colours[7]
        if self.wavelength >= 0.75: self.color =  self.colours[8]
