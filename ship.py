 
import numpy as np
import math
import utils
from numpy import linalg as LA
import pygame


class Ship:
    def __init__(self, x, y, surface):
        # Position of the tip of the ship
        self.pos = np.array([x, y])
        # Rotation angle of the ship relative to the tip of the ship
        self.angle = np.zeros(2)

        # Additional properties goes here:


        # Leave the rest of these properties
        self.surface = surface
        self.radius = 20
        self.color = (255, 0, 0)
        self.collided = False

    # Update properties of the ship
    def update(self, mouse_pos, asteroids, game_status):
        # Action required!
        desired =  mouse_pos - self.pos
        #LA.norm(desired)
        #np.true_divide(desired, 300)
        velocity = desired/300
        velocity *= 10
        self.pos += velocity


        # Set position of ship based on given parameter
        #self.pos = self.pos

        # Determine rotation angle of ship to point at cursor
        angx = mouse_pos[0] - self.pos[0]
        angy = mouse_pos[1] - self.pos[1]
        self.angle = math.atan2(angx, angy)
        #self.angle *= 180/math.pi
        print(self.angle)



        # Leave the rest of the code
        # Check for collision
        if game_status == "started":
            self.collision(asteroids, game_status)

    # Draw the ship onto the canvas
    def draw(self):
        p1 = np.array(utils.rotate((0, 0), self.angle)) + self.pos
        p2 = np.array(utils.rotate((40, 20), self.angle)) + self.pos
        p3 = np.array(utils.rotate((30, 0), self.angle)) + self.pos
        p4 = np.array(utils.rotate((40, -20), self.angle)) + self.pos

        pygame.draw.polygon(
            self.surface,
            self.color,
            [p1, p2, p3, p4]
        )

    # Detect whether ship has collided with an asteroid
    def collision(self, asteroids, game_status):
        for asteroid in asteroids:
            if np.linalg.norm(asteroid.pos - self.pos) < (asteroid.radius + self.radius):
                self.color = (255, 255, 0)
                self.collided = True
                break




