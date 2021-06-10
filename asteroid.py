import pygame
import numpy as np
import math
from random import randint, random

Random = randint(1, 5)
class Asteroid:
    def __init__(self, x, y, radius, surface, a, b):
        # Position of the tip of the asteroid
        self.pos = np.array([x, y])
        # Additional properties goes here:
       
        self.a = a
        self.b = b

        # Leave the rest of these properties
        self.surface = surface
        self.radius = radius

    def update(self, asteroids):
        self.pos[0] += self.a
        self.pos[1] += self.b
      
        #a+=1
        # Action required!
        #self.pos[0] +=a
        #self.pos[1] +=a
        # Set position of asteroid based on given parameter

        # Leave the rest of the code
        # Wrap asteroid around the edges so it always stay on screen
        if self.pos[0] > self.surface.get_width():
            self.pos[0] = 0
        elif self.pos[0] < 0:
            self.pos[0] = self.surface.get_width()

        if self.pos[1] > self.surface.get_height():
            self.pos[1] = 0
        elif self.pos[1] < 0:
            self.pos[1] = self.surface.get_height()

    # Draw the asteroid onto the canvas
    def draw(self):
        pygame.draw.circle(self.surface, (0, 0, 255), (self.pos[0], self.pos[1]), self.radius)
        pygame.draw.circle(self.surface, (0, 255, 255), (0,0), self.radius)
