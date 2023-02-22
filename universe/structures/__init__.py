from ursina import Entity, Vec3, time, distance

from universe.technologies.mathematics.numbers.complex.real.rational.constants import G

class Structure(Entity):
    current_velocity = Vec3(0)
    current_position = Vec3(0)

    current_mass = 0
    current_temperature = 0
    current_brightness = 0

    timespan = 0
    timestamp = 0

    scale_factor = 0
    time_factor = 0

    def __init__(
            self,
            initial_velocity=current_velocity,
            position=current_position,
            mass=current_mass,
            temperature=current_temperature,
            brightness=current_brightness,
            lifespan=timespan,
            timestamp=timestamp,
            scale_factor=scale_factor,
            time_factor=time_factor,
            **kwags
        ):
        super().__init__(
            position=position,
            **kwags
        )
        #self.universe = universe
        self.current_velocity = initial_velocity
        self.position = position
        self.mass = lambda: mass
        self.temperature = temperature
        self.brightness = brightness
        self.lifespan = lifespan
        self.scale_factor, self.time_factor = scale_factor, time_factor
    
    def update(self):
        self.update_time()
        self.update_temperature()
        self.update_electro_magnetic_emissions()
        self.update_velocity()
        self.update_position()
        self.update_lifespan()
    
    def update_time(self):
        self.timestamp = time.dt

    def update_temperature(self):
        pass
    
    def update_electro_magnetic_emissions(self):
        pass

    def update_lifespan(self):
        pass
    
    def update_velocity(self):
        for exo_body in self.parent.entities:
            if exo_body != self and hasattr(exo_body, "mass") and hasattr(exo_body, "position"):
                distance_to_exo_body = distance(self, exo_body)
                force_direction = (exo_body.position - self.position).normalized()
                force = Vec3(force_direction * G * self.mass() * exo_body.mass() / distance_to_exo_body)
                try:
                    acceleration = force / self.mass()
                except ZeroDivisionError as zde:
                    acceleration = Vec3(0)
                self.current_velocity += acceleration * self.timestamp

    def update_position(self):
        self.position += self.current_velocity * self.timestamp


