from vpython import *

class Planet(sphere):
    def __init__(self, mass, radius, pos, visible, initial_pos, **kwargs):
        super().__init__(**kwargs)
        self.mass = mass
        self.radius = radius
        self.velocity = vector(0, 0, 0)
        self.pos = pos
        self.trail = curve(color=self.color, opacity = 0.5 ) 
        self.visible = visible
        self.initial_pos = initial_pos
        self.AM = 0
        self.LM = 0
        self.PE = 0
        self.KE = 0
        